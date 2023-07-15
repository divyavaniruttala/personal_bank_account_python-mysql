import mysql.connector as a
import datetime as date
dates1=date.datetime.now()
con=a.connect(host='localhost',user='root',passwd='123456789',database='divya')

if con.is_connected():
    print("connection establishes to mysql")
def openAcc():
    n=input("Enter your name :  ")
    ac=input("Enter account no :  ")
    db=input("Enter your D.O.B : ")
    p=input("enter your ph number : ")
    ad=input("Enter your address :  ")
    print("\n")
    print(" ==========minimum opening balance 1000 =========”)
    print("\n")
    ob=int(input("Enter opening Balance : "))
    data1=(n,ac,db,p,ad,dates1)
    data2=(n,ac,ob)
    sql1='insert into customers values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amounts values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("\n")
    print("=======ACCOUNT CREATED SUCCESSFULLY ======”)
    print("\n")
    main()

def depoAmo():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No : ")
    data1=(ac,am,dates1)
    sql1='insert into credited values(%s,%s,%s)'
    a="Select total_balance from amounts where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(a,data)
    myresults=c.fetchone()
    tam=myresults[0]+am
    sql="Update amounts set total_balance =%s where acno =%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("\n")
    print("====YOUR AMOUNT DEPOSITED SUCCESSFULLY ===”)
    print("\n")
    main()
def witham():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account No : ")
    data1=(ac,am,dates1)
    sql1='insert into debited values(%s,%s,%s)'
    a="Select total_balance from amounts where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(a,data)
    myresults=c.fetchone()
    tam=myresults[0]-am
    sql="Update amounts set total_balance =%s where acno =%s"
    d=(tam,ac)
    c.execute(sql,d)

    con.commit()
    print("\n")
    print("==WITHDRAWL AMOUNT SUCCESSFULLY ====”) 
    print("\n")
    main()


def loan():
    am=int(input("Enter  loan Amount : "))
    ac=input("Enter Account No : ")
    data1=(ac,am,dates1)
    sql1='insert into loan values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    con.commit()
    print("\n")
    print("====LOAN SANCTIONED SUCCESSFULLY====”) 
    print("\n")
    main()
    
def balance():
    ac=input("enter Account No : ")
    a="Select total_balance from amounts where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresults=c.fetchone()
    print("balance for Account : ",ac,"is",myresults[0])
    print("\n")
    print("==============THANK YOU ==========”) 
    print("\n")
    main()
def closeac():
    ac=input("enter Account No : ")
    sql1="delete from customers where acno=%s"
    sql2="delete from amounts where acno=%s"
    sql3="delete from loan where acno=%s"
    sql4="delete from credited where acno=%s"
    sql5="delete from debited where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    c.execute(sql3,data)
    c.execute(sql4,data)
    c.execute(sql5,data)
    con.commit()
    print("\n")
    print("==YOUR ACCOUNT HAS BEEN REMOVED ==”)
    print("\n")
    main()


def main():
    print("\n")
    print("=========WELCOME TO OURS BANKING ========”)
    print("\n")
    print("=======HOW MAY I HELP YOU=====”)
    print("\n")
    print("""""
    1.OPEN NEW ACCOUNT
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT
    4.APPLY FOR LOAN
    5.BALANCE ENQUIRY
    6.CLOSE AN ACCOUNT""""")
    print("\n")
    choice=input("enter task No : ")
    if(choice=='1'):
        openAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
       witham()
    elif(choice=='4'):
        loan()
    elif(choice=='5'):
        balance()
    elif(choice=='6'):
        closeac()
    else:
        print("\n")
        print("====ENTER CORRECT CHOICE====”)
        print("\n")
        main()
main()




