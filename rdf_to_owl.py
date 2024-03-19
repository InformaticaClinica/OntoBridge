import glob
import rdflib
import datetime

archivos_rdf = glob.glob('./*.ttl')
archivos_owl = glob.glob('./ontology/*.owl')

total_graph = rdflib.Graph()
for path in archivos_owl:
    total_graph.parse(path, format='xml')

print('owl graph done', datetime.datetime.now())

for path in archivos_rdf:
    graph_rdf = rdflib.Graph()
    graph_rdf.parse(path, format='ttl')
    print(f'Graph of {path} created.', datetime.datetime.now())

    for subject, predicate, obj in graph_rdf:
        total_graph.add((subject, predicate, obj))

print ('data added', datetime.datetime.now())
total_graph.serialize("reg_datanex_test.owl", format="xml")
print('finished', datetime.datetime.now())