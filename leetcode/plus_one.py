def plusOne(digits):
  list_string = [str(integer) for integer in digits]
  string = "".join(list_string)
          
  digits_int = int(string)

  digits_int = digits_int + 1

  answer = [int(x) for x in str(digits_int)]
  print(answer)

dgts = input('Digits: ')
plusOne(dgts)