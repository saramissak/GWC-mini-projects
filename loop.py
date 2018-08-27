i = -1 #i starts off as -1
while True: #continue forever
  i += 1

  if(i > 20):
    break #breaks out of the loop (stops) if greater than 20 stops the loop

  # i is odd
  if(i % 2 !=0): #even number divided by two does not have a remainder if it does have a remainder then its odd
    continue #continues the loop kind of like a skip funstion

  print(i)
