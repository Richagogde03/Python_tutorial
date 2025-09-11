score = 95
attendance = 92
projects_completed = 4

if score >= 70:
    print("You passed the exam!")
    if score >= 90:
        print("You passed with distinction!")
        if projects_completed >= 3:
            print("You also completed enough projects for a bonus.")
        else:
            print("You need more projects for a bonus.")
    if attendance >= 80:
        print("You also have good attendance.")
    elif attendance >= 60:
        print("Your attendance is acceptable.")
    else:
        print("Your attendance is poor.")
elif score >= 50:
    print("You can retake the exam.")
else:
    print("You failed the exam.")
