#!/usr/bin/env python
# coding: utf-8

# In[35]:


## Definindo uma classe

class Pessoa:

    def __init__(self,nome):
        self.nome = nome

    def anda(self):
        print(self.nome + ': estou andando')

    def fala(self):
        print(self.nome + ': estou falando')
    
    def marcarUmaReuniao(self):
        print("eu sou uma pessoa comum, vamos conversar?")
        
pessoa = Pessoa('astolfo'); 
pessoa.anda(); 
pessoa.fala();


# In[133]:


## Definindo uma classe filha

class Gerente(Pessoa):
    def __init__(self,nome, salario):
        super().__init__(nome)
        self.salario = salario
        self.dataDeNascimento = "dd/mm/yy"
        self.corDosOlhos = "castanhos" #definindo atributos sem inicializando-os porém não colocando no construtor
        self.__sexo = "masculino"
        
    def darUmaOrdem(self):
        print("eu sou o gerente, estou dando uma ordem")
        
    def marcarUmaReuniao(self):
        print("Eu sou o seu gerente, vamos conversar na minha sala em 10 minutos")
        
    


# In[134]:


g1 = Gerente("mario da silva",1000)
print(g1.nome)
print(g1.corDosOlhos)


# In[135]:


# alterando o valor de um atributo

g1.corDosOlhos = "azuis"
print(g1.corDosOlhos)


# In[136]:


#alterando um atributo "privado"

g1.__sexo = "feminino"
print (g1.__sexo)

# Encapsulamento dentro do python é apenas uma convenção... os atributos são privados quando possuem o __, 
# porém eles podem ser acessados.


# In[137]:


#chamando um método da classe pai na classe filha

g1.fala()


# In[138]:


# chamando um método filho apenas

g1.darUmaOrdem()


# In[139]:


# chamando um método sobrecarregado

g1.marcarUmaReuniao()

