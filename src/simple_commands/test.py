import os

curpath = os.path.abspath(os.curdir)
filename = "simple_examples/command_example/zen_of_python.md"
filepath = os.path.join(curpath, filename)
f = open(filepath)
lines = f.read()
print(lines)
