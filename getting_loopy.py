primes = [2, 3, 5, 7, 11, 13, 17, 19]

def is_even(num):
  if num % 2 == 0:
    return True
  return False 
  
def all_even(list_of_numbers):
  for num in list_of_numbers:
    if num % 2 != 0:
      return False
  return True 
    
def count_even(list_of_numbers):
  count = 0
  for num in list_of_numbers:
    if is_even(num) == True :
      count = count + 1
      
  return count