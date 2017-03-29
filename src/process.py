# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 03:58:28 2015

@author: Naman
"""
from collections import defaultdict

def categorize(chars):
    hand_a=lr(chars[0])
    hand_b=lr(chars[2])
    category={('l',False,'r',False):1,('l',True,'r',True):1,
              ('r',False,'l',False):2,('r',True,'l',True):2,
              ('l',False,'r',True):3,
              ('l',True,'r',False):4,
              ('r',False,'l',True):5,
              ('r',True,'l',False):6,
              ('l',False,'l',True):7,('l',True,'l',False):7,
              ('r',False,'r',True):8,('r',True,'r',False):8,
              ('l',False,'l',False):9,('l',True,'l',True):9,
              ('r',False,'r',False):10,('r',True,'r',True):10}
              
    category=defaultdict(lambda: 0,category)          
    
    return category[hand_a,chars[1],hand_b,chars[3]]
    
    
    
def lr(x):
    
    dict={82:'l',88:'l',70:'l',83:'l',85:'l',66:'l',84:'l',69:'l',
          71:'l',72:'l',91:'l',89:'l',68:'l',87:'l',67:'l',50:'l',51:'l',52:'l',53:'l',54:'l',193:'l',
          90:'r',86:'r',74:'r',80:'r',81:'r',220:'r',222:'r',73:'r',75:'r',76:'r',77:'r',
          187:'r',223:'r',79:'r',78:'r',189:'r',191:'r',192:'r',55:'r',56:'r',57:'r',58:'r',
          49:'r',190:'r',188:'r',
          10:'b', 14:'E', 33:'S'
          }
    return dict.get(x,'n')
    
    
def lr_holdtime(x):
    
    category={('l',False):1,('r',False):2,('l',True):3,('r',True):4,('E',False):5,('E',True):5,
              ('S',False):6,('S',False):6 
             }
    
    category=defaultdict(lambda: 0,category)
    
    return category[lr(x[0]),x[1]]
