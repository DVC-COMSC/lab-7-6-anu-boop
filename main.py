
def getInput():
   userInput = input("Enter values: ")
   return [int(value) for value in userInput.split()]


def makeReverse(numbers):
    reversed = []
    while numbers:
        reversed.append(numbers.pop())
    return reversed


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
