# -*- encoding: utf-8 -*-
# stub: jekyll-titles-from-headings 0.5.1 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-titles-from-headings".freeze
  s.version = "0.5.1".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2018-02-06"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-titles-from-headings".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "2.7.5".freeze
  s.summary = "A Jekyll plugin to pull the page title from the first Markdown heading when none is specified.".freeze

  s.installed_by_version = "3.5.22".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, ["~> 3.3".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.5".freeze])
  s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.43".freeze])
end
