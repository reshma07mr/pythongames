#contact book is used to save name, phone number.

#without a database,storing using list
name=[]
phone_num=[]
#how many entries are needed to add
x=int(input("Enter the number of contacts needed to save: "))

for i in range(x):
    nam_e=input("Enter the name : ")
    name.append(nam_e)

    pho_num=int(input("Enter the phone number : "))
    phone_num.append(pho_num)
    
#displaying
for i in range(len(name)):
    name[i]=name[i].upper()

for i in range(x):
    print("{}\t\t{}".format(name[i], phone_num[i]))

#for searching by name
search_name=input("Enter the name to be searched :")
search_name=search_name.upper()

if search_name in name:
    x=name.index(search_name)
    y=phone_num[x]
    print("Searched name :{}\nPhone number :{}".format(search_name,y))

else:
    print("User not found")
