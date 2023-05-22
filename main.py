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
        numbers.remove(m1)
        if numbers == []:
            return None 
        else:
            m2 = max(numbers)
            return m2 , m1

#h = [5]
#if h == []:
   #print("None")
#else:
 #   m1 = max(h)
  #  print(m1)
   # h.remove(m1)
    #vif h == []:
     #   print ("None")
    #else:
     #   m2 = max(h)
      #  print(m2)
       # print(m1,m2)
