#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Yuliy Lobarev

__author__ = 'Yuliy Lobarev'
__description__ = 'Splitting Drupal 7 export to Hugo Markdown files.'

"""Converting export files from Drupal 7,
created by Views module
to Hugo site generator Markdown files.

The same, as for news, but for comix node types.
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
                        
            
            if line.startswith('issue:'):
                counter = 1
                continue
            
            if counter == 1:
                counter = 2
                continue
                
            if counter == 2:
                title = line.strip()
                line = '---\nissue: "' + line.strip() + '"'
                counter = 0
                outfile = open(title + ".md", 'w')
                print(title)
                
            # correcting URLs for domain and images _0.jpg)
            line = line.replace('http://umneem.org/', '/')
            line = line.replace('{.image-style-none width="800" height="2153"}', '')
            line = line.replace('/sites/default/files/', '/img/comics/')
            line = line.replace('_0.jpg', '.jpg')
                
            # adding quotes
            for variable in variables:
                if line.startswith(variable + ": "):
                    line = variable + ': "' + line[( len(variable) + 1 ):].strip() + '"'
                
                
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
    split_files("comix.md")
    return 0
    

if __name__ == "__main__":
    main()

