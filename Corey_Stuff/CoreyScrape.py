
from requests_html import HTML

with open('/Users/ricksegal/Dev/30DayPython/Corey_Stuff/simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('title')
print(match[0].text)
