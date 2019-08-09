#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:35:02 2019

@author: jnikhil
required packages numpy, cv2, scipy, sklearn, kneed, matplotlib 

"""
import numpy as np
import cv2
import matplotlib.pyplot as plt 
from scipy import ndimage
from sklearn.cluster import KMeans
from kneed import KneeLocator
import argparse
import sys
    
class Segment_Class:
    
    
    '''
    This is class with methods for segmenting the image using k means clustering method
    It clusters, or partitions the image into k-clusters or parts based on the k-centroid
    This class two methods kmeans and object_exctraction
    
    kmeans:
           input paras:image 
           returns: (M,N,3) clusted ouput array and (M,N) labeled array

    object_exctraction:
           input paras:i(M,N,3) image, (M,N) labeled array and label to be extracted
           returns: (M,N,3) array with values corresponding to given label 
    '''
    
    def __init__(self,clusters=4):
        #number of clusters default is 4
        self.clusters = clusters
   
    def kmeans(self,image):
        picture = cv2.GaussianBlur(image,(3,3),0)      # filter size 
        picture = picture.astype(int)
        picture_n = picture.reshape(picture.shape[0]*picture.shape[1], picture.shape[2])
        
        kmeans = KMeans(n_clusters=self.clusters, random_state=0).fit(picture_n)
        labels = kmeans.predict(picture_n)
        seg_pic = kmeans.cluster_centers_[kmeans.labels_]
        cluster_pic = seg_pic.reshape(picture.shape[0], picture.shape[1], picture.shape[2])
        cluster_pic = cluster_pic.astype(int)
        labels_pic = labels.reshape(picture.shape[0], picture.shape[1])
        
        return (cluster_pic,labels_pic)

    def object_exctraction(self,image,label_pic,label):
        output_pic = np.zeros(image.shape,np.uint8)
        
        output_pic[label_pic==label] = image[label_pic==label]
        
        return output_pic

def main():

    image = plt.imread(path)
    picture_n = image.reshape(image.shape[0]*image.shape[1], image.shape[2])

    s2=Segment_Class(K)        # number of clusters K 
    seg_img,label_img = s2.kmeans(image)
     
    print("\nQuantized/ Segmented Image:\n")
    seg_img=seg_img.astype(np.uint8)
    print("\nClose the figure to proceed\n")
    plt.imshow(seg_img)
    plt.show()
              
    # Command Line Input from users
    char = (input('\n\nDo you want view segmented image for specific label (Y/N):'))
    
    while((char != 'N')):  
       
        if (char == 'Y'):    
            print("Enter the specific label from 0 to " + str(K-1) + ":")
            L = int(input(''))
                
            if (0 <=L and L< K):
                output_img = s2.object_exctraction(image,label_img,label=L)
                output_img=output_img.astype(np.uint8)
                print("\nClose the figure to proceed\n")
                plt.imshow(output_img)
                #plt.figure(figsize=(10,8))
                plt.show()
                
            else:
                print("You have entered wrong label")       
    
            char = input('Do you want to view for another label (Y/N): ')
            
        else:   
            char = (input('Type Y or N:'))
            
if __name__=="__main__":
    
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Enter Path to the image")
    ap.add_argument("-n", "--clusters", required = False, type = int,
        help = "Number of clusters K you wish image to be segmented into(default value of K is 4)")
    args = vars(ap.parse_args())
    
    path=args["image"]
    if len(sys.argv)==3:
        K=4
       
    else:
        K=args["clusters"]
    
    main()
