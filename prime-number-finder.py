def prime_finder(n):
  prime_nums = []
  
  prime = 1

  for i in range(2, n + 1):  
    
    #the max a number can be divided by is by itself / 2, which explains int(i//2)+1
    #loops through 2 and max divisable number possible and tests whether it leaves a remainder
    #remainder = not a prime
    for j in range(2, int(i//2)+1): 
      if (i % j == 0):   
        prime = 0
        break

    if (prime == 1):   
      prime_nums.append(i)

    prime = 1
    
  return prime_nums

print(prime_finder(11))