MIN_SCORE = 0.00; MAX_SCORE = 100.00
user_grade = input("Enter a grade: ")
try:
    grade = float(user_grade)
except ValueError:
    print(f"{user_grade} is not a number. Please enter a number")
    raise SystemExit(1)
if grade < MIN_SCORE or grade > MAX_SCORE:
    print(f"{grade} is outside the range.(MIN : {MIN_SCORE}, MAX : {MAX_SCORE})")       
    print("Please enter a valid grade.")
    raise SystemExit(1)
if grade >= 90.00:
    result = "A"
elif 60.00 <= grade < 90.00:
    result = "B"
else:
    result = "C"
print(f"{grade} is {result}")