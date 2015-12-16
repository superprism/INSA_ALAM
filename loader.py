#!/usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np


def matrice_user_item( nFile, nbUser, nbFilm) :
    
    mat = np.zeros((nbUser, nbFilm))
    
    # (<id utilisateur>, <id film>, <rating>, <date>)
    mat1 = np.genfromtxt(nFile, delimiter = "	")
    
    for j in xrange(len(mat1)) :
        
            user = mat1[j][0] - 1
            film = mat1[j][1] - 1
            rating = mat1[j][2]
            
            mat[user][film] = rating
    
    return np.matrix(mat)
    
def check_data(nFile) :
    
    mat1 = np.genfromtxt(nFile, delimiter = "	", dtype = int)
    
    users = -1
    items = -1
    
    for j in xrange(len(mat1)) :
        
        if mat1[j][0] > users:
            
            users = mat1[j][0]
            
        if mat1[j][1] > items:
            
            items = mat1[j][1]
    
    return (users, items)

def remplissage_moyenne_user(mat_ui) :
    
    H = mat_ui.shape[0]
    L = mat_ui.shape[1]
    
    mt = np.mat(np.zeros( (H,L) ))
    
    for l in xrange(H) :
        
        N, S = (0.0,0.0)
        
        for it in xrange(L) :
            
            
            if mat_ui[l, it] <> 0 :
                
                N += 1
                S += mat_ui[l, it]
        
        mean =  S/N if N <> 0 else 0;
        
        
        for it in xrange(L) :
            
            if mat_ui[l, it] == 0 :
                
                mt[l,it] = mean
                
            else :
                
                mt[l,it] = mat_ui[l,it]
    
    return mt


def remplissage_moyenne_film(mat_ui) :
    
    H = mat_ui.shape[0]
    L = mat_ui.shape[1]
    
    mt = np.mat(np.zeros( (H,L) ))
    
    for it in xrange(L) :
        
        N, S = (0.0,0.0)
        
        for l in xrange(H) :
            
            if mat_ui[l, it] <> 0 :
                
                N += 1
                S += mat_ui[l, it]
        
        mean =  S/N if N <> 0 else 0;
        
        
        for l in xrange(H) :
            
            if mat_ui[l, it] == 0 :
                
                mt[l,it] = mean
                
            else :
                
                mt[l,it] = mat_ui[l,it]
    
    return mt
