# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test1() -> object:
    print('This is my first pycharm code.')


def fib_gen(n):
    a = 0
    b = 1
    l = []
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test1()
    l = fib_gen(500)
    print(l)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/ 
