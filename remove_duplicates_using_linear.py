#remove duplicate elements from an unsorted array

import time
import math
start=time.time()
a=[1,32,2,2,1,4,6,45,1,34,5,1,3,5,1,43,6,4,2,2,1,3,6,3,45,4,2,5,3,4,5,6,3,2,2]

##########################
#linear method

def linear_remove(a):
    b=[]
    b.append(a[0])
    for i in range(1,len(a)):
        x=search(a,b,i)
        if(x==0):
            b.append(a[i])
    return b
def search(a,b,i):
        for j in range(len(b)):
            if(a[i]==b[j]):
                return 1
        return 0    
    

if(__name__=='__main__'):
    b=[]
    print "the input array"
    print a
    print "the output "
    b=linear_remove(a)
    print b
    print "time :",time.time()-start
#def remove(a):
    
        
