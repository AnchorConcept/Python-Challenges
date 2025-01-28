# challenges.py

# Challenge 1: Name Printer
name = "Olajide Animashaun"
print(name)

# Challenge 2: Number Guessing Game
RightNo = 5
GuessNo = int(input("Enter a number: "))
if GuessNo == RightNo:
    print("Congratulation,", RightNo , "is correct")
else:
    print("try again")

# Challenge 3: Sum of Two Numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second number: "))
result = num1 + num2
print("The Sum of the first and second number is" ,result)

# Challenge 4: Grade Calculator
Total = 100
Score = int(input("Enter your score: "))
if Score >= 90 and Score <= 100:
    print("Grade A")
elif Score >= 80 and Score < 90:
    print("Grade B")
elif Score >= 70 and Score < 80:
    print("Grade C")
elif Score >= 60 and Score < 70:
    print("Grade D")
elif Score < 60:
    print("Grade F")
