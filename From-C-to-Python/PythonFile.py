class Student:
    def __init__(self, name, grades, honors="?"):
        self.name = name
        self.grades = grades
        self.honors = honors

    def __str__(self):
        return f"Student name: {self.name}, Honors: {self.honors}, Grades: {self.grades}, Average: {self.calculate_average():.2f}"
    
    def calculate_average(self):
        if self.grades:
            return float(sum(self.grades)/len(self.grades))
        return 0.0
    
    def assign_honors(self):
        average = self.calculate_average()
        if average >=16:
            return "Excellent"
        elif 14 <= average < 16:
            return "Very good"
        elif 12 <= average <14:
            return "Good"
        elif 10 <= average <12:
            return "Pass"
        else:
            return "Fail"
        
def best_student(students_list: list):
    if students_list:
        best=students_list[0]
        for s in students_list:
            if s.calculate_average()>best.calculate_average():
                best=s
        return best
    return None