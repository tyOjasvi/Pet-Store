import mysql.connector
from emoji import emojize
import datetime
time = datetime.datetime.now()
mydb=mysql.connector.connect(host="localhost",user="root",password="student")
print("/\____/\                                                                                                                                               /\____/\     ")
print("\ *    * /                                                    THE PET WORLD                                                                 \ *    * /       ")
print(" \ ---- /                                                                                                                                                  \ ---- /       ")
print(" ")
print("                                              'A house is not a home until there is a pet inside'      ")
print("                                                 -lewis dorman            ")
print("")
print("""............Welcome to the place made for the pet lovers by the pet lovers......
            Our pet store offers the best and the most fine graded quality pets and 
            allows you to choose from a wide ranging varieties of imported pets, be it the chirping love birds or the cute ginuea pigs.""")
print(" ")
print("/\____/\                                                                                                                                             /\____/\     ")
print("\ *    * /                                                                                                                                              \ *    * /       ")
print(" \ ---- /                                                                                                                                                \ ---- /       ")
print(" ")
print("                                 TIMINGS OF ACCESSING FOR THIS SESSION: ",time)
print("""****************************************************************************************************************************************""")

#FUNCTIONS FOR VALIDATIONS OF ENTERED DATA
def getquantity(message):    
    while True:
        try:
            userint=int(input(message))
            return userint
        except ValueError:
            print("seems you haven't entered a valid value.try again ")
def getstring(bare):    
    while True:
        try:
            userstring=input(bare)
            if userstring.isalpha()==True:
                return userstring
        except TypeError:
            print("seems you haven't entered a valid value.try again ")
def getphoneno(phone):
    while True:
        try:
            userno=input(phone)
            l=len(userno)
            check=userno.isnumeric()
            if l==10 or check==True:
                return userno
        except:
            print("Please enter a valid phone no. this time.....")


#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20) primary key,password varchar(20))")

while True:
    print("""****1:Signup****
****2:Login****""")
    print(" ")
    ch=int(input("SIGNUP/LOGIN(1,2):"))
#SIGNUP
    if ch==1:
        username=input("ENTER YOUR USERNAME:")
        pw=input("ENTER YOUR PASSWORD:")

        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        print(" ")
        print("YOUR ACCOUNT SUCCESSFULLY CREATED.")
        print("PLEASE LOGIN WITH YOUR USERNAME NOW.")
        print(" ")
        mydb.commit()

