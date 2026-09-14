student_name = input("Enter your name: ")
age = int(input("Enter your age: "))
weekly_study_hours = float(input("What is your goal for weekly study hours? "))
curent_study_hours = float(input("How many hours have you studied this week? "))

study_hours_remaining = curent_study_hours / weekly_study_hours * 100
print(f'\n STUDY TRACKER')
print(f'You have {int(study_hours_remaining)}% of your weekly study goal remaining.')