import requests
from bs4 import BeautifulSoup
import re

re_problems = re.compile(r'^/problems/')
re_ago = re.compile(r'((\d+) hours?, )?(\d+) minutes? ago')

def scrap_user(user):
    ret = []
    resp = requests.get('https://leetcode.com/%s/' % user)
    if not resp.ok:
        print('Failed scraping user %s\'s Leetcode status' % user)
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    for a in soup.find_all('a', href=re_problems):
        status = a.find('span', {'class': 'badge'}).string.strip().replace('\u00A0', ' ')
        if status != 'Accepted':
            continue
        problem = a.find('b').string.strip().replace('\u00A0', ' ')
        ago = a.find('span', {'class': 'text-muted'}).string.strip().replace('\u00A0', ' ')
        match = re.fullmatch(re_ago, ago)
        if match:
            hours, minutes = match.group(2, 3)
            minutes = int(minutes)
            if hours:
                minutes += int(hours) * 60
            ret.append((problem, status, minutes))
    print('Retrieved user %s\'s Leetcode status:' % user, ret)
    return ret
