s = input("Input: ")

splt = (s.split())
size = len(splt) - 1

for x in splt:
  if (x == splt[size]):
    print("Last word: {} \nIt has {} letters" .format(x, len(x)))
