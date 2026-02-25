from sys import stdin 


def main():
    n = int(input())
    pote = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
    if n in pote:
        print(0)
    else:
        for i in range (len(pote)-1, -1, -1):
            if n > pote[i]:
                a = pote[i]
                break
        print(2*(n-a))

main()
