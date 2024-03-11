import sys

# Displaying the current search paths
print("Current search paths:")
for path in sys.path:
    print(path)
print('-' * 40)

# sys.path.append('/tmp')
# or
# export PYTHONPATH=:/tmp

if __name__ == '__main__':
    import tmp_module

    tmp_module.tmp_function()
