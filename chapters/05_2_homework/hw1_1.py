
##### Template for Homework 1, Exercises 1-3 ######


print("********** Homework 1 Exercise 1 **********")

# Do your work for Exercise 1 here

print("Homework 1 Exercise 1: Not implemented") # Delete this line when you write your code!



print("********** Homework 1 Exercise 2 **********")

# Do your work for Excercise 2 here

print("Homework 1 Exercise 2: Not implemented") # Delete this line when you write your code!


def rpc12(rpc1,rpc2):

answer = input('want to play rock paper scissors?')
if answer == ('yes'):
    print ('ok')

rpc1 = input('what do you want to be rock paper or scissors')
rpc2 = input('what do you want to be rock paper or scissors')
if rpc1 == 'rock':print('ok what about player 2') 
if rpc1 == 'paper':
 print('ok what about player 2')
if rpc1 == 'scissors':
 print('ok what about player 2')



def is_triangle(a, b, c):
    print('is_triangle()', a, b, c)
    if a>= b + c:
        print('naw bro you got NO tringies')
    elif b>= a + c:
        print('naw bro you got NO tringies')
    elif c>= b + a:
        print('naw bro you got NO tringies')
   
   
    else:
        print("yeah twin its a tringie")


is_triangle(3, 4, 5)
is_triangle(2, 1, 1)
is_triangle(0, 0, 0)