#LOGIN
    elif ch==2:
        username=input("ENTER YOUR USERNAME:")

        mycursor.execute("select username from signup where username='"+username+"'")
        pot=mycursor.fetchone()

        if pot is not None:
            print("Thats a valid username...",emojize(":thumbs_up:"))

            pw=input("ENTER YOUR PASSWORD:")

            mycursor.execute("select password from signup where password='"+pw+"'")
            a=mycursor.fetchone()

            if a is not None:
                for i in range(0,11):
                    print(emojize(":thumbs_up:"),end="")
             
                print("""...
LOGIN SUCCESSFUL..    .""")
                for i in range(0,11):
                    print(emojize(":thumbs_up:"),end="")
            

                
               
                print("""
==================================================================================================================================
*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*WELCOME TO THE PET WORLD*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^
====================================================================================================================================""")

                mycursor.execute("CREATE TABLE if not exists Available_Animals (animalname varchar(30) primary key,Breed varchar(20),Quantity int(3),Keepername varchar(30),Country_belonged  varchar(30),Price int(4))")
                mycursor.execute("CREATE TABLE if not exists Sell_rec (CustomerName varchar(20),PhoneNumber char(10) unique key,AnimalName varchar(30),Quantity int(100),Price int(4),foreign key (animalname) references Available_Animals(animalname))")
                mycursor.execute("CREATE TABLE if not exists Staff_details (Name varchar(30),Gender varchar(10),Age int(3),PhoneNumber char(10) unique key,Address varchar(40))") 
                mydb.commit()

                while(True):
                    print(" ")
                    print("_"*150)
                    print("""*^*^*^*^*^*  1:Adding a new pet  *^*^*^*^*^
*^*^*^*^*^   2:Selling a pet  *^*^*^*^*^
*^*^*^*^*^   3:Searching available pets  *^*^*^*^*^
*^*^*^*^*^  4:Details of Staff  *^*^*^*^*^
*^*^*^*^*^  5:Sell Records *^*^*^*^*^
*^*^*^*^*^  6:Available Pets  *^*^*^*^*^
*^*^*^*^*^  7:Total Income after the Latest Reset  *^*^*^*^*^ 
*^*^*^*^*^  8:Exit  *^*^*^*^*^""")
                    print(" ")
                    print("/\____/\                       /\____/\     ")
                    print("\ *    * /                        \ *    * /       ")
                    print(" \ ---- /                          \ ---- /       ")

                    a=int(input("Enter your choice:"))
                    print("/\____/\                         /\____/\     ")
                    print("\ *    * /                          \ *    * /       ")
                    print(" \ ---- /                            \ ---- /       ")
                    print("_"*150)
                    print(" ")
                    

    #ADD Animal
                    if a==1:

                        print("All information prompted are mandatory to be filled")
                      
                        
                    
                        animal=getstring("Enter Animal Name:")
                       
                            
                        breed=getstring("Breed:")
                        quantity=getquantity("Enter the quantity: ")
                        
                        
                        keeper=getstring("Enter keeper name:")
                        
                            
                        countrybelong=getstring("Enter country it belongs to:")
                        
                        
                        price=getquantity("Enter the price:")                        
                            

                        mycursor.execute("select * from Available_Animals where animalname='"+animal+"'")
                        row=mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("update Available_Animals set quantity=quantity+'"+str(quantity)+"' where animalname='"+animal+"'")
                            mydb.commit()
                            print(" ")

                            print(animal," successfully added in the records")
                        
                        
                        else:
                            mycursor.execute("insert into Available_Animals(animalname,breed,quantity,keepername,country_belonged,price) values('"+animal+"','"+breed+"','"+str(quantity)+"','"+keeper+"','"+countrybelong+"','"+str(price)+"')")
                            mydb.commit()

                            print(animal," successfully added in the records")

    #SELLING Animal
                    elif a==2:                

                        print("AVAILABLE ANIMALS...")
                        print(" ")

                        mycursor.execute("select * from Available_Animals ")
                        for x in mycursor:
                            print(x)
                      
                        cusname=input("Enter customer name:")
                    
                            
                        phno=getphoneno("Enter phone number:")
                       
                            
                        animal=input("Enter Animal Name:")
                        
                        price=getquantity("Enter the price:")
                        n=int(input("Enter quantity:"))
                       
                       

                        mycursor.execute("select quantity from Available_Animals where animalname='"+animal+"'")
                        lk=mycursor.fetchone()

                        if max(lk)<n:
                            print(x,"Animals are not available!!!!")

                        else:
                            mycursor.execute("select animalname from Available_Animals where animalname='"+animal+"'")
                            log=mycursor.fetchone()

                            if log is not None:
                                mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+animal+"','"+str(n)+"','"+str(price)+"')")
                                mycursor.execute("update Available_Animals set quantity=quantity-'"+str(n)+"' where animalname='"+animal+"'")
                                mydb.commit()

                                print("ANIMAL HAS BEEN SOLD TO ",cusname)

                            else:
                                print("ANIMAL IS NOT AVAILABLE!!!!!!!")

    #SEARCH ANIMALS ON THE BASIS OF GIVEN OPTIONS
                    elif a==3:

                        print("""1:Search by name
2:Search by breed
3:Search by keeper""")

                        l=int(input("Search by?:"))

        #BY ANIMALNAME
                        if l==1:
                            o=getstring("Enter Animal to search:")

                            mycursor.execute("select animalname from Available_Animals where animalname='"+o+"'")
                            tree=mycursor.fetchone()

                            if tree!=None:
                                print("""=========================
==Animal is Available  ==
===============================""")

                            else:
                                print("ANIMAL IS NOT AVAILABLE!!!!!!!")

        #BY BREED
                        elif l==2:
                            g=getstring("Enter breed to search:")

                            mycursor.execute("select breed from Available_Animals where breed='"+g+"'")
                            poll=mycursor.fetchall()

                            if poll is not None:
                                print("""=========================
==Animal is Available  ==
===============================""")
                                mycursor.execute("select * from Available_Animals where breed='"+g+"'")
                                for y in mycursor:
                                    print(y)
                            else:
                                print("ANIMALS OF SUCH BREED ARE NOT AVAILABLE!!!!!!!!!")


        #BY KEEPER NAME
                        elif l==3:
                            au=getstring("Enter keeper name to search:")

                            mycursor.execute("select Keeper from Available_Animals where keepername='"+au+"'")
                            home=mycursor.fetchall()

                            if home is not None:
                                print("""=========================
==Animal is Available  ==
===============================""")
                                mycursor.execute("select * from Available_Animals where keepername='"+au+"'")
                                for z in mycursor:
                                    print(z)
                            else:
                                print("KEEPER NOT AVAILABLE!!!!!!!")
                        mydb.commit()

    #STAFF DETAILS
                    elif a==4:
                        print("1:New staff entry")
                        print("2:Remove staff")
                        print("3:Existing staff details")

                        ch=int(input("Enter your choice:"))

        #NEW STAFF ENTRY
                        if ch==1:
                            fname=getstring("Enter Fullname:")
                            gender=getstring("Gender(M/F/O):")
                            age=getquantity("Age:")
                            phno=getphoneno("Staff phone no.:")
                            add=getstring("Address:")

                            mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
                            print("""----------------------------------
-STAFF IS SUCCESSFULLY ADDED-
----------------------------------------------------""")
                            mydb.commit()

        #REMOVE STAFF
                        elif ch==2:
                            nm=getstring("Enter staff name to remove:")
                            mycursor.execute("select name from staff_details where name='"+nm+"'")
                            toy=mycursor.fetchone()

                            if toy is not None:
                                mycursor.execute("delete from staff_details where name='"+nm+"'")
                                print("""----------------------------------
-STAFF IS SUCCESSFULLY REMOVED-
----------------------------------------------------""")
                                mydb.commit()

                            else:
                                print("STAFF DOESNOT EXIST!!!!!!")

        #EXISTING STAFF DETAILS
                        elif ch==3:
                            mycursor.execute("select * from Staff_details")
                            run=mycursor.fetchone()
                            for t in mycursor:
                                print(t)
                            if run is not None:
                                print("EXISTING STAFF DETAILS...")                        
                                for t in mycursor:
                                    print(t)

                            else:
                                print("NO STAFF EXISTS!!!!!!!")
                            mydb.commit()

    #SELL HISTORY                                
                    elif a==5:
                        print("1:Sell history details")
                        print("2:Reset Sell history")

                        ty=int(input("Enter your choice:"))

                        if ty==1:
                            mycursor.execute("select * from sell_rec")
                            for u in mycursor:
                                print(u)

                        if ty==2:
                            bb=input("Are you sure(Y/N):")

                            if bb=="Y":
                                mycursor.execute("delete from sell_rec")
                                mydb.commit()

                            elif bb=="N":
                                pass

    #AVAILABLE ANIMALS
                    elif a==6:
                        
                        print("AVAILABLE ANIMALS")
                        mycursor.execute("select * from Available_Animals order by animalname")
                        for v in mycursor:
                            print(v)
                    

    #TOTAL INCOME AFTER LATEST UPDATE
                    elif a==7:
                        mycursor.execute("select sum(price) from sell_rec")
                        for x in mycursor:
                            print(emojize(":cherry_blossom:"),"The income of the store uptil now is Rs.",x,emojize(":cherry_blossom:"))
    #EXIT                    
                    elif a==8:
                        break

#LOGIN ELSE PART
            else:
                print("""IT APPEARS YOU HAVE ENTERED AN INCORRECT PASSWORD.
                                        PLEASE RETRY LOGINING IN""")
                print(" ")


        else:
            print(emojize(":collision:"),end=" ")
            print("SORRY THAT'S AN INVALID USERNAME.",emojize(":collision:"))
            print("""PLEASE RETRY.
           IF YOU DON'T HAVE A ACCOUNT THEN SIGN UP.......""")
            print(" ")

    else:
        break


