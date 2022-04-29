import numpy as np
from scipy.optimize import linear_sum_assignment
def step1(m):
    for i in range(m.shape[0]):
        m[i,:]=m[i,:]-np.min(m[i,:])

def step2(m):
    for i in range(m.shape[1]):
        m[i,:]=m[i,:]-np.min(m[i,:])

def step3(m):
    dim=m.shape[0]
    assigned=np.array([])
    assignments=np.zeros(m.shape, dtype=int)
    for i in range (o, dim):
        for j in range(0,dim):
            if (m[i,j]==0 and np.sum(assignments[:,j])==0 and np.sum(assignments[i,:])==0):
                assignments[i,j]=1
                assigned =np.append(assigned,i)

        rows= np.linspace(0,dim-1,dim).astype(int)
        marked_rows=np.setdiff1d(rows,assigned)
        new_marked_rows=marked_rows.copy()
        marked_cols=np.array([])
        while(len(new_marked_rows)>0)
            new_marked_cols=np.array([],dtype=int)
            for nr in new_marked_cols:
                zeros_colsnp.arwhere(m[nr,:]==0).reshape(-1)
                new_marked_cols=np.append(marked_cols,new_marked_cols)
                for nr in new_marked_rows:
                    zeros_cols=np.arwhere(m[nr,:]==0).reshape(-1)
                    new_marked_cols=np.append(new_marked_cols)




