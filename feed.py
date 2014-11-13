#coding: utf-8
print('start')
import feedparser as fp
import yaml
import json
import os,sys

currentDir = os.path.dirname(os.path.realpath(__file__))
bloglist = currentDir + "/blogs.yml"
print(bloglist)
print(sys.version)

try:
    blogs = yaml.load(open(bloglist, encoding="utf-8"))
except Exception as e:
    print(e)
print('start work')
blogs = blogs['blogs']


def getRss(link):
    try:
        f = fp.parse(link)
        entries = []
        for e in f.entries:
            entries.append({
                'title': e.title_detail.value,
                'author': e.author_detail.name,
                'link': e.id,
                'date': ' '.join(e.published.split(' ')[1:4])
            })
    except Exception as e:
        print(e)
    return entries

print('start work2')
all_blogs = []
for b in blogs:
    all_blogs.extend(getRss(b['link']))

open(currentDir + '/rss.json', 'w').write(json.dumps(all_blogs))
print('finished')
