def printMultiplicationTable(number: int) -> None:
    for index in range(1, 11):
        print(f"{number} x {index} = {number*index}")


printMultiplicationTable(int(input("enter a number:")))
