#using heap sort
import random
import math
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
     
def shift(a,b,j,i):
    if(j<>len(a)-1):
        if(a[0]==b[i-1]):
            pass
        else:
            b.append(a[0])
            i=i+1
    else:
        b.append(a[0])
        i=i+1
    return a,b,i  
        
def remove_duplicate(a):   
    j=0
    b=[]
    N=len(a)-1
    for i in range(0,N+1):
        if(i<>N):
            a=heapify(a,N-i+1)
        
        a,b,j=shift(a,b,N-i,j)
        a[0]=a[N-j+1]         
    return b
    

if(__name__=='__main__'):
    b=[]
    print "the input array"
    a=random.sample(range(-50,30),random.randint(0,10))
    #a=[5,9]
    print a
    print "the output "
    b=remove_duplicate(a)
    print b
