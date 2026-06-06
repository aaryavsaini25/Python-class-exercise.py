def add_number_and_previous(num):
    curr=0
    prev=0
    sum=0
    print(sum)
    while curr<num:
        curr=curr+1
        prev=curr-1
        sum=curr+prev
        print(sum)
add_number_and_previous(int(input("Enter a number:")))