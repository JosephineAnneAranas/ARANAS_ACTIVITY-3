# Obtain input from user
Digit = int(input("Enter an Integer (Seconds): "))

# Calculate minutes and remaining seconds
Minutes = Digit // 60
Seconds = Digit % 60

# Display the minutes and remaining seconds calculated
print(Digit, "seconds is", Minutes, "minute/s and", Seconds, "second/s")