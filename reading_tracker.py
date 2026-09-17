name = str(input("Whats your name? "))
book_title = str(input("What book are you currently reading? "))
reading_goal = float(input("What is your reading goal in hours? "))
reading_hours = float(input("How many hours have you read this week? "))
page_reading_goal = float(input("How many pages do you want to read this week? "))
pages_read = int(input("How many pages have you read this week? "))
remaining_pages = int(page_reading_goal - pages_read)
if remaining_pages <= 0:
    remaining_pages = 0
else:
    remaining_pages = int(page_reading_goal - pages_read)

if reading_hours >= int(reading_goal) and pages_read >= int(page_reading_goal):
    reading_status = "on track to complete your goal."
elif reading_hours < int(reading_goal) and pages_read <= int(page_reading_goal):
    reading_status = "on track on page goal but behind on reading hours. \n You need to increase your reading hours." 
elif reading_hours >= int(reading_goal) and pages_read > int(page_reading_goal):
    reading_status = "behind on page goal but on track on reading hours. \n You need to increase your page goal."
else:
    reading_status = "not on track."
print(f"Hello, {name}! You are currently reading '{book_title}'. You have {remaining_pages} pages left to read this week. You are {reading_status}")