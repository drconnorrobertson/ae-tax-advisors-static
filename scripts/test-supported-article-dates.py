import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('dates',Path(__file__).with_name('sync-supported-article-dates.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
url='https://www.aetaxadvisors.com/example/'
base='''<html><head><link rel="canonical" href="'''+url+'''">\n<meta property="article:published_time" content="2023-09-27T00:00:00-04:00">\n<meta property="article:modified_time" content="2026-10-06T00:00:00Z">\n<script type="application/ld+json">{"@type":"BlogPosting","url":"'''+url+'''","datePublished":"2023-09-27","dateModified":"2026-11-08"}</script></head><body><main><p>Updated November 8, 2026.</p><p>Original article.</p></main></body></html>'''
tag='<meta property="article:modified_time" content="2026-10-06T00:00:00Z">'
updated,reason=m.reconcile(base);assert reason and updated==base.replace(tag,'');assert '2023-09-27T00:00:00-04:00' in updated;assert m.reconcile(updated)==(updated,None)
negative=[base.replace('2026-10-06T00:00:00Z','2026-11-08T12:00:00Z'),base.replace('Updated November 8','Updated November 9'),base.replace('Updated November 8, 2026.','No editorial date.'),base.replace('dateModified":"2026-11-08"','dateModified":"2026-11-08T12:34:56Z"'),base.replace('</head>',tag+'</head>'),base.replace('</head>','<link rel="canonical" href="'+url+'">'+'</head>'),base.replace(url,'https://elsewhere.example/'),base.replace('November 8','November 40')]
for source in negative:assert m.reconcile(source)==(source,None)
other='<script type="application/ld+json">{"@type":"BlogPosting","url":"https://www.aetaxadvisors.com/other/","dateModified":"2026-10-01"}</script>'
assert m.reconcile(base.replace('</head>',other+'</head>'))[1]
ambiguous=other.replace('/other/','/example/')
source=base.replace('</head>',ambiguous+'</head>');assert m.reconcile(source)==(source,None)
print('Supported-date correction, exact byte preservation, idempotence, eight negative controls, unrelated-article and ambiguous-article controls passed.')
