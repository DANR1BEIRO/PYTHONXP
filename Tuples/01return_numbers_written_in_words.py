"""
Create a program that has a tuple with numbers written in words,
counting from zero to ten. The program must ask for a integer
as input and return it as a number in words
"""

def numberWords2(number=int):
    number_in_words = ("zero", "one", "two", "three", 
                       "four", "five", "six", "seven",
                       "eight", "nine", "ten")

    while True:
        try:
            number = int(input("Enter a number between 1 to 10: "))
            if 0 <= number <= 10:
                return number_in_words[number]
            else:
                print("Must be a number between 0 to 10")
                
        except ValueError:
            print("Must be an integer number")
            
print(f"You've enter the number {numberWords2()}")


# def numberWords2(number=int):
#     number_in_words = ("zero", "one", "two", "three", 
#                        "four", "five", "six", "seven",
#                        "eight", "nine", "ten")

#     while True:
#         try:
#             number = int(input("Enter a number between 1 to 10: "))
#             if 0 <= number <= 10:
#                 for index, i in enumerate(number_in_words):
#                     if number == index:
#                         return i
#             else:
#                 print("Must be a number between 0 to 10")
                
#         except ValueError:
#             print("Must be an integer number")
            
# print(f"You've enter the number {numberWords2()}")

# def numberWords(number=int):
#     number_in_words = ("zero", "one", "two", "three", 
#     "four", "five", "six", "seven", "eight", "nine", "ten")
    
#     while True:
#         try:
#             number = int(input("Enter an integer number between 0 to 10: "))
#             if 0 <= number <= 10: 
#                 if number == 0:
#                     return number_in_words[0]
#                 elif number == 1:
#                     return number_in_words[1]
#                 elif number == 2:
#                     return number_in_words[2]
#                 elif number == 3:
#                     return number_in_words[3]
#                 elif number == 4:
#                     return number_in_words[4]
#                 elif number == 5:
#                     return number_in_words[5]
#                 elif number == 6:
#                     return number_in_words[6]
#                 elif number == 7:
#                     return number_in_words[7]
#                 elif number == 8:
#                     return number_in_words[8]
#                 elif number == 9:
#                     return number_in_words[9]
#                 elif number == 10:
#                     return number_in_words[10]
#             else:
#                 print("Must be between 0 to 10")
                
#         except ValueError:
#             print("Must be an integer number")

# print(f"You've entered {numberWords(0)}")
    




   
        
    


    

    