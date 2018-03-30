from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
print(f.getvalue())




f1 = StringIO('Hejfjf\nhhhh\njfdjfjdfff!')
while 1:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())
