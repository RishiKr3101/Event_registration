from tkinter import *
from PIL import ImageTk, Image
import sqlite3
r = Tk()
r.title("Registration")

conn = sqlite3.connect("data.db")

c = conn.cursor()

#c.execute(""" CREATE TABLE addresses(
 #              name text,
  #             roll_n integer,
   #            hostel text,
    #           phone_n integer,
     #          email text)
#""")




def submit():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:n, :rn, :h, :pn, :e)", {'n': n.get(), 'rn': rn.get(), 'h': h.get(),
                                                                     'pn': pn.get(), 'e': e.get()})
    conn.commit()
    conn.close()
    n.delete(0, END)
    rn.delete(0, END)
    h.delete(0, END)
    pn.delete(0, END)
    e.delete(0, END)



def show():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM ad")
    records = c.fetchall()
    rec = ''
    for rd in records:
        rec += str(r[0]) + ", roll no.=" + str(rd[1]) + "of hostel " + str(rd[2]) + " and contact:" + str(rd[3])+ "/" + str(rd[4]) + "\n"

    Label(r, text=rec).grid(row=8, column=0, columnspan=2)
    conn.commit()
    conn.close()


n = Entry(r, width=30).grid(row=0, column=1)
rn = Entry(r, width=30).grid(row=1, column=1)
h = Entry(r, width=30).grid(row=2, column=1)
pn = Entry(r, width=30).grid(row=3, column=1)
e = Entry(r, width=30).grid(row=4, column=1)

n_l = Label(r, text="Name").grid(row=0, column=0)
rn_l = Label(r, text="Roll No.").grid(row=1, column=0)
h_l = Label(r, text="hostel").grid(row=2, column=0)
pn_l = Label(r, text="phone no.").grid(row=3, column=0)
e_l = Label(r, text="email").grid(row=4, column=0)


submit_b = Button(r, text="Add record to DataBase", command=submit).grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
show_b = Button(r, text="Show records", command=show).grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


r.mainloop()