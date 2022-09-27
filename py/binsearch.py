# binsearch
# Jihae Park
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 


# This algorithm only works on sorted ArrayLists.

data = [0,1,3,7,9,10]

def binarySearch(data, value):

# create assign variables representing the high, low and middle indices 
# while we're not done:
#   if the item is at middle, return middle
#   otherwise, update high, low, and middle
  low = 0
  high = len(data) - 1
  mid = int((low + high)/2) # average

  #Print out the values of lo:mid:hi for each call
  #print(low + ":" + mid + ":" + high);

  binaryS = True
  
  while(binaryS):
    if(data[mid] == value):
      return mid
    else: # when the data != value
      if(value < data[mid]): # when value < mid
        high = mid - 1
        mid = int((low + high)/2)
      else: #when value > mid
        low = mid + 1
        mid = int((low + high)/2)
      if(low > high): #this was a breakthrough!!! 
        binaryS = False
  return -1 #when the value is not in data 



print("The number's index in the list is ", binarySearch(data,3))