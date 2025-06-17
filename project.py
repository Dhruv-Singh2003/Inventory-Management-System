import mysql.connector
obj=mysql.connector.connect(host="localhost",user="root",passwd="dhruv2496",database="inventory")
cur=obj.cursor()

cur.execute("create table item(ino integer(10) primary key,iname varchar(50),prate float(7,2),srate float(7,2),qis integer(10))")
cur.execute("create table customer(cid integer(10) primary key,cname varchar(60),cadd varchar(100),cmobile integer(10))")
cur.execute("create table supplier(sid integer(10) primary key,sname varchar(60),sadd varchar(100),smobile integer(10))")
cur.execute("create table pmaster(pid integer(10) primary key,pdate date,sid integer(10),total float(7,2))")
cur.execute("create table pdetails(pid integer(10),ino integer(10),qty integer(10),rate float(7,2),total float(7,2))")
cur.execute("create table smaster(saleid integer(10) primary key,sdate date,cid integer(10),total float(7,2))")
cur.execute("create table sdetails(saleid integer(10),ino integer(10),qty integer(10),rate float(7,2),total float(7,2))")
cur.execute("create table ptemp(pid integer(10),ino integer(10),qty integer(10),rate float(7,2),total float(7,2))")
cur.execute("create table stemp(saleid integer(10),ino integer(10),qty integer(10),rate float(7,2),total float(7,2))")
print("tables created ")
#item
def additem():
    ino=int(input("Enter the item no.:"))
    iname=input("Enter the item name:")
    prate=float(input("Enter the purchase rate:"))
    srate=float(input("Enter the selling price:"))
    qis=int(input("Enter the quantities in stock:"))
    q="insert into item values(%s,'%s',%s,%s,%s)"%(ino,iname,prate,srate,qis)
    cur.execute(q)
    obj.commit()
    print("Item added successfully")
def edititem():
    ino=int(input("Enter the item no to be updated:"))
    q="select * from item where ino=%s"%(ino)
    t=0
    cur.execute(q)
    for i in cur:
        if i[0]==ino:
         srate=float(input("Enter the new selling price:"))
         prate=float(input("Enter the new purchase rate:"))
         cur.execute("update item set prate=%s,srate=%s where ino=%s"%(prate,srate,ino))
         obj.commit()
         print("Item edited successfully")
         t=1
    if t==0:     
         print("item doesnt exist")
        
def searchitem(ino):
    temp=0
    q="select * from item where ino=%s"%(ino)
    cur.execute(q)
    for i in cur:
        if i[0]==ino:
            print(i)
            print("Itemno is:",i[0])
            print("Iteam name is:",i[1])
            print("Purchase rate of item is:",i[2])
            print("Selling rate of item is:",i[3])
            print("Quantity of item in stock:",i[4])
            temp=1
    if temp==0:
        print("Item doesnt exist")
   
    

def deleteitem():
    ino=int(input("Enter the item no to be deleted:"))
    t=0
    q="select * from item where ino=%s"%(ino)
    cur.execute(q)
    for i in cur:
        if i[0]==ino:
            q1="delete from item where ino=%s"%(ino)
            cur.execute(q1)
            obj.commit()
            print("Item deleted successfully")
            t=1
    if t==0:
        print("item deosnt exist")
    
#CUSTOMER
def addcustomer():
    cid=int(input("Enter the customer id :"))
    cname=input("Enter the customer name:")
    cadd=input("Enter the customer address:")
    cmobile=input("Enter the mobile no. of customer:")
    q="insert into customer values(%s,'%s','%s','%s')"%(cid,cname,cadd,cmobile)
    cur.execute(q)
    obj.commit()
    print("Customer added successfully")
def editcustomer():
    t=0
    cid=int(input("Enter the customer id to be updated:"))
    q="select * from customer where cid=%s"%(cid)
    cur.execute(q)
    for i in cur:
        if i[0]==cid:
              cmobile=input("Enter the new mobie no. of customer :")
              cadd=input("Enter the new address of customer:")
              cur.execute("update customer set cadd='%s',cmobile='%s' where cid=%s"%(cadd,cmobile,cid))
              obj.commit()
              print("Customer edited successfully")
              t=1
    if t==0:
        print("Customer doesnt exist")
def searchcustomer():
    t=0
    cid=int(input("Enter the customer id to be seached:"))
    q="select * from customer where cid=%s"%(cid)
    cur.execute(q)
    for i in cur:
        if i[0]==cid:
            print(i)
            print("Customer id is:",i[0])
            print("Customer name is:",i[1])
            print("Customer address:",i[2])
            print("Customer mobile no.:",i[3])
            t=1
    if t==0:
        print("Customer doesnt exist")
def deletecustomer():
    t=0
    cid=int(input("Enter customer id to be deleted:"))
    q="select * from customer where cid=%s"%(cid)
    cur.execute(q)
    for i in cur:
        if i[0]==cid:
          q1="delete from customer where cid=%s"%(cid)
          cur.execute(q1)
          obj.commit()
          print("Customer deleted successfully")
          t=1
    if t==0:
        print("Customer doesnt exist")
