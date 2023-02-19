while True:
    try:
        a = int(input("1st number: "))
        exp = int(input("2nd number: "))
        if a <= 0 or exp < 0 :
            raise ValueError
        break
    except ValueError:
        print("This was not an integer! Try again...")

helper = 0
result = 1

for i in range(exp) :
        helper = 0
        for m in range(a) :
            helper += result
        result = helper


print(f"{a} to the power of {exp} equals {result} ")
