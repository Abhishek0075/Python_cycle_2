def rotate (s):
  print("{:s} {:s} {:s}".format("* The string of integers with space","=",s))
  s=s.split()
  l=[int(i) for i in s]
  k=int(input(">> Enter the number of times elements should be rotated : "))
  # Rotation of elements in list by k postion to the right
  for i in range(k):
    x=l.pop()
    l.insert(0,x)
  print("* After rotation : ",l)
  return l
# Tuple form through list comprehension
def compreh(l):
  tup=tuple(i for i in l)
  print("* Tuple form : ",tup)
# Removing duplicates 
def duplicate(l):
  l=set(l)
  l_dup=list(l)
  print("* After removing duplicates : ",l_dup)
  return l_dup
# Results of function f(x)=x^2 - x
def funct(l):
  square=[(x**2-x) for x in l]
  print("* After f(x)=x^2 - x : ",square)
  return square
# Sorting and merging of two lists
def merge(l):
  l_dup=duplicate(l)
  l_dup.sort()
  square=funct(l_dup)
  square.sort()
  merge=l_dup+square
  print("* After sorting and merging : ",merge)

s=str(input("Enter string of integers with spaces : "))
l=rotate(s)
compreh(l)
d=duplicate(l)
sq=funct(l)
merge(l)
