def remove_char(values):
    ans=""
    for i in values:
        if(i>="0" and i<="9"):
            ans+=i
    return int(ans)


def main():
    list1=["HEM-234","HML-123","hello-99"]
    intanswer=list(map(remove_char,list1))
    print(intanswer)


if __name__=="__main__":
    main()