# total_comprehension.py

def mult_function(num):
    return num * 100

def filter_cap(num):
    if num > 3:
        return num

print("")
print("")

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

list2 = list(map(mult_function, my_numbers))
print("--------------")
print(list2)
print("--------------")
print("")
print("--------------")
list3 = list(filter(filter_cap, my_numbers))
print(list3)
print("--------------")
print("")
print("--------------")
list4 = list(map(mult_function,(list(filter(filter_cap, my_numbers)))))
print(list4)
print("--------------")
