# -*- encoding: utf-8 -*-
# stub: jekyll-replace-img 0.5.0 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-replace-img".freeze
  s.version = "0.5.0".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Florian Klampfer".freeze]
  s.date = "2019-08-24"
  s.email = ["mail@qwtel.com".freeze]
  s.homepage = "https://github.com/qwtel/jekyll-replace-img".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "2.5.2.3".freeze
  s.summary = "A Jekyll plugin to replace <img/> tags with custom elements.".freeze

  s.installed_by_version = "3.5.22".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, ["~> 3.3".freeze])
  s.add_development_dependency(%q<nokogiri>.freeze, ["~> 1.10".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.5".freeze])
  s.add_development_dependency(%q<rubocop>.freeze, [">= 0.49.0".freeze, "< 1.0.0".freeze])
  s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.7.0".freeze])
end