#SUPPLIER
def addsupplier():
    sid=int(input("Enter the supplier id :"))
    sname=input("Enter the supplier name:")
    sadd=input("Enter the supplier address:")
    smobile=input("Enter the mobile no. of supplier:")
    q="insert into supplier values(%s,'%s','%s','%s')"%(sid,sname,sadd,smobile)
    cur.execute(q)
    obj.commit()
    print("Supplier added successfully")
def editsupplier():
    sid=int(input("Enter the supplier id to be updated:"))
    t=0
    q="select * from supplier where sid=%s"%(sid)
    cur.execute(q)
    for i in cur:
        if i[0]==sid:
            smobile=input("Enter the new mobie no. of supplier :")
            sadd=input("Enter the new address of supplier:")
            cur.execute("update supplier set sadd='%s',smobile='%s' where sid=%s"%(sadd,smobile,sid))
            obj.commit()
            print("Supplier edited successfully")
            t=1
    if t==0:
        print("Supplier doesnt exist")
def searchsupplier():
    t=0
    sid=int(input("Enter the supplier id to be seached:"))
    q="select * from supplier where sid=%s"%(sid)
    cur.execute(q)
    for i in cur :
        if i[0]==sid:
           print(i)
           print("Supplier id is:",i[0])
           print("Supplier name is:",i[1])
           print("Supplier address:",i[2])
           print("Supplier mobile no.:",i[3])
           t=1
    if t==0:
        print("Supplier doesnt exist")
def deletesupplier():
    t=0
    sid=int(input("Enter supplier id to be deleted:"))
    q="select * from supplier where sid=%s"%(sid)
    cur.execute(q)
    for i in cur:
        if i[0]==sid:
              q1="delete from supplier where sid=%s"%(sid)
              cur.execute(q1)
              obj.commit()
              print("Supplier deleted successfully")
              t=1
    if t==0:
        print("Supplier doesnt exist")
def purchase():
    s=[]
    t=[]
    net=0
    total=0
    ch='y'    
    pdate=input("Enter purchase date in(YYYY-MM-DD):")
    sid=int(input("Enter supplier id:"))
    cur.execute("select sid from supplier")
    for i in cur:
        s.append(i[0])
    if sid in s:
        print("SELECT ITEM YOU WANT TO PURCHASE")
        cur.execute("select * from item")
        for j in cur:
            print(j)
        while ch=='y':
           cur.execute("select count(*) from pmaster")
           w=cur.fetchone()
           if w[0]!=0:
                  cur.execute("select max(pid) from pmaster")
                  pmax=cur.fetchone()
                  pid=pmax[0]+1
           else:
                pid=1
           print("Purchase id is:",pid)
           ino=int(input("Enter the item no of item you want to purchase:"))
           cur.execute("select ino from item")
           for k in cur:
               t.append(k[0])
           if ino in t:
               qty=int(input("Enter the quantity of item to be purchased:"))
               cur.execute("select prate from item where ino=%s"%(ino))
               ate=cur.fetchone()
               rate=ate[0]
               total=qty*rate
               net=net+total
               rec=(pid,ino,qty,rate,total)
               
           else:
              print("Item doesnt exist")
           ch=input("Do you want to purchase more items :")
           q1="insert into pmaster values(%s,'%s',%s,%s)"%(pid,pdate,sid,total)
           cur.execute(q1)
           obj.commit()
           
           q2="insert into pdetails values(%s,%s,%s,%s,%s)"%rec
           cur.execute(q2)
           obj.commit()
           cur.execute("insert into ptemp values(%s,%s,%s,%s,%s)"%rec)
           obj.commit()
           q3="update item,ptemp set qis=qis+qty where item.ino=ptemp.ino"
           cur.execute(q3)
           obj.commit()
           cur.execute("delete from ptemp")
           obj.commit()
           print("Purchasing details recorded successfully")
    else:
        print("Please enter a valid supplier id")
