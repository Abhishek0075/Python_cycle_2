
# setosa list
def setosa(l):
    seto=[]
    for i in range (len(l)):
        if((l[i]["species"])=="setosa"):
            seto.append(l[i])
    return seto
#     Sepal part

# Setosa part
def s_sep_max(l):
    seto=[]
    for i in range (len(l)):
        if((l[i]["species"])=="setosa"):
            seto.append(l[i])
    seto_sep=[]
    for i in range(len(seto)):
        temp=((seto[i]["sepalLength"])*(seto[i]["sepalWidth"]))
        seto_sep.append(temp)
    print("The maximum sepal area in Setosa    : ",max(seto_sep))



# Virginica part
def vir_sep_max(l):
    virg=[]
    for i in range (len(l)):
        if((l[i]["species"])=="virginica"):
            virg.append(l[i])
    virg_sep=[]
    for i in range(len(virg)):
        temp=((virg[i]["sepalLength"])*(virg[i]["sepalWidth"]))
        virg_sep.append(temp)
    print("The maximum sepal area in Virginica : ",max(virg_sep))

# Vesicolor part
def v_sep_max(l):
    vesi=[]
    for i in range (len(l)):
        if((l[i]["species"])=="versicolor"):
            vesi.append(l[i])
    vesi_sep=[]
    for i in range(len(vesi)):
        temp=((vesi[i]["sepalLength"])*(vesi[i]["sepalWidth"]))
        vesi_sep.append(temp)
    print("The maximum sepal area in Versicolor : ",max(vesi_sep))

#      Petal part max 

#   Setosa part
def s_pet_min(l):
    seto=[]
    for i in range (len(l)):
        if((l[i]["species"])=="setosa"):
            seto.append(l[i])
    seto_pet=[]
    for i in range(len(seto)):
        temp=((seto[i]["petalLength"])*(seto[i]["petalWidth"]))
        seto_pet.append(temp)
    print("The minimum petal area in Setosa    : ",min(seto_pet))


#    Virginica part
def vir_pet_min(l):
    virg=[]
    for i in range (len(l)):
        if((l[i]["species"])=="virginica"):
            virg.append(l[i])
    virg_pet=[]
    for i in range(len(virg)):
        temp=((virg[i]["petalLength"])*(virg[i]["petalWidth"]))
        virg_pet.append(temp)
    print("The minimum petal area in Virginica : ",min(virg_pet))

# Vesicolor part 
def v_pet_min(l):
    vesi=[]
    for i in range (len(l)):
        if((l[i]["species"])=="versicolor"):
            vesi.append(l[i])
    vesi_pet=[]
    for i in range(len(vesi)):
        temp=((vesi[i]["petalLength"])*(vesi[i]["petalWidth"]))
        vesi_pet.append(temp)
    print("The minimum petal area in Versicolor : ",min(vesi_pet))

#       Sorting
def area_sort(l):
    l_mult=[]
    for i in range(len(l)):
        temp=((l[i]["petalLength"])*(l[i]["petalWidth"])+(l[i]["sepalLength"])*(l[i]["sepalWidth"]))
        l_mult.append(temp)
    l_mult.sort()
    final_l_total=[]
    for i in range (len(l)):
        for j in range(len(l)): 
            pro=((l[j]["petalLength"])*(l[j]["petalWidth"])+(l[j]["sepalLength"])*(l[j]["sepalWidth"]))
            if(l_mult[i]==pro):
                final_l_total.insert(0,l[j])
                break
    return final_l_total
f=open("iris.json","r")
l=f.read().splitlines()
f.close()
length=len(l)
l=[eval(l[i].strip(",")) for i in range (1,length-1)]
print("{:s}\n{:s}\n{:s}".format(len("Details of all flowers of species setosa : ")*"-","Details of all flowers of species setosa : ",len("Details of all flowers of species setosa : ")*"-"))
print(setosa(l))
print("{:s}\n{:s}\n{:s}".format(len("List of dictionaries according to total area of petal and sepal :")*"-","List of dictionaries according to total area of petal and sepal :",len("List of dictionaries according to total area of petal and sepal :")*"-"))
print(area_sort(l))


