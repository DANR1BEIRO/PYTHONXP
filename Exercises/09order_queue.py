""" 
A delivery company is having difficulty organizing the
sorting of orders and needs to create a routine that
organizeds the order in a queue based on priority

tasks:
1 - add a new order "order 15" at the end of the queue
2 - remove the first order (order 12) from the queue
3 - print the entire queue

expected return: ["order 13", "order 14", "order 15"]
"""

order_queue = ["order 12", "order 13", "order 14"]


def queue_managemente2(array):
    
    return array[1:] + ["order 15"] # slice the list and concatenate 'order 15'

print(queue_managemente2(order_queue))



def queue_management(array):
    
    array.append("order 15")
    array.pop(0)
    return array

print(queue_management(order_queue))
