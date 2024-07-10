
# largest number Finding Between Three number.
# তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা খুঁজে বের করা।

first_number = int(input("Input Your Integer Number: "))
second_number = int(input("Input Your Integer Number: "))
third_number = int(input("Input Your Integer Number: "))

if first_number > second_number and first_number > third_number:
    LargeNumber = first_number
elif second_number > first_number and second_number > third_number:
    LargeNumber = second_number
else:
    LargeNumber = third_number

print("The largest number is:", LargeNumber)