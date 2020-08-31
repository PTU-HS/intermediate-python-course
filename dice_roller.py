
    
def main():
    import random
    dice_rolls = 2
    dice_sum = 0
    for i in range(0, dice_rolls):
    
        roll = random.randint(1,6)
        #Python's f-string functionality. 
        #By putting an f right before the quotes of the string you're printing, 
        #you can then print variables within the string
        dice_sum = dice_sum + roll
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()