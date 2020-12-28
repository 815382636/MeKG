import rdflib
from rdflib.graph import Graph, ConjunctiveGraph
from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS, FOAF

myOntology = Namespace("http://www.semanticweb.org/myOntology#")

# Create the graph
g = Graph()
g.bind("myOntology", myOntology)

# Create the node to add to the Graph
urbanSystem = URIRef(myOntology["urbanSystem"])

# Add the OWL data to the graph
g.add((urbanSystem, RDF.type, OWL.Class))
g.add((urbanSystem, RDFS.subClassOf, OWL.Thing))

name = URIRef(myOntology["name"])
g.add((name, RDF.type, OWL.Class))
g.add((name, RDFS.subClassOf, urbanSystem))
g.add((name, RDF.type, OWL.ObjectProperty))
# label = URIRef(myOntology["Paris"])
# g.add((label, RDF.type, myOntology.urbanSystem))
# g.add((label, myOntology.name, Literal['Paris']))
g.serialize("te1.ttl", format="turtle")  # 推荐保存turtle，阅读方便

