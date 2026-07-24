#FILE HANDLING
#OPERATIONS WITH A FILE:
# 1. r -> kisi bhi file ko only read kar skte h
# 2. a -> kisi bhi existing content k last me new content add kar dega
# 3. w -> i. if a file does not exist then first it will create a file
#         ii. if a file and content already exists in it then it will replace the  previous content with the new content
# 4. x -> creates a file


#Reading a file
# file=open('loops.py','r')  #file is a variable here
# print(file.read())
#file.close()


#Using 'w' mode
# file=open('superman.txt','w')
# file.write('This is ironman file')
# file.close()



#Using 'a' mode
# file=open('superman.txt','a')
# file.write('This content is added at the last')
# file.close()





# with open('superman.txt','r') as chacha:  #open and closes file itself through this code
#     print(chacha.read())

# with open('batman.txt','w') as file:
#     print(file.write('This is my new file'))




# import os #operating system
# os.remove('batman.txt')  # we can remove any file using this