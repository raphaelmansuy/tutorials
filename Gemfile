source "https://rubygems.org"

# Jekyll version
gem "jekyll", "~> 4.3"

# GitHub Pages compatibility
gem "github-pages", group: :jekyll_plugins

# Essential plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-paginate", "~> 1.1"
  gem "jekyll-gist", "~> 1.5"
  gem "jekyll-include-cache", "~> 0.2"
end

# Theme (optional - using custom CSS instead)
# gem "minima", "~> 2.5"

# Performance gems
gem "liquid-c", "~> 4.0" if RUBY_PLATFORM !~ /mswin|mingw|java/

# Windows and JRuby support
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Windows does not include zoneinfo files, so bundle them
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# HTTP client
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]

# Development gems
group :development do
  gem "bundle-audit", "~> 0.1"
end
