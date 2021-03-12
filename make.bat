@ECHO OFF

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=./manual
set BUILDDIR=build
set BF_LANG=en
set SPHINXOPTS=-j auto -D language='%BF_LANG%'

REM Check if sphinx-build is available and fallback to Python version if any
%SPHINXBUILD% 1>NUL 2>NUL
if errorlevel 9009 goto sphinx_python
goto sphinx_ok

:sphinx_python

set SPHINXBUILD=python -m sphinx.__init__
%SPHINXBUILD% 2> nul
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

:sphinx_ok

REM Default to HTML
if "%1" == "" (
	goto html
)

if "%1" == "help" (
	echo.
	echo.Sphinx
	echo.======
	%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	echo.
	echo.Custom Targets
	echo.==============
	echo.Convenience targets provided for building docs
	echo.
	echo.- livehtml             to auto build on file changes on host on localhost
	echo.- readme               to make a 'readme.html' file
	echo.- clean                to delete all old build files
	echo.
	echo.Translations
	echo.------------
	echo.
	echo.- update_po            to update PO message catalogs
	echo.- report_po_progress   to check the progress/fuzzy strings
	echo.
	echo.Checking
	echo.--------
	echo.
	echo.- check_structure      to check the structure of all .rst files
	echo.- check_syntax         to check the syntax of all .rst files
	echo.- check_spelling       to check spelling for text in RST files
	goto EOF
)

if "%1" == "livehtml" (
	sphinx-autobuild --open-browser %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	if errorlevel 1 exit /b 1
	goto EOF
)

if "%1" == "html" (
	:html
	%SPHINXBUILD% -b html %SPHINXOPTS% %O% %SOURCEDIR% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.To view, run:
	echo.  start %BUILDDIR%/html/index.html
	goto EOF
)

if "%1" == "latexpdf" (
	%SPHINXBUILD% -b latex %SPHINXOPTS% %O% %SOURCEDIR% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf
	cd %~dp0
	echo.To view, run:
	echo.  start %BUILDDIR%/html/blender_manual.pdf
	goto EOF
)

if "%1" == "translations" (
	%SPHINXBUILD% -b html -D language='%2' %SPHINXOPTS% %O% %SOURCEDIR% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.  start %BUILDDIR%/html/index.html
	goto EOF
)

if "%1" == "readme" (
	rst2html5.py readme.rst > build/readme.html
	echo.Build finished. The HTML page is in %BUILDDIR%/readme.html.
	echo.To view, run:
	echo.  start %BUILDDIR%/readme.html
	goto EOF
)

if "%1" == "check_syntax" (
	python tools_rst/rst_check_syntax.py --kbd --long
	goto EOF
)

if "%1" == "update_po" (
	python tools_maintenance/update_po.py
	goto EOF
)

if "%1" == "report_po_progress" (
	IF NOT EXIST %cd%/locale GOTO MISSING_LOCALE
	python tools_report/report_translation_progress.py locale/%2 --quiet
	goto EOF

)

if "%1" == "check_spelling" (
	echo. here
	python tools_rst/rst_check_spelling.py
	goto EOF
)

if "%1" == "check_structure" (
	python tools_rst/rst_check_images.py
	goto EOF

) else (
	%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
	goto EOF
)

:EOF
