def get_random_walk_sampled_network(full_network, sample_size=0, teleportation_proba=0.15):
    
    # get list of all nodes in the network
    all_nodes  = [n for n in full_network.nodes()]

    # randomly choose 1 node as starting point
    k_0 = np.random.choice(all_nodes, 1)[0]

    # initialize empty, directed networkx graph
    sampled_network = nx.DiGraph()
    sampled_network.add_node(k_0)

    for i in range(sample_size):
        
        # get a list of all nodes with an in-edge from k_0
        out_nodes_k0 = [tup[1] for tup in full_network.out_edges(k_0)]
        
        # draw random number to determine whether the walker traverses an edge or teleports
        traversion_threshold = (np.random.randint(1, 100)) / 100

        # traverse an edge with probability equal to 1-teleportation_proba
        if traversion_threshold <= (1-teleportation_proba):

            # if node k_0 has at least one outgoing edge, draw a random destination node
            # and add node k_1 to the network
            if len(out_nodes_k0) > 0:
                k_1 = np.random.choice(out_nodes_k0, 1)[0]
                sampled_network.add_node(k_1)
                # add k_0 if not already in nodes
                add_distinct_k0(sampled_network, k_0)
            
            # if node k_0 does not have any outgoing edges and is not yet in nodes, add node k_0 to graph
            # in this case, pick new random k_1 node from all possible nodes (where k_1 !=  k_0)
            # TODO: determine if this is actually useful / needed
            else:
                k_1 = np.random.choice([node for node in all_nodes if node != k_0], 1)[0]
                sampled_network.add_node(k_1)
                # add k_0 if not already in nodes
                add_distinct_k0(sampled_network, k_0)
        
        # teleport to a random node
        else:
            # remove connected nodes from possible teleportation destinations
            teleportation_destinations = [node for node in all_nodes if node not in out_nodes_k0]
            # randomly pick a teleportation destination node
            k_1 = np.random.choice(teleportation_destinations, 1)[0]
            # add this node to the sampled network
            sampled_network.add_node(k_1)
            # add k_0 if not already in nodes
            add_distinct_k0(sampled_network, k_0)

        # update the new starting node to be the previous destination node
        k_0 = k_1

    # all_possible_edges = list(itertools.combinations([n for n in sampled_network.nodes()], 2))
    

    
    return sampled_network