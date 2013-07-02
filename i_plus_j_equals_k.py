#!/usr/bin/python

"""to obtain 2 numbers i & j from already sorted array ,a ,such that a[i]+a[j]=x  """


def user_input():
    print "Do you want to enter numbers Manually(Yes - 1/ No- 0):?"
    x=input()
    a=[]
    if(x==0):
        a=[1,2,3,4,5,6,7,8,9,10,11]
    elif(x==1):
        print "please enter input elements for sorted array: "
        print "press -1 to exit "
        x=input()
        while(x!= -1):
            a.append(x)
            x=input()
    else:
        print "Not a avalid input"
    return a

def accept_number():
    x=raw_input()    
    return int(x)

def search(l,x,n,a):       
    while(l<=n):
        m=(l+n)/2
        if(a[m]==x):
            return m
        elif(x<a[m]):
            n=m-1
        else:            
            l=m+1
    return -1

def split(x,a):
    N=len(a)
    p=N-1    
    r=0
    while(r<=p):
        m=(r+p)/2
        if x<a[m] :
            p=m-1
        else:
            r=x-a[p]            
            m=search(0,r,p,a)            
            if(m<>-1 ):#and p<>m):
                print a[p],a[m]
            p=p-1

            
if(__name__=='__main__'):
    a=user_input()
    print "the input sorted array is:"
    print a
    print"enter a number"
    x=accept_number()
    print "The available combinations such that a[i]+a[j]=k are :"
   
    split(x,a)

                 
    
#search takes - log(n)
#spit takes - n during worst case and log n during best case
#total - nlog(n)
             
    
    
