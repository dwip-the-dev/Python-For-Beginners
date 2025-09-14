age = 25
is_student = True
has_coupon = False

if age < 18:
    print("Youth ticket price: $10")
elif age >= 18 and age < 65:
    if is_student:
        print("Student ticket price: $15")
    elif has_coupon:
        print("Discounted adult ticket price: $18")
    else:
        print("Standard adult ticket price: $25")
else:  # age >= 65
    print("Senior ticket price: $12")