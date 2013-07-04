#divide by 3 sorting technique

#!/usr/bin/python
import math
import random
def divide_by_3(a):
    N=len(a)
    div=int(math.ceil(N/3.0))
    ulimit=2*div
    if(N==1):
        return a
    if(N==2):
        a[0:ulimit]=q_sort(a[0:ulimit],0,ulimit-1)
    if(N%3==1):
        ulimit=(2*div) -1    
    a[0:ulimit]=q_sort(a[0:ulimit],0,ulimit-1)    
    a[div:N]=q_sort(a[div:N],0,N-1-div)       
    a[0:ulimit]=q_sort(a[0:ulimit],0,ulimit-1)    
    return  a
    
def q_sort(a,l,r):
    p=0
    N=len(a)
    if(l<r):        
        x=a[l]           
        p=l+1
        q=r        
        flag=False      
        while(p<q and p<N and q>0):        
            if(x>=a[p]):
                p=p+1
            elif(x<=a[q]):
                q=q-1                
            elif(x<a[p]and x>a[q] and p<q):
                if(a[p]>a[q]):
                    temp=a[p]
                    a[p]=a[q]
                    a[q]=temp                                   
        if(p>=q and flag==False):
            if(x>a[p]):
                pass
            else:
                p=p-1                    
        temp=a[p]
        a[p]=x
        a[l]=temp
        mid=p       
        q_sort(a,l,mid-1)  
        q_sort(a,mid+1,r)
    return a
if(__name__=='__main__'):
    #a=[5,1,6,3,2]#-14,17,-27,-25,26]
    
    for i in range(0,100):
        b=[]
        d=[]
        a=random.sample(range(-50,30),random.randint(0,8))
        b.extend(a)
        c=divide_by_3(b)
        d.extend(a)
        d.sort()
        print "##"
        print i
        print a
        print d
        print c
        if(d==c):
            print "ok"
        else:
            print "failed"
            break
        
            
        
    
    
