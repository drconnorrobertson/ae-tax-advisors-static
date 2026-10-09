from html.parser import HTMLParser
from urllib.parse import urljoin
import re
class Markdown(HTMLParser):
 def __init__(self,url):super().__init__(convert_charrefs=True);self.url=url;self.parts=[];self.active=False;self.skip=0;self.links=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='main':self.active=True
  if not self.active:return
  if t in ['script','style']:self.skip+=1
  if self.skip:return
  if re.fullmatch('h[1-6]',t):self.parts.append('\n\n'+'#'*int(t[1])+' ')
  elif t in ['p','div','section','article','dt','dd','ul','ol','dl','nav']:self.parts.append('\n\n')
  elif t=='li':self.parts.append('\n- ')
  elif t=='br':self.parts.append('\n')
  elif t=='a' and a.get('href'):self.parts.append('[');self.links.append(urljoin(self.url,a['href']))
 def handle_endtag(self,t):
  if t=='main':self.active=False
  if not self.active:return
  if t in ['script','style']:self.skip=max(0,self.skip-1);return
  if self.skip:return
  if t=='a' and self.links:self.parts.append(']('+self.links.pop()+')')
  if re.fullmatch('h[1-6]',t):self.parts.append('\n\n')
 def handle_data(self,d):
  if self.active and not self.skip:self.parts.append(d)
def publish_markdown(out,base,urls):
 for path in urls:
  p=out/path.strip('/')/'index.html';s=p.read_text();m=Markdown(base+path);m.feed(s)
  text=re.sub(r'\n{3,}','\n\n',re.sub(r'[ \t]+',' ',''.join(m.parts))).strip()
  p.with_name('index.md').write_text('# Source: '+base+path+'\n\n'+text+'\n')
  p.write_text(s.replace('</head>','<link rel="alternate" type="text/markdown" href="'+base+path+'index.md"></head>'))
