def birth(m):
  a=0
  b=1
  print( " Month \t\tPairs  " )
  for i in range(m):
    temp=b
    b=a+b
    a=temp
    print("  ",i+1,"\t\t",a,)
month=int(input("Enter the number of months : "))
birth(month)
