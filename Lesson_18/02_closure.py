# function in function
def hello(name):
    def formatted_hello():
        print(f'I wish to say hello to "{str(name).capitalize()}"')

    formatted_hello()


hello('adam')


# closure
#
# The term "closure" in programming originates from the mathematical concept
# of closure in set theory and lambda calculus.
# In programming, closure means that a function "closes" (or captures) its environment or execution context.
# This includes all variables and functions that were available at the time of its creation.

def hello_closure(name):
    def formatted_hello():
        print(f'I wish to say hello to "{str(name).capitalize()}"')

    return formatted_hello


func = hello_closure('Bob')
func()


# # object exist so internal operates with external function and all related parameters

def count(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = count(start=100)
c2 = count(start=200)
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
