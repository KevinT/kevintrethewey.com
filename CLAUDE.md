# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Ruby/Jekyll Commands
- `bundle install` - Install Ruby dependencies
- `bundle exec jekyll serve` - Start local development server at http://localhost:4000
- `rm -rf _site/ ; bundle exec jekyll serve --incremental` - Clean build and serve with incremental regeneration
- `JEKYLL_ENV=production bundle exec jekyll serve` - Serve with production environment settings

### NPM Commands
- `npm run build` - Build all assets (JS, CSS, scripts in parallel)
- `npm run watch` - Watch and rebuild JS/CSS during development (combines watch:js and watch:css)
- `npm run dev` - Start both asset watching and Jekyll server concurrently
- `npm run clean` - Remove built JS assets from assets/js/
- `npm run format` - Format JavaScript files with Prettier

### Content Management
- `ruby ./tools/tag-gen.rb` - Regenerate tag pages in `_tags/` from post frontmatter tags

## Architecture Overview

### Jekyll Site Structure
- **Main content**: Writing posts in `professional/_posts/` with YAML frontmatter
- **Collections**: Projects in `_projects/`, tags in `_tags/`, featured_categories, featured_tags
- **Layouts**: Page templates in `_layouts/` (base, default, post, project, blog, etc.)
- **Includes**: Reusable components in `_includes/` (body, head, styles, components, scripts, templates)
- **Data**: Site data in `_data/` (authors.yml, social.yml, strings.yml, countries.yml)
- **Assets**: Images and files in `assets/`, compiled JS/CSS output

### Theme Integration (Hydejack Pro)
- Based on Hydejack Pro theme with extensive customization
- Theme Sass files organized into `_sass/hydejack/`, `_sass/pooleparty/`, `_sass/pro/`
- Custom overrides in `_sass/my-inline.scss` and `_sass/my-variables.scss`
- JavaScript source in `_js/src/` (entry.js, push-state.js, drawer.js, images.js, etc.)
- Webpack compiles to versioned bundles: `assets/js/hydejack-8.5.2.js` and `hydejack-legacy-8.5.2.js`

### Build Process Flow
1. **Jekyll build**: Processes Markdown/HTML/Liquid → `_site/`
2. **Webpack JS build**: `_js/src/entry.js` → two bundles (modern + legacy with different Babel presets)
   - Modern: ES modules target for modern browsers
   - Legacy: Full polyfills for older browsers (uses @babel/polyfill, core-js)
3. **CSS/Sass build**: `_sass/**/*.scss` → compiled CSS (processed by Jekyll's Sass pipeline)
4. **Script minification**: Minifies scripts in `_includes/scripts/*.js` with uglifyjs

### Content Types & Frontmatter
- **Writing posts**: `professional/_posts/YYYY-MM-DD-title.md` with layout, date, categories, tags
- **Projects**: `_projects/*.md` with custom frontmatter for portfolio items
- **Static pages**: Resume, hypotheses, etc. as `.md` files in root
- **Tags**: Auto-generated via tag-gen.rb from post frontmatter tags field

### Key Configuration (_config.yml)
- Permalink structure: `/blog/:categories/:year-:month-:day-:title/`
- Pagination: 10 posts per page at `/blog/page-:num/`
- Collections: featured_categories, featured_tags, projects, tags (all with output: true)
- Plugins: jekyll-feed, jekyll-paginate, jekyll-seo-tag, jekyll-sitemap, jekyll-replace-img, etc.
- Hydejack settings: post_addons, project_addons, dark_mode config, offline mode

### Important Patterns
- **Tag workflow**: Add tags to post frontmatter → run `ruby ./tools/tag-gen.rb` → generates individual tag pages
- **Asset versioning**: JavaScript bundles use package.json version (8.5.2) in filename
- **Sass architecture**: Splits between `__inline__` (inlined in head) and `__link__` (external stylesheet) for performance
- **Build parallelization**: npm build uses `&` and `wait` to run JS/CSS/scripts builds concurrently

### Development Notes
- Site uses Google Analytics (UA-146968-7) and Disqus (kevint) integration
- Dark mode support available but set to manual (dynamic: false)
- Offline PWA capabilities available but disabled by default
- Custom elements and web components used for progressive enhancement (hy-drawer, hy-img, hy-push-state)
- never mention claude code in commit messages