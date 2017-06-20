import sys

def insertion_sort(*args):
    unsorted_list = args[0]
    for i in range(1,len(unsorted_list)):
        for j in range(len(unsorted_list)-1):
            if(unsorted_list[j]>unsorted_list[j+1]):
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
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
        print(insertion_sort(unsorted_list))
