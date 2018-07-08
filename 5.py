lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))
for s in range(lower,upper+1):
  if(s%2 == 0):
    print(s)
