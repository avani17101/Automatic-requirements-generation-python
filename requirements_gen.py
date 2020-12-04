#!/usr/bin/env python
# coding: utf-8

#usage: python3 requirements_gen.py 
#python3 requirements_gen.py <path dir> <subdir_flag>
#subdir_flag = 1 if want to get libs of sub directory




import os
import numpy as np
import sys


def scan_sub(pw):
    #get all files with .py or .ipynb
    py_files = []
    for it in os.scandir(pw):
        if it.is_dir():
            for file in os.listdir(it.path):
                if file.endswith(".py") or file.endswith(".ipynb"):
                    py_files.append(os.path.join(it.path, file))
    return py_files

sub_dir = 0
py_files = []

# handle args
pw = os.getcwd()
if(len(sys.argv)>1):
    print(sys.argv[1])
    if(sys.argv[1]=='1' or sys.argv[1]=='0'):
        sub_dir = 1
    else: 
	    pw = (sys.argv[1])
else:
    pw = os.getcwd()
if(len(sys.argv)>2):
    if(sys.argv[2]==1):  #subdirectories to be scanned
        sub_dir=1

if(sub_dir==0):
    for file in os.listdir(pw):
        if file.endswith(".py") or file.endswith(".ipynb"):
            py_files.append(os.path.join(pw, file))
else:
    py_files = scan_sub(pw)
print(py_files)


# get all libs from a file
def get_libs(file_name):
    with open(file_name) as f:
        s = []
        for line in f:
            if("import" in line and "i"==line[0]):
                l = line.split(' ')
                lib = l[1].replace('\n','')
                if "." in lib:
                    lib = lib.split('.')
                    s.append(lib[0])
                else:
                    s.append(lib)
            if("from" in line and "f"==line[0]):
                l = line.split(' ')
                lib = l[1].replace('\n','')
                if "." in lib:
                    lib = lib.split('.')
                    s.append(lib[0])
                else:
                    s.append(lib)
    return s

#appending libaries of all python files
raw_reqs = []
for f in py_files:
    libs = get_libs(f)
    if(len(libs)!=0):
        raw_reqs.extend(libs)
        
#writing to requirements.txt (note: this is raw requirements user must look into compatibility etc)
raw_reqs = np.array(raw_reqs)
raw_reqs = np.unique(raw_reqs)

f = open('requirements.txt','w')
for lib in raw_reqs:
    lib = lib.replace(',','')
    print(lib)
    f.write(lib)
    f.write('\n')
f.close()

