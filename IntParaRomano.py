class Solution:
    def intToRoman(self, num: int) -> str:
        list_num = [int(digit) for digit in str(num)]
        lenlist = len(list_num)
        for i, nu in enumerate(list_num):
            if i == 0:
                if nu == 1:
                    if lenlist == 1:
                        list_num[i] = 'I' * nu
                    elif lenlist == 2:
                        list_num[i] = 'X' * nu
                    elif lenlist == 3:
                        list_num[i] = 'C' * nu
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 2:
                    if lenlist == 1:
                        list_num[i] = 'I' * nu
                    elif lenlist == 2:
                        list_num[i] = 'X' * nu
                    elif lenlist == 3:
                        list_num[i] = 'C' * nu
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 3:
                    if lenlist == 1:
                        list_num[i] = 'I' * nu
                    elif lenlist == 2:
                        list_num[i] = 'X' * nu
                    elif lenlist == 3:
                        list_num[i] = 'C' * nu
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 4:
                    if lenlist == 1:
                        list_num[i] = 'IV'
                    elif lenlist == 2:
                        list_num[i] = 'X' * nu
                    elif lenlist == 3:
                        list_num[i] = 'C' * nu
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 5:
                    if lenlist == 1:
                        list_num[i] = 'V'
                    elif lenlist == 2:
                        list_num[i] = 'L'
                    elif lenlist == 3:
                        list_num[i] = 'D' 
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 6:
                    if lenlist == 1:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'D' +('C' * nu)
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 7:
                    if lenlist == 1:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'D' +('C' * nu)
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 8:
                    if lenlist == 1:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'D' +('C' * nu)
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 9:
                    if lenlist == 1:
                        list_num[i] = 'IX'
                    elif lenlist == 2:
                        list_num[i] = 'XC'
                    elif lenlist == 3:
                        list_num[i] = 'CM'
                    elif lenlist == 4:
                        list_num[i] = 'M' * nu
                if nu == 0:
                    list_num[i] = ''
            elif i == 1:
                if nu == 1:
                    if lenlist == 2:
                        list_num[i] = 'I' * nu
                    elif lenlist == 3:
                        list_num[i] = 'X' * nu
                    elif lenlist == 4:
                        list_num[i] = 'C' * nu
                if nu == 2:
                    if lenlist == 2:
                        list_num[i] = 'I' * nu
                    elif lenlist == 3:
                        list_num[i] = 'X' * nu
                    elif lenlist == 4:
                        list_num[i] = 'C' * nu
                if nu == 3:
                    if lenlist == 2:
                        list_num[i] = 'I' * nu
                    elif lenlist == 3:
                        list_num[i] = 'X' * nu
                    elif lenlist == 4:
                        list_num[i] = 'C' * nu
                if nu == 4:
                    if lenlist == 2:
                        list_num[i] = 'IV'
                    elif lenlist == 3:
                        list_num[i] = 'X' * nu
                    elif lenlist == 4:
                        list_num[i] = 'C' * nu
                if nu == 5:
                    if lenlist == 2:
                        list_num[i] = 'V'
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 4:
                        list_num[i] = 'C' * nu
                if nu == 6:
                    if lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'D' +('C' * nu)
                if nu == 7:
                    if lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'D' +('C' * nu)
                if nu == 8:
                    if lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'D' +('C' * nu)
                if nu == 9:
                    if lenlist == 2:
                        nu = nu - 5
                        list_num[i] = 'IX'
                    elif lenlist == 3:
                        list_num[i] = 'XC'
                    elif lenlist == 4:
                        list_num[i] = 'CM'
                if nu == 0:
                    list_num[i] = ''
            elif i == 2:
                if nu == 1:
                    if lenlist == 3:
                        list_num[i] = 'I' * nu
                    elif lenlist == 4:
                        list_num[i] = 'X' * nu
                if nu == 2:
                    if lenlist == 3:
                        list_num[i] = 'I' * nu
                    elif lenlist == 4:
                        list_num[i] = 'X' * nu
                if nu == 3:
                    if lenlist == 3:
                        list_num[i] = 'I' * nu
                    elif lenlist == 4:
                        list_num[i] = 'X' * nu
                if nu == 4:
                    if lenlist == 3:
                        list_num[i] = 'IV'
                    elif lenlist == 4:
                        list_num[i] = 'X' * nu
                if nu == 5:
                    if lenlist == 3:
                        list_num[i] = 'V'
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                if nu == 6:
                    if lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                if nu == 7:
                    if lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                if nu == 8:
                    if lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                    elif lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'L' + ('X' * nu)
                if nu == 9:
                    if lenlist == 3:
                        nu = nu - 5
                        list_num[i] = 'IX'
                    elif lenlist == 4:
                        list_num[i] = 'XC'
                if nu == 0:
                    list_num[i] = ''
            elif i == 3:
                if nu == 1:
                    if lenlist == 4:
                        list_num[i] = 'I' * nu
                if nu == 2:
                    if lenlist == 4:
                        list_num[i] = 'I' * nu
                if nu == 3:
                    if lenlist == 4:
                        list_num[i] = 'I' * nu
                if nu == 4:
                    if lenlist == 4:
                        list_num[i] = 'IV'
                if nu == 5:
                    if lenlist == 4:
                        list_num[i] = 'V'
                if nu == 6:
                    if lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                if nu == 7:
                    if lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                if nu == 8:
                    if lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'V' + ('I' * nu)
                if nu == 9:
                    if lenlist == 4:
                        nu = nu - 5
                        list_num[i] = 'IX'
                if nu == 0:
                    list_num[i] = ''
            if i == lenlist - 1:
                string_num = ''.join(list_num)
                return string_num
roman_number = 1023
print(Solution.intToRoman(roman_number, roman_number))
    

