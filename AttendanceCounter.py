total_students=0

def mark_present():
    global total_students
    total_students+=1

mark_present()
mark_present()
mark_present()

print(total_students)