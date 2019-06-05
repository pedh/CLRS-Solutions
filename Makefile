.PHONY: clean

html:
	emacs -nw --batch -l setup.el -f org-publish-all

clean:
	-rm -rf index.org
