from tkinter import*
#from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3
class employeeclass:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F9F5F6")
        self.root.focus_force()
        #===================
        #all variables=====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()




        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utypes=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()





        #=====searchframe===
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("roboto",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options===
        cnb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("robot",15))
        cnb_search.place(x=10,y=10,width=180)
        cnb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("roboto",15),bg='lightyellow').place(x=200,y=12)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("roboto",15),bg="#47A992",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #====title===
        title=Label(self.root,text="Employee Details",bg="#9DB2BF",font=("roboto",15),fg="black").place(x=50,y=100,width=1000)


        #===content===
        #=====row1====
        lbl_empid=Label(self.root,text="Emp ID",bg="white",font=("goudy old style",15)).place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",bg="white",font=("goudy old style",15)).place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,bg="#F1F6F9",font=("goudy old style",15)).place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,bg="white",font=("goudy old style",15)).place(x=500,y=150,width=180)
        cnb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","other"),state="readonly",justify=CENTER,font=("robot",15))
        cnb_gender.place(x=500,y=150,width=180)
        cnb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,bg="#F1F6F9",font=("goudy old style",15)).place(x=850,y=150,width=180)

        #====row2===
        lbl_name=Label(self.root,text="Name",bg="white",font=("goudy old style",15)).place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",bg="white",font=("goudy old style",15)).place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",bg="white",font=("goudy old style",15)).place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,bg="#F1F6F9",font=("goudy old style",15)).place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,bg="#F1F6F9",font=("goudy old style",15)).place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,bg="#F1F6F9",font=("goudy old style",15)).place(x=850,y=190,width=180)

        #====row3===
        lbl_email=Label(self.root,text="Email",bg="white",font=("goudy old style",15)).place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",bg="white",font=("goudy old style",15)).place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",bg="white",font=("goudy old style",15)).place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,bg="#F1F6F9",font=("goudy old style",15)).place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_password,bg="#F1F6F9",font=("goudy old style",15)).place(x=500,y=230,width=180)
        #txt_utype=Entry(self.root,textvariable=self.var_utypes,bg="#F1F6F9",font=("goudy old style",15)).place(x=850,y=230,width=180)
        cnb_utype=ttk.Combobox(self.root,textvariable=self.var_utypes,values=("Admin","Employee"),state="readonly",justify=CENTER,font=("robot",15))
        cnb_utype.place(x=850,y=230,width=180)
        cnb_utype.current(0)

         #====row4===
        lbl_address=Label(self.root,text="Address",bg="white",font=("goudy old style",15)).place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",bg="white",font=("goudy old style",15)).place(x=500,y=270)
       

        self.txt_address=Text(self.root,bg="#F1F6F9",font=("goudy old style",15))
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,bg="#F1F6F9",font=("goudy old style",15)).place(x=600,y=270,width=180)

        #=====button======
        btn_add=Button(self.root,text="Save",command=self.add,font=("roboto",15),bg="#75C2F6",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("roboto",15),bg="#22A699",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("roboto",15),bg="#E76161",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("roboto",15),bg="#9BA4B5",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)


        #====employee details======
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.employeetable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employeetable.xview)
        scrolly.config(command=self.employeetable.yview)

        self.employeetable.heading("eid",text="Emp id")
        self.employeetable.heading("name",text="Name")
        self.employeetable.heading("email",text="Email")
        self.employeetable.heading("gender",text="Gennder")
        self.employeetable.heading("contact",text="contact")
        self.employeetable.heading("dob",text="D.O.B")
        self.employeetable.heading("doj",text="D.O.J")
        self.employeetable.heading("pass",text="Password")
        self.employeetable.heading("utype",text="utype")
        self.employeetable.heading("address",text="Address")
        self.employeetable.heading("salary",text="Salary")

        self.employeetable["show"]="headings"
        
        self.employeetable.column("eid",width=90)
        self.employeetable.column("name",width=100)
        self.employeetable.column("email",width=100)
        self.employeetable.column("gender",width=100)
        self.employeetable.column("contact",width=100)
        self.employeetable.column("dob",width=100)
        self.employeetable.column("doj",width=100)
        self.employeetable.column("pass",width=100)
        self.employeetable.column("utype",width=100)
        self.employeetable.column("address",width=100)
        self.employeetable.column("salary",width=100)
        self.employeetable.pack(fill=BOTH,expand=1)
        self.employeetable.bind("<ButtonRelease-1>",self.get_data)

        self.show()



#=======================================================
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","empluyee id must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","this employess id is already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        
                                        self.var_password.get(),
                                        self.var_utypes.get(),
                                        self.txt_address.get("1.0",END),

                                        self.var_salary.get(),
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success",'employee added successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employeetable.delete(*self.employeetable.get_children())
            for row in rows:
                self.employeetable.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)     

    def get_data(self,ev):
        f=self.employeetable.focus()
        content=(self.employeetable.item(f))
        row=content["values"]
       # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
                                        
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
                                        
        self.var_password.set(row[7])
        self.var_utypes.set(row[8])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[9])


        self.var_salary.set(row[10])



    def update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","empluyee id must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid employee id",parent=self.root)
                else:
                    cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                        
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        
                                        self.var_password.get(),
                                        self.var_utypes.get(),
                                        self.txt_address.get("1.0",END),

                                        self.var_salary.get(),
                                        self.var_emp_id.get(),
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success",'employee updated  successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","empluyee id must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid employee id",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op==True:                    
                       cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                       con.commit()
                       messagebox.showinfo("delete",'employee deleted successfully',parent=self.root)
                       self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)  
    
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("select")
        self.var_contact.set("")
                                        
        self.var_dob.set("")
        self.var_doj.set("")
                                        
        self.var_password.set("")
        self.var_utypes.set("admin")
        self.txt_address.delete("1.0",END)    
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()

        

    def search(self):       
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="select":
                messagebox.showerror("error","select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("error","search input should be required",parent=self.root )
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+ self.var_searchtxt.get()+ "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employeetable.delete(*self.employeetable.get_children())
                    for row in rows:
                        self.employeetable.insert("",END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    

                                        
        
        




if __name__=="__main__":  
    root=Tk()
    obj=employeeclass(root)
    root.mainloop()       