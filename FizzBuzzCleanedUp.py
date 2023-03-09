number_count = 0
while (number_count <= 99):

        number_count += 1

        if number_count%3 == 0:
            
            print('--Fizz--')

        elif number_count%5 == 0:

            print('--Buzz--')

        else:

            print('--{}--'.format(number_count))


        
    
