import time
from datetime import datetime as dt
hosts_temp = "C:\Users\Varunika Gupta\Documents\python\webite blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,16)<dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hours")
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for x in website_list:
                if x in content:
                    pass
                else:
                    file.write(redirect + " " + x + "\n")

    else:
        with open(hosts_temp,'r+') as file :
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")
    time.sleep(5)
