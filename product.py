from tkinter import*
#from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3
class productclass:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F9F5F6")
        self.root.focus_force()
        #==========================
        self.var_cat=StringVar()
        self.var_sup=StringVar()


        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        self.var_PID=StringVar()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

        #====title===
        title=Label(product_frame,text=" Manage Product Details",bg="#9DB2BF",font=("roboto",18),fg="black").pack(side=TOP,fill=X)

        lbl_category=Label(product_frame,text="Category",font=("roboto",18),bg="white").place(x=30,y=60)
        lbl_Supplier=Label(product_frame,text="Supplier",font=("roboto",18),bg="white").place(x=30,y=110)
        lbl_Product_Name=Label(product_frame,text="Name",font=("roboto",18),bg="white").place(x=30,y=160)
        lbl_Price=Label(product_frame,text="Price",font=("roboto",18),bg="white").place(x=30,y=210)
        lbl_Quantity=Label(product_frame,text="Quantity",font=("roboto",18),bg="white").place(x=30,y=260)
        lbl_Status=Label(product_frame,text="Status",font=("roboto",18),bg="white").place(x=30,y=310)

       
        #====options===
        cnb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("robot",15))
        cnb_cat.place(x=150,y=60,width=200)
        cnb_cat.current(0)

        cnb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("robot",15))
        cnb_sup.place(x=150,y=110,width=200)
        cnb_sup.current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("robot",15),bg="#F1F6F9").place(x=150,y=160,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("robot",15),bg="#F1F6F9").place(x=150,y=210,width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("robot",15),bg="#F1F6F9").place(x=150,y=260,width=200)
       
        cnb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("robot",15))
        cnb_status.place(x=150,y=310,width=200)
        cnb_status.current(0)


         #=====button======
        btn_add=Button(product_frame,text="Save",command=self.add,font=("roboto",15),bg="#75C2F6",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("roboto",15),bg="#22A699",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("roboto",15),bg="#E76161",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("roboto",15),bg="#9BA4B5",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
 
        #=====searchframe===
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("roboto",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #====options===
        cnb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state="readonly",justify=CENTER,font=("robot",15))
        cnb_search.place(x=10,y=10,width=180)
        cnb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("roboto",15),bg='lightyellow').place(x=200,y=12)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("roboto",15),bg="#47A992",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)




         #====product details======
        product_frame=Frame(self.root,bd=3,relief=RIDGE)
        product_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollx=Scrollbar(product_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(product_frame,columns=("PID","Supplier","Category","Name","Price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("PID",text="PID")
        self.product_table.heading("Category",text="cat")
        self.product_table.heading("Supplier",text="sup")
        self.product_table.heading("Name",text="name")
        self.product_table.heading("Price",text="price")
        self.product_table.heading("qty",text="qty")
        self.product_table.heading("status",text="status")
        

        self.product_table["show"]="headings"
        
        self.product_table.column("PID",width=90)
        self.product_table.column("Category",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("Name",width=100)
        self.product_table.column("Price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
       
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        



#=======================================================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("select")
                for i in cat:
                    self.cat_list.append(i[0])  

            cur.execute("select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("select")
                for i in sup:
                    self.sup_list.append(i[0])
            


        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="select" or self.var_name.get()=="":
                messagebox.showerror("error"," all fields are required",parent=self.root)
            else:
                cur.execute("select * from product where Name=? ",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","product already present, try different",parent=self.root)
                else:
                    cur.execute("insert into product(Category,Supplier,Name,Price,qty,status)values(?,?,?,?,?,?)",(
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        
                                        self.var_status.get(),
                                        
                                    
                    ))
                    con.commit()
                    messagebox.showinfo("success",'product added successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)     

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content["values"]
        self.var_PID.set(row[0])
        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
                                        
        self.var_status.set(row[6])
       


        

    def update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_PID.get()=="":
                messagebox.showerror("error","Please select product from list",parent=self.root)
            else:
                cur.execute("select * from product where PID=?",(self.var_PID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid product id",parent=self.root)
                else:
                    cur.execute("update product set category=?,supplier=?,name=?,price=?,dob=?,qty=?,status=? where PID=?",(
                                        
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        
                                        self.var_status.get(),
                                        self.var_PID.get()
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success",'product updated  successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    



    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_PID.get()=="":
                messagebox.showerror("error","select product from the list",parent=self.root)
            else:
                cur.execute("select * from product  where PID=?",(self.var_PID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid product id",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op==True:                    
                       cur.execute("delete from product where PID=?",(self.var_PID.get(),))
                       con.commit()
                       messagebox.showinfo("delete",'product deleted successfully',parent=self.root)
                       #self.show()
                       self.clear()
        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)  
    
    def clear(self):
        
       
        self.var_cat.set("")
        self.var_sup.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
                                        
        self.var_status.set("")
        self.var_PID.set("")
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
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+ self.var_searchtxt.get()+ "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("",END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)    

                                        
        

if __name__=="__main__":  
    root=Tk()
    obj=productclass(root)
    root.mainloop()               