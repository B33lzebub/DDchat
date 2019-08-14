# coding=utf8
#DDchat v. 0.1.0
from tkinter import *
from tkinter import messagebox
import random


# - - - - - - - - - - MAIN WINDOW - - - - - - - - - - -
#
def win1():

    # - - - - - - GENERATOR Random part of USERNAME - - - - - -
    #
    def secgen():
        str = '1234567890'*10 + 'qwertyuiopasdfghjklzxcvbnm'*9 + 'QWERTYUIOPASDFGHJKLZXCVBNM'*6 + '~!@#$%^&*****:?==+<>' #Consist of
        lst = list(str) #str -> list
        random.shuffle(list(str)) #Mixing
        secret = ''.join([random.choice(lst) for x in range(6)]) # Picking
        return secret

    # - - - - - - GENERATOR Random default message - - - - - - -
    #
    def sayhi():
        de = ['> Введите сообщение здесь <'] #1
        dn = ['Привет всем!','Здорово, что это за хрень?','Пжлст, дайте центральных процессоров...','Это был вирус, да?','УDDчи тебе, путник!','Чего нового чуваки?'] #2,3,4,5,6
        da = dn + de*9 #Probability of #1 = 3/5;   6/(9+6) = 6/15 = 3/5;
        hi = ''.join([random.choice(da)]) #Picking
        return hi

    # - - - - - - - - SPAMMER - - - - - - - - - - -
    #
    # def loopproc():
    #    log.insert(END, 'SYSTEM: Hello ' + name.get() + '!\n')
    #    tk.after(10000, loopproc)
    #Only for testing and non public use, srsly. Don't be an asshole.

    # - - - - - - - Entering MSG - - - - - - - - -
    #
    def sendproc(event): #Forwarding
        button_clicked()

    def button_clicked():
        log.config(state=NORMAL) #Making log editable
        if ((text.get() and name.get()) != '') and (text.get() != "> Введите сообщение здесь <") and (name.get() != "> Введите никнейм здесь <"):
            log.insert(END, name.get() + ': ' + text.get() + '\n') #If message not empty and not stupid-default
            f.write(name.get() + ': ' + text.get() + '\n') #Writing
            text.set('')
        else:
            if (text.get() == '') or (text.get() == "> Введите сообщение здесь <"):
                log.insert(END, '' + '[!] ВВЕДИТЕ ТЕКСТ СООБЩЕНИЯ [!]\n')
                text.set('> Введите сообщение здесь <')
            else:
                log.insert(END, '' + '[!] ВВЕДИТЕ НИКНЕЙМ [!]\n')
                name.set('> Введите никнейм здесь <')
        log.config(state=DISABLED) #Making log non editable

    # - - - - - Closing and hiding window - - - - - - -
    #
    def destroy():
        tk.destroy()

    def hide():
        tk.destroy()
        win2()

    # - - - - - - - - INFO / ABOUT - - - - - - - - -
    #
    def info():
        messagebox.showwarning('About',
                               "FAQ:\n\n- Что это такое?\n    Это оффлайн чат для DeadDrop-ов (deaddrops.com)\n    Используйте его для простого и удобного обмена\n    сообщениями с другими пользователями.\n\n- Чем это отличается от редактирования .txt файла?\n    Вообще-то ни чем. Просто такой чат смотрится круче и\n    написан на Python.\n\n- Что внутри?\n    Эта довольно простая программа основана на Python\n    и Tkinter (стандартный GUI пакет)\n    Весь исходный код открыт для чтения и\n    редактирования. ЭТОТ СОФТ НЕ ДЛЯ КОМЕРЧЕСКОГО\n    ИСПОЛЬЗОВАНИЯ.\n\n- Это что-то реально нужное?\n    Решать вам.\n\n- Могу ли я скопировать это на свой DeadDrop?\n    Да, конечно. Но убедитесь, что это последняя и не\n    модифицированная версия.\n    И не забудье ознакомиться с README.\n\n - Откуда я могу скачать последнюю версию этой\n    программы?\n    Из моего GitHub репозитория. Ссылка ниже.\n\nGitHub: github.com/B33lzebub/DDchat\n\nВсё сделал B33lzebub")


    # - - - - - - - WINDOW SETTING  - - - - - - - -
    #
    tk = Tk()
    tk.lift() #Lift window over others
    tk.attributes('-topmost', True) #Lift window over others
    tk.title('Offline Chat') #Title of window
    tk.geometry('500x605+10+10') #Window size
    tk.resizable(False,False) #Make window non resizable
    tk.overrideredirect(True) #Make window looks nice
    tk.tkraise()

    # - - - - - - - FRAMES in WINDOW - - - - - - -
    #
    frame1 = Frame(tk, bg='black') #Title + 2 Buttons
    frame2 = Frame(tk, bg='black') #Main part: LOG + Scrollbar
    frame3 = Frame(tk, bg='black') #Nickname + MSG

    frame1.pack(side = TOP, expand='False', fill = X)
    frame2.pack(side = TOP, expand='False', fill = X)
    frame3.pack(side = BOTTOM, expand='False')

    # - - - - - - - - - StringVar-s - - - - - - - -
    #
    text = StringVar()
    name = StringVar()
    name.set('User_' + secgen())  # Default USERNAME
    text.set(sayhi())  # Default TEXT

    # - - - - - - - OBJECTS AND APPS - - - - - - - -
    #
    scrollbar = Scrollbar(frame2, orient = VERTICAL, bg='black', width='13', jump='1') #SCROLLBAR
    log = Text(frame2, height=29, bg='black', fg='white', yscrollcommand = scrollbar.set) #LOG
    titel = Label(frame1, text="DDchat - offline chat", height=1, bg='black', fg='white') #TITEL
    nick = Entry(frame3, textvariable=name, borderwidth=2, bg='black', fg='white') #NICKNAME
    ibut = Button(frame3, text="v. 0.1.0 alpha", bg='black', fg='white') #INFORMATION BUTTON
    msg = Entry(frame3, textvariable=text, borderwidth=2, bg='black', fg='white') #MESSAGE
    but = Button(frame3, text='Send', bg='yellow') #ENTER BUTTON
    xbut = Button(frame1, text='☓', bg='black', fg='white', font='times 9') #CLOSE BUTTON
    sbut = Button(frame1, text='—', bg='black', fg='white', font='times 9') #HIDE BUTTON

    # - - - - - - - - - PACKING - - - - - - - - -
    #
    xbut.pack(side=RIGHT, expand='false', ipadx=25, ipady=1)
    sbut.pack(side=RIGHT, expand='false', ipadx=25, ipady=1)
    titel.pack(side=LEFT, fill='x', expand='false')
    scrollbar.pack(side = RIGHT, ipady=210, expand='True')
    log.pack(side=LEFT, fill='both', expand='True')

    # - - - - - - - - - GRIDS - - - - - - - - - -
    #
    #Upside
    nick.grid(row=1, column=1, rowspan=1, columnspan=1, ipady=15, ipadx=135)
    ibut.grid(row=1, column=2, rowspan=1, columnspan=1, ipady=13, ipadx=14)
    #Downside
    msg.grid(row=5, column=1, rowspan=1, columnspan=1, ipady=20, ipadx=135)
    but.grid(row=5, column=2, rowspan=1, columnspan=1, ipady=17, ipadx=35)

    # - - - - - - OBJ-S CONFIGURATIONS - - - - - - -
    #
    but.configure(command=button_clicked)
    xbut.configure(command=destroy)
    sbut.configure(command=hide)
    ibut.configure(command=info)
    scrollbar.config(command = log.yview)
    nick.config(insertbackground='white')
    msg.config(insertbackground='white')

    # - - - - - - - - SYSTEM MSGS - - - - - - - - - -
    #
    log.insert(END, '-'*51 + '\n  ____ _________ ____    ____ ____ ____ ____ ____\n /  _ Y  __/  _ Y  _ \  /  _ Y  __Y  _ Y  __Y ___\\\n | | \|  \ | / \| | \|  | | \|  \/| / \|  \/|    \\\n | |_/|  /_| |-|| |_/|  | |_/|    / \_/|  __|___ |\n \____|____\_/ \|____/  \____|_/\_\____|_/  \____/\n\n' + '-'*51 + '\n                 _   _______   _\n                ( ) /       \ ( )\n                 \\\\/  _   _  \//\n                  \| (_) (_) |/\n                   |    _    |\n                   /\ _/_\_ /\\\n                  // |     | \\\\\n                 (_) |[] []| (_)\n                     |_____|\n\n' + '-'*51 + '\n')
    log.insert(END, 'DDchat: Показано 50 последних сооббщений\n' + '-'*51 + '\n')
    log.insert(END, '\n' + ' ' * 10 + '> НЕ ЗАБУДЬТЕ ВВЕСТИ НИКНЕЙМ! <' + '\n\n')
    log.config(state=DISABLED)

    # - - - - Opening and reading TAIL of DB - - - -
    #
    with open('chat.txt') as f:
        data = f.readlines()
        tail = data[-50:]

    # - - - - - - Showing tail in LOG - - - - - - - -
    #
    log.config(state=NORMAL)
    for line in tail:
        log.insert(END, (line))
    log.config(state=DISABLED)

    #- - - - - - - - - OTHER - - - - - - - - -
    #
    f = open('chat.txt','a')
    msg.bind('<Return>', sendproc) #Enter button -> send
    #tk.after(10000, loopproc) - SPAMMER
    tk.mainloop() #loop

# - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - HIDDEN WINDOW - - - - - - - - - - - #
#
def win2():

    # - - - - - - Opening main window - - - - -
    #
    def open_win1():
        tk.destroy()
        win1()

    # - - - - - - - WINDOW SETTING  - - - - - - - -
    #
    tk=Tk()
    tk.lift() #Lift window over others
    tk.attributes('-topmost', True) #Lift window over others
    tk.title('Offline Chat Hidden')  #Title of window
    tk.geometry('48x26+10+10')  #Window size
    tk.resizable(False, False) #Make window non resizable
    tk.overrideredirect(True)  #Make window looks nice
    tk.tkraise()

    # - - - - - - - FRAMES in WINDOW - - - - - - -
    #
    frame1 = Frame(tk, bg='black')  #FRAME

    # - - - - - - - - - PACKING - - - - - - - - - -
    #
    frame1.pack(side=TOP, expand='False', fill=X)

    # - - - - - - - - - OBJECTS - - - - - - - - - -
    #
    but = Button(frame1, text='Back', bg='yellow')  #BUTTON "Back"

    # - - - - - - - - - PACKING - - - - - - - - - -
    #
    but.pack(expand='false', ipadx=5, ipady=1) #BUTTON size

    # - - - - - - - OBJ-S CONFIGURATIONS - - - - - -
    #
    but.configure(command=open_win1)

    tk.mainloop() #loop

win1() # Main window start

# THE END
# Created by B33lzebub
# GitHub: github.com/B33lzebub
