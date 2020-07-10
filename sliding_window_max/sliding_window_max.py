from collections import deque

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
  maxes = []
  dq = deque()

  for i in range(k):
    while dq and nums[i] >= nums[dq[-1]]:
      dq.pop()
    dq.append(i)

  for i in range(k, len(nums)):
    maxes.append(nums[dq[0]])
    while dq and dq[0] <= i-k:
      dq.popleft()
    while dq and nums[i] >= nums[dq[-1]]:
      dq.pop()
    dq.append(i)
  
  maxes.append(nums[dq[0]])

  return maxes

if __name__ == '__main__':
  # Use the main function here to test out your implementation 
  arr = [1, 3, -1, -3, 5, 3, 6, 7]
  k = 3

  print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
