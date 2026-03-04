student = { "SUSHMA": 85, "GEETHU": 90,"ANSHU": 75}
value_to_find = 85
for key, value in student.items():
    if value == value_to_find:
        print("Key for value", value_to_find, "is:", key)
        break
else:
    print("Value not found")