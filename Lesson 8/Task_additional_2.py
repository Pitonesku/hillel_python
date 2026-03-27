# import math

# def find_gcd(a, b):
#     if a == b:
#         return a
#     if max(a,b)%min(a,b) == 0:
#        return min(a,b)
#     else: 
#         return find_gcd(min(a,b),max(a,b)%(min(a,b)))


 

    
# def find_gcd(a, b):
#     if b == 0:
#         return a
#     return find_gcd(b, a % b)

# print(find_gcd(7,11))   

# sentence = "    Hello my friend"
# def reverse_words(sentence):
#     index =  (sentence.strip().index(" "))
    
     
#     return ("".join((sentence[:sentence.find(" ")])[::-1]),sentence.find)

# print(reverse_words(sentence))


#Additional 3



number = "123"


def sum_of_digits(number):
       result = 0
       number = str(number)
       for digit  in number: 
              result = result + int(digit)   
       return result
print(sum_of_digits(number)) 



