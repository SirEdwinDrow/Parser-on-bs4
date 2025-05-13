from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('input URL')
html = req.read()

soup = BeautifulSoup(html, 'html.parser') #type of parser
news = soup.find_all('div', class_='product-card__wrapper') #main selector

results = []

for item in news:# second selectors
    title = item.find('span', class_='product-card__name-separator ').get_text(strip=True)
    price = item.find('b', class_='red').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'price': price,
        'href': href,
    })

f = open('test.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Название № {i}\n\nНазвание: {item["title"]}\nЦена: {item["price"]}\nСсылка: {item["href"]}\n\n**********************\n')
    i += 1
print('Всё готово')
f.close()
