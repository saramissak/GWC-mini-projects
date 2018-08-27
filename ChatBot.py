# --- Define your functions below! ---

def introduce_self(name):
    print("Hi " + name)



# --- Put your main program below! ---

def main():
    user = input("What is your name?")
    introduce_self(user)
    lol(user)
    idek = input("Do you like popcorn?")
    random(idek)
    while True:
        answer = input("(What will you say?)")
        print("That's cool!")


def lol(name):
    print("you're so pretty " + name)

def random(omg):
    print(omg)






if __name__ == "__main__":

  main()


'''
other way of doing it: 


def introduce_self():
    print("Hi! I am a chatbot! No I am not human which may be a little disappointing to you. My name is Sara."")



def main():

  while True:

    answer = input("How bout you?")

    print("That's an awsome name! What's your favorite sports?")
    user_input = input()

    print("That's nice. Do you play any sports?")
    user_input = input()

    print("What do you do in your freetime?")
    user_input = input()

    print("That's great! Why do you do that?")
    user_input = input()

    print("Oh that's great")
    user_input = input()







if __name__ == "__main__":

  main()'''
