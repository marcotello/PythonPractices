import time

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print ("Items: {}, {}".format(first_loop_item,second_loop_item))
            
            
start = time.time()
Quad_Example([1,2,3,4])
end = time.time()
print(end-start)