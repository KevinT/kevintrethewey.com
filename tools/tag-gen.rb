require 'fileutils'
require 'yaml'

tags_dir = "_tags" # You can use /tags directly too
FileUtils.mkdir_p(tags_dir)

site_tags = Dir["professional/_posts/*.md"]
  .flat_map { |f| YAML.load_file(f)["tags"] || [] }
  .uniq
  .sort

site_tags.each do |tag|
  filename = File.join(tags_dir, "#{tag.downcase.strip.gsub(' ', '-')}.md")
  next if File.exist?(filename)

  File.write(filename, <<~MARKDOWN)
    ---
    layout: tag
    tag: #{tag}
    permalink: /tags/#{tag.downcase.strip.gsub(' ', '-')}/
    ---
  MARKDOWN
  puts "Created: #{filename}"
end
