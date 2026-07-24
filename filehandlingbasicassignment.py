# %% [markdown]
# File Handling Assignment (Basic)
 
# Solve the following questions using Python File Handling.

# %% [markdown]
# ## Q1. Create a File
# 
# User se filename aur content input lo aur us content ko file me save karo.

# filename=input("enter your file name:")
# content=input("enter your content")
# with open("filename",'w') as file:
#     content.write("This is my content file")

# %% [markdown]
# ## Q2. Read a File
# 
# User se filename input lo aur file ka content print karo.

# file_name=input("enter file name:")
# with open('filename','r') as file:
#     print(file.read())

# %% [markdown]
# ## Q3. Check File Exists
# 
# User se filename lo. Agar file exist karti hai to **File Exists** print karo, warna **File Does Not Exist**.
# from pathlib import Path

# filename=input("enter file name:" )
# path=Path(filename)
# if path.exists():
#     print("file already exists")
# else:
#     print("file does not exist")

# %% [markdown]
# ## Q4. Update a File
# 
# Ek existing file me naya content append (add) karo.

# with open('filename','a') as file:
#     print(file.write("add this in the last"))
    

# %% [markdown]
# ## Q5. Delete a File

# import os
# os.remove('students.txt')ere


# %% [markdown]
# ## Q6. Rename a File
# 
# Old filename aur new filename input lo aur file rename karo.

# from pathlib import Path
# import os
# old_name=input("enter old file name")
# new_name=input("enter new file name")
# path=Path(old_name)

# if path.exists():
#  os.rename(old_name,new_name)
#  print("file name changed succesfully")
# else:
#  print("file does not exist")

# %% [markdown]
# ## Q7. Create Multiple Files
# 
# Loop ka use karke user se 3 filenames lo aur teeno files create karo.

# for i in range(3):
#  file_name=input("enter file names:")

#  with open("file_name",'w') as file:
#    pass
#  print("file_name")
# %% [markdown]
# ## Q8. Count Characters
# 
# Ek file read karo aur usme total characters count karke print karo.

# with open("newname",'r') as file:
#     content=file.read()
# print(len(content))

# %% [markdown]
# ## Q9. Count Words
# 
# Ek file read karo aur usme total words count karke print karo.

# with open("newname",'r') as file:
#     content=file.read()
# print(len(content.split()))


# %% [markdown]
# ## Q10. Mini File Manager
# 
# Menu Driven Program banao:
# 
# 1. Create File
# 2. Read File
# 3. Update File
# 4. Delete File
# 5. Rename File
# 0. Exit
# 
# User ke choice ke hisaab se operation perform karo.


import os
from pathlib import Path

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
    print("Press 5 for renaming a file")
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
       rename_file()




