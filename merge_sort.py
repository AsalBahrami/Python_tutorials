'''merge sort uses divide and conquer algorithm. the main concept is
dividing a list into halved sub lists and so on until having single
elements(sub lists with 2 elements and 1 length ) after
dividing we will merge it together meanwhile sorting it by
putting smaller elements earlier in
the initialized list(here named result)'''
def merge(arr):

    '''A return statement is used to end the
     execution of the function call
    and “returns” the result (value of the expression
    following the return keyword) to the caller.
    The statements after the return statements are
    not executed. If the return statement is without
    any expression, then the special value None is returned.'''

    '''
    i think this "if" says execute the function until reaching all 
    elements as couple ones with length 1 and then merge it.
    When this happens we need no more recursive divisions into a and b.
    so when we write if statement after defining a and b it does not work
    and gives us an infinity recursion.
    but feel free to write it after mid,i,j and result initialization.we will
    get the same result.
    '''
    if len(arr) < 2:
        return arr

    mid=int((len(arr))/2)
    b=merge(arr[:mid])
    a=merge(arr[mid:])
    i=0
    j=0
    result=[]

    while i<len(b) and j<len(a):
        if a[j]<b[i]:
            result.append(a[j])
            j+=1
        else:
            result.append(b[i])
            i+=1

    result+=b[i:]
    result+=a[j:]
    return result

list_it = [10, 7, 4, 0, 8, 12, 9]
print(merge(list_it))
# or writing it as the following
print("the required list is : ",*list_it," after sorting: ",*merge(list_it))
# or
print("the required list is :{} and after sorting is {} ".format(list_it,merge(list_it)))
# but the above pints convert it into str and thats not request from.