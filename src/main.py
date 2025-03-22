import random


class RockPaperScissors:
    """Rock Paper Scissors game class."""
    def __init__(self, ):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self, ):
        return random.choice(self.choices)

    def get_user_choice(self, ):
        user_choice = input('Enter your choice (R/r for rock, P/p for paper, S/s for scissors): ')
        if user_choice.lower() == 'r':
            return 'rock'
        elif user_choice.lower() == 'p':
            return 'paper'
        elif user_choice.lower() == 's':
            return 'scissors'
        else:
            print('Invalid choice. Please try again')
            return self.get_user_choice()

    def choose_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            self.user_score += 0
        elif user_choice == 'rock' and computer_choice == 'scissors':
            self.user_score += 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            self.user_score += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            self.user_score += 1
        else:
            self.computer_score += 1

    def play(self, ):
        maximum_score = input('Enter the maximum score to win the game: ')
        if not maximum_score.isdigit():
            print('Invalid input. please enter a number')
            return self.play()
        maximum_score = int(maximum_score)
        while self.user_score < maximum_score and self.computer_score < maximum_score:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f'User choice: {user_choice}')
            print(f'Computer choice: {computer_choice}')
            self.choose_winner(user_choice, computer_choice)
            print(f'User score: {self.user_score}')
            print(f'Computer score: {self.computer_score}')
        if self.user_score == maximum_score:
            print('Congratulations! You won the game :)')
        else:
            print('Owh! Computer won the game :(')


if __name__ == '__main__':
    while True:
        game = RockPaperScissors()
        game.play()
        play_again = input('Do you want to play again? (any key for yes, N/n for no): ')
        if play_again.lower() == 'n':
            break
