import os, sys, requests
from bs4 import BeautifulSoup
from colorama import init,Fore
init(autoreset=True)

try:
    os.mkdir(sys.argv [1])
except:
    pass

stack = []

def read_or_write_site(filename, mode='w'):
    url = requests.get('https://' + filename).text
    soup = BeautifulSoup(url, 'html.parser')
    elem = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li', 'a','span'])
    with open(os.path.join(os.getcwd(), sys.argv[1], f'{filename.rsplit(".", 1)[0]}.txt'), mode) as f:
        if mode == 'w':
            stack.append(url.rsplit(".", 1)[0])
            for i in elem:
                f.write(i.get_text().replace('\n', ''))
                if i.name=='a':
                    print(Fore.BLUE + i.get_text().replace('\n', ''))
                else:
                    print(i.get_text().replace('\n', ''))
        else:
            print(f.read())

while True:
    url = input("\n")
    if "." in url:
        if requests.get('https://' + url):
            read_or_write_site(url)
    elif url.rsplit('.', 1)[0] in stack:
        read_or_write_site(url, mode='r')
    elif url == 'back':
        try:
            stack.pop()
            read_or_write_site(stack[-1], mode='r')
        except IndexError:
            continue

    elif url == 'exit':
        break
    else:
        print('Error: Incorrect URL')
