from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import os 
import sqlite3
class salesclass:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F9F5F6")
        self.root.focus_force()
        self.bill_list=[]
        self.var_invoice=StringVar()
        
        #title==
        lbl_title=Label(self.root,text=" View Customer Bills",font=("goudy old style",30),bg='#ACB1D6',fg="BLACK",bd=1,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_invoice=Label(self.root,text=" Invoice No.",font=("times new roman",15),bg='white').place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg='#F1F6F9').place(x=160,y=100,width=180,height=28)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=490,y=100,width=120,height=28)
        
        # Bill list
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)
        
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        
        
        # Bill area
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)
        
        lbl_title2=Label(bill_frame,text="Customer Bill Area",font=("goudy old style",20),bg='#ADC4CE').pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly2.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
       #==images====
        self.bill_photo=Image.open("images/img1.png")
        self.bill_photo=self.bill_photo.resize((350,300))
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=700,y=150)
        
        self.show()
        #=========================================
    def show(self):
        del self.bill_list[:]
        self.Sales_list.delete(1,END)
           
        for i in os.listdir('bill'):
                # print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                
    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
            
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
         
         
    def clear(self):
            self.show()
            self.bill_area.delete('1.0',END)
            
if __name__:"__main__"
root=Tk()
obj=salesclass(root)
root.mainloop()
         
        
