min_stones = 1
pile = 50
max_stones = 5
player = 1



def valid_answer():
    while True:
        guess_text=input(f"player{player} how many stones do you want to take") 
        try:
            guess = int(guess)
            if guess > max_stones or guess < min_stones:
                raise ValueError()
            return guess
        except:
            print("who do you think you are you little brat🧌")


def play_nihmsyes(pile, max_stones):
        global player
        print (f"there are (pile) nimsyes")
        while pile >0:
             answer = valid_answer()
             pile -= answer
             if player == 1:
                  player = 2
             else:
                  player = 1
        if pile > 0 and player == 1:
             print("PLAYER ONE WINS NIMSYES🎊")
        else:
             print("player two takes the nimsyes")
             












#take stones
# ask p2
# take
# reapeat until done 







