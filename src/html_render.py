with open('data/comments_data.json', 'r',encoding='utf8') as f:
    data = f.read()
jsfile = 'var data = ' + data
with open('html/data.js', 'w', encoding='utf8') as f:
    f.write(jsfile)