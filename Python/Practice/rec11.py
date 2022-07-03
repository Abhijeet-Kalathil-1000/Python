def fun(i):
    if(i < 5):
        print(i)
        i = i +1
        fun(i)

def main():
    fun(0)
    

if __name__=="__main__":
    main()