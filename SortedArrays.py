from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        num_list = nums1 + nums2
        num_list.sort()
        lenlist = len(num_list)
        median = int(lenlist / 2)
        resto = lenlist % 2
        if resto == 1:
            numlist = num_list[median]
            return numlist
        if resto == 0:
            num = num_list[median - 1]
            num2 = num_list[median]
            num = num + num2
            return num / 2

lista1 = input("Digite a sua lista de números de 1 digito")
lista2 = input("Digite a sua lista de números de 1 digito")
lista1 = [digit for digit in (lista1)]
lista2 = [digit for digit in (lista2)]
lista1 = list(map(int,lista1))
lista2 = list(map(int,lista2))

print(Solution.findMedianSortedArrays(lista1, lista1, lista2))

