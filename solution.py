import sys

class Solution:
  def __init__(self, r, c, l, h, pizza):
    self.r = r
    self.c = c
    self.l = l
    self.h = h
    self.pizza = pizza
    self.lower_item = 'X'
    self.lower_item_count = 0
    self.max_slices = 0
    self.total_score = 0
    self.slices = []

  def make_slice(self, row, col):
    expansion = [ True, True, True, True] # Top, Right, Bottom, Left
    size = 1
    corners = [ (row, col), (row, col), (row, col), (row, col) ] # top - left, top - right, bottom - right, bottom - left
    cur_row, cur_col = row, col

    while any(expansion) and size < h:
      for direction in expansion:
        if not direction:
          continue

        border_check = { 0: cur_row == 0, 1: cur_col == c - 1, 2: cur_row == r - 1, 3: cur_col == 0 }
        if border_check[direction]:
          expansion[direction] = False
          continue

        if direction == 0:

          corners[0] = (corners[0][0], corners[0][1] - 1)
        elif direction == 1:

        elif direction == 2:

        elif direction == 3:



  def solve(self):
    print("Solving for:\nr: {},\tc: {},\tl: {},\th: {}\npizza: {}\n".format(r, c, l, h, pizza))

    # Find limiting ingredient T or M -----
    number_of_T, number_of_M = 0, 0
    for row in pizza:
      number_of_T += row.count('T')
      number_of_M += row.count('M')

    self.lower_item = 'T'
    self.lower_item_count = number_of_T
    if number_of_M < number_of_T:
      self.lower_item, self.lower_item_count = 'M', number_of_M

    print('lower_item: {},\t lower_item_count: {}\n'.format(self.lower_item, self.lower_item_count))
    # ----- ----- ----- ----- ----- ----- -----

    self.max_slices = lower_item_count // l

    # step 1 find a lower_item
    for row in range(r):
      for col in range(c):
        if pizza[row][col] == 'X':
          continue

        if pizza[row][col] == lower_item:
          print('found {} at {}:{}'.format(lower_item, row, col))
          self.slices.append(self.make_slice(row, col))

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

  solution = Solution(*[ int(data.strip()) for data in input_data[0].split(' ')], input_data[1:])
  result = solution.solve()

  # Write result to output file -----

  # ----- ----- ----- ----- ----- ----- -----