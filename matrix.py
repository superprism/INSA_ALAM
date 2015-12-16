#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np




def simplifier( mat, k) :
  
  #Decomposition
  
  U, s, Vs = np.linalg.svd(mat, full_matrices=False)
  
  mini = len(mat) if len(mat) <= len(mat[0]) else len(mat[0])

  sk = np.zeros(s.shape)
  Uk = np.zeros(U.shape)
  Vk = np.zeros(Vs.shape)

  Uk[:,:k] = U[:,:k]
  
  Vk[:k,:] = ((Vs.T)[:,:k]).T
  
  sk[:k] = s[:k]
  sk = np.diag(sk)

  return (Uk, sk, Vk)



def approx(Uk, sk, Vk, u, i) :

  #Ligne u et colonne i

  Uku = Uk[u,:]
  Vki = Vk[:,i].T

  return np.dot( Uku, np.dot(sk, Vki) )


