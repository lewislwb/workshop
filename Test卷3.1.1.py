def decor(say_happy):
    def wrapper():
        print("\n")
        say_happy()
    return wrapper
@decor

def say_happy():
    print("I am happy")

say_happy()
