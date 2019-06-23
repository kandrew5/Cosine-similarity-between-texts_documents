# -*- coding: utf-8 -*-
"""
@author: Andrew Kallistros
"""
from scipy import spatial #library for the cosine similarity
import math #library for factorial function
import string

def main():
    while True:
        try:
            print("How many documents do you want to compare?")
            k=int(input())
        except ValueError: #in case the input is not valid
            print("Not valid option")
            continue
        else: 
            break
    d={}
    splitv={}
    wordv=[]
    documents=[]
    tempv=[]
    for i in range(k):
        print ("Please insert the document name!")
        while True:
            try:
                p=str(input())
                open(p, "r")
            except IOError:  #in case there is no such file
                print ("Error: No such file was found. Try again!.")
                continue
            break
        
        documents.append(p)
        f=open(documents[i], "r")
        d[i]=f.read()
        splitv[i]=(d[i].lower().translate(str.maketrans('', '', string.punctuation)).split())#remove punctuation and Uppercase characters
        y=splitv[i]
        wordv.extend(y) #pros8etw sthn telikh lista oles tis lexeis
   
    wordv=list(dict.fromkeys(wordv))  #afairw ta duplicate ths listas
    #print("This is the list with the dinstinc words from each text")
    #print(wordv)#lista me oles tis lexeis
    
    for i in range(k):
        tempv.clear()
        tempv.extend(splitv[i])
        d1=[0]*len(wordv)#arxikopoioume to d1 me 0
        for x in range(0, len(tempv), 1):
            for y in range(0, len(wordv), 1):
                if tempv[x]==wordv[y]:
                    d1[y]=d1[y]+1 #pros8etei 1 sto antistoixo stoixeio ths listas
        splitv[i]=d1
    #print(splitv) #dictionary pou exei ola ta dianusmata
    A= [[0]*len(splitv) for y in range(0,len(splitv), 1)] #arxikopoioume enan nxn lista
    for i in range(0, len(splitv), 1):
        for x in range(0, len(splitv), 1):
            if (i < x):
                 result = 1-spatial.distance.cosine(splitv[i],splitv[x]) #briskoume to cosine
                 A[i][x]=round(result, 4) #apo8hkeuoume to apotelesma rounded me duo decimals
             
    while True:
        try:
            print("How many pairs do you want to be printed?")
            y=int(input())
        except ValueError:
            print("Not valid option")
            continue
        if y>1: #elegxos an exoume valid ari8mo upologizontas to binomial coefficient
            a = math.factorial(k)
            c = math.factorial(k-2)  # that appears to be useful to get the correct result
            div = a // (2 * c)
            if y>div:
                print("Sorry not enough documents. Try a smaller number")
                continue
            else:
                break
        else:
            break
        
    for z in range(y):
        max=0
        doc1=0
        doc2=0
        i=0
        x=0
        for i in range(k):
            for x in range(k):
                if (A[i][x]>max):
                    max=A[i][x]
                    doc1=i
                    doc2=x


        print("Documents " + documents[doc1] +", "+documents[doc2]+" with similarity: "+ str(max))
        A[doc1][doc2]=0 #erase the biggest similarity
    #we print the documents and their similarity
        
main()