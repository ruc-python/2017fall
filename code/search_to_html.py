import time 

class ImageSearch:
    def __init__(self, tagfile):
        self.data = map(str.strip, open(tagfile).readlines())
     
    def search(self, query):
        s_time = time.time()
        hitlist = []
        for line in self.data:
            imageid, userid, tags = line.strip().split('\t') # tab character as separator
            tagset = set(tags.split())
            if query in tagset:
                hitlist.append(imageid)
        timecost = time.time() - s_time
        return {'content':hitlist, 'time':timecost}

img_width = 150
img_height = 150
tagfile = '/Users/xirong/VisualSearch/flickr10k/TextData/id.userid.rawtags.txt'
searcher = ImageSearch(tagfile)       
# results = searcher.search(...)
query = 'flower'
query = 'cat'
results = searcher.search(query)
#hitlist = ['2483368623'] * 20
hitlist = results['content']

resfile = '%s.html' % query

html_content = []
html_content.append("<html>")

header = '<h1>search results of %s, %d hits, %.3f seconds</h1>' % (query, len(hitlist), results['time'])
html_content.append(header)

html_content.append('<table>')
columns = 5
rows = len(hitlist) / columns

for i in range(rows):
    html_content.append('<tr>')
    for j in range(columns):
        index = i*columns + j 
        imageid = hitlist[index]
        url = 'http://localhost:9000/img/%s.jpg' % imageid
        img_tag = '<img width=%d height=%d src=%s></img><br>%s' % (img_width, img_height, url, imageid)
        html_content.append('<td>%s</td>' % img_tag)

    html_content.append('</tr>')

html_content.append('</table>')

html_content.append("</html>")

fw = open(resfile, 'w')
fw.write('\n'.join(html_content))
fw.close()


