# James Ward, February 2018
# A program to find the smallest number divisible by integers 1 to 20 
# with no remainder

n = 2530
for j in range(11, 21):
    i = n/j
    if i % 2 == 0:
     print (n) 
else:
     n = n + 1
      