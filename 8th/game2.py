"""Game guess the number
PC guesses the number itself"""
    
import numpy as np
    
number = np.random.randint(1, 101) # загадываем число

def random_predict(number:int=1) -> int:
    """ Guess  number randomly

    Args:
        number (int, optional): number to guess. Defaults to 1.

    Returns:
        int: count
    """ 
    
    count = 0
        
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)                    
        if  number == predict_number:
            break
    return(count)

print(f'number of tries: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости, те рял соучайныз чисел будет всегда одинаковым
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
# change
if __name__ == '__main__':
    score_game(random_predict)
        
