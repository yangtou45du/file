#!/usr/bin/env python
# -*- coding: cp936 -*-
#1.�ļ���д����
helloFile=open("d:\\lianxi\\file\\hello.txt",'w+')
helloFile.write('helloContent')
helloFile.seek(0,0)
content=helloFile.read()
print(content)
print(helloFile.tell())
helloFile.close()
