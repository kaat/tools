#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Yuliy Lobarev

__author__ = 'Yuliy Lobarev'
__description__ = 'Splitting Drupal 7 export to Hugo Markdown files.'

"""Converting export files from Drupal 7,
created by Views module
to Hugo site generator Markdown files.

The same, as for news, but for article node types.
"""


def split_files(infilepath):
    """Function to find lines to split at and to do the splitting.
    
    Syntax: split_files(file_path_to_look_for_files)
    """
    title = None
    outfile = None
    counter = 0
    variables=["title", "categories", "layout"]
    with open(infilepath) as infile:
        for line in infile:
            line = line.strip()
                        
            # finding file name         
            if line.startswith('title:'):
                title = line[6:].strip()
                outfile = open(title + ".md", 'w')
                print(title)
            
            # using Nid to create aliases
            if line.startswith('Nid:'):
                line = 'aliases: \n      - /' + line[4:].strip() + '/'
                
            # three parts desription assembling, also adding quotes
            if line.startswith('description:'):
                counter = 1
                continue
            
            if counter == 1:
                counter = 2
                continue
                
            if counter == 2:
                line = 'description: "' + line.replace('"', '').strip() + '"'
                counter = 0
                
            # correcting URLs for domain and images: 
            # /sites/default/files/styles/large/public/field/image/
            line = line.replace('http://umneem.org/', '/')
            line = line.replace('{.flowr}', '')
            line = line.replace('{.flowl}', '')
            line = line.replace('/sites/default/files/styles/large/public/field/image/', \
                '/static/img/')
                
            # adding quotes
            for variable in variables:
                if line.startswith(variable + ": "):
                    line = variable + ': "' + line[( len(variable) + 1 ):].strip() + '"'
                
            # adding --- to the title
            if line.startswith('title:'):
                line = "---\n" + line
                
            # YAML header finishing
            if line == 'content-begins:':
                line = "---"
    
            # finding beginnings and ends of each part and saving it
            if line.startswith('---end-of-content---:'):
                outfile.close()
                outfile = None
                continue
            elif outfile is not None:
                outfile.write(line + '\n')
    return 0
                
                
def main():
    """The main list of commands.
    """
    print("Running conversion...")
    # splitting the file
    split_files("import_art.md")
    return 0
    

if __name__ == "__main__":
    main()

