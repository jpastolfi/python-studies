# 1
guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  n = None
  while True:
    if n is None:
      line_data = text_file.readline().strip().split(",")
    else:
      line_data = n.strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = line_data[1]
    guests[name] = age
    n = yield line_data

guests_generator = read_guestlist('guest_list.txt')

# 2 & 3
for i in range(14):
  if i == 10:
    guests_generator.send('Jane, 35')
  next(guests_generator)
  
# 4
alcoholic_guests = (name for name, age in guests.items() if int(age) >= 21)

# 5
def table1():
  for i in range(1, 6):
    yield "Chicken", "Table 1", "Seat {}".format(i)
def table2():
  for i in range(6, 11):
    yield "Beef", "Table 2", "Seat {}".format(i)
def table3():
  for i in range(11, 16):
    yield "Fish", "Table 3", "Seat {}".format(i)
def all_tables():
  yield from table1()
  yield from table2()
  yield from table3()

# 6
all = all_tables()

def assign_tables(guests, generator):
  for guest in guests:  
    yield guest, next(all)

print(list(assign_tables(guests, all)))