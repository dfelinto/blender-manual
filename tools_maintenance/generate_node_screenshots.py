import bpy
from dataclasses import dataclass
from itertools import islice


@dataclass
class Rectangle:
    x: float
    y: float
    width: float
    height: float


def cut_image(old_path, new_path, rect):
    image = bpy.data.images.load(old_path)

    total_width, total_height = image.size
    assert total_width >= rect.x + rect.width
    assert total_height >= rect.y + rect.height

    old_pixels = image.pixels
    new_pixels = []

    for y in range(rect.y, rect.y + rect.height):
        row_start = y * total_width + rect.x
        row_end = row_start + rect.width
        new_pixels.extend(old_pixels[4 * row_start:4 * row_end])

    image.scale(rect.width, rect.height)
    image.pixels = new_pixels
    image.filepath_raw = new_path
    image.save()

    bpy.data.images.remove(image)


def node_region_rect(region, node):
    location = node.location
    dimensions = node.dimensions

    view_to_region = region.view2d.view_to_region
    bottom_left = view_to_region(
        location.x, location.y - dimensions.y, clip=False)
    top_right = view_to_region(
        location.x + dimensions.x, location.y, clip=False)

    return Rectangle(bottom_left[0], bottom_left[1], top_right[0] - bottom_left[0], top_right[1] - bottom_left[1])


def iter_node_names(tree_type):
    if tree_type == 'GEOMETRY':
        for cls in bpy.types.GeometryNode.__subclasses__():
            yield cls.__name__
    elif tree_type == 'COMPOSITING':
        for cls in bpy.types.CompositorNode.__subclasses__():
            yield cls.__name__
    elif tree_type == 'SHADER':
        for cls in bpy.types.ShaderNode.__subclasses__():
            yield cls.__name__
    elif tree_type == 'TEXTURE':
        for cls in bpy.types.TextureNode.__subclasses__():
            yield cls.__name__


class MakeScreenshotsOperator(bpy.types.Operator):
    bl_idname = "test.make_screenshots"
    bl_label = "Make Screenshots"

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)

        tree_type = context.space_data.node_tree.type
        self.node_names_iterator = islice(iter_node_names(tree_type), 10000)

        return self.prepare_next_node(context)

    def prepare_next_node(self, context):
        try:
            node_name = next(self.node_names_iterator)
        except:
            return {'FINISHED'}
        node_tree = context.space_data.node_tree
        for node in node_tree.nodes:
            node.location.x = 10000
        node = node_tree.nodes.new(node_name)
        node.select = False
        node.show_preview = False
        self.current_node = node
        self.current_name = node_name
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        temp_path = f"/home/jacques/Downloads/temp.png"
        filepath = f"/home/jacques/Downloads/node-types_{self.current_name}.png"
        bpy.ops.screen.screenshot_area(filepath=temp_path)

        rect = node_region_rect(context.region, self.current_node)
        margin = 15
        rect.x -= margin
        rect.y -= margin
        rect.width += margin * 2
        rect.height += margin * 2

        bpy.ops.screen.screenshot_area(filepath=filepath)

        cut_image(temp_path, filepath, rect)
        context.area.tag_redraw()

        return self.prepare_next_node(context)


bpy.utils.register_class(MakeScreenshotsOperator)
