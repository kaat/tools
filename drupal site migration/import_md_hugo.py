#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Yuliy Lobarev


__author__ = 'Yuliy Lobarev'
__description__ = 'Splitting Drupal 7 export to Hugo Markdown files.'

"""Converting export files from Drupal 7,
created by Views module
to Hugo site generator Markdown files.

The converter is for news node types.
"""


def split_files(infilepath):
    """Function to find lines to split at and to do the splitting.
    
    Syntax: split_files(file_path_to_look_for_files)
    """
    title = None
    outfile = None
    accumulator = ""
    variables=["title", "categories",  "Nid", "description", "layout"]
    with open(infilepath) as infile:
        for line in infile:
            line = line.strip()
                        
            # finding file name         
            if line.startswith('Nid:'):
                title = line[4:].strip()
                outfile = open(title + ".md", 'w')
                print(title)
                
            if line.startswith('description:'):
                line = line.replace('"', '')
                
            # adding quotes
            for variable in variables:
                if line.startswith(variable + ": "):
                    line = variable + ': "' + line[( len(variable) + 1 ):].strip() + '"'
                
            # saving the title before writing to the file
            if line.startswith('title:'):
                accumulator = "---\n" + line
                
            # adding the line with Nid to the saved lines
            if line.startswith('Nid:'):
                line = accumulator + "\n\n" + line
                
            # YAML header finishing
            if line == 'content-begins:':
                line = "---"
    
            
            # finding beginnings and ends of each part and saving it
            if line.startswith('title:') and (outfile is None):
                line = "---\n" + line
                continue
            elif line.startswith('---end-of-content---:'):
                outfile.close()
                outfile = None
                continue
            elif outfile is not None:
                outfile.write(line + '\n')
    return 0
                
                
def main():
    """The main list of commands.
    """
    # splitting the file
    split_files("import.md")
    return 0
    

if __name__ == "__main__":
    print("running conversion...")
    main()

