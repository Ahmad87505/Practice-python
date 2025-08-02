#Methods of list
l=[1,2,3,4,5,6]
print(l)
#This is the first method
l.append(7)
print(l)
#This is the second method
e=[4,5,6,7,8,9,12,13,10]
print(e)
e.sort()
print(e)
#This is the third method
f=[1,2,3,4,5,6,7,8,9]
print(f)
f.sort(reverse=True)
print(f)
#This is the fourth method
g=[3,4,5,6,7,8]
print(g)
g.reverse()
print(g)
#This is the fifth method
h=[7,8,9]
print(h)
print(h.index(7))

#This is the sixth method
k=[7,8,6,7,8,6]
print(k)
print(k.count(7))
#This is the seventh method
d=[2,3,4,5,6,7,8]
print(d)
m= d.copy()
m[0]=0
print(d)
#This is the eight method
b=[9,8,7,6]
print(b)
b.insert(1,889)
print(b)
#This is the ninth method
j=[500,1000,1500]
s=[1,2,3,4]
s.extend(j)
print(s)