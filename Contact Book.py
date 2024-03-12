print("-------------Contact Book-------------\n\n")
cbook=dict()
def add():
    cname=input("Contact name: ")
    cd=[i for i in input("Enter contact details(number,mailID,address) : ").split(",")]
    cbook[cname]=cd
    print("Contact added\n")
    
def update():
    if len(cbook)==0:
            print("Your contact book is empty!")
            u=(input("Add a new Contact? (Yes/No): ")).lower()
            if u=="yes":
                add()
            else:
                pass
    c=input("Contact name: ")
    if c in cbook:
        print("What do you want to update?\n1) number\n2) mailid\n3) address")
        up=int(input("choice: "))
        if up==1:
            n=input("New number: ")
            cbook[c][0]=n
        elif up==2:
            m=input("New mailid: ")
            cbook[c][1]=m
        elif up==3:
            a=input("New address: ")
            cbook[c][2]=a
        else:
            print("Invalid choice!")
        print("Contact updated\n")
    else:
        print("Contact is not present!\n")
        
def delete():
    if len(cbook)==0:
            print("Your contact book is empty!")
            u=(input("Add a new Contact? (Yes/No): ")).lower()
            if u=="yes":
                add()
            else:
                pass
    try:
        d=input("Contact to be deleted: ")
        del cbook[d]
    except:
        print("Contact not present!\n")
    else:
        print("Contact deleted\n")
def display():
    if len(cbook)==0:
            print("Your contact book is empty!")
    else:
        print("--------------Contact Book--------------")
        i=1
        for k,v in cbook.items():
            print("{}.Name: {}\n  Number: {}\n  MailId: {}\n  Address: {}".format(i,k,v[0],v[1],v[2]))
            i+=1
        print("----------------------------------------\n")
    
def search():
    if len(cbook)==0:
            print("Your contact book is empty!")
    try:
        c=input("Contact Name: ")
        print("  Name: {}\n  Number: {}\n  MailId: {}\n  Address: {}\n".format(c,cbook[c][0],cbook[c][1],cbook[c][2]))
    except:
        print("Contact not present!\n")


while True:
    print("...............................................")
    print("1) Add Contact\n2) Update Contact Details\n3) Delete Contact\n4) Display Contacts\n5) Search Contact\n6) Exit")
    ch=int(input("Enter your choice = "))
    if ch==1:
        add()
    elif ch==2:
        update()
    elif ch==3:
        delete()
    elif ch==4:
        display()
    elif ch==5:
        search()
    elif ch==6:
        break
    else:
        print("Invalid Choice!")
