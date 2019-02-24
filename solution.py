import sys

class Solution:
  def __init__(self, r, c, l, h, pizza):
    self.r = r
    self.c = c
    self.l = l
    self.h = h
    self.pizza = pizza
    self.lower_item = 'X'
    self.higher_item = 'X'
    self.lower_item_count = 0
    self.max_slices = 0
    self.total_score = 0
    self.slices = []

  def make_slice(self, row, col):
    expansion = [ True, True, True, True] # Top, Right, Bottom, Left
    size = 1
    corners = [ (row, col), (row, col), (row, col), (row, col) ] # top - left, top - right, bottom - right, bottom - left
    cur_row, cur_col = row, col
    
    count = { 'T': 0, 'M': 0 }
    count[self.lower_item] += 1
    self.pizza[row] = self.pizza[row][:col] + 'X' + self.pizza[row][col + 1:]

    while any(expansion) and size < self.h:
      for direction in expansion:
        if not direction:
          continue

        cur_boundry = { 
          0: corners[0][0], 1: corners[1][1], 2: corners[2][1], 3: corners[3][1] 
        }
        border_check = { 
          0: cur_boundry[0] == 0, 
          1: cur_boundry[1] == self.c - 1, 
          2: cur_boundry[2] == self.r - 1, 
          3: cur_boundry[3] == 0 
        }

        if border_check[direction]:
          expansion[direction] = False
          continue

        if direction == 0:
          # increase the row and then check if lower_item count satisfies
          new_row = pizza[corners[0][0] - 1][corners[0][1]:corners[1][1]]
          new_row_lower_items, new_row_higher_items = new_row.count(self.lower_item), new_row.count(self.higher_item)
          if count[self.lower_item] + new_row_lower_items > self.l or sum(count.values()) + len(new_row) > h:
            expansion[0] = False
            continue

          count[self.lower_item] += new_row_lower_items
          count[self.higher_item] += new_row_higher_items

          # update corners
          corners[0] = (corners[0][0] - 1, corners[0][1])
          corners[1] = (corners[1][0] - 1, corners[1][1])
        elif direction == 1:

        elif direction == 2:

        elif direction == 3:
          # if less than l then take it

    # check if lower item counts satisfy
    # return slice coordinates


  def solve(self):
    print("Solving for:\nr: {},\tc: {},\tl: {},\th: {}\npizza: {}\n".format(r, c, l, h, pizza))

    # Find limiting ingredient T or M -----
    number_of_T, number_of_M = 0, 0
    for row in pizza:
      number_of_T += row.count('T')
      number_of_M += row.count('M')

    self.lower_item, self.higher_item = 'T', 'M'
    self.lower_item_count = number_of_T
    if number_of_M < number_of_T:
      self.lower_item, self.lower_item_count = 'M', number_of_M
      self.higher_item = 'T'

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