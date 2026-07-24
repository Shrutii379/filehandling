# %% [markdown]
# # File Handling Assignment (CRUD)
# 
# Easy Beginner Assignment

# %% [markdown]
# ## Q1. Create File
# 
# Create a function `create_file()` that asks the user for a filename and content, then creates a new file.
# 
# **Example**
# ```
# Enter filename: notes.txt
# Enter content: Python is easy.
# 
# Output:
# File Created Successfully
# ```

"""with open("notes.txt",'w') as file:
    print(file.write("Python is easy"))
print("File created successfully")"""


# %% [markdown]
# ## Q2. Read File
# 
# Create a function `read_file()` that asks for a filename and displays its content.
# 
# **Example**
# ```
# Enter filename: notes.txt
# 
# Output:
# Python is easy.
# ```

"""def read_file():
    filename=input("enter filename")
    with open(filename,'r') as file:
     print(file.read())
read_file()"""

# %% [markdown]
# ## Q3. Update File
# 
# Create a function `update_file()` that appends new content to an existing file.
# 
# **Example**
# ```
# Enter filename: notes.txt
# Enter content: I love Python.
# 
# Output:
# File Updated Successfully
# ```

"""def update_file():
    filename=input("enter file name")
    with open(filename,'a') as fs:
        print(fs.write("\nI love Python"))
    print("file updated successfully")
update_file()"""

# %% [markdown]
# ## Q4. Delete File
# 
# Create a function `delete_file()` that deletes a file entered by the user.
# 
# **Example**
# ```
# Enter filename: notes.txt
# 
# Output:
# File Deleted Successfully
# ```
"""import os
def delete_file():
    filename=input("enter file name")
    os.remove(filename)
    print("file deleted successfully")
delete_file()"""


# %% [markdown]
# ## Q5. Rename File
# 
# Create a function `rename_file()` that renames an existing file.
# 
# **Example**
# ```
# Enter old filename: notes.txt
# Enter new filename: python_notes.txt
# 
# Output:
# File Renamed Successfully
# ```
"""import os
from pathlib import Path
def rename_file():
    old_name=input("enter old file name:")
    path=Path(old_name)

    if path.exists():
       new_name=input("enter  new file name")
       os.rename(old_name,new_name)
       print("file name changed")
    else:
        print("file does not exist")

rename_file()"""



# %% [markdown]
# ## Q6. Create Folder
# 
# Create a function `create_folder()` that creates a new folder.
# 
# **Example**
# ```
# Enter folder name: MyFiles
# 
# Output:
# Folder Created Successfully
# ```

"""from pathlib import Path
import os
def create_folder():
    foldername=input("enter folder name:")
    path=Path(foldername)

    if path.exists():
        print("folder already exists")
    else:
        os.mkdir(foldername)
        print("folder created successfully!!")
create_folder()"""

# %% [markdown]
# ## Q7. Delete Folder
# 
# Create a function `delete_folder()` that removes an empty folder.
# 
# **Example**
# ```
# Enter folder name: MyFiles
# 
# Output:
# Folder Deleted Successfully
# ```
"""from pathlib import Path
import os
def delete_folder():
    foldername=input("enter folder name:")
    path=Path(foldername)

    if path.exists():
        os.rmdir(foldername)
        print("folder deleted successfully")
    else:
         print("folder does not exist")
delete_folder()"""


# %% [markdown]
# ## Q8. Menu Driven Program
# 
# Create a menu-driven program that calls all the above functions.
# 
# ```
# ------ MENU ------
# 1. Create File
# 2. Read File
# 3. Update File
# 4. Delete File
# 5. Rename File
# 6. Create Folder
# 7. Delete Folder
# 0. Exit
# ```
# 
# The program should keep running until the user enters `0`.
# 

import os
from pathlib import Path




def create_file():
    filename = input('Enter your filename: ')
    path = Path(filename)

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



