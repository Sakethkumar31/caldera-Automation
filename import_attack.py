from py2neo import Graph, Node
import json

graph = Graph("bolt://host.docker.internal:7687", auth=("neo4j", "Saketh@@2004"))

with open("cti/enterprise-attack/enterprise-attack.json", "r") as file:
    data = json.load(file)

for obj in data['objects']:
    if obj['type'] == 'attack-pattern':
        technique = Node("Technique", id=obj['id'], name=obj['name'], description=obj.get('description', ''))
        graph.merge(technique, "Technique", "id")

print("MITRE ATT&CK data imported successfully!")
