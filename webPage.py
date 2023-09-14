def webPage():
    import webbrowser
    web1 = "https://www.bbc.co.uk/"
    web2 = "https://en.wikipedia.org/wiki/Main_Page"
    web3 = "https://www.nasa.gov/"
    answer = int(input("1 for the bbc, 2 for wiki, 3 for nasa: "))
    if answer == 1:
        webbrowser.open(web1)
    elif answer == 2:
        webbrowser.open(web2)
    else:
        webbrowser.open(web3)

webPage()






