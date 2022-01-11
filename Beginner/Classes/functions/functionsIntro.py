


def greeting(name):
    txt = "hello "+ name
    return txt
    
def f(x):
    y=x+2
    #print(y) # this is not the output of the function, this is just us printing the output 
    return y
    

def print_minutes_per_day(days):
    hours= 24 * days
    minutes = hours*60
    seconds= minutes*60
    print(minutes)
    



print_minutes_per_day(3)