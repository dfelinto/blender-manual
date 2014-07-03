
FIXME(Template Unsupported: Doc:2.6/Reference/Nodes/Node Editor;
{{Doc:2.6/Reference/Nodes/Node Editor}}
)


Buttons for work with Compositing nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure:: /images/26-Manual-Compositing-Node-Header-Additionally.jpg

   Buttons for work with Compositing nodes


Free Unused Button
__________________


This button frees up memory space when you have a very complex node map. Recommended.


Backdrop
________


Use the active viewer node output as a backdrop. When enabled,
additional settings appear in the Header and the Properties Panel:


.. figure:: /images/26-Manual-Compositing-Node-Header-Backdrop-Channels.jpg

   Backdrop Channels.


:guilabel:`Backdrop Channels`
   Set the image to be displayed with :guilabel:`Color`\ , :guilabel:`Color and Alpha`\ , or just :guilabel:`Alpha`\ .


.. figure:: /images/26-Manual-Compositing-Node-Header-Zoom-Offset.jpg

   Options of Zoom and Offset of Backdrop.


:guilabel:`Zoom`
   Sets how big the backdrop image is.
:guilabel:`Offset`
   Change the screen space position of the backdrop, or click the :guilabel:`Move` button, or shortcut :kbd:`Alt-mmb` to manually move it.


Auto Render
___________


Re-render and composite changed layer when edits to the 3d scene are made.


Perfomance for Compositing Nodes in Node Editor
-----------------------------------------------


.. figure:: /images/26-Manual-Compositing-Node-Panel-Perfomance.jpg

   Perfomance for Compositing Nodes in Node Editor


:guilabel:`Render`
   Set quality when rendering in Node Editor.
:guilabel:`Edit`
    Set quality when editing in Node Editor
:guilabel:`Chunksi`
   Max size of a title (smaller values give better distribution of multiple threads, but more overhead).
:guilabel:`OpenCL`
   Enable GPU calculations when working in Node Editor.
:guilabel:`Buffer Groups`
   Enable buffering of group nodes.
:guilabel:`Two Pass`
   Use two pass execution during editing: first calculate fast nodes, second pass calculate all nodes.
:guilabel:`Viewer Border`
   Use boundaries for viewer nodes and composite backdrop.
:guilabel:`Highlight`
   Highlight nodes that are being calculated.