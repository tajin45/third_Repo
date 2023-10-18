def num_divide3(num) :
    count = 0
    for i in range (1, num+1) :
        if i % 3 == 0 :
            count += 1
    return count

while True : 
        user_input = input("Please enter a positive integer or 'Done' to terminate:")
        if user_input.lower() == 'done' :
            print("Bye!!!")
            break
        try:
            num = int(user_input)
            if num <= 0 :
                print("Please enter a positive integer.")
            else:
                #result = num_divide3(num)
                print("Numbers divisible by 3 from 1 to ",num,": ",num_divide3(num))
        except :
                print("Invalid input.")