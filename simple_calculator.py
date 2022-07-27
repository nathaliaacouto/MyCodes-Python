#functions
def sub(number1, number2):
        answer = 0
        answer = number1 - number2
        print("subtração: {}" .format(answer))

def mult(number1, number2):
        answer = 0
        answer = number1 * number2
        print("multiplicação: {}" .format(answer))

def divi(number1, number2):
        answer = 0
        answer = number1 / number2
        print("divisão: {}" .format(answer))

def newNumbers():
        num1 = int(input('primeiro número: '))
        num2 = int(input('segundo número: '))
        return num1, num2

#recieve numbers
exit = 1

while exit != 0:
        new = input('gostaria de adicionar novos números? s / n: ')
        if new == 's':
                num1, num2 = newNumbers()

        choice = input ('\ns - soma / u - subtração / m - multiplicação / d - divisão / e - sair: ')

        if choice == 's':
                answer = 0
                answer = num1 + num2
                print("soma: {}" .format(answer))
        elif choice == 'u':
                sub(num1, num2)
        elif choice == 'm':
                mult(num1, num2)
        elif choice == 'd':
                divi(num1, num2)
        elif choice == 'e':
                exit = 0
        else:
                print("opção inválida");
