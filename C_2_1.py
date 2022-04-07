def birth(m):
  a=0
  b=1
  print(" {:s}\n{:s}\n{:s}{:s}{:s}{:s}{:s}".format((22)*"_","|  Month |\tPairs  |","|",(8)*"-","|",(13)*"-","|"))
  for i in range(m):
    temp=b
    b=a+b
    a=temp
    e=str(a)
    st=len(e)
    if(i==m-1):
        print("{:s}{:d}{:s}{:s}{:s}{:d}{:s}{:s}\n {:s}".format("|  ",i+1,"\t"," |","\t",a,(6-(st-1))*" ","|",(22)*"-"))
    else:
        print("{:s}{:d}{:s}{:s}{:s}{:d}{:s}{:s}\n{:s}{:s}{:s}{:s}{:s}".format("|  ",i+1,"\t"," |","\t",a,(6-(st-1))*" ","|","|",(8)*"-","|",(13)*"-","|"))
month=int(input("Enter the number of months : "))
birth(month)
