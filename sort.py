# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # # implement your algorithm here
    # # define the sorted and unsorted list-- create a variable to use later
    # indexing_length = range(1, len(li) )
    # # for loop to perform operation on all the values
    # for i in indexing_length:
    #     #sort all values 
    #     to_sort = li[i]
    #     # a while loop to loop w the conditional logic 
        
    #     while li[i - 1] > to_sort and i>0:
    #         li[i], li[i-1] = li[i-1], li[i]
    #         i=i-1
    #     return li
#iterate up through the list dragging down elements untill they are in their oproper place (either at the start of the list or next to a value to the left of it that is smaller)
    for current_index in range(len(li)):
        #for easy computation store number that is being moved
        comparison_number = li[current_index]
        inner_index = current_index -1
        while inner_index >= 0 and  li[inner_index] > li[current_index]:
            li[inner_index], li[inner_index + 1] = li[inner_index + 1], li[inner_index]
            inner_index -= 1
        

       



# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(li)
print(is_sorted(li))
