#Return the number of times a character appears in a String

s = input("Text: ")
aux = input("Caracter: ")
str_l = list(s)
count = 0

for j in range(len(str_l)):
  if (aux == str_l[j]):
    count = count + 1

print("The caracter '{}' appers {} times in the text" .format(aux, count))