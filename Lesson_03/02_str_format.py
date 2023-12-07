name = 'Adam'
surname = 'Yellow'

t1 = 'Hello, %s!' % name   # old style
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
t2 = 'Hello, {0} {1}!'.format(name, 'Big Surname')   # python 2-3
t3 = f'Hello,{surname} {name=}!'       # f-strings
print(t1)
print(t2)
print(t3)
#
TEMPLATE = "Happy new {0} YEAR!"
year = 2024
print(TEMPLATE.format(year))


e1 = """Example1
        Multiline
     """
e2 = "Example2"
e3 = "Example3 can't be simple\n000000"
e4 = 'Bar "Night"'  # best practices
print(e1)
print(e2)
print(e3)


t4 = 'c:\windows\temp'
print(t4)

t5 = r'c:\windows\temp\n'
print(t5)
print(repr(t4))


