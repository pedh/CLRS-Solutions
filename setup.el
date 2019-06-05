(require 'ox-publish)

(setq org-publish-project-alist
      '(("html"
	 :base-directory "."
	 :base-extension "org"
	 :publishing-directory "_build/html"
	 :exclude "README\\.org\\|_build"
	 :recursive t
	 :publishing-function org-html-publish-to-html
	 :author "pedh"
	 :email "hcn518@gmail.com"
	 :auto-sitemap t
	 :sitemap-filename "index.org"
	 :sitemap-title "CLRS Solutions"
	 :html-link-up "/project/clrs"
	 :html-link-home "/project/clrs"
	 :html-head "<link rel=\"stylesheet\" type=\"text/css\" href=\"/css/org-info.css\" />"
	 :infojs-opt "path:/js/org-info.js")
	("static"
	 :base-directory "."
	 :base-extension "py\\|c"
	 :publishing-directory "_build/html"
	 :recursive t
	 :publishing-function org-publish-attachment
	 )))
