# James Ward, Exercise 3, Collatz program

i=int(input("Enter a number: "))

while i > 1:
  if i % 2 == 0:
      i = i/2
      print(i)
  else: i = (i*3)+1
  print(i)
     






