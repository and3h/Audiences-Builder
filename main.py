import random , string ,_thread
from tkinter import ttk ,messagebox,filedialog
from tkinter import *
import webbrowser

def thread_start():
    try:
        _thread.start_new_thread( start, () )
    except:
        messagebox.showerror("Error", "Error: unable to start thread \n Code Error : 1")
def start():
    saveop = {'filetypes': [('VCard File', '.vcf'), ('Text', '.txt')]}
    Number = Entry_Number.get()
    Country_Code = Entry_Country.get()
    Oprator = Entry_Oprator.get()
    if Number.isdigit() and Country_Code.isdigit() and Oprator.isdigit():
        try:
            file = open(filedialog.asksaveasfilename(**saveop), 'w')
            a = 0
            while a <= int(Number):
                a = a + 1
                ran = random.randint(0000000, 9999999) #crate RANDOM NUMBERS
                ranstr = (''.join(random.choice('qwertyuiiopasdfghjklzxcvbnm') for _ in range(5, 20)))
                out = ('\nBEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{0};;;\nFN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{1}\nTEL;CELL;PRF:+{4}{2}{3}\nEND:VCARD\n'.format(ranstr, ranstr, int(Oprator), ran, int(Country_Code)))
                file.write(out)
            file.close()
            messagebox.showinfo('Complet','Your Audiences were made')
        except ValueError:
            messagebox.showerror("Error", "ValueError: I/O operation on closed file. \n Code Error : Out-1")
        except:
            messagebox.showerror("Error", "Error: CAN NOT TO SAVE Audiences. \n Code Error : Out-2")
    else:
        messagebox.showerror("Error", "Error: Enter INTGER to Text Fileds. \n Code Error : Int-1")
def HELP():
    webbrowser.open('http://tgme.ir/Vcf')
def new():
    Entry_Number.delete(0,'end')
    Entry_Oprator.delete(0,'end')
    Entry_Country.delete(0,'end')
def About():
    msg = messagebox.showinfo('About us', '''
    Website : www.andeh.ir

    email : sasan_andeh@yahoo.com

    ver : 1.1
    ''')
def Load_File():
    filetype = (("Text Files", "*.txt"), ("Text Files", "*.txt"))
    messagebox.showinfo('اخطار', '''
        اگر از شماره ایران استفاده میکنید لطفا
        0 اول را پاک کنید
        نحوره درست شماره های داخل فایل : 9123456789
         نحوره نادرست شماره های داخل فایل : 09123456789
        ''')
    filename = filedialog.askopenfilename(initialdir="C:/", title="Select VCF file", filetypes=filetype)
    txt_file = str(filename)
    Entry_Text_File.delete(0, 'end')
    Entry_Text_File.insert(0, txt_file)
def Save_File():
    saveop = {'filetypes': [('VCard File', '.vcf'), ('Text', '.txt')]}
    path_file = Entry_Text_File.get()
    Country_Code = Entry_Country_File.get()
    if path_file != '':
        Numbers =  open(path_file,'r')
        Number = Numbers.readlines()
        file = open(filedialog.asksaveasfilename(**saveop), 'w')
        for i in Number:
            ranstr = (''.join(random.choice('qwertyuiiopasdfghjklzxcvbnm') for _ in range(5, 20)))
            out = '''
            
BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{0};;;
FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{1}
TEL;CELL;PRF:+{2}{3}
END:VCARD
                  
                        '''.format(ranstr, ranstr, Country_Code, i)
            file.write(out)
        file.close()
        messagebox.showinfo('Complet', 'Your Audiences were made')





main = Tk() # main Form
main.title('Audiences Creator') #Title
#main.iconbitmap('ico.ico') #icon program
main.geometry('310x200')
main.resizable(width=False, height=False)


######################## MENU Config
menu = Menu(main)
main.config(menu=menu)
filemenu = Menu(menu)
helpmenu = Menu(menu)
menu.add_cascade(label='فایل' , menu=filemenu)
menu.add_cascade(label= 'راهنمایی', menu=helpmenu)
filemenu.add_command(label='جدید',command=new)
filemenu.add_command(label= 'خروج', command=main.destroy)
helpmenu.add_command(label='راهنمایی',command=HELP)
helpmenu.add_command(label='درباره ما',command=About)
######################################################3


############### Tabs
tabs = ttk.Notebook(main)
tab_main = ttk.Frame(tabs)
tab_file_txt = ttk.Frame(tabs)

#############ADD TABS
tabs.add(tab_main,text='MAIN')
tabs.add(tab_file_txt,text='READING FILE')

############ ADDTAB TO MIAN FORM
tabs.pack(side=RIGHT,expand=1 ,fill='both')


############# TAB MAIN Widgets
lbl_Number =Label(tab_main,text ='How many do you need :')
lbl_Number.grid(row=1,column=0,pady=5,padx=5)

Entry_Number = Entry(tab_main)
Entry_Number.grid(row=1,column=1,pady=5,padx=5)

lbl_Country = Label(tab_main,text='Country Code(98,1,45...): ')
lbl_Country.grid(row=2,column=0,pady=5,padx=5)

Entry_Country = Entry(tab_main)
Entry_Country.grid(row=2,column=1,pady=5,padx=5)

lbl_Oprator =Label(tab_main,text='Oprator Code(515,933...):')
lbl_Oprator.grid(row=3,column=0,padx=5,pady=5)

Entry_Oprator = Entry(tab_main)
Entry_Oprator.grid(row=3,column=1,pady=5,padx=5)

btn_Create = ttk.Button(tab_main,text='Start',command=thread_start)
btn_Create.place(y=125,x=110)

############# TAB READING  FILE Widgets
lbl_Country_File = Label(tab_file_txt,text='Country Code :')
lbl_Country_File.grid(row=0,column=0,pady=10)

Entry_Country_File = Entry(tab_file_txt)
Entry_Country_File.grid(row=0,column=1,ipadx=25)


lbl_Text_File = Label(tab_file_txt,text='File (*.txt): ')
lbl_Text_File.grid(row=1,column=0,pady=5)

Entry_Text_File = Entry(tab_file_txt,text='File (*.txt): ')
Entry_Text_File.grid(row=1,column=1,pady=5,padx=0,ipadx=25)

btn_Text_File = ttk.Button(tab_file_txt,text='....',command=Load_File, width=4)
btn_Text_File.grid(row=1,column=2,pady=5,padx=5)

btn_Create2 = ttk.Button(tab_file_txt,text='Create',command=Save_File)
btn_Create2.place(y=125,x=110)






main.mainloop()