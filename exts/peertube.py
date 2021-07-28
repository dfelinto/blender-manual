#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from sphinx.environment import BuildEnvironment
from sphinx.locale import __
from sphinx.util import logging

logger = logging.getLogger(__name__)

def get_size(d, key):
    if key not in d:
        return None
    m = re.match("(\d+)(|%|px)$", d[key])
    if not m:
        raise ValueError("invalid size %r" % d[key])
    return int(m.group(1)), m.group(2) or "px"

def css(d):
    return "; ".join(sorted("%s: %s" % kv for kv in d.items()))

class peertube(nodes.General, nodes.Element): pass

def visit_peertube_node(self, node):
    instance = node["instance"]
    aspect = node["aspect"]
    width = node["width"]
    height = node["height"]

    if not (self.config.peertube_instance or instance):
        logger.warning(__("No peertube instance defined"))
        return

    if instance is None:
        instance = self.config.peertube_instance

    if aspect is None:
        aspect = 16, 9

    div_style = {}
    if (height is None) and (width is not None) and (width[1] == "%"):
        div_style = {
            "padding-bottom": "%f%%" % (width[0] * aspect[1] / aspect[0]),
            "width": "%d%s" % width,
            "position": "relative",
        }
        style = {
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
        }
        attrs = {
            "src": instance + "videos/embed/%s" % node["id"],
            "style": css(style),
        }
    else:
        if width is None:
            if height is None:
                width = 560, "px"
            else:
                width = height[0] * aspect[0] / aspect[1], "px"
        if height is None:
            height = width[0] * aspect[1] / aspect[0], "px"
        style = {
            "width": "%d%s" % width,
            "height": "%d%s" % (height[0], height[1]),
        }
        attrs = {
            "src": instance + "videos/embed/%s" % node["id"],
            "style": css(style),
        }
    attrs["allowfullscreen"] = "true"
    div_attrs = {
        "CLASS": "peertube_wrapper",
        "style": css(div_style),
    }
    self.body.append(self.starttag(node, "div", **div_attrs))
    self.body.append(self.starttag(node, "iframe", **attrs))
    self.body.append("</iframe></div>")

def depart_peertube_node(self, node):
    pass

def visit_peertube_node_latex(self, node):
    instance = node["instance"]

    if not (self.config.peertube_instance or instance):
        logger.warning(__("No peertube instance defined"))
        return

    if instance is None:
        instance = self.config.peertube_instance

    self.body.append(r'\begin{quote}\begin{center}\fbox{\url{' + instance + r'videos/watch/%s}}\end{center}\end{quote}'%node['id'])


class PeerTube(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "instance": directives.unchanged,
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
    }

    def run(self):
        instance = self.options.get("instance")
        if "aspect" in self.options:
            aspect = self.options.get("aspect")
            m = re.match("(\d+):(\d+)", aspect)
            if m is None:
                raise ValueError("invalid aspect ratio %r" % aspect)
            aspect = tuple(int(x) for x in m.groups())
        else:
            aspect = None
        width = get_size(self.options, "width")
        height = get_size(self.options, "height")
        return [peertube(id=self.arguments[0], instance=instance, aspect=aspect, width=width, height=height)]


def unsupported_visit_peertube(self, node):
    self.builder.warn('PeerTube: unsupported output format (node skipped)')
    raise nodes.SkipNode


_NODE_VISITORS = {
    'html': (visit_peertube_node, depart_peertube_node),
    'latex': (visit_peertube_node_latex, depart_peertube_node),
    'man': (unsupported_visit_peertube, None),
    'texinfo': (unsupported_visit_peertube, None),
    'text': (unsupported_visit_peertube, None)
}


def setup(app):
    app.add_node(peertube, **_NODE_VISITORS)
    app.add_directive("peertube", PeerTube)
    app.add_config_value('peertube_instance', "", True, [str])
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
