"""Game guess the number
PC guesses the number itself"""
    
import numpy as np
    
# number = np.random.randint(1, 101) # загадываем число

def random_predict(number:int=1) -> int:
    """ Guess  number randomly

    Args:
        predict_number (int, optional): number to guess. Defaults to 1.

    Returns:
        int: How many tries to guess the number
    """ 
    
    predict_number = np.random.randint(1, 101) # загадываем число
    
    count = 0 # Tries count
    min_number = 1 # Define min value
    max_number = 100 # Define MAX value
        
    while True:
        count += 1
        print('Given number:', number, 'Guess:', predict_number, ':', 'Try:', count)

        if predict_number > number:
           max_number = predict_number - 1
           predict_number = (max_number + min_number) // 2
 
 
        elif predict_number < number:
           min_number = predict_number + 1
           predict_number = (max_number + min_number) // 2
        else:
            print(f'The algoritm guessed the number {number} after {count} tries')
            break
    return count
random_predict()

print(f'number of tries: {random_predict()}')

def score_game(random_predict) -> int:
    """What's the average number of tries out of 1000 runs to guess the number

    Args:
        random_predict ([type]): Number guessing function

    Returns:
        int: Average number of tries
    """

    count_ls = [] # list to store number of tries
    np.random.seed(1) # determine a seed to make results replicable
    random_array = np.random.randint(1, 101, size=(1000)) # creating a list of numbers to guess

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # finds the average number of tries

    print(f'Average number of tries is {score}')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)
    
        
