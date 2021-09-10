# homework
import re
import pandas as pd 
import numpy as np
df= pd.read_csv('dataset.csv')
print(df)
df_make=df.loc[(df['Make']=='BMW')]
print(df_make)

df_make.to_csv('bmw.csv'   )
df_bmw = pd.read_csv('bmw.csv')
print(df_bmw)
cols = list(df.columns.values)
df_mean=df_bmw[cols[-1]]
print(df_mean)
df_msrp=df_mean.mean()
print(df_msrp)# fuck you mean it took me a whole hours for this
print(df)
import re 
df_year=(df[df['Year']>=2015])

print(df_year)
df_year.to_csv('missing_Hp.csv')
print(df_year)
print(df_year.isnull().sum())
df_the_ones_with_no_hp =df_year[df_year['Engine HP'].isnull().values]# took another 3 hours oooh god!!!!!!!!!!!!!!!
print(df_the_ones_with_no_hp)
#so take away if if you want a comparion not to give you just true or false things just do ths dataframename[dataframename again[your nyanya vitungu hapa ndani just like the above line]]
print(df)
df_the_ones_with_no_hp_all = df[df['Engine HP'].isnull().values]
print(df_the_ones_with_no_hp_all)
df_mean_hp =df[cols[-1]].mean()
print(df_mean_hp)
print(df_the_ones_with_no_hp_all.fillna(df_mean_hp))
df_the_ones_with_no_hp.to_csv('updated_hp.csv')
print(df_the_ones_with_no_hp_all.isnull().sum())
df_mean_after=df[cols[-1]].mean()
print(df_mean_after)

df_RR=df.loc[(df['Make']=='Rolls-Royce')]
print(df_RR)
df_RR2=df_RR[['Engine HP','Engine Cylinders','highway MPG']]
print(df_RR2 )
df_RR3=df_RR2.drop_duplicates()
print(df_RR3)
x=df_RR3.values
print(x)
a=x.T
xtx=a.dot(x)
print(xtx)

xtx_inv =np.linalg.inv(xtx)
print(xtx_inv)
def matrix_matrix_multiplication(a,x):
	assert a.shape[1]==x.shape[0]
	n= a.shape[0]
	m= x.shape[1]
	result = np.zeroes(n,m)

	for i in range(m):
		m1 = x[:,1]
		am1  =matrix_matrix_multiplication(a,m1)

		result[:,1]=am1

		return result

		print(matrix_matrix_multiplication) 

# so for an identity matrx we use np.eye(the number you want )

#xtx = a*x
#print(xtx)


y=np.array([1000,1100,900,1200,1000,850,1300])
z=xtx_inv.dot(a)
w=z.dot(y)

print(w)

