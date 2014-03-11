# Various useful utilities for the pipeline.
# First command (splitPath) is from Rubra
import sys
import os.path

def splitPath(path):
    (prefix, base) = os.path.split(path)
    (name, ext) = os.path.splitext(base)
    return (prefix, name, ext)

def isGenbank(refFile):
    ref_file = open(refFile, "rU")
    line = ref_file.readline()
    ref_file.close()
    return line.startswith('LOCUS')   

def isFasta(refFile):
    ref_file = open(refFile, "rU")
    line = ref_file.readline()
    ref_file.close()
    return line.startswith('>')   

# get first value from a simple file
def getValue(coverFile):
    file = open(coverFile, "r")
    values = file.readline()
    file.close()
    valueList = values.split()
    value = valueList[0]
    return value

# get the cover (depth) for a replicon from the coverage file 
# and return as integer * 2
def getCover(coverFile, replicon):
    file = open(coverFile, "r")
    if replicon.find('.') != -1:
        temp_rep = replicon.split('.')
        replicon = temp_rep[0]
    for line in file:
        if line.startswith(replicon):
            values = line.split()
            value = int(float(values[2]) * 2)
    file.close()
    return value

#turn a replicon into a key value(integer) for 'hash' table
def get_key(name):
    out_number = 0
    for letter in range(0, len(name)):
        char = name[letter]
        try:
            out = int(char)
        except:
            if (char.upper()=='A') or (char.upper()=='J') or (char.upper()=='S'):
                out = 1
            elif (char.upper()=='B') or (char.upper()=='K') or (char.upper()=='T'):
                out = 2
            elif (char.upper()=='C') or (char.upper()=='L') or (char.upper()=='U'):
                out = 3
            elif (char.upper()=='D') or (char.upper()=='M') or (char.upper()=='V'):
                out = 4
            elif (char.upper()=='E') or (char.upper()=='N') or (char.upper()=='W'):
                out = 5
            elif (char.upper()=='F') or (char.upper()=='O') or (char.upper()=='X'):
                out = 6
            elif (char.upper()=='G') or (char.upper()=='P') or (char.upper()=='Y'):
                out = 7
            elif (char.upper()=='H') or (char.upper()=='Q') or (char.upper()=='Z'):
                out = 8
            elif (char.upper()=='I') or (char.upper()=='R'):
                out = 9
            else:
                out = 9
        out_number += out
    out_number = out_number*(out+1)
    return out_number