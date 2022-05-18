import markdown

# Simple conversion in memory
md_text = '# Hello\n\n**Text**'
html = markdown.markdown(md_text)
print(html)

pages = ["page-accueil1.md", "page2.md", "page3.md", "page4.md"]

i=0

for page in pages:
    markdown.markdownFromFile(
        input = pages[i],
        output = 'page'+str([i])+'.html',
        encoding='utf8'

    )
    i=i+1