# take attendence easily
import os
import csv
import tkinter


def read_csv(filename):
    data = []
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        for i in rdr:
            if rdr.line_num == 1:
                continue
            if len(i)>0:
                data.append(i)
    return data

def bin_search(data,c,x):
    '''binary search for x in data in col c
    consider data as 2d list [[a,1],[b,2]]'''
    ul = len(data)
    ll = 0
    mid = ul//2
    while ul > ll:
        mid = (ul - ll)//2 +ll #??
        if data[mid][c] > x:
            ll = mid +1
        elif data[mid][c] < x:
            ul = mid -1
        elif data[mid][c] == x:
            return mid
    return -1

def mark_absent(data,reg_id):
    #data[1]
    #get id using bin_search and update data
    pass

def mark_present(data,reg_id):
    pass

#filename = input("file name: ").strip()
# TODO make ui using tkinter 
# TODO input keyboard to do stuff
# TODO UI to create 

