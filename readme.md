# To install dependencies
$ bundle install

# To start site locally
$ bundle exec jekyll serve
$ rm -rf _site/ ; bundle exec jekyll serve --incremental

# To visit site locally
http://localhost:4000 

# To regenerate tag pages
ruby ./tools/tag-gen.rb

# To consider
1. TinyLetter newsletter integration?
1. Pottery project detail
1. Better image on AdvisorPro
1. Add blog posts