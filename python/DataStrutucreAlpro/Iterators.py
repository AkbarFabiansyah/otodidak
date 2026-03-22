x = "global value"
def outer():
    x = "enclosing value"
    def inner():
        x = "local value"
        print(x)
    inner()
outer()