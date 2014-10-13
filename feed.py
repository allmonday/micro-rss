import feedparser as fp
import yaml
import json

bloglist = "./blogs.yml"

blogs = yaml.load(open(bloglist))
blogs = blogs['blogs']


def getRss(link):
    f = fp.parse(link)
    entries = []
    for e in f.entries:
        entries.append({
            'title': e.title_detail.value,
            'author': e.author_detail.name,
            'link': e.id,
            # 'summary': e.summary
        })
    return entries

all_blogs = []
for b in blogs:
    all_blogs.extend(getRss(b['link']))

open('rss.json', 'w').write(json.dumps(all_blogs))
