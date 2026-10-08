class student ():
    def __init__(self, name, rollno, listofmarks):
        self.name = name
        self.rollno = rollno
        self.marks = listofmarks

    def calculate_total(self):
        total_marks = sum(self.marks)
        return total_marks

    def calculate_average(self):
        total_marks = self.calculate_total()
        average_marks = total_marks / len(self.marks)
        return average_marks    

    def determine_grade(self):
        average_marks = self.calculate_average()
        if average_marks >= 90:
            return "A"
        elif average_marks >= 80:       
            return "B"
        elif average_marks >= 70:
            return "C"
        elif average_marks >= 60:
            return "D"
        else:
            return "F"
    def complete_details(self):
        total_marks = self.calculate_total()
        average_marks = self.calculate_average()
        grade = self.determine_grade()

        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Total Marks:", total_marks)
        print("Average Marks:", average_marks)
        print("Grade:", grade)
        
student= student("Tarush", 101, [85, 90, 78, 88, 92])
student.complete_details()
