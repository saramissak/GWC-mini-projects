GerToEng = {
  'Halo': 'Hello',
  'Guten Morgen': 'Good Morning',
  'Warum?': 'Why',
  'eins': 1,
  'zwei': 2,
  'drei': 3,
  'vier': 4,
  'fuenf': 5,
}
five = GerToEng['fuenf']
print(five)
print(GerToEng)


our_students = {
    "kingsley": {
        "age": 21,
        "gender": "male",
        "fav_movies": ['the orphan', 'incredibles'],
    },
    "dallas":{
        'age': 52,
    },
    "total_students": 21,
}

if 'laura' in our_students.keys():
    print(our_students["laura"])
print(our_students)
print(our_students['total_students'])
print(our_students['dallas'])
print(our_students['dallas']['age'])
