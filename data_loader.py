import pandas as pd
import numpy as np
from operator import itemgetter
import os
import igraph as ig
import networkx as nx
import config

def load_profile_data(dir_string):

    directory = os.fsencode(dir_string)

    profile_array = []
    COL_INDICES = [0, 3, 7]
        
    for profile_data_file in os.listdir(directory):
        with open(dir_string + (str(profile_data_file)[2:-1])) as f:
            for line in f:
                profile_array.append(itemgetter(*COL_INDICES)(line.split("\t")))
    
    return np.array(profile_array)

def profile_data_to_df(profile_array, replace_null_strings=True):
    
    profile_df = pd.DataFrame(data=profile_array[0:,0:], 
                  index=[i for i in range(profile_array.shape[0])],
                  columns=['user_id', 'gender', 'age'])
    
    if replace_null_strings:
        profile_df.replace('null', -999999, inplace=True)
        profile_df.astype(int)
        profile_df.replace(-999999, np.nan, inplace=True)
    
    return profile_df

def load_graph_data(path, package='igraph'):
    packages = ['igraph', 'networkx']
    assert package in packages
    
    if package == 'networkx':
        graph = nx.DiGraph()
        with open(path) as f:
            [graph.add_edge(*(int(vert) for vert in line.rstrip().split())) for line in f]
    
    if package == 'igraph':
        graph = ig.Graph(directed=True)
        graph.add_vertices(config.NUM_NODES)
        with open(path) as f:
            [graph.add_edge(*(int(vert) for vert in line.rstrip().split())) for line in f]
    return graph

def read_ncol_graph():
    graph = ig.Graph(directed=True)
    g = graph.Read_Ncol(config.GRAPH_PATH, names=True, directed=True)
    return g

def write_pkl_graph(graph, file_name: str):
    graph.write_pickle(config.ROOT + file_name)
    print("Successfully serialized graph!")

def read_pkl_graph(file_name: str):
    _graph = ig.Graph(directed=True)
    Graph = _graph.Read_Pickle(config.ROOT + file_name)
    return Graph