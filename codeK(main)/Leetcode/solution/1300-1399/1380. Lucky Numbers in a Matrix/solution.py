class Solution(object):
  def luckyNumbers(self, matrix):
      """
      :type matrix: List[List[int]]
      :rtype: List[int]
      """
      lucky_nums = []
      
      for i in range(len(matrix)):
          row_min = min(matrix[i])
          col_index = matrix[i].index(row_min)
          
          # Check if this minimum is the maximum in its column
          is_lucky = True
          for row in matrix:
              if row[col_index] > row_min:
                  is_lucky = False
                  break
          
          if is_lucky:
              lucky_nums.append(row_min)
              
      return lucky_nums