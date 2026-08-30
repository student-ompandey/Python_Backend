# file handling project 

from pathlib import Path
import os

def createFile():
    name = input("Please tell your file name :- ")
    p = Path(name)

    try:
        if not p.exists():
              with open(p, "w") as fs:
                 data = input("what do you want to write in file :- ")
                 fs.write(data)
        
                 print("file created successfully")
        
        else:
            print("this file already exits")    

    except Exception as err:
        print(f"An error occured as {err}")

    
def readFile():
    try:
         name = input("Which file you want to read :- ")
         p = Path(name)
         if p.exists() and p.is_file():
                with open(p, 'r') as fs:
                    data = fs.read()
                    print(data)
        
                print("file readed successfully")
         else:
                print("this file doesnot exits")

    except Exception as err:
        print(f"An error occured as {err}")


def updateFile():
    try:
        name = input("Which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
                print("press 1 for change the file name :-")
                print("press 2 for overwriting the data of the file :-")
                print("press 3 for appending some data in your the file :-")
        
                res = int(input("Tell your response :- "))
                if res == 1:
                   name2 = input("tell your new file name :- ")
                   p2 = Path(name2)
                   p.rename(p2)
        
                if res == 2:
                    with open(p, 'w') as fs:
                        data = input("what you want to write this will overwrite the data :- ")
                        fs.write(data)
        
                if res == 3:
                            with open(p, 'a') as fs:
                                data = input("what you want to append :- ")
                                fs.write(" " +data)

    except Exception as err:
        print(f"an error occured as {err}")
    

def delete():
    try:
        name = input("Which file you want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
                os.remove(p)
                print("File remove successfully");
        else:
                print("No such file exits")

    except Exception as err:
        print(f"an error occured {err}")




print("press 1 for creating file")
print("press 2 for reading file")
print("press 3 for update file")
print("press 4 for delete file")

check = int(input("Please tell your response :- "))

if check==1:
    createFile()

if check==2:
    readFile()

if check==3:
    updateFile()

if check==4:
    delete()