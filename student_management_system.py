from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
f = ("Arial", 25, "bold")

def f1():
    aw.deiconify()
    mw.withdraw()

def f2():
    mw.deiconify()
    aw.withdraw()

def f3():
    vw.deiconify()
    mw.withdraw( )
    vw_st_data.delete(1.0, END)
    con = None
    try:
        con = connect("gg.db")
        cursor = con.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info = info + "id = " + str(d[0]) +"|"+ " name = " + str(d[1])+"|"+ " mark = "+str(d[2]) +"\n"+" ========================== " +"\n"
        vw_st_data.insert(INSERT, info)
    except Exception as e:
        showerror("issue", str(e))
    finally:
        if con is not None:
            con.close()
def f4():
    mw.deiconify()
    vw.withdraw()

def f5():
    id =0
    try:
        id = int(aw_ent_id.get())
        if id <1:
            raise Exception("min id shud be 1")
    except ValueError:
        showerror("Issue", "interger only")
        aw_ent_id.delete(0, END)
        aw_ent_id.focus()
        return
    except Exception as e:
        showerror("Issue", str(e))
        aw_ent_id.delete(0, END)
        aw_ent_id.focus()
        return       
    name = aw_ent_name.get()
    if(name=="") or (name.strip() =="") or (not name.isalpha()) or (len(name) < 2):
        showerror("issue", "invalid name")
        aw_ent_name.delete(0, END)
        aw_ent_name.focus()
        return
    mark = (aw_ent_mark.get())
    if(mark=="") or (mark.strip()=="") or (mark=="!@#$")  or (mark.isalpha()) or ( float(mark) > 100) or (float(mark) < 0):
        showerror("issue","enter valid marks")
        aw_ent_mark.delete(0, END)
        aw_ent_mark.focus()
        return

    con = None
    try:
        con = connect("gg.db")
        cursor = con.cursor()
        sql = "insert into student values('%d','%s','%s')"
        cursor.execute(sql%(id,name,mark))
        con.commit()
        showinfo("Sucess", "record created")
        aw_ent_name.delete(0, END)
        aw_ent_id.delete(0, END)
        aw_ent_mark.delete(0,END)
        aw_ent_id.focus()
    except Exception as e:
        con.rollback()
        showerror("issue", str(e))
    finally:
        if con is not None:
            con.close()

def f6():
    dw.deiconify()
    mw.withdraw()
def f7():
    mw.deiconify()
    dw.withdraw()
def f8():
    con = None
    try:
        con = connect("gg.db")
        cursor = con.cursor()
        sql = "delete from student Where id = ('%d')"
        id = int(dw_ent_id.get())
        

        try : 
            id = int(id)
        except Exception as e : 
            showerror("Failed" , "Id must be integer only") 	
            dw_ent_id.delete(0 , END)
            dw_ent_id.focus()
            return
        cursor.execute(sql %(id))
        if cursor.rowcount == 1 :
            con.commit()
            showinfo("Success" , "Record deleted")
            dw_ent_id.delete(0 , END)
            dw_ent_id.focus()
            return
        else :
            showerror("Failed" , "Record does not exists ")
            dw_ent_id.delete(0 , END)
            dw_ent_id.focus()
            return

    except Exception as e:
        con.rollback()
        showerror("issue", "Invalid id")
        dw_ent_id.delete(0 , END)
        dw_ent_id.focus()
    finally:
        if con is not None:
            con.close()
def f9():
    uw.deiconify()
    mw.withdraw()

def f10():
    id = uw_ent_id.get()
    if(id=="") or (id.strip=="") or (int(len(id))<1) or (id.isalpha()) or (id=="!@#$"):
        showerror("Issue","Invalid id")
        uw_ent_id.delete(0, END)
        uw_ent_id.focus()

        return 
    nm = uw_ent_name.get()
    if(nm=="") or (nm.strip=="") or (not nm.isalpha()) or (float(len(nm))<2) :
         showerror("Issue","Invalid name")
         uw_ent_name.delete(0, END)
         uw_ent_name.focus()
         return
    mr = uw_ent_mark.get()
    if(mr=="") or (mr.strip=="") or (mr.isalpha()) or (float(mr)<0) or (float(mr)>100) :
         showerror("Issue","Invalid name")
         uw_ent_mark.delete(0, END)
         uw_ent_mark.focus()
         return
         
         



    con = None
    try:
        con = connect("gg.db")
        cursor = con.cursor()
        sql1 = "update student set name = '%s', mark = '%s'  where  id = '%d'"
        nm = str(uw_ent_name.get())
        sal = int(uw_ent_mark.get())
        id = int(uw_ent_id.get())
        cursor.execute(sql1%(nm,sal,id))
        con.commit()
        showinfo("Sucess", "record Updated")
        uw_ent_name.delete(0, END)
        uw_ent_id.delete(0, END)
        uw_ent_mark.delete(0,END)
        uw_ent_id.focus()
    except Exception as e:
        con.rollback()
        showerror("issue", str(e))
    finally:
        if con is not None:
            con.close()        
    
