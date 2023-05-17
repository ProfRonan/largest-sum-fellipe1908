"""Module with functions."""


#def largest_sum(numbers: list[int]) -> tuple[int, int]:
    #"""Encontra e retorna os dois números que somados dão o maior valor."""
    #primeiro = 0  # o primeiro número da soma
    #segundo = 0  # o segundo número da soma
    #return primeiro, segundo
def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if numbers == []:
        return None
    else:
        m1 = max(numbers)
        return m1
        numbers.remove(m1)
        m2 = max(numbers)
        return m2

#h = [10,9,8,5,30,20,5]
#m1 = max(h)
#print(m1)
#h.remove(m1)
#m2 = max(h)
#print(m2)
#print(m1+m2)
