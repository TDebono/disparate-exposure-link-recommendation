import jsonpickle
import networkx

from networkx.readwrite import json_graph

def serialize(call_graph, file_path):
    '''Function to serialize a NetworkX DiGraph to a JSON file.'''
    if not isinstance(call_graph, networkx.DiGraph):
        raise Exception('call_graph has be an instance of networkx.DiGraph')

    with open(file_path, 'w+') as _file:
        _file.write(jsonpickle.encode(
            json_graph.adjacency_data(call_graph))
        )

def deserialize(file_path):
    '''Function to deserialize a NetworkX DiGraph from a JSON file.'''
    call_graph = None
    with open(file_path, 'r+') as _file:
        call_graph = json_graph.adjacency_graph(
            jsonpickle.decode(_file.read()), 
            directed=True
        )
    return call_graph