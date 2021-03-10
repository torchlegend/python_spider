import requests
import bs4
import csv

file = open("douban.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow(["num", "title", "rate", "recommendation"])

for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'}
    res = requests.get(url, headers=header)
    # print(res.text)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    # print(bs)
    bs = bs.find('ol', class_='grid_view')
    # print(bs)
    for titles in bs.find_all('li'):

        try:
            num = titles.find('em', class_='').text
            title = titles.find('span', class_='title').text
            rate = titles.find('span', class_='rating_num').text
            rec = titles.find('span', class_='inq').text
            # print(rec)
            # print(num, title, rate, rec)
            writer.writerow([num, title, rate, rec])
        except AttributeError as e:
            # print(e)
            writer.writerow([num, title, rate])

file.close()
print("douban.csv写入完成")
