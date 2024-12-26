# A player will create a secret code, usually a 4-digit number.  This number should have no repeated digits.
# Another player makes a guess (4 digit number) to crack the secret number. Upon making a guess, 2 hints will be provided - Cows and Bulls.

# Bulls indicate the number of correct digits in the correct position
# and cows indicates the number of correct digits in the wrong position.

# For example, if the secret code is 1234 and the guessed number is 1246 then we have 2 BULLS (for the exact matches of digits 1 and 2)
# and 1 COW (for the match of digit 4 in the wrong position)

# The player keeps on guessing until the secret code is cracked.
# The player who guesses in the minimum number of tries wins.

class CowsAndBulls:
    def __init__(self, num):
        self.bulls = 0
        self.cows = 0
        self.num = num
        self.number = [int(digit) for digit in str(self.num)]

    def run_game(self):
        self.second_player()

    
    def second_player(self):
        while True:

            player_guess = input("Guess :")
            if len(player_guess) == 4:
                self.validate_guess(player_guess)

            elif len(player_guess) != 4:
                print("Invalid number.")

            else:
                print("Something Went Wrong.")

    
    def validate_guess(self, guess):
        self.bulls = 0
        self.cows = 0

#       split the number into 4 separate digits
        guess_list = [int(d) for d in guess]

#       -> create a replica of the original number
        unknown = self.number[:]

#       -> iterate for any bulls

        for x in range(4):
            if guess_list[x] == unknown[x]:
                self.bulls += 1
                guess_list[x] = -1
                unknown[x] = -2
#       -> if any bulls are found we mark it so we don't count duplicates


        for j in range(4):
            if guess_list[j] in unknown:
                self.cows += 1
                guess_list[j] = -2
#       -> if any cows are found we mark it

        print("--------------------")
        print(f"Response: BULLS: {self.bulls}")
        print(f"Response: COWS: {self.cows}")


#       if the user guesses 4 digits in the correct position
        if self.bulls == 4:
            print("--------------------")
            print(f"You have guessed the number correctly: {self.number}")
            exit()


if __name__ == '__main__':
#               -> Any Number
    x_ = CowsAndBulls(8965)
    x_.run_game()
