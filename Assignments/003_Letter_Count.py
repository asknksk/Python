"""
Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes 
word / text analysis. You are asked to calculate the number of letters or any chars in 
the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter/chars of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.
"""
sentence =  input("Please enter your sentences : ")

my_dict = {}
new_sent = set(sentence)

for i in new_sent:
    counter = sentence.count(i)
    my_dict[i] = counter
print(my_dict)