"""
a,b=map(int,input().split('+'))
print(a)
print(b)
print(a+b)
if a<b:
    print("a is less than b")
elif a>b:
    print("a is greater than b")
else:
    print("a equals to b")

l=list(map(int,input().split()))
print(l)
print(l[0],l[3])
t=tuple(map(int,input().split()))
print(t)
"""
"""
a=[1,2,2,4,4,5,6,4,6,8,3]
s=set(a)
print(s)

if 4 in s:
    print("Element is present")
else:
    print("Element is not present")
"""

"""a=[1,2,1,2,1,4,5,6,7,7,8,8,2,2,1]
target=8
if target in a:
    print(target)
else:
    print("not found")"""
    
"""for i in range(1,10,3):
    print(i,end=" ")"""

"""i=1
while i<10:
    print(i,end=" ")
    i+=1"""

"""a=[1,2,3,2,3,4,5,3,4,5,6,9]
target=3
flag=0
for i in a:
    if(i==target):
        flag=flag+1
print(flag)"""

"""a=[1,2,3,2,3,4,5,3,4,5,6,9]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)"""

a=[1,1,2,3,4,5,2,3,6,7,8]
min=a[0]
for i in a:
    if(i<min):
        min=i
print(min)