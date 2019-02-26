'''
Author: Prateek
To be implemented:
- if there is a l violation on all 4 sides then what ?
- Consider l values for higher item also
- change input pizza to list of lists instead of list of strings
- MODIFY HOW THE TOTAL SCORE IS CALCULATED X
'''

import code
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
    corners = [ [row, col], [row, col], [row, col], [row, col] ] # top - left, top - right, bottom - right, bottom - left
    cur_row, cur_col = row, col
    
    count = { 'T': 0, 'M': 0 }
    count[self.lower_item] += 1
    self.pizza[row] = self.pizza[row][:col] + 'X' + self.pizza[row][col + 1:]

    # step 2 exapnd around lower item until you satisfy l
    # mark areas already cut
    # try to maximise and reach h in a slice
    '''
    eg:
    -----------
   | TM |T| TT |
   | TM |M| MT |
   | TT |T| TT |
    -----------
    '''
    while any(expansion) and sum(count.values()) < self.h:
      for direction in range(4):
        if not expansion[direction]:
          continue

        cur_boundry = { 
          0: corners[0][0], 1: corners[1][1], 2: corners[2][0], 3: corners[3][1] 
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
          new_row = self.pizza[corners[0][0] - 1][corners[0][1]:corners[1][1] + 1]
          new_row_lower_items, new_row_higher_items = new_row.count(self.lower_item), new_row.count(self.higher_item)
          visited = True if new_row.count('X') > 0 else False
          if visited or count[self.lower_item] + new_row_lower_items > self.l or sum(count.values()) + len(new_row) > self.h:
            expansion[0] = False
            continue

          count[self.lower_item] += new_row_lower_items
          count[self.higher_item] += new_row_higher_items

          # update corners
          corners[0] = [corners[0][0] - 1, corners[0][1]]
          corners[1] = [corners[1][0] - 1, corners[1][1]]

          # set to X everyone in the new_row
          # code.interact(local=dict(globals(), **locals()))
          self.pizza[corners[0][0]] = self.pizza[corners[0][0]][:corners[0][1]] + 'X' * len(new_row) + self.pizza[corners[0][0]][corners[1][1] + 1:]
        elif direction == 1:
          #code.interact(local=dict(globals(), **locals()))
          new_col = [self.pizza[row][corners[1][1] + 1] for row in range(corners[1][0], corners[2][0] + 1)]
          new_col_lower_items, new_col_higher_items = new_col.count(self.lower_item), new_col.count(self.higher_item)
          visited = True if new_col.count('X') > 0 else False
          if visited or count[self.lower_item] + new_col_lower_items > self.l or sum(count.values()) + len(new_col) > self.h:
            expansion[1] = False
            continue

          count[self.lower_item] += new_col_lower_items
          count[self.higher_item] += new_col_higher_items

          # update corners
          corners[1] = [corners[1][0], corners[1][1] + 1]
          corners[2] = [corners[2][0], corners[2][1] + 1]

          # set to X everyone in the new_col
          for row in range(corners[1][0], corners[2][0] + 1):
            self.pizza[row] = self.pizza[row][:-1] + 'X'
        elif direction == 2:
          # increase the row and then check if lower_item count satisfies
          new_row = self.pizza[corners[2][0] + 1][corners[0][1]:corners[1][1] + 1]
          new_row_lower_items, new_row_higher_items = new_row.count(self.lower_item), new_row.count(self.higher_item)
          visited = True if new_row.count('X') > 0 else False
          if visited or count[self.lower_item] + new_row_lower_items > self.l or sum(count.values()) + len(new_row) > self.h:
            expansion[2] = False
            continue

          count[self.lower_item] += new_row_lower_items
          count[self.higher_item] += new_row_higher_items

          # update corners
          corners[3] = [corners[3][0] + 1, corners[3][1]]
          corners[2] = [corners[2][0] + 1, corners[2][1]]

          # set to X everyone in the new_row
          self.pizza[corners[3][0]] = self.pizza[corners[3][0]][:corners[3][1]] + 'X' * len(new_row) + self.pizza[corners[3][0]][corners[2][1] + 1:]
        elif direction == 3:
          # check if lower item counts satisfy -- implement later
          # if less than l then take it -- implement later
          new_col = [self.pizza[row][corners[0][1] - 1] for row in range(corners[0][0], corners[3][0] + 1)]
          new_col_lower_items, new_col_higher_items = new_col.count(self.lower_item), new_col.count(self.higher_item)
          visited = True if new_col.count('X') > 0 else False
          if visited or count[self.lower_item] + new_col_lower_items > self.l or sum(count.values()) + len(new_col) > self.h:
            expansion[3] = False
            continue

          count[self.lower_item] += new_col_lower_items
          count[self.higher_item] += new_col_higher_items

          # update corners
          corners[0] = [corners[0][0], corners[0][1] - 1]
          corners[3] = [corners[3][0], corners[3][1] - 1]

          # set to X everyone in the new_col
          for row in range(corners[0][0], corners[3][0] + 1):
            self.pizza[row] = 'X' + self.pizza[row][1:]
        
    # check if lower item counts satisfy -- implemented later
    return [corners[0], corners[2]]


  def solve(self):
    # Find limiting ingredient T or M -----
    number_of_T, number_of_M = 0, 0
    for row in self.pizza:
      number_of_T += row.count('T')
      number_of_M += row.count('M')

    # step 1 find a lower_item
    self.lower_item, self.higher_item = 'T', 'M'
    self.lower_item_count = number_of_T
    if number_of_M < number_of_T:
      self.lower_item, self.lower_item_count = 'M', number_of_M
      self.higher_item = 'T'

    print('lower_item: {},\t lower_item_count: {}\n'.format(self.lower_item, self.lower_item_count))
    # ----- ----- ----- ----- ----- ----- -----

    self.max_slices = self.lower_item_count // self.l

    for row in range(self.r):
      for col in range(self.c):
        if self.pizza[row][col] == self.lower_item:
          self.slices.append(self.make_slice(row, col))

    ts = 0
    for x in range(self.r):
      ts += self.pizza[x].count('X')

    print("\n\n-------------FINAL----------------")
    print("Final Score: {}".format(ts))
    print("Max Possible Score: {}".format(self.r * self.c))
    print("------------------------------------\n\n")
    return self.slices
    
if __name__ == "__main__":
  # Parse input and create pizza matrix -----
  try:
    input_file_path = sys.argv[1]
  except IndexError as e:
    print("Provide input file as argument.")
    sys.exit()

  output_file_path = "output.txt" if not sys.argv[2] else sys.argv[2]

  input_data = []
  with open(input_file_path, 'r') as f:
    input_data = f.readlines()

  # ----- ----- ----- ----- ----- ----- -----

  solution = Solution(*[ int(data.strip()) for data in input_data[0].split(' ')], [row.strip() for row in input_data[1:]])
  result = solution.solve()

  # Write result to output file -----

  with open(output_file_path, 'w') as f:
    f.write("{}\n".format(len(result)))
    for coord in result:
      f.write("{} {} {} {}\n".format(coord[0][0], coord[0][1], coord[1][0], coord[1][1]))
  
  # ----- ----- ----- ----- ----- ----- -----