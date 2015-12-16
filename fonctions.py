#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import loader as ld
import matrix as mmat

#On doit construire les deux matrices de user-items
def maes( file1ap, file2te, k, remplissage = "users") :

  #Dimension des matrices
  
  d1 = ld.check_data(file1ap)
  
  #Matrice user-item du test

  mui_t = ld.matrice_user_item( file2te, d1[0], d1[1] )

  #Matrice des suggestions

  mui_a = ld.matrice_user_item( file1ap, d1[0], d1[1] )

  if remplissage == "users" :

    muif_a = ld.remplissage_moyenne_user(mui_a)

  else :
    
    muif_a = ld.remplissage_moyenne_film(mui_a)

  mae = []
  v1 = np.mat(np.ones(d1[0]))
  v2 = np.mat(np.ones(d1[1]))

  for i in xrange(1,k) :

    dec_a = mmat.simplifier(muif_a, i)  #Calcul décomposition à i
    
    m_sug = np.dot(dec_a[0], np.dot(dec_a[1], dec_a[2]) ) #Matrice suggestions

    #On calcule la mae

    m = abs(m_sug - mui_t)

    mae += [np.dot(v1, np.dot(m, v2.T))[0,0]/(d1[0]*d1[1])]
    
  return mae

#On doit construire les deux matrices de user-items
def mae( file1ap, file2te, k, remplissage = "users") :

  #Dimension des matrices
  
  d1 = ld.check_data(file1ap)
  
  #Matrice user-item du test

  mui_t = ld.matrice_user_item( file2te, d1[0], d1[1] )

  #Matrice des suggestions

  mui_a = ld.matrice_user_item( file1ap, d1[0], d1[1] ) #Mat u-i

  if remplissage == "users" :

    muif_a = ld.remplissage_moyenne_user(mui_a)     #Remplissage

  else :
    
    muif_a = ld.remplissage_moyenne_film(mui_a)

  maes = []

  for i in xrange(1,k) :

    dec = mmat.simplifier(muif_a,i) #Decomposition k
    
    msug = np.dot( dec[0], np.dot( dec[1], dec[2] )) #Matrice sugs

    c,s = 0.0,0.0

    for i in xrange(d1[1]) :
      for u in xrange(d1[0]) :
        if mui_t[u,i] <> 0 :

          c += 1
          s += abs( mui_t[u,i] - msug[u,i] )

    maes += [s/c]
    
  return maes
