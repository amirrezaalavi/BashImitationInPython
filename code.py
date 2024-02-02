import pygame
import os
import random
import shutil
codes = []
line = []
commands = ["cd","mv","cp","rename","ls","addtofile","exist","search","mkdir","rmdir","cat","touch"]
path = []
fpath = ""
illegal = ["K_TAB","K_ENTER","K_ESCAPE","K_RETURN","K_BACKSPACE"]
pygame.init()
pygame.font.init()
display = pygame.display.set_mode((800,600))
old_fpath = ""
old_path = []
result = []
os = ""
g_massage = ""
de_massage = ""
p_massage = ""
## IMPORTANT!!!
def addcodes():
    for i in range(48,58):
        codes.append("K_" + chr(i))
    for i in range(97,123):
        codes.append("K_" + chr(i))
    codes.append("K_EQUAL","K_HASH","K_EXCLAIM","K_PERIOD","K_COMMA","K_DOLLAR")
    codes.append("K_SLASH","K_BACKSLASH","K_COLON","K_SEMICOLON","K_AT","K_CARET","K_RIGHTBRACKET","K_RIGHTBRAKET","K_QUOTEDBL","K_QUOTED")
    codes.append("K_ESCAPE","K_RETURN","K_BACKSPACE")
    # correct or not? K_ENTER
    codes.append("K_TAB","K_ENTER")
    codes.append("K_LESS")
    codes.append("K_GREATER")
    codes.append("K_QUESTION","K_PLUS","K_MINUS","K_LEFTPAREN","K_RIGHTPAREN","K_AMPERSAND")

def switch(var,compares):
    for i in range(len(compares)):
        if(var == compares[i]):
            return compares[i]
    return False

pygame.init()
pygame.font.init()
display = pygame.display.set_mode((800,600))
old_fpath = ""
old_path = []
result = []
g_massage = ""
de_massage = ""
p_massage = ""


# PROBLEM!!
# accounting:
def add_account(line):
    if():
        print("I can't find your OS, please let me know by login to a directory ---> \"cd [somewhere]\"")
        start()
    name = line[1]
    password = input("please enter a password for your account(between 4 and 10 digits):")
    if(len(password) < 4 or len(password) > 10):
        for i in range(4):
            password = input("invalid password, please try again:")
            if(len(password) > 4 or len(password) < 10):
                break
            if(i == 3):
                print("too many attempts, please try again later...")
                start()
    if(len(password) > 4 or len(password) < 10):
        if(os == "windows"):
            nu = input("enter name of user you want to make: ")
            user = input("for continue, please enter your computer user name: ")
            add = "C:\\Users\\" + user + "\\" + nu
            if (os.path.isdir(add)):
                print("I have a question : ARE YOU KIDDING ME? you had created that account!")
                start()
            else:
                try:
                    os.mkdir(add)

                except FileNotFoundError:
                    print("Oops! no user found in computer with this name!!!")
                    start()




        # if(os.path.isdir("/home/aloi_cmd")):
        #     a = "/home/aloi_cmd/" + name
        #     if(os.path.isdir(a)):
        #         print("I have a question : ARE YOU KIDDING ME? you had created that account!")
        #         start()
            # else:
            #     user = input("for continue, please enter your password: ")
            #     add = "C:\\Users\\" + user + "\\" + counter
            #     try:
            #        os.mkdir(add)
            #        counter = counter + 1
            #     except FileNotFoundError:
            #         print("Oops! no user found with this name!!!")
            #         start()





####
def search(array):
    try:
        global result
        path = array[0]
        fn = array[1]
        a = os.listdir(path)
        for i in range(len(a)):
            b = add_slash(path + add_bslash(a[i]))
            if(len(a[i]) >= len(fn)):
                name = a[i]
                equal = True
                for j in range(len(fn)):
                    if(fn[j] != name[j]):
                        equal = False
                if(equal == True):
                    result.append(b)
            if(os.path.isdir(b)):
                c = []
                c.append(b)
                c.append(fn)
                search(c)
        return(result)
    except PermissionError:
        print("\n", p_massage, "\n")




def goto(add):
    global fpath, path, old_path, old_fpath
    address = add[1]
    addres = add_bslash(address)
    b = fpath + addres
    old_path = path
    old_fpath = fpath
    if (os.path.isdir(b)):
        c = find_slash(addres)
        if (c == "/"):
            a = address.split("/")
            for i in a:
                q = "/" + i
                path.append(q)
        if (c == "\\"):
            a = address.split("\\")
            q = a[0]
            for i in range(1,len(a)):
                q = q + "\\" + a[i]
                path.append(q)
        fpath = ""
        for i in range(len(path)):
            fpath = fpath + path[i]
        start()
    else:
        print("\nno directory with this name! check your address.\n")
        start()
