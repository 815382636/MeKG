from rdflib.namespace import OWL, RDF, RDFS
from rdflib import Graph, Literal, Namespace, URIRef

# 构造链接数据工具的命名空间
LDT = Namespace("http://www.linkeddatatools.com/plants#")

# 创建图
graph = Graph()

# 创建节点并添加到图
Plant = URIRef(LDT["planttype"])

# 将OWL数据添加到图
graph.add((Plant, RDF.type, OWL.Class))
graph.add((Plant, RDFS.subClassOf, OWL.Thing))
graph.add((Plant, RDFS.label, Literal("The plant type")))
graph.add((Plant, RDFS.comment, Literal("The class of all plant types")))

# OWL和LDT绑定命名空间
graph.bind("owl", OWL)
graph.bind("ldt", LDT)

graph.serialize("graph.ttl", format="turtle")  # 推荐保存turtle，阅读方便
# graph.serialize("graph.xml",format="xml")
