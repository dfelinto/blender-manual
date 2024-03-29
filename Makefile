# -*- mode: gnumakefile; tab-width: 4; indent-tabs-mode: t; -*-
# vim: tabstop=4

define HELP_TEXT
Custom Targets
==============

Convenience targets provided for building docs.

- html (default)       to build the HTML web-site.
- singlehtml           to build the HTML web-site as a single page.
- livehtml             to auto build on file changes on host on localhost.
- epubpdf              to convert an epub file to PDF.
- readme               to make a 'readme.html' file.
- clean                to delete all old build files.

Translations
------------

- update_po            to update PO message catalogs.
- report_po_progress   to check the progress/fuzzy strings.

Checking
--------

- check_structure      to check the structure of all .rst files.
- check_syntax         to check the syntax of all .rst files.
- check_spelling       to check spelling for text in RST files.
endef
# HELP_TEXT (end)

# -----------
# System Vars
OS:=$(shell uname -s)

# End System Vars
# ---------------

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXBUILD     ?= sphinx-build
SPHINXAUTOBUILD ?= sphinx-autobuild
SOURCEDIR        = ./manual
BUILDDIR        ?= build
BF_LANG         ?= en
SPHINXOPTS      ?= -j auto -D language='$(BF_LANG)'
LATEXOPTS       ?= "-interaction nonstopmode"


# -----------------------
# for echoing output only
ifeq ($(OS), Darwin)
	OPEN_CMD="open" # MACOS.
else
	OPEN_CMD="xdg-open" # Linux/FreeBSD.
endif
# end output for echoing
# ----------------------


ifneq "$(findstring singlehtml, $(MAKECMDGOALS))" ""
	.DEFAULT_GOAL := singlehtml
else ifneq "$(findstring latexpdf, $(MAKECMDGOALS))" ""
	.DEFAULT_GOAL := latexpdf
else ifneq ("$(shell which $(SPHINXAUTOBUILD) 2> /dev/null)", "")
	.DEFAULT_GOAL := livehtml
else
	.DEFAULT_GOAL := html
endif


# --------------------
# Check commands exist

.SPHINXBUILD_EXISTS:
	@if ! which $(SPHINXBUILD) > /dev/null 2>&1; then \
		echo -e >&2 \
			"The '$(SPHINXBUILD)' command was not found.\n"\
			"Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to\n"\
			"point to the full path of the '$(SPHINXBUILD)' executable.\n"\
			"Alternatively you can add the directory with the executable to your PATH.\n"\
			"If you don't have Sphinx installed, grab it from http://sphinx-doc.org)\n"; \
		false; \
	fi

# End command checking
# --------------------

html: .SPHINXBUILD_EXISTS
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "To view, run:"
	@echo "  "$(OPEN_CMD) $(shell pwd)"/$(BUILDDIR)/html/index.html"

livehtml:
	@$(SPHINXAUTOBUILD) --open-browser --delay 0 "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

latexpdf: .SPHINXBUILD_EXISTS
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@make -C "$(BUILDDIR)/latex" LATEXOPTS="-interaction nonstopmode"
	@echo "To view, run:"
	@echo "  "$(OPEN_CMD) $(shell pwd)"/$(BUILDDIR)/latex/blender_manual.pdf"

epubpdf: .SPHINXBUILD_EXISTS
	@$(SPHINXBUILD) -M epub "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@ebook-convert $(BUILDDIR)/epub/*.epub blender_manual.pdf \
		--pdf-default-font-size 16 \
		--pdf-mono-font-size 14 \
		--margin-left 0 \
		--margin-right 0 \
		--pdf-page-margin-left 50 \
		--pdf-page-margin-right 50 \
		--pdf-page-margin-top 50 \
		--pdf-page-margin-bottom 50 \

readme:
	@rst2html5 readme.rst > $(BUILDDIR)/readme.html
	@echo "Build finished. The HTML page is in $(BUILDDIR)/readme.html."
	@echo "To view, run:"
	@echo "  "$(OPEN_CMD) $(shell pwd)"/$(BUILDDIR)/readme.html"

check_syntax:
	@python3 tools_rst/rst_check_syntax.py --long --title --kbd > rst_check_syntax.log
	@echo "Lines:" `cat rst_check_syntax.log | wc -l`
	@python3 tools/open_quickfix_in_editor.py rst_check_syntax.log
	@rm rst_check_syntax.log

check_structure:
	@python3 tools_rst/rst_check_images.py

check_spelling:
	@python3 tools_rst/rst_check_spelling.py

update_po:
	@python3 ./tools_maintenance/update_po.py

report_po_progress:
	@python3 tools_report/report_translation_progress.py --quiet \
	         `find locale/ -maxdepth 1 -mindepth 1 -type d -not -iwholename '*.svn*' -printf 'locale/%f\n' | sort`

# ----------------------
# Help for build targets

export HELP_TEXT
help:
	@echo ""
	@echo "Sphinx"
	@echo "======"
	@echo ""
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "$$HELP_TEXT"

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option. $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile .SPHINXBUILD_EXISTS
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
