# Drupal 7 to Hugo site migration #

These tools were created to migrate a dynamic Drupal site to a static one.
At first I thought to use RSS feeds as a source for migration, but decided to use Views module, which I used already to create RSS feeds on the site. I could create a data structure, similar to Hugo's MD files with Front Matter. But it needed some andjustments.
To create MD files from HTML I used Pandoc. The HTML file was saved from the link, created by the Views module, then I removed everything before  <code><!-- !Main Content --></code> and after <code><!-- !Feed Icons --></code>  tags.

<code>pandoc --wrap=none news.html -o news.md</code> 

Then I used Sed to remove HTML tags:

<code>cat news.md | sed '/</ {:k s/<[^>]*>//g; /</ {N; bk}}' | sed '/^$/N;/^\n$/D' > news_txt.md</code> 

The resulting file can be converted with the Python scripts and copied to a Hugo content folder.


## Examples ##

TXT files are exported settings from Views module.
MD files are example of exported content after executing two commands above.

