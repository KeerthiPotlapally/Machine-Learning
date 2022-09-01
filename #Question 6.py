#Question 6 
#How many unique words have been used in the sentence? Use the split methods and set 
#to get the unique words.

def printWords(l):
     
    # for loop for iterating
    for i in l:
        print(i)
 
 
# Driver code
str = "I am a teacher and I love to inspire and teach people"
 
# storing string in the form of list of words
s = set(str.split(" "))
 
# passing list to print words function
printWords(s)