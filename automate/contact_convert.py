#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 Yuliy Lobarev

__author__ = 'Yuliy Lobarev'
__description__ = 'Converting Windows contact files to proper format for future export to Vcard.'

"""Converting Windows contact files to proper format
for future export to Vcard.

These improper Contact files are produced during
contact syncronisation from Iphone via Itunes to Windows 7 OS.

The script works on a folder with Contact files.
"""
import os

def convert_files(filepath, filepathout):
    """Function to conver Windows .contact files.
    
    Syntax: convert_files(input_folder, output_folder)
    """
    outfile = None
    fileslist = []
    # Magic strings to insert phone between them
    insertpart1 = '<c:PhoneNumberCollection c:Version="1" ' + \
        'c:ModificationDate="2018-05-17T07:51:56Z">' + \
        '<c:PhoneNumber c:ElementID="6dff7e9d-94f7-4cca-97e7-6d5eb5458e6e" ' + \
        'c:Version="1" c:ModificationDate="2018-05-17T07:51:56Z">' + \
        '<c:Number c:Version="1" c:ModificationDate="2018-05-17T07:51:56Z">'
    insertpart2 = '</c:Number><c:LabelCollection>' + \
        '<c:Label c:Version="1" c:ModificationDate="2018-05-17T07:51:56Z">' + \
        'Voice</c:Label><c:Label c:Version="1" ' + \
        'c:ModificationDate="2018-05-17T07:51:56Z">' + \
        'Personal</c:Label></c:LabelCollection>' + \
        '</c:PhoneNumber></c:PhoneNumberCollection></c:contact>'

    for file in os.listdir(filepath):
        if file.endswith(".contact"):
            fileslist.append(file)
    for filename in fileslist:
              
        with open( os.path.join(filepath, filename), encoding='utf_8') as infile, \
            open( os.path.join(filepathout, filename ), 'w', encoding='utf_8') as outfile:
            print("Converting file " + filename)
            
            for line in infile:
                # Finding a line with number and extracting number.
                if line.find('PropTag0x800A001F') > 0:
                    phonebegins = line.find('c:type="string">') + 16
                    phoneends = line.find('</MSWABMAPI:')
                    phone = line[phonebegins:phoneends].strip()
                    print('Phone number: ',  phone)
                    
                # Finding a line to insert a number.
                if line.find('<c:ContactIDCollection>') > 0:
                    insertposition = len(line) - len('</c:contact>') - 1
                    line = line[0:insertposition] + insertpart1 + phone + insertpart2
                    
                # saving lines to file
                outfile.write(line)
            
            # finishing with the file
            outfile.close()

    return 0
                
                
def main():
    """The main list of commands.
    """
    # converting the files
    # assuming that the script exists in the folder
    # with input and output folders
    print("Running conversion...")
    convert_files("in", "out")
    return 0
    

if __name__ == "__main__":
    main()

