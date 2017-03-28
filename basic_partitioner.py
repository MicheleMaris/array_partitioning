def trivial_partitioner(ipvalue,lkeys=None) :
   """keys,ptable=trivial_partitioner(ipvalue)
      a very simple, slow, but robust partitioner.
      input : 
         ipvalue = array of integers
      output :
        keys = array of unique values in ipvalue (np.unique(ipvalue))
        ptable = array of arrays, 
                 each ith sub array is the list of elements in ipvalue
                 whith value given by keys[ith]
   """
   import copy
   import numpy as np
   keys=np.unique(ipvalue) if lkeys == None else np.array(lkeys)
   ptable=[]
   for k in keys :
      ptable.append([t for t in range(len(ipvalue)) if ipvalue[t]==k])
   return np.array(ptable),np.array(keys)

def sparse_partitioner(pvalue) :
   """keys,ptable,itv,isort=sparse_partitioner(ipvalue)
      a very fast partitioner.
      input : 
         ipvalue = array of integers
      output :
        keys = array of unique values in ipvalue (np.unique(ipvalue))
        ptable = array of arrays, 
                 each ith sub array is the list of elements in ipvalue
                 whith value given by keys[ith]
        itv = list of intervals in isort corresponding at keys[ith]
        isort = list of sorted elements in ipvalue, equivalent to
                np.argsort(ipvalue)
   """
   import copy
   import numpy as np
   isort=np.argsort(pvalue)
   spvalue=pvalue[isort]
   borders=np.where(spvalue[1:]-spvalue[:-1]>0)[0]
   itv=[]
   k1=0
   for k in borders :
      itv.append([k1,k])
      k1=k+1
   itv.append([k1,len(isort)-1])
   ptable=[]
   keys=[]
   for k in itv :
      keys.append(pvalue[isort[k[0]]])
      ptable.append(isort[k[0]:(k[1]+1)])
   return np.array(keys),np.array(ptable),np.array(itv),isort

