from search_engines import Google, Bing
from search_engines.multiple_search_engines import MultipleSearchEngines, AllSearchEngines


def read_conteiners():
    file_contents = open('search_engine/data.txt', 'r')
    return [linea.rstrip() for linea in file_contents]


def query_search(query):
    dict_results = {
        "programs": None, "seminar": None, "symposium": None, "congress": None, "courses": None,
        "conference": None, "diploma": None, "certificate": None, "talk": None,
        "webinar": None, "workshops": None, "colloquium": None, "intership": None,

    }
    results_querys_plus = []
    separte_result = []

    for plus in read_conteiners():
        engine = Bing()
        results = engine.search(query + " " + plus, 10)
        results_querys_plus.append(results)

    for information in results_querys_plus:
        information_individual = []
        for item in information:
            add_item = {"title": item['title'], "link":
                        item['link'], "text": item['text']}

            information_individual.append(add_item)
        separte_result.append(information_individual)
        information_individual = []
    position_query = 0
    for cheat in read_conteiners():

        dict_results[cheat] = separte_result[position_query]
        position_query += 1

    return dict_results
