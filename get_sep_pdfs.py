from lxml import html
from requests import Session
from urllib.parse import urlparse, urlunparse

LOGIN_URL = 'https://leibniz.stanford.edu/friends/login/'
TITLES_URL = 'https://leibniz.stanford.edu/friends/info/title_list/'
TITLES_XPATH = '//div[@id="content"]/div[3]/div/ul/li/a/@href'

login_data = {'email':'',
              'password':''}

s = Session()
_ = s.post(LOGIN_URL, data=login_data)

titles_page = s.get(TITLES_URL)
tree = html.fromstring(titles_page.content)
titles_urls = tree.xpath(TITLES_XPATH)

for title_url in titles_urls:
    parsed_url = urlparse(title_url)
    path_parts = parsed_url.path.split('/')
    pdf_name = path_parts[4]
    path_parts[3] = 'view'
    path_parts[-1] = 'sc' # single page
    path_parts.append('')
    path = '/'.join(path_parts)
    pdf_url = urlunparse(parsed_url._replace(path=path))
    d = s.get(pdf_url)
    with open('pdfs/' + pdf_name + '.pdf', 'wb') as f:
        f.write(d.content)

    
