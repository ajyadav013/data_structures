import sys
import json


def selection_sort(*args):
    unsorted_list = args[0]
    for i in range(len(unsorted_list)):
        least = i
        for j in range(i+1,len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[least]:
                least = j
        temp = unsorted_list[least]
        unsorted_list[least] = unsorted_list[i]
        unsorted_list[i]  = temp
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
        print(selection_sort(unsorted_list))