####




def find_slash(p):
    if(len(fpath) > 0):
        if(fpath[0] == "/"):
            return("/")
        elif(fpath[2] == "\\"):
            return("\\")
        else:
            return False


    else:
        if(p[0] == "/"):
            return("/")
        elif(p[2] == "\\"):
            return("\\")
####




def goback():
    global fpath , path
    if(fpath == ""):
        print(de_massage)
    fpath = ""
    a = len(path) - 1
    del path[a]
    for i in range(len(path)):
        fpath = fpath + path[i]
    start()
####




def cat(line):
    b = add_bslash(line[1])
    b = add_slash(fpath + b)
    if(fi_in_dir(fpath, line[1])):
        f = open(b,"r")
        e = f.readlines()
        for i in range(len(e)):
            print(e[i])
        f.close()
    else:
        print("\noh-oh! please check the file name or your directory...\n")
    start()
####



def touch(line):
    if(fpath == ""):
        print(de_massage)
    b = fpath + "/"  + line[1]
    f = open(b,"x")
    f.write("# Created! \n")
    f.close()
    print(g_massage)
    start()
####




def add_slash(a):
    b=""
    for i in range(len(a)):
        b = b+a[i]
        if(a[i] == "\\" and a[i-1] != "\\" and a[i+1] != "\\"):
            b = b+ "\\"
        elif(a[i] == "/" and a[i-1] != "/" and a[i+1] != "/"):
            b = b + "/"
    return(b)
####



def fi_in_dir(a, b):
    c= list_dir(a)
    for i in range (len(c)):
        if(c[i] == b):
            return(True)
    return(False)
####



def add_bslash(a):
    if(len(fpath) >=1 and fpath[0] == "/" and a[0] != "/"):
        h = a
        a = "/"
        a = a + h
        return (a)
    elif(len(fpath) >=1 and fpath[2] == "\\" and a[0] != "\\"):
        h = a
        a = "\\"
        a = a + h
        return (a)
    else:
        return(a)
####




def cp(line):
    if(line[1] == "-t"):
        sdes = line[2]
        sdes = add_bslash(sdes)
        sdes = fpath + sdes
        sdes = add_slash(sdes)
        fdes = line[3]
        shutil.copy(sdes , fdes)
    elif(line[1] == "-r"):
        sdes = line[2]
        fdes = line[3]
        sdes = add_bslash(sdes)
        fdes = add_bslash(fdes)
        sdes = fpath + sdes
        sdes = add_slash(sdes)
        fdes = fpath + fdes
        fdes = add_slash(fdes)
        shutil.copy(sdes , fdes)
    else:
        sdes = add_slash(line[1])
        fdes = add_slash(line[2])
        shutil.copy(sdes , fdes)
    print(g_massage)
    start()
####


def rename(line):
    sdes = line[2]
    fdes = line[3]
    sdes = add_bslash(sdes)
    fdes = add_bslash(fdes)
    sdes = fpath + sdes
    sdes = add_slash(sdes)
    fdes = fpath + fdes
    fdes = add_slash(fdes)
    os.rename(sdes , fdes)
    print(g_massage)
    start()




####
def mv(line):
    if(line[1] == "-t"):
        sdes = line[2]
        sdes = add_bslash(sdes)
        sdes = fpath + sdes
        sdes = add_slash(sdes)
        fdes = line[3]
        shutil.move(sdes , fdes)
    elif(line[1] == "-r"):
        sdes = line[2]
        fdes = line[3]
        sdes = add_bslash(sdes)
        fdes = add_bslash(fdes)
        sdes = fpath + sdes
        sdes = add_slash(sdes)
        fdes = fpath + fdes
        fdes = add_slash(fdes)
        shutil.move(sdes , fdes)
    else:
        sdes = add_slash(line[1])
        fdes = add_slash(line[2])
        shutil.move(sdes , fdes)
    print(g_massage)
    start()
####




def addto(line):
    d = line[1]
    a = line[2]
    a = a.split("\"")
    d = add_bslash(d)
    d = add_slash(fpath + d)
    file = open(d, "a")
    file.write(a[1])
    file.close()
    print(g_massage)
    start()

####





def list_dir(a):
    c = add_slash(a)
    b = os.listdir(c)
    return(b)
