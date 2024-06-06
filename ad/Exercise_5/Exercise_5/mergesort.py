'''
def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort):#2.its a mergeSort Funktion so dont have to Emphasize again in the variable
    if (
        len(list_to_sort) > 1
    ):#1.These conditions are redundant, this sentence is enough
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
'''
def merge_sort(data):
    #Recursively split and merge a list, sorting it in ascending order
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(data, left_half, right_half)


def merge(data, left, right):
    #"Merge the two halves of a list into a single ordered list
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1


import matplotlib.pyplot as plt

def plot_data(data, title):
    #plot figure
    plt.figure()
    plt.plot(range(len(data)), data)
    plt.title(title)
    plt.xlabel('index')
    plt.ylabel('Value')
    plt.show()

# data test
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_data(data_list, 'Origin')
merge_sort(data_list)
plot_data(data_list, 'Sorted')
