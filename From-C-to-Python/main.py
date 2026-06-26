import PythonFile as pf

student_list=[]
student_list.append(pf.Student("Alice", grades=[17.5, 15.0, 18.0]))
student_list.append(pf.Student("Bob", grades=[9.0, 11.5, 8.0]))
student_list.append(pf.Student("Charlie", grades=[13.0, 12.5, 14]))

for s in student_list:
    s.honors = s.assign_honors()
    print(s)

print(f"The best is :\n{pf.best_student(student_list)}")