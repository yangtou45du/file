#!/usr/bin/env python
# -*- coding: cp936 -*-
import os
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
            print List
            dict={}
            score=[]
            for i in List:
                if i.replace(" ","").isalpha():
                    dict["name"]=i
                    #List.remove(i)
                elif i.count("-")>1:
                    dict['time']=i
                    #List.remove(i)
                else:
                    if '-' in i:
                        score.append(float(i.replace('-', '.')))
                    elif ':' in i:
                        score.append(float(i.replace(':', '.')))
                    else:
                        score.append(float(i))

            dict["score"]=list(sorted(set(score)))[:3]

            print dict

        except Exception as e:
            print 'error'+str(e)
    return dict['name']+' fastest times are '+str(dict['score'])

print change("james2.txt")
