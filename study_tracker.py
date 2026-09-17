student_name = input("Enter your name: ")
age = int(input("Enter your age: "))
weekly_study_hours = float(input("What is your goal for weekly study hours? "))
current_study_hours = float(input("How many hours have you studied this week? "))
remaining_study_hours = (weekly_study_hours - current_study_hours)
remaining_study_percentage = (remaining_study_hours / weekly_study_hours) * 100
if remaining_study_hours < 0:
    print(f"You have exceeded your weekly study goal by {-remaining_study_hours} hours.")
    remaining_study_hours = 0
    remaining_study_percentage = 0
print(f'\n STUDY TRACKER')
print(f'Name: {student_name}')
print(f'Age: {age}')
print(f'You have {int(remaining_study_hours)} hours of your weekly study goal remaining.')
print(f'You have completed {int(current_study_hours)} hours of your weekly study goal.')
print(f'You have {int(remaining_study_percentage)}% of your weekly study goal remaining.')
