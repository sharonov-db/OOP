from classes_objects.Praktika_3.Sortirovka import Sortirovka
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(sum(3, 5))  # Press Ctrl+F8 to toggle the breakpoint.
    s = Sortirovka()
    n = [1, 0, 2]
    print(f"n = {n}")
    print(f"sorted n = {s.sortirovka(n)}")
    print()
    n = (1, 0, 2)
    print(f"n = {n}")
    print(f"sorted n = {s.sortirovka(n)}")
    print()
    n = (1, "test", 2)
    print(f"n = {n}")
    print(f"sorted n = {s.sortirovka(n)}")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
