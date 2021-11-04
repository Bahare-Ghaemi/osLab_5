
import csv
print('welcome to my store...')
products = []

def showMenu():
    print("*** MENU ***")
    print("1-Add")
    print("2-Edit")
    print("3-Delete")
    print("4-Show List")
    print("5-Search")
    print("6-Buy")
    print("7-Save")
    print("8-Exit")


totalPrice = 0

#------------Add--------------
def add():
    #f = open('myFile.csv','a')
    productId = int(input('enter Id of product : '))
    for product in products:
        if productId == product['code']:
            print("product is existed now!!!")
            break
    productName = input('enter name of product : ')
    productPrice = int(input('enter price of product : '))
    productCount = int(input('enter count of product : '))
    products.append({'code':productId,'name':productName,'price':productPrice,'count':productCount})

#-----------------------------

#------------Edit-------------

def edit():
    productN = input('enter name of product you want to edit : ')
    for product in products:
            if productN == product['name']:
                price_ = input("enter the new price : ")
                product['price'] = price_
                #products.remove(product)
                print("OK!!!! The price changed")
            else:
                print("the product does NOT exist")

#------------------------------

#------------Delete-------------

def delete():
    productN = input('enter name of product you want to edit : ')
    for product in  products:
        if product["name"] == productN:
            products.remove(product)
            print("the product deleted...")
            return
        else:
            print("the product does NOT exist")
#-------------------------------

def showList():
    print('id\tname\tprice\tcount')
    for product in products :
        print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'],'\t')

def load_data():
    f=open("myFile.csv",'r')
    for row in f:
        info = row[:-1].split(',')
        product={"code":info[0],"name":info[1],"price":info[2],"count":info[3]}
        products.append(product)
    

#----------Search-----------

def search():
    productN = input('enter name of product you want to search : ')
    for product in products:
        if productN == product['name']:
            print(product)  
        else:
            print("the product does NOT exist")

#---------------------------

#------------Buy-------------
def buy():
    showMenu()
    productN = input('enter name of product you want to buy')
    for product in products:
        if productN == product['name']:
            count_ = int(product["count"])
            if count_ != 0:
                count_ -= 1
                product["count"]=count_
                
            else:
                Delete(productN)
                break
        else:
            print("we don't have a product with this name!!!")

#---------------------------

#-----------Save-----------

def save():
    proArray=['','','','']
    f=open("myFile.csv",'a')
    writer = csv.writer(f)
    for product in products:
        proArray[0]=product["code"]
        proArray[1]=product["name"]
        proArray[2]=product["price"]
        proArray[3]=product["count"]
        writer.writerow(proArray) 
    print("Your product added...")

#--------------------------


#--------------------------
def loadDataFromFile():
    print('\n******** DATA ********')
    f = open('myFile.csv','r')
    for row in f:
        info = row[:-1].split(',')
        newDict = {'code':info[0],'name':info[1],'price':info[2],'count':info[3]}
        products.append(newDict)

    print('****************\n')

#loadDataFromFile()

while True:
    showMenu()
    choice = int(input("enter your choice : "))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        delete()
    elif choice == 4:
        showList()
    elif choice == 5:
        search()
    elif choice == 6:
        buy()
    elif choice == 7:
        save()
    elif choice == 8:
        break
    else:
        print('your input is NOT valid !!!')
