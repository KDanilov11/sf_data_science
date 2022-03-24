"""Game guess the number"""
    
import numpy as np
    
number = np.random.randint(1, 101) # загадываем число
    
count = 0
    
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100 "))
    print()
        
    if  predict_number > number:
        print('Number is smaller <<')        
            
    elif predict_number < number:
        print('Number is bigger >>')
                
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток')
        break # end of the game and quiting the cicle 
