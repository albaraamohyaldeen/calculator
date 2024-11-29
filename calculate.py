import tkinter
from tkinter import *
from tkinter import messagebox

tki = Tk()
tki.title('calculator')
tki.geometry('571x611+55+55')
tki.resizable(False,False)
tki.configure(bg = '#17161b')
 #متغير حفظ الأرقام

quetions = ''



#عرض الأرقام على الشاشة
def show(value):
   global quetions
   quetions = quetions+value
   
   label_res.config(text = quetions)

#مسح الشاشة  
def clear():
   global quetions
   quetions=''
   
   label_res.config(text = quetions)
   

#كود الحسبة
def calculate():
   global quetions
   res = ''
   if quetions != '':
      try:
         res = eval(quetions)
         
      except:
         res = 'error'
         quetions =''
  
   label_res.config(text = res)
  
#مستطيل عرض الحسبة
label_res = Label(tki ,width =25,height=4,text='',font=('courier',31))
label_res.pack()


#أزرار الحاسبة   
Button(tki ,width= 7 ,height= 1, text= 'c' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#191d95', command = lambda : clear()).place(x=25,y=361)
Button(tki ,width= 3 ,height= 1 , text= '%' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#191d95',command =  lambda : show('%')).place(x=365,y=361)
Button(tki ,width= 3 ,height= 1 , text= '/' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#191d95',command =  lambda : show('/')).place(x=535,y=361)
Button(tki ,width= 3 ,height= 1 , text= '*' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#391d95', command = lambda : show('*')).place(x=535,y=501)
Button(tki ,width= 3 ,height= 1 , text= '+' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#391d95', command = lambda : show('+')).place(x=535,y=621)
Button(tki ,width= 3 ,height= 1 , text= '-' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#391d95', command = lambda : show('-')).place(x=535,y=741)
Button(tki ,width= 3 ,height= 3 , text= '=' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#391d95', command = lambda: calculate()).place(x=535,y=861)

Button(tki ,width= 3 ,height= 1 , text= '1' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('1')).place(x=25,y=501)
Button(tki ,width= 3 ,height= 1 , text= '2' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('2')).place(x=195,y=501)
Button(tki ,width= 3 ,height= 1 , text= '3' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('3')).place(x=365,y=501)
Button(tki ,width= 3 ,height= 1 , text= '4' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show('4')).place(x=25,y=621)
Button(tki ,width= 3 ,height= 1 , text= '5' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show('5')).place(x=195,y=621)
Button(tki ,width= 3 ,height= 1 , text= '6' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show('6')).place(x=365,y=621)
Button(tki ,width= 3 ,height= 1 , text= '7' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('7')).place(x=25,y=741)
Button(tki ,width= 3 ,height= 1 , text= '8' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('8')).place(x=195,y=741)
Button(tki ,width= 3 ,height= 1 , text= '9' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show('9')).place(x=365,y=741)

Button(tki ,width= 7 ,height= 1 , text= '0' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('0')).place(x=25,y=861)
Button(tki ,width= 3 ,height= 1 , text= '.' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show('.')).place(x=365,y=861)

Button(tki ,width= 3 ,height= 1 , text= '(' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36',command =  lambda : show('(')).place(x=25,y=1021)
Button(tki ,width= 3 ,height= 1 , text= ')' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show(')')).place(x=195,y=1021)
Button(tki ,width= 3 ,height= 1 , text= '°' ,font=('courier',30,'bold'),bd = 1,fg='#fff',bg='#2a3d36', command = lambda : show('°')).place(x=365,y=1021)


Button(tki,width=54,height=1,font= ('courier',9,'normal'),bd=1,fg='#fff',bg='#121d34').place(x=11,y=309)
Button(tki,width=1,height=30,font= ('courier',13,'bold'),bd=1,fg='#fff',bg='#121d34').place(x=-41,y=65)
Button(tki,width=1,height=30,font= ('courier',13,'bold'),bd=1,fg='#fff',bg='#121d34').place(x=701,y=65)
Button(tki,width=20,height=1,font= ('courier',25,'bold'),bd=1,fg='#fff',bg='#121d34').place(x=11,y=1125)
Button(tki,width=28,height=1,font= ('courier',18,'bold'),bd=1,fg='#fff',bg='#121d34').place(x=11,y=0)







tki.mainloop()
