import imp
f, filename, description = imp.find_module('sys')
sys = imp.load_module('sys', f, filename, description)
print(sys)
os = __import__('os')
print(os.path)
filename = "t.py"
f = open("t.py")
description = ('.py', 'U', 1)
t = imp.load_module('some', f, filename, description) # t就是`import t`后的结果
print(t)
