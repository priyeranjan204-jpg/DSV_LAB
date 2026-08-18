def my_abs(val):
    if isinstance(val,(int,float)):
        if val<0:
            return 0-val
        return val
    print("Invalid input")

print(my_abs("Hi"))