def sale():
    s=[]
    t=[]
    net=0
    total=0
    ch='y'    
    sdate=input("Enter seling date in (YYYY-MM-DD):")
    cid=int(input("Enter customer id:"))
    cur.execute("select cid from customer")
    for i in cur:
        s.append(i[0])
    if cid in s:
        print("SELECT ITEM YOU WANT TO SALE")
        cur.execute("select * from item")
        for j in cur:
            print(j)
        while ch=='y':
           cur.execute("select count(*) from smaster")
           l=cur.fetchone()
           if l[0]==0:
                   saleid=1
           else:
               cur.execute("select max(saleid) from smaster")
               smax=cur.fetchone()
               saleid=smax[0]+1
           print("Sale id is:",saleid)
           ino=int(input("Enter the item no of item you want to sale:"))
           cur.execute("select ino from item")
           for k in cur:
               t.append(k[0])
           if ino in t:
               qty=int(input("Enter the quantity of item to be sold:"))
               cur.execute("select srate from item where ino=%s"%(ino))
               ate=cur.fetchone()
               rate=ate[0]
               total=qty*rate
               net=net+total
               rec=(saleid,ino,qty,rate,total)
               
           else:
              print("Item doesnt exist")
           ch=input("Do you want to sale more items :")
           q1="insert into smaster values(%s,'%s',%s,%s)"%(saleid,sdate,cid,total)
           cur.execute(q1)
           obj.commit()
           
           q2="insert into sdetails values(%s,%s,%s,%s,%s)"%rec
           cur.execute(q2)
           obj.commit()
           cur.execute("insert into stemp values(%s,%s,%s,%s,%s)"%rec)
           obj.commit()
           q3="update item,stemp set qis=qis - qty where item.ino=stemp.ino"
           cur.execute(q3)
           obj.commit()
           cur.execute("delete from stemp")
           obj.commit()
           print("Selling details recorded successfully")
    else:
        print("Please enter a valid customer id")
def itemdetail():
    print("ITEMNO.,NAME,PURRATE,SALERATE,QTY")
    cur.execute("select * from item")
    for i in cur:
        print(i)
def customerdetail():
    print("CUSID,NAME,ADD.,MOB.NO.")
    cur.execute("select * from customer")
    for i in cur:
        print(i)
def supplierdetail():
    print("SUPID,NAME,ADD.,MOB.NO.")
    cur.execute("select * from supplier")
    for i in cur:
        print(i)
def saledetail():
    print("SALEID,DATE,CUSID,TOTAL")
    bd=input("Enter the beginning date:")
    ed=input("Enter the ending date:")
    q="select * from smaster where sdate between '%s' and '%s'"%(bd,ed)
    cur.execute(q)
    for i in cur:
        print(i)
def purchasedetail():
    print("PURID,DATE,SUPID,TOTAL")
    bd=input("Enter the beginning date:")
    ed=input("Enter the ending date:")
    q="select * from pmaster where pdate between '%s' and '%s'"%(bd,ed)
    cur.execute(q)
    for i in cur:
        print(i)
    
while True:
    print("-----------------------WELCOME TO INVENTORY---------------------------")
    print("                          1.ITEM                                 ")
    print("                          2.CUSTOMER                             ")
    print("                          3.SUPPLIERS                            ")
    print("                          4.TRADE                                ")
    print("                          5.COMMERCE DETAILS                     ")
    print("                          6.EXIT                                 ")
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            print(" 1.ADD ITEM")
            print(" 2.EDIT ITEM")
            print(" 3.SEARCH ITEM")
            print(" 4.DELETE ITEM")
            print(" 5.EXIT       ")
            C=int(input("Enter your choice:"))
            if C==1 :
                additem()

            elif C==2:
                 
                 edititem()

            elif C==3:
                  a=int(input("Enter the item no. to be searched"))
                  searchitem(a)

            elif C==4:
                  deleteitem()

            elif C==5:
                
                   break

    elif ch==2:
        while True:
            print(" 1.ADD CUSTOMER")
            print(" 2.EDIT CUSTOMER")
            print(" 3.SEARCH CUSTOMER")
            print(" 4.DELETE CUSTOMER")
            print(" 5.EXIT       ")
            C=int(input("Enter your choice:"))
            if C==1 :
                addcustomer()

            elif C==2:
                 editcustomer()

            elif C==3:
                  searchcustomer()

            elif C==4:
                  deletecustomer()

            elif C==5:
                break
        

    elif ch==3:
        while True:
            print(" 1.ADD SUPPLIER")
            print(" 2.EDIT SUPPLIER")
            print(" 3.SEARCH SUPPLIER")
            print(" 4.DELETE SUPPLIER")
            print(" 5.EXIT       ")
            C=int(input("Enter your choice:"))
            if C==1 :
                addsupplier()

            elif C==2:
                 editsupplier()

            elif C==3:
                  searchsupplier()

            elif C==4:
                  deletesupplier()

            elif C==5:
                
                   break
        
            

    elif ch==4:
        while True:
            print("1.SALE  ")
            print("2.PURCHASE")
            print("3.EXIT  ")
            C=int(input("Enter your choice:"))
            if C==1:
                  sale()
            elif C==2:
                purchase()
            elif C==3:
                break

    elif ch==5:
        while True:
            print("1.ITEM DETAILS")
            print("2.CUSTOMERS DETAILS")
            print("3.SUPPLIERS DETAILS")
            print("4.SALE DETAILS")
            print("5.PURCHASE DETAILS")
            print("6.EXIT")
            C=int(input("Enter your choice:"))
            if C==1 :
                itemdetail()

            elif C==2:
                 customerdetail()

            elif C==3:
                  supplierdetail()

            elif C==4:
                  saledetail()

            elif C==5:
                purchasedetail()

            elif C==6:
                break
                
        
    elif ch==6:
         break


