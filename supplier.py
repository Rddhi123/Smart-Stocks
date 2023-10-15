from tkinter import*
#from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3
class supplierclass:

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




        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        
        




        #=====self.root===
       

        #====options===
        lbl_search=Label(self.root,text="Invoice No.",font=("roboto",15))
        lbl_search.place(x=700,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("roboto",15),bg='lightyellow').place(x=800,y=80,width=160)
        btn_search=Button(self.root,text="Search",command=self.search,font=("roboto",15),bg="#47A992",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

        #====title===
        title=Label(self.root,text="Supplier Details",bg="#9DB2BF",font=("roboto",20,"bold"),fg="black").place(x=50,y=10,width=1000,height=40)


        #===content===
        #=====row1====
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style",15)).place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,bg="#F1F6F9",font=("goudy old style",15)).place(x=180,y=80,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,bg="white",font=("goudy old style",15)).place(x=500,y=150,width=180)
        
        #====row2===
        lbl_name=Label(self.root,text="Name",bg="white",font=("goudy old style",15)).place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,bg="#F1F6F9",font=("goudy old style",15)).place(x=180,y=120,width=180)
        
        #====row3===
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("goudy old style",15)).place(x=50,y=160)  
        txt_contact=Entry(self.root,textvariable=self.var_contact,bg="#F1F6F9",font=("goudy old style",15)).place(x=180,y=160,width=180)
       
         #====row4===
        lbl_desc=Label(self.root,text="Description",bg="white",font=("goudy old style",15)).place(x=50,y=200)
        
        self.txt_desc=Text(self.root,bg="#F1F6F9",font=("goudy old style",15))
        self.txt_desc.place(x=180,y=200,width=470,height=120)
        
        #=====button======
        btn_add=Button(self.root,text="Save",command=self.add,font=("roboto",15),bg="#75C2F6",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("roboto",15),bg="#22A699",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("roboto",15),bg="#E76161",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("roboto",15),bg="#9BA4B5",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)


        #====employee details======
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.suppliertable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.suppliertable.xview)
        scrolly.config(command=self.suppliertable.yview)

        self.suppliertable.heading("invoice",text="Invoice No..")
        self.suppliertable.heading("name",text="Name")
        self.suppliertable.heading("contact",text="Contact")
        self.suppliertable.heading("desc",text="desc")
        

        self.suppliertable["show"]="headings"
        
        self.suppliertable.column("invoice",width=90)
        self.suppliertable.column("name",width=100)
        self.suppliertable.column("contact",width=100)
        self.suppliertable.column("desc",width=100)
        
        self.suppliertable.pack(fill=BOTH,expand=1)
        self.suppliertable.bind("<ButtonRelease-1>",self.get_data)

        self.show()



#=======================================================
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","invoice must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","invoice no. already assigned, try different",parent=self.root)
                else:
                    cur.execute("insert into supplier(invoice,name,contact,desc)values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        
                                        self.var_contact.get(),
                                        self.txt_desc.get("1.0",END),

                                        
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success",'supplier added successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.suppliertable.delete(*self.suppliertable.get_children())
            for row in rows:
                self.suppliertable.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)     

    def get_data(self,ev):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content["values"]
       # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        
        self.var_contact.set(row[2])
        self.txt_desc.delete("1.0",END)
        self.txt_desc.insert(END,row[3])


        



    def update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","invoice no. must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid invoice no.",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(
                                        
                                        self.var_name.get(),
                                        
                                        self.var_contact.get(),
                                                                                                                                                                                         self.txt_desc.get("1.0",END),

                                        
                                        self.var_sup_invoice.get(),
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success",'supplier updated  successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","invoice no. must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid invoice no.",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op==True:                    
                       cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                       con.commit()
                       messagebox.showinfo("delete",'supplier deleted successfully',parent=self.root)
                       self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)  
    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")        
        self.var_contact.set("")                                                                                       
        self.txt_desc.delete("1.0",END)          
        self.var_searchtxt.set("")       
        self.show()

        

    def search(self):       
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            
            if self.var_searchtxt.get()=="":
                messagebox.showerror("error","invoice no. should be required",parent=self.root )
            else:
                cur.execute("select * from supplier where invoice=?",( self.var_searchtxt.get(),) )
                rows=cur.fetchone()
                if rows!=None:
                    self.suppliertable.delete(*self.suppliertable.get_children())
                    
                    self.suppliertable.insert("",END,values=sqlite3.Row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    

                                        
        
        




if __name__=="__main__":  
    root=Tk()
    obj=supplierclass(root)
    root.mainloop()       