import math
import random
import time
start=time.time()
def heapify(b,N):      
        h=int(math.ceil(math.log(N,2)))
        
        l=int(math.floor(N/2.0))#(len(b)/2.0))
        if(h==0):
            h=1       
        for k in range(0,h):          
            for i in range(l,k,-1):                
                i=i-1                
                j=(2*i +1)             
                if j<N-1:                
                    if(b[j]>b[j+1]):                        
                        if(b[i]<b[j]):                           
                           b=swap(b,i,j)
                    else:
                        if(b[j+1]>b[i]):
                            b=swap(b,i,j+1)
                else:                    
                    if(b[j]>b[i]):
                        b=swap(b,i,j)       
        return b
def swap(b,i,j):    
    t=b[i]
    b[i]=b[j]
    b[j]=t
    return b
def rearrange(b):
    N=len(b)-1
    i=0
    while(N-i>=1):
        b=heapify(b,N-i+1)
        b=swap(b,0,N-i)        
        i=i+1
    return b
if(__name__=='__main__'):
    print"the input "
    for i in range(0,100):
        print"###"
        b=random.sample(range(-50,30),random.randint(0,80))
        
        #print"the sorted array"
        print "input",b        
        c=[]
        a=rearrange(b)
        c.extend(a)       
        b.sort()
        print "output ",c
        #case testing 
        if(c==b):
            print "ok"
            print i
        else:
            print "fail"
            print b
            print c            
            break
    print "time :",time.time()-start
    
    
        
        
