class Solution:
    def romanToInt(self, s: str) -> int:
        list_num = [digit for digit in (s)]
        lenlist = len(list_num)
        list_num2 = []
        skip = False
        for i, nu in enumerate(list_num):
            if skip:
                skip = False
            elif nu == 'I':
                if i + 1 == lenlist:
                    list_num2.append(1)
                elif list_num[i + 1] == 'X':
                    list_num2.append(9)
                    skip = True
                elif list_num[i + 1] == 'V':
                    list_num2.append(4)
                    skip = True
                else:
                    list_num2.append(1)
            elif nu == 'V':
                list_num2.append(5)
            elif nu == 'X':
                if i + 1 == lenlist:
                    list_num2.append(10)
                elif list_num[i + 1] == 'L':
                    list_num2.append(40)
                    skip = True
                elif list_num[i + 1] == 'C':
                    list_num2.append(90)
                    skip = True
                else:
                    list_num2.append(10)
            elif nu == 'L':
                list_num2.append(50)
            elif nu == 'C':
                if i + 1 == lenlist:
                    list_num2.append(100)
                elif list_num[i + 1] == 'D':
                    list_num2.append(400)
                    skip = True
                elif list_num[i + 1] == 'M':
                    list_num2.append(900)
                    skip = True
                else:
                    list_num2.append(100)
            elif nu == 'D':
                list_num2.append(500)
            elif nu == 'M':
                list_num2.append(1000)
        return sum(list_num2)
pergunta = input('Digite o número em Romano:')            
ba = Solution.romanToInt(pergunta,pergunta)
print(ba)
