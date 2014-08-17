
all:
	# './' (input), './html/' (output)
	sphinx-build -b html ./manual ./html
	echo "firefox ./html/contents.html"

pdf:
	sphinx-build -b latex ./manual ./latex
	make -C ./latex
	echo "evince latex/blender_manual.pdf"

clean:
	rm -rf html latex

