#!/usr/local/bin/python3

print ("Hello World")

import sys
print (sys.path)


fr = open("data/foo.txt", "r+")
str = fr.read(5)
print ("Foo file content: ", str)
fr_position = fr.tell()
print ("File positon : ", fr_position)


fr.close()

fo = open ("data/foowrite.txt", "wb")
print ("File name:", fo.name)




