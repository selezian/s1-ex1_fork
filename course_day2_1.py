for a in range(1,11):
    for b in range (1,11):
        if b < a :
            continue
        c = a * b
        print(f"{a} X {b} = {c}")
    print("--------------")