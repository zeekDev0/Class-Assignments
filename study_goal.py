name = str(input("Whats your name? "))
weekly_study_goal = float(input("What is your weekly study goal in hours? "))
hours_studied = float(input("How many hours have you studied this week? "))
remaining_hours = int(weekly_study_goal - hours_studied)
if remaining_hours <= 0:
    if remaining_hours > weekly_study_goal:
        remaining_hours = 0
    print(f"Hello, {name}! You have reached your weekly study goal.")
else:
    print(f"Hello, {name}! You have {remaining_hours} hours left to meet your weekly study goal.")