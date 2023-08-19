import itertools
from roster import student_roster
from classroom_organizer import ClassroomOrganizer

student_roster_iterator = iter(student_roster)

for i in range(1, 11):
  print(next(student_roster_iterator))

my_rooster = ClassroomOrganizer(student_roster)
print('---')
print(my_rooster.get_seats_options(my_rooster.sorted_names, 2))
print('---')
def get_student(tuple):
  return tuple[0]
math_as_favorite = my_rooster.get_students_with_subject('Math')
science_as_favorte = my_rooster.get_students_with_subject('Science')
science_and_math_students = list(itertools.chain(math_as_favorite, science_as_favorte))
result = list(map(get_student, science_and_math_students))
print(my_rooster.get_seats_options(result, 4))