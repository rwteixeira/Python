x = 1

def hello(name):
    return f"Hello {name}!"

name = str(input("Nome: "))
print(hello(name))

# ----------------------------------
x: int  = 1

def hello(name: str) -> str:
    return f"Hello {name}!"

name = str(input("Nome: "))
print(hello(name))
