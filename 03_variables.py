'Variables are the containers for storing the data.'
'..... Creating variable......'
a='Python' #string
b=2025      #integer
c=0.151     #float
print(a)    # o/p: Python
print(a,b,c)    # o/p: Python 2025 0.151

d='Python'
d='self-learning' 
# it provide the value of the latest variable so
# Python is overwrite by self-learning.
print(d) # o/p: self-learning

e=2025
e='September'
print(e) # o/p: September


'......casting........'
f=str(71.004)
g=int(0.001)
h=float(20.01)
print(f,g,h)  # o/p:  71.004 0 20.01


'.....getting data type of variables...... '
i=True
j=2.020
k=15
l='Python'
m=['a','b']
n={'a','b'}
o={'car':'bmw'}
p=('learn',)
print(type(i),type(j),type(k),type(l),type(m),type(n),type(o),type(p))