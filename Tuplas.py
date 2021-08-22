#!/usr/bin/env python
# coding: utf-8

# In[4]:


# tuplas são listas, porém são imutáveis

tupla = (12, 'string', 13.7, 'outra string')
print(tupla)

#posso imprimir um elemento só da tupla 
print ('elemento 2: ', tupla[2])


# In[5]:


# posso juntar duas tuplas

tupla1 = (10, 'string')
tupla2 = (20, 'mais uma')

tupla3 = tupla1 + tupla2

print(tupla3)


# In[6]:


# Se tentarmos mudar uma tupla ocorrerá um erro
tupla4 = (10, 20, 30)
tupla4[2] = 0


# In[10]:


# posso usar um laço de repetição para percorrer uma tupla

tupla5 = ('primeiro', 'segundo', 'terceiro')

for i in range(0,3):
    print(tupla5[i])

