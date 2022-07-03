from sys import *
import webbrowser
import re
import urllib3

def is_connected():
    try:
        urllib3.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib3.URLError as err:
        return False

def Find(string):
    ur = re.findall('htpp[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def Weblauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new = 2)

def main():
    print("______________AUtomation______________")
    print("Applicaiton name :"+argv[0])

    if (len(argv)!=2):
        print("Error : invalid number of arguments")
        exit()
    
    if(argv[1]=="-h") or(argv[1]=="-H"):
        print("The script is used open URL wich are written in one file")
        exit()
    
    if(argv[1]=="-u") or(argv[1]=="-U"):
        print("Usage : ApplicaiotName Name_of_File")
        exit()
    
    try:
        connected = is_connected()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect internet ....")

    except ValueError:
        print("Error :Invalid Datatype of input")
    except Exception as E:
        print("Error : Invalid input",E)


if __name__=="__main__":
    main()