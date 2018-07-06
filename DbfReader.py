from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from pathlib import Path
import zipfile

root = Tk()

def onOpen1():
    e1.delete(0, END)
    e1.insert(0, filedialog.askopenfilename(filetypes=(("файлы запросов", "*.ZIP;*.zip")
                                                             , ("All files", "*.*"))))


def unzip():

     zip_ref = zipfile.ZipFile(e1.get(), 'r')
     spisok=zip_ref.namelist()
   #  print(spisok)
     q='Q{'+Path(e1.get()).resolve().stem+'}.DBF'


    # print(q)

     zip_open=zip_ref.open(q)



     stroka=zip_open.read().decode('cp866')


     stroka=stroka[320:370]
   #  print(stroka)


     zip_ref.close()


    # print('Работа завершена')

     mb.showinfo(message=Path(e1.get()).resolve().name+'\n -это '+stroka)



l3 = Label(root, text='Путь на файл', justify=RIGHT)

e1 = Entry(root, width=50)



b1 = Button(root, text="Выбрать zip файл для просмотра ", command=onOpen1)


l3.grid(row=0,column=0)

e1.grid(row=0, column=1,  padx=5, pady=5)



b1.grid(row=0, column=2, padx=5, pady=5)

b3 = Button(root, text="Посмотреть", command=unzip)
b3.grid(row=3, column=2, padx=5, pady=5)

root.title("Утилита для просмотра имени поставщика в zip архиве ")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))


root.mainloop()