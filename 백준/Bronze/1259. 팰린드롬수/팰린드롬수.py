while True:
    num = str(input())
    if num == "0":
        break
    if num == "".join(list(reversed(num))):
        print("yes")
    else:
        print("no")