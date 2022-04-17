from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title("โปรแกรมคำนวณเพื่อบรรลุอรหันต์")
GUI.geometry('800x800')

bg = PhotoImage(file= r"D:\Users\pattanapec\Desktop\Python\SiaO.png")
BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='ต้องการซื้อข้าวเหนียวมะม่วงเพื่อบรรลุอรหันต์กี่กิโลกรัม',font=(None,20))
L.pack() #แปะเข้าไปใน GUI

v_quantity = StringVar() #เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 99 #ราคา 99 บาทต่อกิโล * จำนวนมะม่วง
        messagebox.showinfo('ราคาทั้งหมดเพื่อบรรลุอรหันต์','ราคาข้าวเหนียวมะม่วงทั้งหมด {} บาท, บรรลุอรหันต์แล้ว!'.format(calc))
        v_quantity.set('')
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด', 'ตกนรก!')
        v_quantity.set('')
        E1.focus()

B = ttk.Button(GUI, text='คำนวณ', command=Cal)
B.pack(ipadx=30, ipady=20)

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา