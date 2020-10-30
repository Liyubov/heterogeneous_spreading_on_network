def extinction_time(N,t0,tmax,sim_times,sim_nodes,sim_actions):
    
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
    
    return sim_times[-1]
