def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if '()' in s:
                    s = s.replace('()', '')
            elif '[]' in s:
                    s = s.replace('[]', '')
            elif '{}' in s:
                    s = s.replace('{}', '')

        if (s == ''):
                return True
        elif (s != ''):
                return False

string = input('Input: ')
answer = isValid(0, string)
print(answer)