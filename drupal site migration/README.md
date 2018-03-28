# Drupal 7 to Hugo site migration #

These tools were created to migrate a dynamic Drupal site to a static one.
At first I thought to use RSS feeds as a source for migration, but decided to use Views module, which I used already to create RSS feeds on the site. I could create a data structure, similar to Hugo's MD files with Front Matter. But it needed some andjustments.
To create MD files from HTML I used Pandoc. The HTML file was saved from the link, created by the Views module, then I removed everything before and after these tags:

    <!-- !Feed Icons -->
    <!-- !Main Content -->

    pandoc --wrap=none news.html -o news.md

Then I used Sed to remove HTML tags:

    cat news.md | sed '/</ {:k s/<[^>]*>//g; /</ {N; bk}}' | sed '/^$/N;/^\n$/D' > news_txt.md

The resulting file can be converted with the Python scripts and copied to a Hugo content folder:

    import_md_hugo_comix.py
    import_md_hugo.py
    import_md_hugo_articles.py

Another tool is used to convert existing MD files created by Pandoc from DOCX files to Hugo compartible MD files with a Front Matter. Basically the tool transforms this header:

    ## Глава 1. Крайне маловероятный день
    
    ...

to that header:

    ---
    title: "Глава 1. Крайне маловероятный день"
    description: "Глава 1. Крайне маловероятный день"
    categories: "глава"
    layout: "chapters"
    weight: "1"
    date: "2013-11-27"
    lastmod: "2018-03-14"
    ---
    
    ...


## Examples ##

TXT files are exported settings from Views module.
MD files are example of exported content after executing two commands above.

