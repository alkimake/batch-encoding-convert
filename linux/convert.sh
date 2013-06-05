#!/bin/bash

# converts xml and java files

DIR=$1

for f1 in $(find $DIR -name '*.xml' -or -name '*.java'); do
 print "Converting: $fl"
 mv $fl $fl.old
 sed 's/$'"/`echo \\\r`/" $fl.old >> $f1
 rm -f $fl.old
done