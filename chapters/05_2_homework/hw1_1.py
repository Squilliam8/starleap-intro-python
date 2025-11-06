import getpass

print('ROCK.  PAPER.   SCISSORS.')

def playrps():

    rpc1 = getpass.getpass('player one, rock paper or scissors')
    rpc2 = getpass.getpass('player two, rock paper or scissors')

    if rpc1 == 'rock' and rpc2 == 'paper':
        print('ANNOUNCER: PLAYER TWO WINS A LIFETIME SUPPLY OF WHITE MONSTER')
        print('ANNOUNCER: PLAYER ONE HAS TO DRINK A REDBULL. GROSS...')

    if rpc1 == 'rock' and rpc2 == 'rock':
        print('ANNOUNCER: dang twin its a tie')

    if rpc1 == 'rock' and rpc2 == 'scissors':
        print('ANNOUNCER: PLAYER ONE GETS WILLIAMS AIRSOFT GUN!!! WILLIAM: WHAT NO I DIDNT SIGN UP FOR THIS!! ')

    if rpc1 == 'paper' and rpc2 == 'rock':
        print('ANNOUNCER: PLAYER ONE WINS A LIFETIME SUPPLY OF MONSTER')

    if rpc1 == 'paper' and rpc2 == 'paper':
        print(' ANNOUNCER: thats boring its a tie')

    if rpc1 == 'paper' and rpc2 == 'scissors':
        print('ANOUNCER:player one is really bad at this')

    if rpc1 == 'scissors' and rpc2 == 'rock':
        print('ANNOUNCER:PLAYER TWO WINS BRAGGING RIGHTS')

    if rpc1 == 'scissors' and rpc2 == 'paper':
        print('ANOUNCER: player one wins normaly ')

    if rpc1 == 'scissors' and rpc2 == 'scissors':
        print('ANNOUCER: tie.                                ANNOUNCER: i dont get paid enough for this')

playrps()

answer = 'yes'
while answer == 'yes':
    print('ANNOUNCER: ALRIGHT FOLKS WELCOME TO THE ROCK PAPER SCISSORS GAME SHOW TODAY WE HAVE TWO CONTESTANTS BATTLING FOR INFINITE MONSTER AND AIRSOFT GUNS! ')
    playrps() 
    answer = input ('do you want to play the rock paper scissors game show?')


