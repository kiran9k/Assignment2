#merge iterative

#!/usr/bin/python
import random
import math
def merge_sort(a):
    N=len(a)
    if(N==0):
        return a
    no_levels=int(math.ceil(math.log(N,2)))    
    for i in range(0,no_levels):
        max_size=2**i
        no_of_merge=int(math.ceil(N/max_size))
        for j in range(0,no_of_merge):
            merged_array=[]
            start_index=2*max_size*j
            mid_index=start_index+max_size
            end_index=mid_index+max_size-1
            if(N-1<mid_index):
                pass
            else:
                if(end_index<=N):
                    pass
                elif(end_index>N):
                    end_index=N-1
                merged_array=merge(a[start_index:mid_index],a[mid_index:end_index+1])
                a[start_index:end_index+1]= merged_array
                
    return a

def merge(a,b):
    c=[]
    pos_start=0
    pos_mid=0
    while(pos_start<len(a) and pos_mid<len(b)):
        if(a[pos_start]<b[pos_mid]):
            c.append(a[pos_start])
            pos_start=pos_start+1
        else:
            c.append(b[pos_mid])
            pos_mid=pos_mid+1
    if(pos_start<len(a)):
        c.extend(a[pos_start:len(a)])
    else:
        if(pos_mid<len(b)):
            c.extend(b[pos_mid:len(a)])
    return c
        
if(__name__=='__main__'):
    
    a=[]
    d=[]
    e=[]
    from testing import *
    for i in range(0,100):
        a,d=one_d_testing()
        e=merge_sort(a)
        print a
        print d
        print e
        if(d==e):
            print "ok"
        else:
            print "failed"
            break
        print "########"
    """for i in range(0,100):
        c=[]
        d=[]
        #a=[5,-9, 0,5]
        a=random.sample(range(-20,60),random.randint(0,20))
        c.extend(a)
        b=merge_sort(c)
        d.extend(a)
        d.sort()
        print "##############"
        if(d==b):
            print a
            print b
            print d
            print "ok",i
        else:
            print "failed"
            print i
            print a
            print c
            print b
            break"""
    
            
