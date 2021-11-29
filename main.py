import sys

_currentDegree = 0
_heaterStatus = False
_altitute = 0

# get keyboard key from user
def get_key():
    key = input("Enter key: ")
    if key == "":
        return None
    else:
        return key

# check if get_key is A
if get_key() == "A":
    print("Currrent degree: ", _currentDegree)
    print("Heater status: ", _heaterStatus)
    print("Altitute: ", _altitute)
#else check if get_key is Esc
elif get_key() == "Esc":
    sys.exit()
#else check if get_key is W then open a website in browser
elif get_key() == "W":
    import webbrowser
    webbrowser.open("http://www.google.com")