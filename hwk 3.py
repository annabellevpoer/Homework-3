#  Annabelle Poer

my_list = []
n = int(input())
for i in range(0, n):
    elements = map(int, input().split())
    my_list = [e for e in elements if e >= 0]
    my_list.sort()


print(my_list)