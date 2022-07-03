
class Demo:
    def __init__(self):
        print("Inside Init (Construstor)")
    def __del__(self):
        print("Inside del (Disstructor)")

def main ():
    print("Inside main")
    obj = Demo()
    print("End Main")

if __name__=="__main__":
    main()
    print("end of app")