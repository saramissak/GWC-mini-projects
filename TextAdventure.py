
# Update this text to match your story.

start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.'''

print(start)



print("Type 'left' to go left or 'right' to go right.") 

user_input = input()

while user_input != "left" and user_input != "right":
	print('try again')
	user_input = input()

if user_input == "left":

    print("You decide to go left and...") # Update to match your story.


    # Continue code to finish story.

 

elif user_input == "right":

    print("You choose to go right and ...") # Update to match your story.

    

    # Continue code to finish story.
#have one of the next three lines not all
#else:
#if not(user_input == "left" or user_input =="right") 	
#elif user_input != "left" or "right":
	#print("That is an invalid input. Try again! 'left' or 'right'?")
	#if user_input != 'left' or 'right':
		#print("That is an invalid input. Try again! 'left' or 'right'?")