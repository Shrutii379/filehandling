"""
CRUD - File Handling
Create
Read
Update
Delete
Rename a file.
"""
import os
from pathlib import Path



#----CREATE-----
def create_file():
    filename = input('Enter your filename: ')#spiderman.txt
    path = Path(filename)#c:\users\shrut\OneDrive\desktop\filehandling\superman.txt

    if path.exists():
        print('File already exists')
    else:
        with open(filename, 'w') as file:
            content = input('Enter your content: ')
            file.write(content)
            print('File Created...')

def read_file():
    filename = input('Enter your filename: ')
    path = Path(filename)
    if path.exists():
        with open(filename, 'r') as file:
           print(file.read())
    else:
        print('File does not exists...')

def update_file():
  filename=input('enter name of your file')
  path=Path(filename)
  if path.exists():
    with open(filename,'a') as file:
     content=input('enter your file content:')
     file.write(content)
     print('content added successfully')
  else:
      print('file does not exist')




def del_file():
    filename = input("Enter your filename: ")

    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully")
    else:
        print("File does not exist") 



def create_folder():
    foldername = input("enter your folder name:")
    path = Path(foldername)
    if path.exists():
        print("folder already exist")
    else:
        os.mkdir(foldername)
        print("folder created successfully!!")




def del_folder():
    foldername = input("enter your folder name:")
    path = Path(foldername)

    if path.exists():
        os.rmdir(foldername)
        print("folder deleted successfully!!")

    else:
        print("folder does not exist")



def rename_file():
    old_name=input("enter your file name")
    path=Path(old_name)

    if path.exists():
        new_name=input("enter your file name:")
        os.rename(old_name,new_name)
        print("File name changed...")
    else:
        print("file does not exist")        
       



while True:
    print("------Menu-----")
    print("Press 0 for exiting....")
    print("Press 1 for Creating a file")
    print("Press 2 for Reading a file")
    print("Press 3 for Updating a file")
    print("Press 4 for Deleting a file")
    print("Press 5 for  creating a folder")
    print("Press 6 for deleting a folder")
    print("Press 7 for renaming a file")
    choice = int(input('Enter your choice: '))

    if choice == 0:
        print('Exiting...')
        break

    elif choice == 1:
        create_file()

    elif choice == 2:
        read_file()

    elif choice==3:
        update_file()

    elif choice==4:
        del_file()

    elif choice==5:
        create_folder()

    elif choice==6:
        del_folder()

    elif choice==7:
       rename_file()
