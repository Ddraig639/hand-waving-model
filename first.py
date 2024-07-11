def cal():
    print("hello! Please choose the opertion u would like to carry out:")
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 modulus")
    print("6 exponential")
    inp = input("")
    result = 0
    print(inp.isdigit())
    if inp.isdigit():
        if int(inp) != 0 and int(inp) <= 6:
            numa = int(input("input the first value: "))
            numb = int(input("input the second value: "))
            rr
        else:
            print("Invalid input")
    else:
        print("Invalid input")


cal()
