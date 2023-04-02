from bs4 import BeautifulSoup


with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# find() - шукаємо перший знайдений тег з таким класом, ід ... і всі вкладені в нього елементи,
# find_all() - шукаємо всі теги з таким класом, ід ... і всі вкладені в нього елементи

# page_info = soup.find('h2')
# print(page_info)

# page_info = soup.findAll('h2')
# print(page_info)
# for elem in page_info:
#     print(elem.text.strip())

# page_info = soup.find('h2', class_='info_name')
# print(page_info.text.strip())

# page_info = soup.find('h2', class_='info_name').find('span').text
# print(page_info)

# page_info = soup.find('div').find('h2', {'class': 'info_name', 'id': 'name'}).text.strip()
# print(page_info)

# page_info = soup.find('div', 'info_wrap').find_all('span')
# print(page_info)
# print(page_info[2].text)

# page_info_links_1 = soup.find(class_='social').find('ul').find_all('a')
# page_info_links_2 = soup.find_all('a')
# # print(page_info_links_2)
#
# for item in page_info_links_2:
#     text = item.text
#     a_href = item.get('href')
#     print(f"{text}: {a_href}")


# find_parent() - шукаємо тег з таким класом, ід ... і перший знайдений його 'батько' тег,
# find_parents() - шукаємо тег з таким класом, ід ... і всі вище стоячі теги включаючи body і html

# page_info = soup.find(class_='blog').find_parent()
# print(page_info)

# page_info = soup.find(class_='blog').find_parents()
# print(page_info)


# next_element - відображає наступний елемент після найденного,
# previous_element - відображає попередній елемент перед найденим

# page_info = soup.find(class_='info_name').next_element.next_element
# print(page_info)


# next_siblings - відображає наступний елемент після найденного в одному спільному класі,
# previous_siblings - відображає попередній елемент перед найденим в одному спільному класі

# page_info = soup.find(class_='blog').next_sibling.next_sibling
# print(page_info)

# re.compile - шукає по короткому виразі цілу назву

# page_info = soup.find('a', string=re.compile('Boom'))
# print(page_info)

# page_info = soup.find_all(string=re.compile('([Bb]oom)'))
# print(page_info)
