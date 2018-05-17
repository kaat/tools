#!/bin/bash
shopt -s nullglob;
mkdir -p out;
for file in *.vcf;
do 

  echo Converting for $file;
  iconv -f WINDOWS-1251 -t utf8 "${file}" -o "out/${file}"

done
