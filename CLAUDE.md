# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Ruby/Jekyll Commands
- `bundle install` - Install Ruby dependencies
- `bundle exec jekyll serve` - Start local development server at http://localhost:4000
- `rm -rf _site/ ; bundle exec jekyll serve --incremental` - Clean build and serve with incremental regeneration

### NPM Commands  
- `npm run build` - Build all assets (JS, CSS, scripts)
- `npm run watch` - Watch and rebuild JS/CSS during development
- `npm run dev` - Start both asset watching and Jekyll server
- `npm run clean` - Remove built JS assets
- `npm run format` - Format JavaScript files with Prettier

### Content Management
- `ruby ./tools/tag-gen.rb` - Regenerate tag pages from blog post frontmatter

## Architecture Overview

### Jekyll Site Structure
- **Main content**: Blog posts in `professional/_posts/` with YAML frontmatter
- **Collections**: Projects in `_projects/`, tags in `_tags/`
- **Layouts**: Page templates in `_layouts/` 
- **Includes**: Reusable components in `_includes/`
- **Data**: Site data in `_data/`
- **Assets**: Images and files in `assets/`, compiled JS/CSS output

### Theme Integration
- Uses Hydejack Pro theme with extensive customization
- Theme components in `_includes/` directories (body, head, styles, components, scripts, templates)
- Custom styling in `_sass/`
- JavaScript source in `_js/` compiled via Webpack to `assets/js/`

### Build Process
- Jekyll processes Markdown/HTML and builds to `_site/`
- Webpack compiles JavaScript from `_js/src/` to `assets/js/hydejack-*.js`
- CSS built from Sass files in `_sass/`
- Site configuration in `_config.yml`

### Content Types
- **Blog posts**: Professional writing in `professional/_posts/` with tags
- **Projects**: Portfolio items in `_projects/`
- **Static pages**: Resume, hypotheses, etc. as `.md` files in root
- **Tags**: Auto-generated tag pages in `_tags/` via Ruby script

### Development Notes
- Posts use YAML frontmatter for metadata, tags, and layout selection
- Tag system generates individual tag pages automatically
- Site supports dark mode, responsive design, and offline capabilities
- Uses Google Analytics and Disqus comments integration