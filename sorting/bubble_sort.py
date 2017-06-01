import sys
import json


"""
Sorting from right to left
"""

def bubble_sort(*args):
    unsorted_list = args[0]
    #print(unsorted_list)
    count = 0
    for i in range(len(unsorted_list), 0, -1):
        j = len(unsorted_list) - 1
        while j > count:
            prev_list_item_index = j -1
            if unsorted_list[j] < unsorted_list[prev_list_item_index]:
                unsorted_list[j], unsorted_list[prev_list_item_index] = unsorted_list[prev_list_item_index], unsorted_list[j]
            j -= 1
        count += 1
    return unsorted_list
    
    
if __name__=='__main__':
    unsorted_list = []
    if len(sys.argv)==1:
        print('Enter atleast 1 number')
    else:    
        for arg in sys.argv[1:]:
            try:
                arg = int(arg)
            except ValueError:
                arg = json.loads(arg)
            unsorted_list.append(arg)
        print(bubble_sort(unsorted_list))
