import random
a = random.randint(1, 50)




count = 5
while count != 0:
    # if count == 0:
    #     break

    user_input = int(input("Guess the number : "))

    if(user_input == a):
        print(f"number is {a}")
        break

    elif user_input > a:
        print("to high")
        count = count - 1  
        continue
          

    elif user_input < a:
        print("too low")
        count = count - 1
        continue


if count==0:
    print(f"game over. right no is {a}")
        

        
