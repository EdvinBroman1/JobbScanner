import urllib.request
import re
import time
import os

clear = lambda: os.system('cls')
all_websites = {"https://candidate.hr-manager.net/Vacancies/List.aspx?customer=elkjop_nordic&MediaId=4629&uiculture=sv"} #elgig

keyword = "Halmstad"

while True:
    for website in all_websites:
        f = urllib.request.urlopen(website)
        myfile = f.read().decode('utf-8')
        print(myfile)
        count = re.findall(keyword, myfile)
        if len(count) != 0:
            clear()
            print("NYTT JOBB...")
    time.sleep(10800)
