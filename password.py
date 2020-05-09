import subprocess

def write(result):
    file = open("password.txt", "w")
    for i in result:
        file.write(i["name"]+"<-------->"+i["password"]+"\n")
    file.close()


def run():
    a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell= True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode('utf-8').split('\n')
    a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
    list = []
    for i in a:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i , 'key=clear'], shell= True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode('utf-8').split('\n')
        result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]
        try:
            get_name = {"name": i, "password": result[0]}
        except Exception:
            get_name = {"name": i, "password": "Can not find password"}
        list.append(get_name)
    return list

result = run()
write(result)
