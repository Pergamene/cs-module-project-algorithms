'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
  index = 0
  length = len(arr)
  while index < length:
    if arr[index] == 0:
      arr.pop(index)
      arr.append(0)
      length -= 1
    else:
      index += 1
  return arr

if __name__ == '__main__':
  arr = [0, 3, 1, 0, -2]

  print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
