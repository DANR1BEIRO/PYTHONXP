"""
Create a program that has a tuple with numbers written in words,
counting from zero to twenty. The program must ask for a integer
as input and return it as a number in words
"""

def number_in_words(number=int):
    written_in_words = ("zero", "one", "two", "three", 
                       "four", "five", "six", "seven",
                       "eight", "nine", "ten", "eleven",
                       "twelve", "thirteen", "fourteen",
                       "fifteen", "sixteen", "seventeen",
                       "eighteen", "nineteen", "twenty")

    while True:
        try:
            number = int(input("Enter a number between 1 to 20: "))
            if 0 <= number <= 20:
                return written_in_words[number]
            else:
                print("Must be a number between 0 to 20")
                
        except ValueError:
            print("Must be an integer number")
            
print(f"You've enter the number {number_in_words()}")


# def number_in_words2(number=int):
#     written_in_words = ("zero", "one", "two", "three", 
#                        "four", "five", "six", "seven",
#                        "eight", "nine", "ten", "eleven",
#                        "twelve", "thirteen", "fourteen",
#                        "fifteen", "sixteen", "seventeen",
#                        "eighteen", "nineteen", "twenty")

#     while True:
#         try:
#             number = int(input("Enter a number between 1 to 20: "))
#             if 0 <= number <= 20:
#                 for index, i in enumerate(written_in_words):
#                     if number == index:
#                         return i
#             else:
#                 print("Must be a number between 0 to 20")
                
#         except ValueError:
#             print("Must be an integer number")
            
# print(f"You've enter the number {number_in_words2()}")


   
        
    


    

    