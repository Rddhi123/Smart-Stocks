from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F9F5F6")
        self.cart_list=[]
        self.chk_print=0
        #====title=====
        #self.icon_title=Image.open("logo1.png")
        title=Label(self.root,text="Smart Stocks",font=("times new roman",40,"bold"),bg="#FFD0D0",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #====btn=====
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",20,"bold"),bg="white",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #====CLK===
        self.lbl_clock=Label(self.root,text="Welcome to SMART STOCKS",font=("times new roman",15),bg="#9BABB8")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #===Product_Frame====
        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        
        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #===product search frame=====
        self.var_search=StringVar()
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90) 
        
        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("Times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)     
        
        lbl_search=Label(ProductFrame2,text="Product Name",font=("Times new roman",15,"bold"),bg="white").place(x=5,y=45) 
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("Times new roman",15),bg="light yellow").place(x=128,y=47,width=150,height=22) 
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        #====Product details frame======
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(ProductFrame3,columns=("PID","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("PID",text="PID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="qty")
        self.product_table.heading("status",text="status")

        self.product_table["show"]="headings"
        
        self.product_table.column("PID",width=40)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=40)
        self.product_table.column("status",width=90)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note_=Label(ProductFrame1,text="Note:'Enter 0 quantity to remove product from the cart' ",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #===customer frame========
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame1.place(x=420,y=110,width=530,height=70)
        
        cTitle=Label(CustomerFrame1,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame1,text="Name",font=("Times new roman",15),bg="white").place(x=4,y=30) 
        txt_name=Entry(CustomerFrame1,textvariable=self.var_cname,font=("Times new roman",13),bg="light yellow").place(x=80,y=35,width=180) 
        lbl_contact=Label(CustomerFrame1,text="Contact No.",font=("Times new roman",15,),bg="white").place(x=270,y=30) 
        txt_name=Entry(CustomerFrame1,textvariable=self.var_contact,font=("Times new roman",13),bg="light yellow").place(x=380,y=35,width=140) 
        
        #===cal_cart_frame====
        cal_cart_Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_cart_Frame1.place(x=420,y=190,width=530,height=360)
        
        #====cal_frame=======
        self.var_cal_input=StringVar()
        cal_Frame1=Frame(cal_cart_Frame1,bd=9,relief=RIDGE,bg="white")
        cal_Frame1.place(x=5,y=10,width=270,height=340)
        
        
        self.txt_cal_input=Entry(cal_Frame1,textvariable=self.var_cal_input,font=("arial",15,'bold'),width=21,bd=10,relief=GROOVE,state="readonly",justify="right")
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(cal_Frame1,text="7",font=("arial",15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(cal_Frame1,text="8",font=("arial",15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(cal_Frame1,text="9",font=("arial",15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(cal_Frame1,text="+",font=("arial",15,'bold'),command=lambda:self.get_input("+"),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
        btn_4=Button(cal_Frame1,text="4",font=("arial",15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(cal_Frame1,text="5",font=("arial",15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(cal_Frame1,text="6",font=("arial",15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(cal_Frame1,text="-",font=("arial",15,'bold'),command=lambda:self.get_input("-"),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
        btn_1=Button(cal_Frame1,text="1",font=("arial",15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(cal_Frame1,text="2",font=("arial",15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(cal_Frame1,text="3",font=("arial",15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(cal_Frame1,text="*",font=("arial",15,'bold'),command=lambda:self.get_input("*"),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0=Button(cal_Frame1,text="0",font=("arial",15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_clr=Button(cal_Frame1,text="clear",font=("arial",15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
        btn_equal=Button(cal_Frame1,text="=",font=("arial",15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(cal_Frame1,text="/",font=("arial",15,'bold'),command=lambda:self.get_input("/"),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        
        
        
        
        
        
        
        
        
        
        
        #====cart frame===
        cart_frame=Frame(cal_cart_Frame1,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        self.cart_Title=Label(cart_frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray")
        self.cart_Title.pack(side=TOP,fill=X)


        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.Carttable=ttk.Treeview(cart_frame,columns=("PID","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Carttable.xview)
        scrolly.config(command=self.Carttable.yview)

        self.Carttable.heading("PID",text="PID")
        self.Carttable.heading("name",text="Name")
        self.Carttable.heading("price",text="Price")
        self.Carttable.heading("qty",text="qty")
       

        self.Carttable["show"]="headings"
        
        self.Carttable.column("PID",width=40)
        self.Carttable.column("name",width=90)
        self.Carttable.column("price",width=90)
        self.Carttable.column("qty",width=40)
        self.Carttable.pack(fill=BOTH,expand=1)
        self.Carttable.bind("<ButtonRelease-1>",self.get_data_cart)
        
        #==add cart widgets frame====
        self.var_PID=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        add_cart_widgets_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        add_cart_widgets_frame.place(x=420,y=550,width=530,height=110)
        
        lbl_p_name=Label(add_cart_widgets_frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(add_cart_widgets_frame,textvariable=self.var_pname,font=("times new roman",15),bg="light yellow",state="readonly").place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(add_cart_widgets_frame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_q_price=Entry(add_cart_widgets_frame,textvariable=self.var_price,font=("times new roman",15),bg="light yellow",state="readonly").place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(add_cart_widgets_frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_q_qty=Entry(add_cart_widgets_frame,textvariable=self.var_qty,font=("times new roman",15),bg="light yellow").place(x=390,y=35,width=120,height=22)
        
        self.lbl_inStock=Label(add_cart_widgets_frame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear_cart=Button(add_cart_widgets_frame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(add_cart_widgets_frame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #====billing area=======
        billframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billframe.place(x=953,y=110,width=410,height=410)
        
        BTitle=Label(billframe,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="white",fg="black").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billframe,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billframe,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #===billing buttons====
        billmenuframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billmenuframe.place(x=953,y=520,width=410,height=140)
        
        self.lbl_amt=Label(billmenuframe,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg='#3f51b5',fg='white')
        self.lbl_amt.place(x=2,y=5,width=120,height=70)
        
        self.lbl_discount=Label(billmenuframe,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg='#8bc34a',fg='white')
        self.lbl_discount.place(x=124,y=5,width=120,height=70)
        
        self.lbl_net_pay=Label(billmenuframe,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg='#607d8b',fg='white')
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)
        
        btn_print=Button(billmenuframe,text="Print",command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg='lightgreen',fg='white')
        btn_print.place(x=2,y=80,width=120,height=50)
        
        btn_clear_all=Button(billmenuframe,text="Clear All",command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg='gray',fg='white')
        btn_clear_all.place(x=124,y=80,width=120,height=50)
        
        btn_generate=Button(billmenuframe,text="Generate/Save Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",14,"bold"),bg='#009688',fg='white')
        btn_generate.place(x=246,y=80,width=160,height=50)
        
        
        #====footer=======
        footer=Label(self.root,text='IMS-Inventory Management System',font=("times new roman",11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.show()
        # self.bill_top()
        self.update_data_time()

        
        #====all functions=======
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
         
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
        
    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select PID,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root) 
              
    def search(self):       
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("error","search input should be required",parent=self.root )
            else:
                cur.execute("select PID,name,price,qty,status from product where name LIKE '%"+ self.var_search.get()+ "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("",END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("error",f"error due to :{str(ex)}",parent=self.root)   
             
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content["values"]
        self.var_PID.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set('1')
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        
    def get_data_cart(self,ev):
        f=self.Carttable.focus()
        content=(self.Carttable.item(f))
        row=content["values"]
        
        self.var_PID.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set('1')
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
    
    def add_update_cart(self):
        if self.var_PID.get()=='':
            messagebox.showerror('Error',"Please select product from the list",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror('Error',"Quantity is required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
             messagebox.showerror('Error',"Quantity is required",parent=self.root)  
        else:
            # price_cal=(int(self.var_qty.get())*float(self.var_price.get()))
            # price_cal=float(price_cal)   
            price_cal=self.var_price.get()
            #PID,name,price,qty,stock
            cart_data=[self.var_PID.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            self.cart_list.append(cart_data)
            #===update cart=====
            present='no'
            index_=-1
            for row in self.cart_list:
                if self.var_PID.get()==row[0]:
    
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present\nDo you want to update | Remove from the cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                       self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get()#qty
                        
    
            else:
                self.cart_list.append(cart_data)
                
            self.show_cart()
            self.bill_updates()
        
        
    
            
    def bill_updates(self):
        bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            # PID,name,price,qty,stock 
             
           self.bill_amt=bill_amt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amt*5)/100
        self.net_pay= self.bill_amt-self.discount
        self.lbl_amt.config(text=f'Bill Amnt\n{str(self.bill_amt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cart_Title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")
    
    
    def show_cart(self):
        try:
            self.Carttable.delete(*self.Carttable.get_children())
            for row in self.cart_list:
                self.Carttable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please add Product to the cart!!",parent=self.root)
        else:
            #===bill top====
            self.bill_top()
            #bill middle====
            self.bill_middle()
            #bill bottom=====
            self.bill_bottom()
            
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated/Save in Backend")
            self.chk_print=1
            
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 98725***** , Mumbai-400001
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            
            for row in self.cart_list:
                #PID,name,price,qty,stock
                PID=row[0] 
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(int(row[3]))==int(row[4]):
                    status="Inactive"
                if int(int(row[3]))!=int(row[4]):
                    status="Active"
                    
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                #===update qty in product table====
                cur.execute('Update Product set,qty=?,status=? where PID=?',(
                    qty,
                    status,
                    PID
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def clear_cart(self):
         self.var_PID.set('')
         self.var_pname.set('')
         self.var_price.set('')
         self.var_qty.set('')
         self.lbl_inStock.config(text=f"In Stocks")
         self.var_stock.set('')
           
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cart_Title.config(text=f"Cart \t Total Product :[0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        
    def update_data_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to SMART STOCKS\t\t Date: {str(date_)}\t\t Time: {str(time_)}\t\t")
        self.lbl_clock.after(200,self.update_data_time)
        
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
        else:
            messagebox.showerror('Print',"Please generate bill,to print the receipt",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
    
if __name__=="__main__":  
    root=Tk()
    obj=BillClass(root)
    root.mainloop()