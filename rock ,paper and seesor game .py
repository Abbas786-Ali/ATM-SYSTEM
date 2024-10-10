import random
user_choice=int (input("enter your choic: 1 for Rock ,2 for paper ,3 for scissors\n"))
commputer_choice=random.randint(1,3) 
print(f"cpmputer choice {commputer_choice} \n")
if(user_choice==commputer_choice):
    print("game is draw")
elif(commputer_choice>user_choice):1
    print("computer win the game and you lose")
elif(user_choice>commputer_choice) :
    print("you win the game  and computer lose") 
elif(user_choice<commputer_choice):
    print('you win the game  and you lose')  
elif( commputer_choice<user_choice):
    print('computer win the game  and you lose')  
elif(user_choice<=0):
    print('please enter volid number')