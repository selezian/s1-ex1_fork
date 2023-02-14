while True:
    try:
        a = input("Please enter a number: ")
        if a[0] == "0":
            raise Exception
        if int(a) <= 0:
            raise ValueError
        break
    except ValueError:
        print("This was not an integer! Try again...")
    except Exception:
        print("Please don't use a leading zero!  Try again...")

l = len(a)
i = l-1

while i >= 0 :
    if a[l-i-1] != a[i]:
        print(f"The number {a} is not a palindrome !")
        break
    i -= 1
else:
    print(f"The number {a} is really a palindrome!")


