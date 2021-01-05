# -----------
# System Vars
OS:=$(shell uname -s)

# End System Vars
# ---------------

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./manual
BUILDDIR      = build
BF_LANG       ?= en
SPHINXOPTS    ?= -j auto -D language='$(BF_LANG)'
LATEXOPTS     ?= "-interaction nonstopmode"

# full paths
CHAPTERS_FULL:=$(filter %/, $(wildcard manual/*/))
# names only
CHAPTERS:=$(notdir $(sort $(CHAPTERS_FULL:%/=%)))
# intersect make goals and possible chapters
QUICKY_CHAPTERS=$(filter $(MAKECMDGOALS),$(CHAPTERS))


# -----------------------
# for echoing output only
ifeq ($(QUICKY_CHAPTERS), )
	CONTENTS_HTML="index.html"
else
	CONTENTS_HTML="contents_quicky.html"
endif

# os specific
ifeq ($(OS), Darwin)
	# OSX
	OPEN_CMD="open"
else
	# Linux/FreeBSD
	OPEN_CMD="xdg-open"
endif
# end output for echoing
# ----------------------


ifneq "$(findstring singlehtml, $(MAKECMDGOALS))" ""
	.DEFAULT_GOAL := singlehtml
else ifneq "$(findstring latexpdf, $(MAKECMDGOALS))" ""
	.DEFAULT_GOAL := latexpdf
else
	.DEFAULT_GOAL := html
endif


$(CHAPTERS): $(.DEFAULT_GOAL)


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
	@QUICKY_CHAPTERS=$(QUICKY_CHAPTERS) \
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "To view, run:"
	@echo "  "$(OPEN_CMD) $(shell pwd)"/$(BUILDDIR)/html/$(CONTENTS_HTML)"

latexpdf: .SPHINXBUILD_EXISTS
	@QUICKY_CHAPTERS=$(QUICKY_CHAPTERS) \
	$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@make -C "$(BUILDDIR)/latex" LATEXOPTS="-interaction nonstopmode"
	@echo "To view, run:"
	@echo "  "$(OPEN_CMD) $(shell pwd)"/$(BUILDDIR)/latex/blender_manual.pdf"

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
	@python3 tools_rst/rst_check_locale.py

check_spelling:
	@python3 tools_rst/rst_check_spelling.py

update_po:
	@python3 ./tools_maintenance/update_po.py

report_po_progress:
	@python3 tools_report/report_translation_progress.py --quiet \
	        `find locale/ -maxdepth 1 -mindepth 1 -type d -not -iwholename '*.svn*' -printf 'locale/%f\n' | sort`

# ----------------------
# Help for build targets

help:
	@echo ""
	@echo "Sphinx"
	@echo "======"
	@echo ""
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Custom Targets"
	@echo "=============="
	@echo "Convenience targets provided for building docs"
	@echo ""
	@echo "- readme               to make a 'readme.html' file"
	@echo "- clean                to delete all old build files"
	@echo ""
	@echo "Chapters               to quickly build a single chapter"
	@$(foreach ch,$(CHAPTERS),echo "- "$(ch);)
	@echo ""
	@echo "Translations"
	@echo "------------"
	@echo ""
	@echo "- update_po            to update PO message catalogs"
	@echo "- report_po_progress   to check the progress/fuzzy strings"
	@echo ""
	@echo "Checking"
	@echo "--------"
	@echo ""
	@echo "- check_structure      to check the structure of all .rst files"
	@echo "- check_syntax         to check the syntax of all .rst files"
	@echo "- check_spelling       to check spelling for text in RST files"
	@echo ""

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option. $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile .SPHINXBUILD_EXISTS
	@QUICKY_CHAPTERS=$(QUICKY_CHAPTERS) \
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
