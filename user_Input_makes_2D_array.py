'''
task of this bunch of codes is taking user inputs to make a 2D array with required numbers of
rows and columns and values of them.
'''
import numpy as np
# initial number of rows and columns for the desired array
row=int(input("enter the number of rows"))
column=int(input("enter the number of columns"))

# +1 because : we want it to begin with index 1.not 0
# so the first question in terms of taking values is NOT :
# 'enter value for 0 row and for 0 column.' BUT:
# 'enter value for 1 row and for 1 column.'
arr=[[int(input("enter value for {} row and for {} column".format(r+1,c+1)))
      for c in range(column)]for r in range(row)]

arr=np.array(arr)
print(arr)

'''
 task of this code is taking user inputs to give them access to
 required values of database.
 there is 3 solutions
 '''

array=np.array([[2017,4,21],[2017,9,0],[2016,70,19],[1998,182,3]])
# user gives input to access the required one.(linear complexity)

# !! NOTE that it's better passing argument's name as an invented name that
# is not already defined in python(as function for example)
# so DO NOT write list because list() is already a function in python.
def give_access(my_list):
    row_number = [int(input("Enter number of row"))]
    column_number = [int(input("Enter number of column"))]
    # check if the length of given request matches the length of array
    if row_number or column_number in len(my_list):
        required_array = my_list[row_number, column_number]
        return required_array
    else:
        return give_access(my_list)


print(give_access(array))

#required_array=array[3,2]
#print(required_array)

#required_array=array[row_number,column_number]
#print(required_array)