####




def show_dir(line):
    try:
        b = add_bslash(line[1])
        b = add_slash(fpath + b)
    except IndexError:
        b = fpath

    if(b == ""):
        print(de_massage)
        start()

    a = list_dir(b)
    print()
    print()
    for i in range(len(a)):
        des = add_bslash(a[i])
        fdes = add_slash(fpath + des)
        if(os.path.isdir(fdes) == True):
            print(a[i],"\t\t[FOLDER]")
        else:
            print(a[i])
            print()
    print()
    print()
    start()
####




def rmdir(line):
    if (fpath == ""):
        print(de_massage)
    dire=line[1]
    a = fpath + "/" +dire
    os.rmdir(dire)
    start()
####




def rm(line):
    des = add_bslash(line[1])
    fdes = fpath + des
    if(os.path.isfile(fdes)):
        os.remove(fdes)
####




def mkdir(line):
    fn=line[1]
    dire = fpath+"/"+fn
    os.mkdir(dire)
    start()
####



def isdir(line):
    b=[]
    fn=line[2]
    dire=line[1]
    if(fi_in_dir(dire, fn) == True):
        print(g_massage)
    else:
        print("\noh-oh! I think you were wrong :|\n")
####




def help():
    print("OK,")
    f = open("help", "r")
    start()
####



def get_massages():
    global de_massage, g_massage, p_massage
    d = open("dir_undefined_massage","r")
    g = open("good_massage","r")
    p = open("permission_massage", "r")
    m = d.readlines()
    rand = random.randint(0, len(m)-1)
    de_massage = m[rand]
    m = g.readlines()
    rand = random.randint(0, len(m)-1)
    g_massage = m[rand]
    m = p.readlines()
    rand = random.randint(0, len(m)-1)
    p_massage = m[rand]


####



def start():
    global fpath, os
    if(fpath != "" and os == ""):
        if fpath[0] == "/":
            os = "unix"
        else:
            os = "dos"
    for event in pygame.event.get():
        a = switch(event.keydown.get(), codes)
        if a :
            if a not in illegal :
                fpath = fpath + a[2]
                # WRITE WHAT WAS TYPED
                start()
            elif a == "K_TAB" :
                line.split(" ")
                for i in commands:
                    a = True
                    for j in range(len(line[0])):
                        if line[j] != i[j]:
                            a = False
                            break;
                    if a == True:
                        fpath = i
                        start()
                        # WRITE THAT COMMAND AGAIN!
            elif a == "K_ENTER" or a == "K_RETURN":
                line = fpath.split(" ")
                if(line[0] =="cd" or line[0] == "change directory"):
                    if(line[1] == ".."):
                        goback()
                    elif(line[1] == "root" or line[1] == "/"):
                        fpath = ""
                        path = []
                        start()
                    elif(line[1] == "prev"):
                        fpath = old_fpath
                        path = old_path
                        start()
                    else:
                        goto(line)
                if (fpath != ""):
                    if(line[0] == "ls" or line[0] == "list directory"):
                        show_dir(line)
                    elif(line[0] == "pwd"):
                        if fpath == "":
                            print("\nactually.... no where!!! [HA HA HA ... ] try to enter path by using \"cd\" command\n")
                            start()
                        print(fpath)
                        start()
                    elif(line[0] == "rmdir" or line[0] == "remove directory"):
                        rmdir(line)
                    elif(line[0] == "mkdir" or line[0] == "make directory"):
                        mkdir(line)
                    elif(line[0] == "exist"):
                        isdir(line)
                    elif(line[0] == "cat" or line[0] == "file index"):
                        cat(line)
                    elif(line[0] ==  "search"):
                        array = []
                        array.append(fpath)
                        array.append(line[1])
                        result = search(array)
                        for i in range(len(result)):
                            print(result[i])
                        start()
                    elif(line[0] == "touch" or line[0] == "make file"):
                        touch(line)
                if (line[0] == "addtofile"):
                    addto(line)
                elif(line[0] == "cp" or line[0] == "copy"):
                    cp(line)
                elif(line[0] == "mv" or line[0] == "move"):
                    mv(line)
                elif(line[0] == "rename" or line[0] == "rename"):
                    rename(line)
                elif(line[0] == "help" or line[0] == "bring your commands for me"):
                    help()
                elif(line[0] == "exit"):
                    exit()
                else :
                    print("\nI don't know, but somethings wrong! Maybe your entered a wrong command or you didn't defined path(for commands who need path)\n")
                    start()

start()
