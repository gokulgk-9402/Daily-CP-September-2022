def MainProgram(f):
    def Create(old_value):
        def new_value(*args, **kwds):
            return f * old_value(*args, **kwds)
        return new_value
    return Create

@MainProgram(5)
def return_value(n):
    return n

res = return_value(5)
print(res)