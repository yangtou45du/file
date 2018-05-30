#!/usr/bin/env python
# -*- coding: cp936 -*-
import os
#1.文件读写过程
'''
统计三个文件最大的三个数
jamesDate=open("jamesDate.txt")
julieData=open("julie.txt")
mikeyData=open("mikey.txt")
sarahData=open("sarah.txt")
'''
def change(filename):
    if os.path.exists(filename):
        List=[]
        try:
            Data=open(filename)
            for line in Data:
                try:
                    List=line.strip('\n').split(',')
                except Exception as e:
                    print "err"+str(e)
            #print List
            for i in range(0,len(List)):
                if '-' in List[i]:
                    List[i]=float(List[i].replace('-','.'))
                elif ':'in List[i]:
                    List[i]=float(List[i].replace(':','.'))
                else:
                    List[i]=float(List[i])
        except Exception as e:
            print 'error'+str(e)
        # set 去重，sorted排序
        finally:
            Data.close()
        #print set(List)
        #print (sorted(set(List)))
        return list(sorted(set(List)))[:3]
    else:
        return (filename+' not exists')
    #print jamesList

jamesList=change('james.txt')
print jamesList
julieList=change('julie.txt')
print julieList
mikeyList=change('mikey.txt')
print mikeyList
sarahList=change('sarah.txt')
print sarahList







