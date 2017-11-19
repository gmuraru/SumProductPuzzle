#! /usr/bin/python                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                  
import itertools                                                                                                                                                                                                                                                                  
import collections                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                  
tuples = set(itertools.combinations(range(2, 100), 2))                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                  
prods = collections.defaultdict(list)                                                                                                                                                                                                                                             
sums = collections.defaultdict(list)                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                  
# Generate all possible sums and prods                                                                                                                                                                                                                                            
# prods[product] keep all possible tuples that could generate that product                                                                                                                                                                                                        
# sums[sum] keep all possible tuples that could generate that sum                                                                                                                                                                                                                 
for i, j in tuples:                                                                                                                                                                                                                                                               
    prods[i * j].append((i, j))                                                                                                                                                                                                                                                   
    sums[i + j].append((i, j))                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                  
remain_pairs = set()                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                  
# Select only specific tuples                                                                                                                                                                                                                                                     
# S = a + b                                                                                                                                                                                                                                                                       
# For a given S check that all possible "a" and "b" do not generate a unique                                                                                                                                                                                                      
# product                                                                                                                                                                                                                                                                         
for _, elem in sums.iteritems():                                                                                                                                                                                                                                                  
    if all(len(prods[x * y]) > 1 for x, y in elem):                                                                                                                                                                                                                               
        for tup in elem:                                                                                                                                                                                                                                                          
            remain_pairs.add(tup)                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                  
# Both players have this information                                                                                                                                                                                                                                              
remain_prod = collections.defaultdict(list)                                                                                                                                                                                                                                       
unique_prod = set()                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                  
# Possible candidates for the product                                                                                                                                                                                                                                             
for i, j in remain_pairs:                                                                                                                                                                                                                                                         
    remain_prod[i * j].append((i, j))                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                  
# The product he has is unique - Mr. P knows the value of the product and                                                                                                                                                                                                         
#can check it directly with the values                                                                                                                                                                                                                                            
for key, elem in remain_prod.iteritems():                                                                                                                                                                                                                                         
    if len(remain_prod[key]) == 1:                                                                                                                                                                                                                                                
        unique_prod.add(elem[0])                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                  
# Mr. S knows only the unique values for the product                                                                                                                                                                                                                              
#But he could try generating all the sums (the terms of the sum would have                                                                                                                                                                                                        
#the product equal with one unique value form the previously found list)                                                                                                                                                                                                          
remain_sum = collections.defaultdict(list)                                                                                                                                                                                                                                        
unique_sum = set()                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                  
# Mr. S must only find the unique value - check with his value                                                                                                                                                                                                                    
for i, j in unique_prod:                                                                                                                                                                                                                                                          
    remain_sum[i+j].append((i, j))                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                  
for key, elem in remain_sum.iteritems():                                                                                                                                                                                                                                          
    if len(remain_sum[key]) == 1:                                                                                                                                                                                                                                                 
        unique_sum.add(elem[0])                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                  
print ("Found value {}".format(unique_sum))     
