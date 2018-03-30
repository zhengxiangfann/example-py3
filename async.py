def framework(login):
    try:
        it = logic()
        s = next(it)
        print('[FX] login:', s)
        print('[FX] do some')
        it.send('async:' + s)
    except StopIteration:
        pass

def logic():
    s = 'mylogin'
    r = yield s
    print(r)

framework(logic)
