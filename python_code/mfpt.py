
import numpy as np
import networkx as nx
from numpy.linalg import solve
from tqdm import tqdm
from numpy.linalg import inv

###############################################################################

class first_passage_time:
    
    def __init__(self,graph):
        self.graph = graph
        
        
    def mean(self, weightMatrix, source=None, target=None):
        """
        Compute the mean-first passage time for weighted network
        
        Parameters
        --------
                
            weightMatrix : ndarray
                  
                
        Returns:
        --------
        
            MFPT matrix : ndarray
                
        """           
        
        assert nx.is_connected(self.graph), "The network has to be connected" 
        A = np.asarray(nx.to_numpy_matrix(self.graph, dtype=float, weight=None).T)
        #print("The graph is directed:", nx.is_directed(g))
        #N = g.number_of_nodes()
        s = A.sum(1)
        Aw = np.multiply(A,weightMatrix)
        sw = Aw.sum(1)
        P = (Aw.T/sw).T
        #print("sum over columns of P", P.sum(1))  
        #assert np.all(s) > 0, "The network has to be connected"
        assert np.all(np.isclose(P.sum(axis=1), 1, rtol=1e-10)), "Non valid transition matrix" 
        
        
        self.nodes = self.graph.number_of_nodes()
        targets = range(self.nodes)
               
        I = np.eye( self.nodes,self.nodes )
        J = np.ones( (self.nodes, self.nodes) )
        M = np.zeros( (self.nodes, self.nodes) )

        e = np.ones( self.nodes )
        
        pi = sw.astype(float)/(np.nonzero(A)[1].shape[0])
        # assert(np.all(np.isclose(np.matmul(pi,P)-pi, 0., rtol=1e-5)), "ERROR in computing pi" 

        PI = np.outer(e, pi)
        Z = inv(I-P+PI)
        K = (I-Z+np.matmul(J,np.diag(np.diag(Z))))
        M = np.matmul(K,inv(np.diag(np.diag(PI))))
        np.fill_diagonal(M, 0)

        # MFPT = np.zeros((self.nodes,self.nodes),dtype=float)
        # for ii in targets:
        #     for jj in targets:
        #         MFPT[ii][jj] = (Z[jj][jj]-Z[ii][jj])/pi[jj]

        # assert np.all(np.isclose(MFPT-M, 0, rtol=1e-5)), "ERROR in computing M"


        
        # v = -1./self.nodes * (M.sum(1)+M.sum(0)) 
        if source is None:
            if target is None:
                return M  
            else:
                return M[:,target]
            
        else:
            if target is None:
                return M[source,:]
            else:
                return M[source,target]
    
        
# 
# 
# ###############################################################################
#     
# if __name__ == "__main__":
#     
#     # CHECK VERSIONS 
#     vers_python0 = '2.7.11'
#     vers_numpy0  = '1.11.0'
#     vers_netx0   = '1.9.1'
#     
#     from networkx import __version__ as vers_netx
#     vers_python = '%s.%s.%s' % version_info[:3]
#     vers_numpy  = np.__version__
#     
#     
#     print '\n---------'
#     print '---------'
#     print '---------'
#     print '---------'
#     print '---------'
#     print 'Required modules:'
#     print 'Python:   tested for: %s.  Yours: %s'    % (vers_python0, vers_python)
#     print 'numpy:    tested for: %s.  Yours: %s'    % (vers_numpy0, vers_numpy)
#     print 'networkx: tested for: %s.   Yours: %s'    % (vers_netx0, vers_netx)
#     print '--------'
#     print '--------'
#     print '--------'
#     print '--------\n'
#     
# 
