x = int(input(as))
print(x)

def oops():
    while True:
        try:
            x = int(input("Enter something:"))
            break
        except IndexError:
            print("OOOOOOOPS! Invalid index!")
            break
        except ValueError:
            print("Ops! Invalid Value!")
            break
    break

oops()


