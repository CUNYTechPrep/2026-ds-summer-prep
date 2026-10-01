## THIS CODE WILL BREAK BECAUSE OF WHY....?


if __name__ == '__main__': 
    age = input("Please enter your age: ")
    print(f'You are {age} years old')
    keep_going = input('Would you like to keep going? Y or N')
    if keep_going == 'Y':
        print( 'in 10 years you will be', age+10, 'years old')
   
