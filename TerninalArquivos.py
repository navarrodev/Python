#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Entrada e saida são as operações mais básicas da programação
# A saída é feita com o comando print()
# agora veremos a entrada

entrada1 = input('Digite um numero:')
numero1 = int(entrada1)

entrada2 = input('Digite um numero:')
numero2 = int(entrada2)

print('O resultado é:', numero1+numero2)


# In[2]:


ano1 = '1980'
ano2 = '1990'
ano3 = '2000'
ano4 = '2010'

texto = "Alterando o valor de sep"
print(texto)
print(ano1, ano2, ano3, ano4, sep='--->')


# In[3]:


# pula uma linha
print()

texto = "Alterando o valor de sep e end"
print(texto)
print(ano1, ano2, ano3, ano4, sep='--->', end='...\n')


# In[5]:


# é possível ainda escrever um texto em um arquivo

entrada3 = input('Digite algo para colocar no arquivo')

with open('arquivo.txt', 'w') as f:
    f.write(entrada3)
    
with open('arquivo.txt', 'r') as f:
    print(f.read())
    
    

