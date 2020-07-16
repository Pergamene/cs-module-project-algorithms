from math import factorial, floor

'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
  if n == 0:
    return 1
  counts = _generate_counts(n)
  return _find_permunations(counts)

def _generate_counts(n):
  all_counts = set()
  max_threes = floor(n / 3)
  max_twos = floor(n / 2)
  for threes in range(max_threes+1):
    for twos_max in range(max_twos+1):
      twos = twos_max
      while (3 * threes + 2 * twos) > n:
        twos -= 1
      ones = n - 3 * threes - 2 * twos
      total = threes + twos + ones
      all_counts.add((total, threes, twos, ones))
  return all_counts

def _find_permunations(counts):
  count_total = 0
  for count in counts:
    total, threes, twos, ones = count
    permutations = factorial(total) / (factorial(threes) * factorial(twos) * factorial(ones))
    count_total += int(permutations)
  return count_total 

if __name__ == "__main__":
  # Use the main function here to test out your implementation
  num_cookies = 5

  print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
