# For a given number, find all numbers less than the number. The number should be divisible by 3 and 5.
# একটি প্রদত্ত সংখ্যার জন্য, সংখ্যার চেয়ে ছোট সমস্ত সংখ্যা খুঁজুন। সংখ্যা 3 এবং 5 দ্বারা বিভাজ্য হওয়া উচিত।


InputValue = int(input("input your Number : "))

cal = []
for i in range(1, InputValue):
    if i % 5 & i % 3 == 0:
        cal.append(i)
print(cal)