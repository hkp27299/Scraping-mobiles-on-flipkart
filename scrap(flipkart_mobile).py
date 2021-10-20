import requests
from bs4 import BeautifulSoup

page = int(input("Enter number of pages: "))

for i in range(page):

    print('#####################################################################')

    b_url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_4&otracker1=AS_QueryStore_OrganicAutoSuggest_0_4&as-pos=0&as-type=RECENT&as-backfill=on&page="
    f_url = b_url + str(i+1)
    sc = requests.get(f_url)
    soup = BeautifulSoup(sc.text,'html.parser')
    #print(soup)
    phone = soup.find_all('div',{'class':'_4rR01T'})
    prize = soup.find_all('div',{'class':'_30jeq3 _1_WHN1'}) 

    count = 0
    for name in phone:
        print(phone[count].text)
        print(prize[count].text)
        count += 1