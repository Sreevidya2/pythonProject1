# using decorates we can add some extra features to the exsisting functions
'''def div(a,b):
    if a<b:
        a,b = b,a
    print(a/b)
div(2,4)'''

# if we cant change  the function then we use other function to modify exsisting function i.e., decorators
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner


div = smart_div(div)   # updating function using decorators


div(2, 4)

