#!/usr/bin/python
import random
def find_pos(a):
    i=0
    j=len(a)-1
    k=k_element()
    while(i<j):
        if(a[i]+a[j]==k):
            return a[i],a[j]
        elif(a[i]+a[j]<k):
            i=i+1
        else:
            j=j-1
def k_element():
    k=raw_input("Enter a number(k): ")
    try:
        k=int(k)
        return int(k)
    except:        
        print "\nplease reenter"
        return k_element()
    
        
        
if(__name__=='__main__'):
    a=random.sample(range(0,10),random.randint(2,8))
    #a=[1,7,6,4]
    a.sort()
    print a
    k=2
    print find_pos(a)
            
