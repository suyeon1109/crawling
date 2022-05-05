import requests
from bs4 import BeautifulSoup

# url = "https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"


# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup= BeautifulSoup(html, 'html.parser')
#     ul = soup.select_one('#s_content > div.section > ul')
#     titles = ul.select('li > dl > dt > a')
#     for title in titles:
#         print(title.get_text())
    
# else:
#     print(response.status_code)



#2
# url = "https://search.shopping.naver.com/search/category/100000022"


# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup= BeautifulSoup(html, 'html.parser')
#     ul = soup.select_one('#__next > div > div.style_container__1YjHN > div > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul')
#     titles = ul.select('ul > div > div > li > div > div.basicList_info_area__17Xyo > div > a')
    
#     for title in titles:
#         print(title.get_text())
    
# else:
#     print(response.status_code)




# params = {
#     'pageNo':1,
#     'rangeType' : 'ALL',
#     'orderBy': 'recentData',
#     'keyword': '파이썬'
# }

# response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params = params)


# print(response.status_code)
# #print(response)
# print(response.url)



#쿠팡포기
url = "https://www.coupang.com/np/search?component=&q=%EB%B9%A8%EB%8C%80&channel=user"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup= BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.productList')
    titles = ul.select('a > dl > dd > div > div')
    print(ul)
    
    for title in titles:
        print(title.get_text())
    
else:
    print(response.status_code)
