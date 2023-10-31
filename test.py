def fluar():
    def fdalam():
        print('fdalam() dipanggil')
        print('fluar() dipanggil')

    fdalam()


fluar()
fluar()


def outher_function(siapa):
    def inner_function():
        print(f"hello,{siapa}")

    inner_function()


outher_function("upi")


def outer():
    message = 'local'

    def inner():
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)


outer()


def f(n):
    import time
    if n == 0:
        print(" Go!")
        return
    print(n, end=' ')
    time.sleep(1)
    f(n - 1)


f(3)
f(10)
