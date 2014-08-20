TODO
====

Cleanup:

- Replace all instances of 'nicetip' with the '.. tip::' directive.
- Replace some unnecessary tables with bullets - eg: 'render/output/video.rst:220'
- FIXME(Link Type Unsupported: ... we have a lot of these, could automate fixes.
- There are links into http://wiki.blender.org, these need to be corrected
- Fix titles, allowing only one h1 per file (clearer menu structure)


Conventions:

- Choose a way to reference UI elements, ':guilabel:' is used all over, but may want to just use bold/italic.
- lots of lines over 120 length (low priority)
- check out the following syntax for titles

```
h1 header
*********

h2 header
=========

h3 header
---------

h4 header
~~~~~~~~~

```

Sections should be generally structured structured as follows:

- folder_name
	- index.rst (contains links to internal files)
	- introduction.rst
	- section_1.rst
	- section_2.rst
	
For example:

- rendering (folder)
	- index.rst
	- cyles (folder)
		- index.rst
		- introduction.rst
		- materials (folder)
			- index.rts
			- introduction.rst
			- volumes.rst
