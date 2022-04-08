s="1 2 3 4 4 9 7 7 1 2 5 6 7"
print("{:s} {:s} {:s}".format("* The string of integers with space","=",s))
s=s.split()
l=[int(i) for i in s]
k=int(input(">> Enter the number of times elements should be rotated : "))
# Rotation of elements in list by k postion to the right
for i in range(k):
  x=l.pop()
  l.insert(0,x)
print("* After rotation : ",l)
# Tuple form through list comprehension
tup=tuple(i for i in l)
print("* Tuple form : ",tup)
# Removing duplicates 
tup=set(tup)
l_dup=list(tup)
print("* After removing duplicates : ",l_dup)
# Results of function f(x)=x^2 - x
square=[(x**2-x) for x in l_dup]
print("* After f(x)=x^2 - x : ",square)
# Sorting and merging of two lists
l_dup.sort()
square.sort()
merge=l_dup+square
print("* After sorting and merging : ",merge)