ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
total = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8]
average = total/len(ages)
print(average)
print(sum(ages)/len(ages))

total = 0
for age in ages:
    total= total+ age
print(total/len(ages))
