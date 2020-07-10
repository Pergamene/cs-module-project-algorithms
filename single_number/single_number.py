'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
  # Your code here
  numberMap = {}
  for num in arr:
    count = numberMap.get(num)
    if count is None:
      numberMap.update({num: 1})
    if count == 1:
      numberMap.pop(num)
  return list(numberMap.keys()).pop(0)



if __name__ == '__main__':
  # Use the main function to test your implementation
  arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

  print(f"The odd-number-out is {single_number(arr)}")