def f11():
    mw.deiconify()
    uw.withdraw()

def f12():
	con = None
	try:
		con = connect("gg.db")
		cursor = con.cursor()
		sql = 'SELECT name, mark FROM student ORDER BY mark ASC '
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		mark = []
		for i in data:
			name.append(i[0])
			mark.append(i[1])
		plt.figure(figsize=(8,6))
		c = ['red', 'yellow', 'green' , 'orange' ]
		plt.rcParams.update({'text.color': "red", 'axes.labelcolor': "green"})
		
		plt.bar(name , sorted(mark) ,  color= c)
		plt.xlabel("Names of student" , fontsize = 15)
		plt.ylabel("mark of student", fontsize = 15)
		plt.title("Highest Mark's student in ascending order", fontsize = 15)
		plt.grid()
		plt.show()
	except Exception as e:
		showerror("issue ", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()


mw = Tk()
mw.title("Student App")
mw.geometry("700x600+50+50")
mw.configure(bg='light blue')

mw_btn_add = Button(mw, text="Add ", font=f,command=f1,height=1,width=6,fg='red',bg='light green')
mw_btn_delete = Button(mw, text="Delete ", font=f,command=f6,height=1,width=6,fg='red',bg='light green')
mw_btn_update = Button(mw, text="Update ", font=f, command=f9,height=1,width=6,fg='red',bg='light green')
mw_btn_view = Button(mw, text="View ", font=f, command=f3,height=1,width=6,fg='red',bg='light green')
mw_btn_chart = Button(mw , text="charts",font=f,command=f12,height=1,width=6,fg='red',bg='light green')
mw_btn_add.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_chart.pack(pady=10)


aw = Tk()
aw.title('Add student')
aw.geometry("700x600+50+50")
aw.configure(bg='light blue')
aw_lab_id =Label(aw, text="enter id", font=f,fg='Blue',bg='light blue')
aw_ent_id = Entry(aw, font=f)
aw_lab_name =Label(aw, text="enter name", font=f,fg='Blue',bg='light blue')
aw_ent_name = Entry(aw, font=f)
aw_lab_mark =Label(aw, text="enter mark", font=f,fg='Blue',bg='light blue')
aw_ent_mark = Entry(aw, font=f)
aw_btn_save =Button(aw, text="save", font=f, command=f5,fg='red',bg='light green')
aw_btn_back =Button(aw, text="back", font=f, command=f2,fg='red',bg='light green')

aw_lab_id.pack(pady=10) 
aw_ent_id.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_mark.pack(pady=10)
aw_ent_mark.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()

vw = Tk()
vw.title("view data")
vw.geometry("700x600+50+50")
vw.configure(bg='light blue')
vw_st_data = ScrolledText(vw, font=f, height=10, width=35,fg='red',bg='light yellow')
vw_btn_back = Button(vw, font=f, text="back",command=f4,fg='red',bg='light green')
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

dw = Tk()
dw.title('Delete student')
dw.geometry("700x600+50+50")
dw.configure(bg='light blue')
dw_lab_id =Label(dw, text="enter id", font=f,fg='Blue',bg='light blue')
dw_ent_id = Entry(dw, font=f)

dw_btn_delete =Button(dw, text="delete", font=f, command=f8,fg='red',bg='light green')
dw_btn_back =Button(dw, text="back", font=f, command=f7,fg='red',bg='light green')

dw_lab_id.pack(pady=10) 
dw_ent_id.pack(pady=10)

dw_btn_delete.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()


uw = Tk()
uw.title('Update student')
uw.geometry("700x600+50+50")
uw.configure(bg='light blue')
uw_lab_id = Label(uw,text='enter id',font=f,fg='Blue',bg='light blue')
uw_ent_id = Entry(uw,font=f)

uw_lab_name =Label(uw,text='enter name',font=f,fg='Blue',bg='light blue')
uw_ent_name =Entry(uw,font=f)

uw_lab_mark = Label(uw,text='enter mark',font=f,fg='Blue',bg='light blue')
uw_ent_mark = Entry(uw,font=f)

uw_btn_update =Button(uw, text="Update", font=f, command=f10,fg='red',bg='light green')
uw_btn_back =Button(uw, text="Back", font=f, command=f11,fg='red',bg='light green')

uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)


uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)

uw_lab_mark.pack(pady=10)
uw_ent_mark.pack(pady=10)

uw_btn_update.pack(pady=10)
uw_btn_back.pack(pady=10)


uw.withdraw()




def on_closing():

        mw.destroy()
        aw.destroy()
        vw.destroy()
        dw.destroy()
        uw.destroy()
mw.protocol("WM_DELETE_WINDOW", on_closing)
aw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
dw.protocol("WM_DELETE_WINDOW", on_closing)
uw.protocol("WM_DELETE_WINDOW", on_closing)

mw.mainloop()
