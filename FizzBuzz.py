def FizzBuzz(num):
  maxval = num
  num = []
  for i in range(1, maxval+1):
    if i % 3 == 0 and i % 5 == 0 :
      num.append("FizzBuzz")
      # print("FizzBuzz")
    elif (i % 3 == 0) :
      num.append("Fizz")
      # print("Fizz")
    elif (i % 5 == 0) :
      num.append("Buzz")
      # print("Buzz")
    else :
      num.append(str(i))
      # print(i)
  num =" ".join(num)
  return num

# keep this function call here 
print(FizzBuzz(input()))