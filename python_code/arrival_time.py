
def arrival_time(N,t0,tmax,sim_times,sim_nodes,sim_actions):
    
    """
    Compute the extinction time of the epidemic process
    Args:
        N (int): Number of the node in the graph
        t0 (float): Initial time
        tmax (float): Maximum time
        sim_times (list): List of the times of the simulation
        sim_nodes (list): List of the state of the nodes
        sim_actions (list): List of the actions (int if recovery, tuple if infection)
        
    Returns:
        float: Extinction time (time of the last step)
    """
    
    matrix=np.zeros(N)
    for i in range(len(sim_actions)):
        action = sim_actions[i]
        prev_state = sim_nodes[i]
        if type(action)==tuple:
            n1=action[0]
            n2=action[1]
            if prev_state[n1]=='S':
                matrix[n1]=sim_times[i+1]
            else:
                matrix[n2]=sim_times[i+1]
    
    return matrix

