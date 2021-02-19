#KMP 알고리즘
def advertise(pattern):
    table=[0]*l
    cnt=0
    for i in range(1, l):
        while cnt>0 and pattern[i]!=pattern[cnt]:
            cnt=table[cnt-1]
        if pattern[i]==pattern[cnt]:
            cnt+=1
            table[i]=cnt

    return l-table[l-1]

if __name__ == "__main__":
    l=int(input())
    s=input()
    print(advertise(s))
