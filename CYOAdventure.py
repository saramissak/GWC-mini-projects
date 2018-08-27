start = '''
You wake up in the morning and school is closed and your friends want to go to the beach,
but your crush also wants to hang out.'''

print(start)

print('''You have the both options. Do you want to hang out with your
friends, or your crush? Type either 'friends' or 'crush'.''')
user_input = input()

while user_input != "friends" and user_input != "crush" and user_input != "parents" and user_input != "walk" and user_input != "again" and user_input != "lie" and user_input != "truth" and user_input != "fate" and user_input != "scream" and user_input != "thank him" and user_input != "number":
	print('try again')
	user_input = input()



if user_input == "friends":
    print('''On your way to the beach the tire of the car pops. Do want to call your
    parents or walk to the beach? Type 'parents' or 'walk'.''')
    user_input = input()
    if user_input == "parents":
        print('''You called your parents and they don't pick up, do you to try calling again or call your crush?
        Type 'again' or 'crush'.''')
        user_input = input()
        if user_input == "again":
            print("Your parents finally pick up and they drive you to the beach. You have a peaceful day at the beach.")
        elif user_input == 'cush':
            print("You call your crush and he gets mad at you so you all go home.")
    elif user_input == "walk":
        print('''You're walking to the beach and you step into quick sand. Do you scream for help or accept your fate.
        Type 'fate' or 'scream'.''')
        user_input = input()
        if user_input == "fate":
            print("GAME OVER")
        elif user_input == "scream":
            print('''A hot lifeguard comes to your rescue and he helps you out. Do you thank him or thank him and ask him for his number?
            Type 'number' or 'thank him'.''')
            user_input = input()
            if user_input == "thank him":
                print("You peacfully enjoy the frest of your day at the beach.")
            elif  user_input =="number":
                print("You two hit it off and he becomes your new boyfriend.")




elif user_input == "crush":
    print('''While you're with your crush the tire of the car pops. Do want to call your
    parents or walk to the beach? Type 'parents' or 'walk'.''')
    user_input = input()
    if user_input == "parents":
        print('''You called your parents and they pick up. They ask you who ask who you are withself.
        Do you tell them the truth or lie? Type 'lie' or 'truth'.''')
        user_input = input()
        if user_input == "lie":
            print('''You're parents find out the truth and get mad so you get grounded and go home.''')
        elif user_input== "truth":
            print('''Your parents have trust you and they drive you two to the beach. You and your crush have an amazing time.''')

    elif user_input== "walk":
        print("You two hit it off and he becomes your boyfriend.")
