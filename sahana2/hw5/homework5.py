#Git is a version control system that tracks the history of your code.
#GitHub is an online server that you store + share Git projects 

#Terminal is where you make commands that displays text and interacts with the operating system
#Commandline is the actual text based interface where you type 

#Local Repository is the one on your computer, a folder with version control abilities 
#Remote Repository is the one on Github that tracks changes when pushed from local to remote 

#Version Control is the abilitiy to keep history on changes made to code 

#Staging Area is where you prepare changes to be committed and tells Git what you want to commit 

#Git add means adding files to staging area 

#Git commit means committing changes to code to your version history 

#Git push means pushing changes from local repo to remote repo 

#Git status tells you the current state of the working directory and staging area 

#git pull gets the newest changes from the remote repo to the local repo 

#pwd is print working directory 

#ls is list contents of directory 

#cd is change directories 

#nano is create or edit a file 

#touch is create a file 

#mv is move one file or directory to a directory or to rename a file or directory 

#rm is to remove a file or directory

#cat is to list the contents or read file data and merge files 

#pwd will tell you what the current directory is 
#ls will list the contents of the directory 
#cd ../brianna_repo and then git pull origin main to grab newest update from remote repo 
#I would move it with: mv homework.py cd ../judy_decal/homework 
#to move to the repository i would also do cd ../judy_decal/homework
#to see the contents of homework.py i would do cat homework.py
#to save changes and pugh it would be: git add . , git commit -m"done with hw", git push origin main
#updates that you made are not made locally need to git pull to integrate the remote changes that happened 
#to move to Recents/ it would be cd /tilde/Recent/

def checkDataType(input):
    return type(input)


def evenOrOdd(number):
    if number % 2 == 0: 
        print('Even')
    else:
        print('Odd')


def sumWithLoop(numbers):
    total  = 0
    for x in numbers:
        total+= x 
    return total 

def duplicateList(lst):
    new_list = list()
    for i in range(len(lst)):
        for j in range(2):
            new_list.append(lst[i])
    return new_list
print(duplicateList(['a','b','c']))
#the error is there needs to be a colon after functino name 

