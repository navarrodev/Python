#!/usr/bin/env python
# coding: utf-8

# In[5]:


# listas são coleções não homogeneas de dados (os dados não são do mesmo tipo)

lista1 = [10, 'eu sou legal', 13.5]

print(lista1)


# In[6]:


# posso imprimir um elemento por vez

print(lista1[1])


# In[7]:


# posso ainda atualizar um valor na lista

print(lista1[1])
lista1[1] = 'eu sou muito legal demais'
print(lista1[1])


# In[10]:


# posso eliminar o ultimo elemento da lista com a função pop()
lista2 = [10,20,30,40]
lista2.pop()
print (lista2)


# In[11]:


# ou também posso eliminar um elemento especifico da lista com o operador del

lista3 = [10,20,30,40,50,60]

del lista3[2]
print(lista3)


# In[12]:


# posso percorrer a lista com um for

for index in range (0,len(lista3)):
    print(lista3[index])


# In[25]:


# posso definir uma lista de listas

matriz = [[10,20,30],[40,50,60],[70,80,90]]

print (matriz)

for i in range(0,3):
    print('\n')
    for j in range(0,3):
        print(matriz[i][j], '-' ,end="")

