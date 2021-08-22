#!/usr/bin/env python
# coding: utf-8

# In[1]:


# operador se

num = 8
if num==8:
    print('legall')


# In[3]:


# operador então

num = 9
if num==9:
    print('legall')
else:
    print('mais legal')


# In[4]:


# encadeamento de If's

notadoaluno = 4

if notadoaluno > 9:
    print('ele é um gênio!')
elif notadoaluno < 9:
    if notadoaluno > 5:
        print ('nota regular')
    else:
        print('nota ruim')


# In[1]:


# igualdade, maior e menor, etc...
# == Igual
# != Diferente 
# > Maior que
# < Menor que
# >= Maior ou igual que
# <= Menor ou igual que

num = 5

if(num == 5):
    print('verdade')

if num > 2:
    print('verdade')
    
if num < 10:
    print('é menor que 10')


# In[10]:


# operador lógico E

num1 = 2
num2 = 4

if num1 == 2 and num2 == 4:
    print('os numeros são iguais a 2 e 4')
else:
    print('os numeros não são iguais a 2 e 4')
    


# In[14]:


# operador lógico OR

nome = "cristiano"
time = "juventus"


if nome == "cristiano" or time == 'juventus' :
    print('ele joga bem')
else:
    print('não sei quem é')


# In[6]:


# operador lógico NOT

afirmacao = 'verdade'

#proposicao sem o not

if (afirmacao == 'verdade') :
    print('é verdade')
else:
    print('não é verdade')

#proposicao com o not
    
if not (afirmacao == 'verdade') :
    print('é verdade')
else:
    print('não é verdade')

