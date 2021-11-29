import sys
import webbrowser

_currentDegree = 0
_heaterStatus = False
_altitute = 0

# get keyboard key from user
def get_key():
    key = input("Enter key: ").lower()
    if key == "":
        return None
    else:
        return key
        
def getKeyAndRun():
    # check if get_key is A
    if get_key() == "a":
        print("Currrent degree: ", _currentDegree)
        print("Heater status: ", _heaterStatus)
        print("Altitute: ", _altitute)
    #else check if get_key is Esc
    elif get_key() == "q":
        sys.exit()
    #else check if get_key is W then open a website in browser
    elif get_key() == "w":
        webbrowser.open("https://github.com/muratkabia/ColdDrone")


# main function greeting
def main():
    print("Welcome to ColdDrone")
    print("Press A to get information")
    print("Press Esc to exit")
    print("Press W to open website")
    while True:
        getKeyAndRun()
    

# if __name__ is "__main__" run main()
if __name__ == "__main__":
    main()