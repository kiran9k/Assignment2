#k-way merge sort

#!/usr/bin/python
import math
import time
import random
start=time.time()

def heapify(b,d):
    N=len(b)
    if(N>1):
        h=int(math.ceil(math.log(N,2)))
        l=int(math.floor((len(b)/2.0)))        
        if(h==0):
            h=1
        for k in range(0,h):        
            for i in range(l,k,-1):            
                i=i-1                
                j=(2*i +1)
                if j<N-1:                
                    if(b[j]<b[j+1]):                        
                        if(b[i]>b[j]):                           
                           b=swap(b,i,j)
                           d=swap(d,i,j)
                    else:
                        if(b[j+1]<b[i]):
                            b=swap(b,i,j+1)
                            d=swap(d,i,j+1)
                else:                    
                    if(b[j]<b[i]):
                        b=swap(b,i,j)
                        d=swap(d,i,j)
    return b,d

def swap(b,i,j):    
    t=b[i]
    b[i]=b[j]
    b[j]=t
    return b
   

def append_initial_elements(a,c,d,x):## x=len(a)
    b=[]           
    for i in range(0,x):
        if(a[i]<>[]):
            b.append(a[i][0])
            c.append(0)
            d.append(i)
    while(len(c)<x):
        c.append(0)
    return b

def add_elements(a,b,c,d):
    z=d[0]
    y=c[z]
    x=len(a[z])
    if(y+1<x):       
        l=[]        
        y=y+1
        c[z]=y               
        r= a[z][y]
        r=int(r)    
        b[0]=r      
    else:            
            l=[]
            q=[]            
            M=len(b)-1
            for i in range(0,M):
                l.append(b[i+1])
                q.append(d[i+1])        
            b=l
            d=q              
    return b,d
    
    
def k_way(a):
    b=[]
    c=[]
    d=[]    
    e=[]
    if(a==[]):
       pass
    else:               
        N=0
        b=append_initial_elements(a,c,d,len(a))
        
        for i in range (0,len(a)):
            N=len(a[i])+N
        for i in range (0,N):       
            b,d=heapify(b,d)       
            e.append(b[0])       
            z=d[0]
            b,d=add_elements(a,b,c,d)
            
    return e

            
    
        
        
        
    

if(__name__=='__main__'):
    
    e=[]
    a=[[],[],[],[],[],[]]
    q=[]
    for j in range(0,100):
        q=[]
        for i in range (len(a)):
            a[i]=random.sample(range(-20,60),random.randint(0,20))
            a[i].sort()
        #a=[1,2,3,4,5,6,7]
        print a

        for i in range(len(a)):
            q.extend(a[i])
        q.sort()                 
       
        e=k_way(a)
        #print "\n\nthe final sorted array:\n"
        print e
        #print b
        if(q==e):
            print "ok"
        else:
            print "failed"
            print j
            print a
            print e
            print q
            break
        print "###"
    print "time for exec ",time.time()-start
    
    
    





    """ a- large array which is split into parts.array b holds one element from each of these parts
array c- used to remember the position of the element in the a[i][j]
here c contains the value of j for each element in b
the array -d is used to keep track of the reshuffling of elements in b
whenever any of elements in b is reshufled, elements of d are also shuffled"""

"""elements to be given in the form of 2-D elements table"""


