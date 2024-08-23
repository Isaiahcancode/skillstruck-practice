counter = 0
while True:
   
    user_input = int(input("Enter a number (0 to stop): "))

    if user_input == 0:
        print(counter)
        break
    else:
        counter+=1
    
