while True:
    try:
        a = int(input("1st number: "))
        exp = int(input("2nd number: "))
        if a <= 0 or exp < 0 :
            raise ValueError
        break
    except ValueError:
        print("This was not an integer! Try again...")

result = a
helper = a
if exp == 0 :
    result = 1
else :
    for i in range(1,exp) :
        for m in range(1,a) :
            helper += result
        result = helper

print(f"{a} to the power of {exp} equals {result} ")
