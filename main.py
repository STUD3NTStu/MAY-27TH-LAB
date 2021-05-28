'''
Question 1:
'''
'''
Structured english:
ask the user to input a binary number.
assign the input to an object.
assign the length of the input minus one to an object.
assign the total to an object.
create a while loop.
  the value of the current iteration multiplied by 2 to the power of the length minus one is added to the total.
  the length object is now equal to the length object minus 1.
print the total.

Pseudo code:
print('Please input a binary number to convert into decimal.')
binary is equal to input()
power is equal to int(len(binary)-1)
total is equal to 0
for i in binary:
  total is equal to total plus int(i)*2**power
  power is equal to power minus 1
print(total)
'''
'''
Code:
'''
'''
print('Please input a binary number to convert into decimal.')
binary=input()
power=int(len(binary)-1)
total=0
for i in binary:
  total+=int(i)*2**power
  power-=1
print(total)
'''
'''
print('Please input a binary number to convert into decimal.')
binary=input()
power=int(len(binary)-1)
total=0
for i in binary:
  while i!=0:
    total+=int(i)*2**power
    power-=1
    i+=i
print(total)
'''
'''
Question 2:
'''
'''
Structured english:
ask the user to enter any number of words they like that are only separated by ?.
assign the input an object.
replace all instances of the questionmark with spaces. Then, count all of the instances of ? and add one for the first word of the sentence before printing the total number of words.

Pseudo code:
print("Enter any number of words only separated by: ?.")
x equals input()
print('The final sentence is:\n', x.replace('?', ' '), '\n' 'and there are', x.count('?')+1, 'words in the sentence')
'''
'''
Code:
'''
'''
print("Enter any number of words only separated by: ?.") #asks the user to input as many words as they like.
x=input() #assigns the input to a object.
print('The final sentence is:\n', x.replace('?', ' '), '\n' 'And there are', x.count('?')+1, 'words in the sentence') #takes the input and replaces all instances of '?' with spaces before it counts all instances of the questionmark and adds one for the first word.
'''