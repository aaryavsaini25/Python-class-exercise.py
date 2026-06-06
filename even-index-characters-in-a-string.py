def evenchar(str):
    length=len(str)
    for i in range(0,length):
        if i % 2 == 0:
            print(str[i])
evenchar(input("Enter a word:"))