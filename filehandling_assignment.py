# %% [markdown]
# # Python File Handling Assignment (Top 7)
# 
# Solve the following questions. Input/Output examples are provided.

# %% [markdown]
# ## Q1. Create a File
# 
# Write a program to create a file named `student.txt` and write your name into it.
# 
# ### Example Output (File Content)
# ```
# Rahul
# ```

# with open('student.txt','w') as file:
#     file.write("Rahul")


# %% [markdown]
# ## Q2. Read File
# 
# Read the contents of `student.txt` and print them.
# 
# ### Example Output
# ```
# Rahul
# ```


# with  open("student.txt",'r') as file:
#      print(file.read())

# %% [markdown]
# ## Q3. Write Multiple Lines
# 
# Create a file `fruits.txt` and write these fruits on separate lines:
# - Apple
# - Mango
# - Banana
# - Orange
# 
# Then read and print the file.
# 
# ### Expected Output
# ```
# Apple
# Mango
# Banana
# Orange
# ```

# with open("fruits.txt",'w') as file:
#    file.write("Apple\nMango\nBanana\nOrange")

# with open("fruits.txt",'r') as file:
#    print(file.read())

# %% [markdown]
# ## Q4. Append Data
# 
# Append `Grapes` to `fruits.txt` and print the final file.
# 
# ### Expected Output
# ```
# Apple
# Mango
# Banana
# Orange
# Grapes
# with open("fruits.txt", "w") as file:
#     file.write("Apple\nMango\nBanana\nOrange")
 
# file=open('fruits.txt','a')
# file.write('\nGrapes')

# with open('fruits.txt','r') as file:
#  print(file.read())



# %% [markdown]
# ## Q5. Count Lines
# 
# Count the total number of lines in a file.
# 
# ### Example File
# ```
# Apple
# Mango
# Banana
# Orange
# Grapes
# ```
# 
# ### Expected Output
# ```
# Total Lines = 5
# ```

# with open("fruits.txt", "r") as file:
#     line_count=len(file.readlines())
# print("Total lines=",line_count)


# %% [markdown]
# ## Q6. Count Characters
# 
# Count the total number of characters in a file.
# 
# ### Example File
# ```
# Hello
# Python
# ```
# 
# ### Expected Output
# ```
# Total Characters = 12
# ```

# content="Hello\nPython"
# print(len(content))


# %% [markdown]
# ## Q7. Count Words
# 
# Count the total number of words in a file.
# 
# ### Example File
# ```
# Python is very easy
# ```
# 
# ### Expected Output
# ```
# Total Words = 4
# ```


# content="Python is very easy"
# count_words=len(content.split())
# print("Total words = ",count_words)



