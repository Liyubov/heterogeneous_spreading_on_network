# General problem of heterogeneous spreading on networks
Folder to keep ongoing code for producing simulations of heterogeneous spreading of SIR model on a network.
This is common work by P.Holme, F.Ianelli, L.Tupikina-Bauer and G.Simon (CRI master).

## How to use the repository?
1. The code in **"main_heterogeneous_spreading.py"** simulates 
the SIR model on heterogeneous network, where transmission rate beta 
is different on heterogeneous nodes. One can insert the list of the different heterogeneous nodes you want to put in a network at (one at a time, not all together). We make simulations on Watts-Strogatz and Albert-Barabasi networks.

2. In the file **"compute_global_measure.py"** we put computation of global measures, such as 
- extinction time
- averaged arrival time

3. In the file **"compute_local_measure.py"** we compute local measures such as 
- probability of a node to be infected
- arrival time to a node

4. We also put files in separate files for arrival time and extinction time calculations.

## Contact 
For any questions or comments contact us or make pull request if you find errors.

# License
GNU General Public License.
