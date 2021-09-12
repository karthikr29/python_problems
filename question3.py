# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print
# the dictionary.Suppose the following input is supplied to the program: 8
# Output should be : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input("Enter an number : "))
my_dict = { 1 : 1}

for i in range(1, number + 1):
    my_dict[i] = i*i

print(my_dict)
