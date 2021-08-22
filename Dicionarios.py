#!/usr/bin/env python
# coding: utf-8

# In[5]:


# dicionários são estruturas de "chave - elemento"

dicionario1 = {}

dicionario1['maca'] = 'é uma fruta'
dicionario1['carro'] = 'é um veículo'
dicionario1['ovo'] = 'veio da galinha'
print (dicionario1)


# In[7]:


# você pode imprimir apenas 1 elemento chamando pela chave

print (dicionario1['maca'])


# In[8]:


# você pode deletar um elemento usando a chave

del dicionario1['ovo']

print (dicionario1)


# In[9]:


# você pode alterar um valor usando a chave

dicionario1['maca'] = 'é uma fruta gostosa'
print (dicionario1['maca'])

