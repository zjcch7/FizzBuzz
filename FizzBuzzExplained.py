#Value holder for the number
number_count = 0

#count to 100
while (number_count <= 99):
#increase the count 1
        number_count += 1
#Print Fizz if number is divisible by 3
        if number_count%3 == 0:
            
            print('--Fizz--')
#Print Fizz if number is divisible by 5
        elif number_count%5 == 0:

            print('--Buzz--')
#Print number if neither
        else:

            print('--{}--'.format(number_count))


        
    
