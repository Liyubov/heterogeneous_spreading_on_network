
def outbreak_time(N,t0,tmax,sim_times,sim_nodes,sim_actions):
    
    """
    Compute the time of the maximum number of I that were present at one point, called outbreak time
    Args:
        N (int): Number of the node in the graph
        t0 (float): Initial time
        tmax (float): Maximum time
        sim_times (list): List of the times of the simulation
        sim_nodes (list): List of the state of the nodes 
        sim_actions (list): List of the actions (int if recovery, tuple if infection)
        
    Returns:
        float: Time of the outbreak
    """
    
    nb_steps = len(sim_times)
    matrix=np.zeros([nb_steps])
    for i in range(nb_steps):
        matrix[i] = len([node for node,state in sim_nodes[i].items() if state in ['I']])
    
    return sim_times[np.argmax(matrix)]
