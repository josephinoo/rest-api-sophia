from search_engines import Google

engine = Google()
results = engine.search("Joseph Avila Alvarez")
links = results.links()
print(links)