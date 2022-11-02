import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    list_number = list(map(int, str(i+1)))
    total = list_number.count(3) + list_number.count(6) + list_number.count(9)

    if total == 3:
        print("---", end = ' ')
    elif total == 2:
        print("--", end =' ')
    elif total == 1:
        print("-", end = ' ')
    else:
        print(i+1, end = ' ')
