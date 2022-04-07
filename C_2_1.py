def birth(m):
  a=0
  b=1
  print(" {:s}\n{:s}\n{:s}{:s}{:s}{:s}{:s}".format((23)*"_","|  Month |\tPairs  |","|",(8)*"-","|",(14)*"-","|"))
  for i in range(m):
    temp=b
    b=a+b
    a=temp
    if(i==m-1):
        print("{:s}{:d}{:s}{:s}{:s}{:d}{:s}{:s}".format("|  ",i+1,"\t"," |","\t",a,"\t","|"))
    else:
        print("{:s}{:d}{:s}{:s}{:s}{:d}{:s}{:s}\n{:s}{:s}{:s}{:s}{:s}".format("|  ",i+1,"\t"," |","\t",a,"\t","|","|",(8)*"-","|",(14)*"-","|"))
  print("",(23)*"-")
month=int(input("Enter the number of months : "))
birth(month)
