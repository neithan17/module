# A program to ouput student name, exam score and course work mark of an individual.
student_name =input("Name: ")
exam_score =int(input("Exam score = "))
course_work_mark =int(input("course work mark = "))

final_score=int((exam_score/100)*70)+(course_work_mark)
print (f"Final Score= {final_score}")


