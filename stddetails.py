import sys
if len(sys.argv) !=3:
  print("Uage: python student.py <name> <rollno>")
  sys.exit(1)
script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]
print("Script Name:", script_name)
print("Student name:", name)
print("Roll Number:", rollno)
