import webbrowser

done = False

while not done:
    print('Welcome to WebBrowser!')
    print('Press 1 to learn Python.')
    print('Press 2 to learn Modules.')
    print('Press 3 to learn Python, Fullstack, English on Code.')
    print('Press 4 to Leave.')
    choise = input('>')

    if choise == '1':
        webbrowser.open('https://www.python.org')
    elif choise == '2':
        webbrowser.open('https://docs.python.org/3/py-modindex.html')
    elif choise == '3':
        webbrowser.open("https://pages.onebitcode.com/")
    elif choise == '4':
        done = True
    else:
        print('Invalid input!')
