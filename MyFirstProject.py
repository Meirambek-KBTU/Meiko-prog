import os
import os.path

def MainMenu():
    print("""
    Welcome Athena ready for work
    0 - exit/quit
    1 - to manage a file 
    2 - to manage a directory""")

def FileOperation():
    print("""
    0 - Return to MainMenu
    1 - Show all files
    2 - Create new file 
    3 - Delete a file 
    4 - Rename file 
    5 - Add content to this file
    6 - Rewwrite content of this file""")
    add = int(input())
    if add == 0:
        return 0
    elif add == 1:
        from os import listdir
        from os.path import isfile, join
        files = [f for f in listdir(r"C:\Users\lenovo\Desktop\PP2") if isfile(join(r"C:\Users\lenovo\Desktop\PP2", f))]
        print(files)
    elif add == 2:
        FileName = input("New file name : ")+".txt"
        a = open(FileName,"tw")
        a.close()
    elif add == 3:
        FileName = input("File name : ")+".txt"
        a = True
        while a:
            try:
                os.remove()
            except FileNotFoundError:
                print("File was NOT find")
                answ = input("""
    Do you want to repeat?
    if you want to repeat press enter.
    Print (no) if don't want.
    """)
                if answ == 'no':
                    a = False
            else:
                print("File was deleted")
                a = False
    elif add == 4:
        a = True
        while a:
            FileName1 = input("Old file name : ")+".txt"
            FileName2 = input("New file name : ")+".txt"
            try:
                os.rename(FileName1, FileName2)
            except FileNotFoundError:
                print("File was NOT find")
                answ = input("""
    Do you want to repeat?
    if you want to repeat press enter.
    Print (no) if don't want.
    """)
                if answ == 'no':
                    a = False
            else:
                print("File name is successfully changed")
                a = False
    elif add == 5:
        b = True
        while b:
            FileName = input("Open file : ")+".txt"
            try:
                a = open(FileName, "at")
            except FileNotFoundError:
                print("File not found")
                answ = input("""
    Do you want to repeat?
    if you want to repeat press enter.
    Print (no) if don't want.
    """)
                if answ == 'no':
                    b = False
            else:
                information = input()
                a.write(information)
                a.close()
                b = False
    elif add == 6:
        b = True
        while b:   
            FileName = input("Open file : ")+".txt"
            try:
                a = open(FileName, "wt")
            except FileNotFoundError:
                print("File not found")
                answ = input("""
    Do you want to repeat?
    if you want to repeat press enter.
    Print (no) if don't want.
    """)
                if answ == 'no':
                    b = False
            else:
                information = input()
                a.write(information)
                a.close()
                b = False
    
def DirOperation():
    print("""
    0 - Return to MainMenu
    1 - Rename directories
    2 - Number of files
    3 - Number of directory 
    4 - list content 
    5 - Create new directories
    6 - Create new files
    """)
    add = int(input())
    if add == 0:
        return 0
    elif add == 5:
        DirectoryName = input("New directory name : ")
        os.mkdir(DirectoryName)
        print("Directory was created ")
    elif add == 1:
        a= True
        while a:
            DirName1=input("Old dir name : ")+".txt"
            DirName2=input("New dir name : ")+".txt"
            try:
                os.rename(DirName1,DirName2)
            except FileNotFoundError:
                print("File was NOT find")
                answ = input("""
    Do you want to repeat?
    if you want to repeat press enter.
    Print (no) if don't want.
    """)
                if answ == 'no':
                    a = False
            else:
                print("Dir name was changed")  
    elif add == 2:
        cmd=0
        for f in os.listdir():
            File=os.path.join(f)
            if os.path.isdir(File):
                cmd=cmd+1
        print("Number of Files is: ",cmd)
    elif add == 3:
        cmd=0
        for f in os.listdir():
            Dir=os.path.join(f)
            if os.path.isdir(Dir):
                cmd=cmd+1
        print("Number of Directory is: ",cmd)
    elif add == 4:
       print(os.listdir())
    elif add == 5:
        DirectoryName = input("New directory name : ")
        os.mkdir(DirectoryName)
        print("Directory was created ")
    elif add == 6:
        FileName = input("New file name : ")+".txt"
        a = open(FileName,"tw")
        a.close()

Work = True
while Work:
    MainMenu()
    add = int(input())
    if add == 0:
        print("program will out")
        Work=False 
    elif add == 1:
        print("you in file manager")
        FileOperation()
    elif add == 2:
        print("you in current location")
        DirOperation()

    