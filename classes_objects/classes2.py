class A:

    def __new__(cls):
        print("Object created")
        return super().__new__(cls)

    def __int__(self):
        print("Object initialized")

    def __del__(self):
        print("Object deleted")
