from tkinter import*
#from PIL import Image,ImageTk 
from employee import employeeclass
from supplier import supplierclass
from category import categoryclass
from product import productclass
from sales import salesclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F9F5F6")
        #====title=====
       # self.icon_title=Image.open("logo1.png")
        #self.icon_title=self.icon_title.resize((100,100),Image)
        #self.icon_title=ImageTk.PhotoImage(self.icon_title)
        
        title=Label(self.root,text="Smart Stocks",font=("times new roman",40,"bold"),bg="#FFD0D0",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====btn=====
        btn_logout=Button(self.root,text="Logout",font=("times new roman",20,"bold"),bg="white",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #====CLK===
        self.lbl_clock=Label(self.root,text="Welcome to SMART STOCKS",font=("times new roman",15),bg="#9BABB8")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====leftmenu====
       
        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=110,width=200,height=565)

        lbl_menu=Label(leftmenu,text="Menu",font=("times new roman",20,"bold"),bg="#79E0EE").pack(side=TOP,fill=X)
        btn_employee=Button(leftmenu,text="Employee",command=self.employee,font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(leftmenu,text="Supplier",command=self.supplier,font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(leftmenu,text="Category",command=self.category,font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(leftmenu,text="Product",command=self.product,font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(leftmenu,text="Sales",command=self.sales,font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(leftmenu,text="Exit",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====CONTENT===
        self.lbl_employee=Label(self.root,text="Total employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#D7BBF5",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

         #====CONTENT===
        self.lbl_supplier=Label(self.root,text="Total supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFD9C0",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
         #====CONTENT===
        self.lbl_category=Label(self.root,text="Total category\n[ 0 ]",bd=5,relief=RIDGE,bg="#A0BFE0",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
         #====CONTENT===
        self.lbl_product=Label(self.root,text="Total product\n[ 0 ]",bd=5,relief=RIDGE,bg="#A0BFE0",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
         #====CONTENT===
        self.lbl_sales=Label(self.root,text="Total sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#FFD89C",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)





        #====footor===  
        lbl_footor=Label(text="IMS inventory management system \n for any issues contact:000000000 ",font=("times new roman",10),bg="#9BABB8").pack(side=BOTTOM,fill=X)
#===================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)   

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)    
         
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)    

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)    
                  
              
    


if __name__=="__main__":  
    root=Tk()
    obj=IMS(root)
    root.mainloop()
