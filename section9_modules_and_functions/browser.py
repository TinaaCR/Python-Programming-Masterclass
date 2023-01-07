import webbrowser

# webbrowser.open("https://www.python.org/", new=1)   # new=1 skulle åpnet python siden i et nytt vindu, men det skjedde ikke. men dette kan løses på en annen måte:

# chrome = webbrowser.get(using='chrome')
# chrome.open_new("https://www.python.org/")

# help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='; ', end= " ")  # sep= står for separator

windows = webbrowser.get(using='windows-default')
windows.open("http://www.python.org/")