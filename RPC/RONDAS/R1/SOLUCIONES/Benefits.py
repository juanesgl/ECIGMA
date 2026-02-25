from sys import stdin 


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = int(input())
    mul1 = (c - a[0])*a[1]
    mul2 =(c - b[0])*b[1] 
    if (mul1 >= mul2):
        print(1) 
    else:
        print(2)

main()


