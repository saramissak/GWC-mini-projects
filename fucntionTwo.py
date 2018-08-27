def main():
    list2 = [1, 2, 3]
    num(list2)
    print(num(list2))

def num(list):
  total = 0
  for i in list:
    total += i
  return total
  #print(total)

if __name__ == "__main__":
    main()
