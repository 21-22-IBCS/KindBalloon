def N(Num):
    a = 0
    c = 1000
    for i in range (len(Num)):
        a = i
        c = Num[i]
        for b in range (len(Num) - i):
            if (Num[i] > Num[i+b]):
                if (Num [i+b] < c):
                    c = Num[i+b]
                    a = i + b
        Num[a] = Num[i]
        Num[i] = c
    return Num

def main():
    print(N([100,10,35,48,1,5,3,2,1,9,5]))

if __name__ == "__main__":
    main()
