class Destructor_:
    def __init__(self) -> None:
        print("Class created")

    def __del__(self):
        print("Destructor Called")



def Create_Object_Function():
    print("Object Created")

    Obj = Destructor_()
    print("Object function exiting...")

    return Obj

print("Calling  Create_Object_Function ")
Obj = Create_Object_Function()

print("Program ended")
