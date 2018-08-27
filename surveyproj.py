import json

questions = ["what is your name?", "What's your favorite animal?", "What's your favorite color?", "What's your astrology sign?", "What's you favorite snack from the kitchens at appnexus?"]
quesKeys = ["name", "animal", "color", "sign", "snack"]
people = []

def survey():

    #number= int(input('How many people being interviewed?')) #asks how many people are being interviewed and stores it into a variable
    #while number == '': #asks user for a response if they dont give a response and checks
    #    print('you must give a reponse')
    #    user_input=input()
    #index=0
    #while index < number: #repeats while loop while index is less than the number of people
    quesDict = { } #makes the inital dictionary
    #name = input(questions(1)) #creates key for dictionary
    for ques in range(len(questions)): #asks questions in the list
        answer = input(questions[ques]) #switches through the questions
        while answer == '':
            print('you must give a reponse')
            user_input=input()
            if user_input!= '':
                break
        quesDict[quesKeys[ques]] = answer #matches the key to the question into the dictionary
        #print(answer)
        #print(quesDict)
    #people.append(quesDict) #inserts name as a key into the dictionary
    #index += 1
    return quesDict



#survey()

'''
questions = ["What's your age?", "How many hours a day do you sleep?"]
keys = ["age", "sleep"]
responses = []

def take_survey():
    response = {}
    for i in range(len(questions)):
        print(questions[i])
        user_input = input("")
        while user_input == "":
            print("You must give a response")
            user_input=input()
        response[keys[i]] = int(user_input)
    return response
'''
def main():
    while True:
        quesDict = survey()
        people.append(quesDict)
        print("Do you want to take the survey again? Type Y for yes, N for no.")
        user_input = input()
        if user_input == "N":
            break

    dictionaryToJSON = json.dumps(people)
    f = open('responswJSON.txt.txt', 'w')
    f.write(dictionaryToJSON)
    f.close()
    print(people)

if __name__ == "__main__":
  main()
