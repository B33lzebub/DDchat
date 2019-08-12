from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def win2():

    def open_win1():
        tk.destroy()
        win1()

    tk=Tk()
    tk.lift() #Lift window over others
    tk.attributes('-topmost', True) #Lift window over others
    text = StringVar()
    text.set('Hello there!')  # Default TEXT
    tk.title('Offline Chat')  # Title of window
    tk.geometry('48x26+10+10')  # Window size
    tk.resizable(False, False)  # Make window unresizable
    tk.overrideredirect(True)  # Make window looks nice
    tk.tkraise()

    frame1 = Frame(tk, bg='black')  # Title + 2 Buttons
    frame1.pack(side=TOP, expand='False', fill=X)

    but = Button(frame1, text='Back', bg='yellow')  # ENTER BUTTON

    but.pack(expand='false', ipadx=5, ipady=1)

    but.configure(command=open_win1)

    tk.mainloop()

def win1():
    # - - - - - - - - SPAMMER - - - - - - - - - - -
    #
    # def loopproc():
    #    log.insert(END, 'SYSTEM: Hello ' + name.get() + '!\n')
    #    tk.after(10000, loopproc)

    # - - - - - - - Entering MSG - - - - - - - - -
    def sendproc(event):
        log.config(state=NORMAL)
        if (text.get() and name.get()) != '':
            log.insert(END, name.get() + ': ' + text.get() + '\n')
            f.write(name.get() + ': ' + text.get() + '\n')
            text.set('')

        else:
            log.insert(END, '' + 'ENTER USER NAME OR MASSAGE\n')
        log.config(state=DISABLED)

    def button_clicked():
        log.config(state=NORMAL)
        if (text.get() and name.get()) != '':
            log.insert(END, name.get() + ': ' + text.get() + '\n')
            f.write(name.get() + ': ' + text.get() + '\n')
            text.set('')
        else:
            log.insert(END, '' + 'ENTER USER NAME OR MASSAGE\n')
        log.config(state=DISABLED)

    def destroy():
        tk.destroy()

    def hide():
        tk.destroy()
        win2()


    def info():
        messagebox.showwarning('About',
                               "- WTF is this?\n    This is offline chat for DeadDrops (deaddrops.com)\n    Use it for nicely and easyest chating and reading messages\n    by other users.\n\n- What the diffrent between editting .txt file?\n    Actually nothing. But it^s looks more brutal and\n    it coded on Python.\n\n- What is this based on?\n    This simple program based on Python and Tkinter (standard     GUI package)\n    All source code is open for reading and editting. THIS IS            NOT FOR COMERCIAL USE.\n\n- Is this really usefull thing?\n    No just for fun and becous i can.\n- Can i copy this program on my own DeadDrop?\n    Yes, sure. But be sure its last not modified version.\n\n - Where can i download last version of this program?  \n    In my GitHub repository. Link down below.\n\nGitHub: github.com/B33lzebub/DDchat\n\nCreated by B33lzebub")

    # - - - - - - - WINDOW SETTING - - - - - - - -
    #
    tk = Tk()
    tk.lift() #Lift window over others
    tk.attributes('-topmost', True) #Lift window over others
    text = StringVar()
    name = StringVar()
    name.set('User') #Default USERNAME
    text.set('Hello there!') #Default TEXT
    tk.title('Offline Chat') #Title of window
    tk.geometry('500x605+10+10') #Window size
    tk.resizable(False,False) #Make window unresizable
    tk.overrideredirect(True) #Make window looks nice
    tk.tkraise()

    # - - - - - - - FRAMES in WINDOW - - - - - - -
    #
    frame1 = Frame(tk, bg='black') #Title + 2 Buttons
    frame2 = Frame(tk, bg='black') #Main part - LOG + Scrollbar
    frame3 = Frame(tk, bg='black') #Nickname + MSG

    frame1.pack(side = TOP, expand='False', fill = X)
    frame2.pack(side = TOP, expand='False', fill = X)
    frame3.pack(side = BOTTOM, expand='False')

    # - - - - - - - OBJECTS AND APPS - - - - - - - -
    #
    scrollbar = Scrollbar(frame2, orient = VERTICAL, bg='black', width='13', jump='1') #SCROLLBAR
    log = Text(frame2, height=29, bg='black', fg='white', yscrollcommand = scrollbar.set) #LOG
    titel = Label(frame1, text="Log Cat and All That Things", height=1, bg='black', fg='white') #TITEL
    nick = Entry(frame3, textvariable=name, borderwidth=2, bg='black', fg='white') #NICKNAME
    ibut = Button(frame3, text="v. 0.0.6 alpha", bg='black', fg='white') #INFORMATION BUTTON
    msg = Entry(frame3, textvariable=text, borderwidth=2, bg='black', fg='white') #MESSAGE
    but = Button(frame3, text='Send', bg='yellow') #ENTER BUTTON
    xbut = Button(frame1, text='╳', bg='black', fg='white', font='times 9') #CLOSE BUTTON
    sbut = Button(frame1, text='—', bg='black', fg='white', font='times 9') #HIDE BUTTON
    # - - - - - - - USING OBJ&APPS - - - - - - - - -
    #
    #nick.pack(side=BOTTOM, fill='x', expand='false')
    #msg.pack(side=LEFT, fill='x', expand='true')
    #but.pack(side=LEFT, expand='false')
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
    log.insert(END, '-'*51 + '\n  ____ _________ ____    ____ ____ ____ ____ ____\n /  _ Y  __/  _ Y  _ \  /  _ Y  __Y  _ Y  __Y ___\\\n | | \|  \ | / \| | \|  | | \|  \/| / \|  \/|    \\\n | |_/|  /_| |-|| |_/|  | |_/|    / \_/|  __|___ |\n \____|____\_/ \|____/  \____|_/\_\____|_/  \____/\n\n' + '-'*51 + '\n                 _   _______   _\n                ( ) /       \ ( )\n                 \\\\/  _   _  \//\n                  \| (_) (_) |/\n                   |    _    |\n                   /\ _/_\_ /\\\n                  // |     | \\\\\n                 (_) |[] []| (_)\n                     |_____|\n\n' + '-'*51 + '\n\n')
    log.insert(END, 'SUSTEM: SHOWED 50 LAST MASSAGES\n' + '-'*51 + '\n')
    log.config(state=DISABLED)

    # - - - - Opening and reading TAIL of DB - - - -
    #
    with open('msgs.txt') as f:
        data = f.readlines()
        tail = data[-50:]

    # - - - - - - Showing tail in LOG - - - - - - - -
    #
    log.config(state=NORMAL)
    for line in tail:
        log.insert(END, (line))
    log.config(state=DISABLED)
    #- - - - - - - - - - - - - - - - - - - - - - - -


    f = open('msgs.txt','a')
    msg.bind('<Return>', sendproc)
    #tk.after(10000, loopproc) - SPAMMER
    tk.mainloop()

win1()

