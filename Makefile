
all:
	# './' (input), './html/' (output)
	sphinx-build -b html . ./html
	echo "firefox ./html/contents.html"

pdf:
	sphinx-build -b latex . ./latex
	make -C ./latex
	echo "evince latex/blender_manual.pdf"

clean:
	rm -rf html latex

