#!/usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np
import matplotlib.pyplot as plt

class show :

  def __init__(self) :

    self.Nfig = 0
    self.square = False
    self.interpolation = "none"

  def draw_mat(self, matrices) :


    self.Nfig = len(matrices)

    plt.figure(figsize=(20,10))
    
    if not self.square :

      for i in xrange(len(matrices)) :

        plt.subplot(1,self.Nfig,i)
        plt.imshow(matrices[i], interpolation = self.interpolation)


    else :

      n = int((self.Nfig)**0.5) + 1

      for i in xrange(len(matrices)) :

        plt.subplot(n,n,i)
        plt.imshow(matrices[i], interpolation = self.interpolation)


  def show(self) :

    plt.show()
