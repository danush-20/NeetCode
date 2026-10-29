
# Generate a list that can be sorted with custom code
my_list = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 33, 17, 78, 29, 61]

n = len(my_list)

for i in range(n):
    for j in range(n):
        if my_list[j] > my_list[i]:
             my_list[i] , my_list[j] = my_list[j] , my_list[i]
print(my_list)