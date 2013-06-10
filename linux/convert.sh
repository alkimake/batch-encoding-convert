#!/bin/bash

# converts xml and java files

DIR=$1

for i in $(find $DIR -name '*.xml' -or -name '*.java'); do
 iconv -f WINDOWS-1252 -t UTF8 $i -o $i."utf8";
 mv $i."utf8" $i;
done
