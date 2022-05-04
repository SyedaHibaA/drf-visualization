from urllib.request import urlopen


def url_to_txt():
    drfURL = "<URL to convert>"
    fileURL = "<name of file to save to>"

    print("Starting content extraction")
    with urlopen(drfURL) as webpage:
        content = webpage.read().decode()
    print("Finished content extraction")

    print("Starting content printing")
    with open(fileURL, 'w') as output:
        output.write(content)
    print("Finished content printing")
