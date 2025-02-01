# Grading System
# Create a program that:
# Takes a numerical score (0–100) as input from the user.
# Determines the corresponding letter grade based on the following scale:
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: Below 60
# Outputs the letter grade.

class Student:
    
    GRADE_RANGE = {
        "F": (0, 59),
        "D": (60, 69),
        "C": (70, 79),
        "B": (80, 89),
        "A": (90, 100)
        }
    
    def __init__(self, score=None):
        self.score = score if score is not None else self.get_input("Your score: ", "score")
        self.grade = self.get_grade()
        pass
    
    def get_input(self, prompt, type_input):
        while True:
            try:
                score = float(input(prompt))
                if score < 0 or score > 100:
                    print(f"{type_input.capitalize()} must be between 0 and 100")
                else:
                    return score
            except ValueError:
                print("Must be an integer positive number")
                
    def get_grade(self):
        for grade, (low, high) in self.GRADE_RANGE.items():
            if low <= self.score <= high:
                return grade
            
    def display_results(self):
        print(f"Based on your score {self.score}\nYou're classified as grade {self.grade}")
    
    def __str__(self):
        return f"\nScore: {self.score}\nGrade: {self.grade}"
    

student = Student(90)
student.display_results()
print(student)
