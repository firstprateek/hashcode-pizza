import sys

def solve(r, c, l, h, pizza):
  print("Solving for:\nr: {},\tc: {},\tl: {},\th: {}\npizza: {}\n".format(r, c, l, h, pizza))

  # Find limiting ingredient T or M -----
  number_of_T, number_of_M = 0, 0
  for row in pizza:
    number_of_T += row.count('T')
    number_of_M += row.count('M')

  lower_item = 'T'
  lower_item_count = number_of_T
  if number_of_M < number_of_T:
    lower_item, lower_item_count = 'M', number_of_M

  print('lower_item: {},\t lower_item_count: {}\n'.format(lower_item, lower_item_count))
  # ----- ----- ----- ----- ----- ----- -----

  max_slices = lower_item_count // l

  # step 1 find a lower_item
  for row in range(r):
    for col in range(c):
      if pizza[row][col] == 'X':
        continue

      if pizza[row][col] == lower_item:
        #make_slice(row, col, pizza)
        print('found {}:{}'.format(row, col))
  # step 2 exapnd around lower item until you satisfy l
  # mark areas already cut
  # try to maximise and reach h in a slice
  '''
  -----------
 | TM |T| TT |
 | TM |M| MT |
 | TT |T| TT |
  -----------
  '''
if __name__ == "__main__":
  # Parse input and create pizza matrix -----
  try:
    input_file_path = sys.argv[1]
  except IndexError as e:
    print("Provide input file as argument.")
    sys.exit()

  input_data = []
  with open(input_file_path, 'r') as f:
    input_data = f.readlines()

  # ----- ----- ----- ----- ----- ----- -----
  
  solution = solve(*[ int(data.strip()) for data in input_data[0].split(' ')], input_data[1:])