def multipyoradd(a,b):
    c=a*b
    d=a+b
    if a*b<=1000:
        print(f"{a} x {b} = {c}")
    else:
        print(f"{a} + {b} = {d}")
multipyoradd(int(input("Enter your first number: ")),int(input("Enter your first number: ")))