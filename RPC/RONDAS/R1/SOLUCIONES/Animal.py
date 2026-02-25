from sys import stdin 


def main(): 

    input_data = stdin.read().split() 

    for i in range(0, len(input_data), 10):

        ans = 1  

        for j in range(i, i + 10):
            ans = ans * (int(input_data[j])+1)
    print(ans - 1)
    
main()
