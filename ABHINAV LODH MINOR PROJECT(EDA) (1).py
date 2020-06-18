#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("C:/Users/DELL/Downloads/StudentsPerformance.csv")


# In[4]:


data.head()


# In[7]:


data.tail()


# In[7]:


data.columns.tolist()


# In[15]:


data.dtypes


# In[15]:


data.shape


# In[16]:


data.describe()


# In[17]:


data.nunique()


# In[19]:


data.isnull().sum()


# In[6]:


student=data


# In[7]:


student.head()


# In[106]:


student.tail()


# In[12]:


student.corr()


# In[10]:


corelation = student.corr()
sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)


# In[60]:


plt.figure(figsize=(15,20))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(321)
sns.scatterplot(x='math score', y='reading score', hue='gender', data=student)

plt.subplot(322)
sns.scatterplot(x='math score', y='reading score', hue='race/ethnicity', data=student)

plt.subplot(323)
sns.scatterplot(x='math score', y='reading score', hue='parental level of education', data=student)

plt.subplot(324)
sns.scatterplot(x='math score', y='reading score', hue='lunch', data=student)

plt.subplot(325)
sns.scatterplot(x='math score', y='reading score', hue='test preparation course', data=student)


# In[61]:


plt.figure(figsize=(15,20))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(321)
sns.scatterplot(x='math score', y='writing score', hue='gender', data=student)

plt.subplot(322)
sns.scatterplot(x='math score', y='writing score', hue='race/ethnicity', data=student)

plt.subplot(323)
sns.scatterplot(x='math score', y='writing score', hue='parental level of education', data=student)

plt.subplot(324)
sns.scatterplot(x='math score', y='writing score', hue='lunch', data=student)

plt.subplot(325)
sns.scatterplot(x='math score', y='writing score', hue='test preparation course', data=student)


# In[62]:


plt.figure(figsize=(15,20))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(321)
sns.scatterplot(x='reading score', y='writing score', hue='gender', data=student)

plt.subplot(322)
sns.scatterplot(x='reading score', y='writing score', hue='race/ethnicity', data=student)

plt.subplot(323)
sns.scatterplot(x='reading score', y='writing score', hue='parental level of education', data=student)

plt.subplot(324)
sns.scatterplot(x='reading score', y='writing score', hue='lunch', data=student)

plt.subplot(325)
sns.scatterplot(x='reading score', y='writing score', hue='test preparation course', data=student)


# In[75]:


plt.rcParams['figure.figsize']=(20,10)
sns.countplot(student['math score'])


# In[76]:


plt.rcParams['figure.figsize']=(20,10)
sns.countplot(student['reading score'])


# In[77]:


plt.rcParams['figure.figsize']=(20,10)
sns.countplot(student['writing score'])


# In[40]:


sns.distplot(student['math score'],hist_kws=dict(edgecolor='k',linewidth=1))
print('Minimum marks in maths is',student['math score'].min())
print('Minimum marks in maths is',student['math score'].max())


# In[43]:


sns.distplot(student['reading score'],hist_kws=dict(edgecolor='k',linewidth=1))
print('Minimum marks in reading score is',student['reading score'].min())
print('Minimum marks in reading score is',student['reading score'].max())


# In[42]:


sns.distplot(student['writing score'],hist_kws=dict(edgecolor='k',linewidth=1))
print('Minimum marks in writing score is',student['writing score'].min())
print('Minimum marks in writing score is',student['writing score'].max())


# In[48]:


sns.catplot(x='math score', kind='box',data=student)
Q1=student['math score'].quantile(0.25)
Q3=student['math score'].quantile(0.75)
IQR=Q3-Q1
Median=student['math score'].median()
print('Q1 value is',Q1)
print('Median value is',Median)
print('Q3 value is',Q3)
print('Upper whisker is',(Q3+1.5*IQR))
print('Lower whisker is',(Q1-1.5*IQR))


# In[26]:


sns.catplot(x='reading score', kind='box',data=student)
Q1=student['reading score'].quantile(0.25)
Q3=student['reading score'].quantile(0.75)
IQR=Q3-Q1
Median=student['reading score'].median()
print('Q1 value is',Q1)
print('Median value is',Median)
print('Q3 value is',Q3)
print('Upper whisker is',(Q3+1.5*IQR))
print('Lower whisker is',(Q1-1.5*IQR))


# In[50]:


sns.catplot(x='writing score', kind='box',data=student)
Q1=student['writing score'].quantile(0.25)
Q3=student['writing score'].quantile(0.75)
IQR=Q3-Q1
Median=student['writing score'].median()
print('Q1 value is',Q1)
print('Median value is',Median)
print('Q3 value is',Q3)
print('Upper whisker is',(Q3+1.5*IQR))
print('Lower whisker is',(Q1-1.5*IQR))


# In[8]:


sns.violinplot(student['math score'])


# In[54]:


sns.violinplot(student['reading score'])


# In[55]:


sns.violinplot(student['writing score'])


# In[39]:


sns.jointplot(x = "math score", y ="reading score", data=student)
sns.jointplot(x = "math score", y ="writing score", data=student)
sns.jointplot(x = "reading score", y ="writing score", data=student)


# In[ ]:


#Observation from above plots

#MATH SCORE
#1.Highest score= 100
#2.Lowest score= 0
#3.Maximum student scored 65 

#READING SCORE
#1.Highest score= 100
#2.Lowest score= 17
#3.Maximum student scored 72 

#WRITING SCORE
#1.Highest score= 100
#2.Lowest score= 10
#3.Maximum student scored 74


# In[40]:


plt.figure(figsize=(20,10))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(141)
plt.title('Gender', fontsize=20)
student['gender'].value_counts().plot.pie(autopct="%1.1f%%")

plt.subplot(142)
plt.title('Race/Ethnicity', fontsize=20)
student['race/ethnicity'].value_counts().plot.pie(autopct="%1.1f%%")

plt.subplot(143)
plt.title('Parental Level of Education', fontsize=20)
student['parental level of education'].value_counts().plot.pie(autopct="%1.1f%%")

plt.subplot(144)
plt.title('Lunch', fontsize=20)
student['lunch'].value_counts().plot.pie(autopct="%1.1f%%")


# In[ ]:


#Observation from above plot

#1.There are more females in class.
#2.Students from group C is most and group A is least.
#3.Percentage of parents who attented some college is most and who attented master's degree is least.
#4.More student have standard lunch.


# In[53]:


print(student.gender.value_counts())
student.gender.value_counts().plot(kind='bar')


# In[56]:


print(student['race/ethnicity'].value_counts())
student['race/ethnicity'].value_counts().plot(kind='bar')


# In[57]:


print(student['parental level of education'].value_counts())
student['parental level of education'].value_counts('parental level of education').plot(kind='bar')


# In[58]:


print(student['lunch'].value_counts())
student['lunch'].value_counts('parental level of education').plot(kind='bar')


# In[59]:


print(student['test preparation course'].value_counts())
student['test preparation course'].value_counts('parental level of education').plot(kind='bar')


# In[66]:


plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(131)
plt.title("Math Score")
sns.barplot(x='gender',y='math score', data=student)

plt.subplot(132)
plt.title("Reading Score")
sns.barplot(x='gender',y='reading score', data=student)

plt.subplot(133)
plt.title("Writing Score")
sns.barplot(x='gender',y='writing score', data=student)


# In[ ]:


#Observation from above curve

#1.Male scored better in Math.
#2.Females scored better in Reading.
#3.Females scored better in Writing.


# In[67]:


plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(131)
plt.title("Math Score")
sns.barplot(x='race/ethnicity',y='math score', data=student)


plt.subplot(132)
plt.title("Reading Score")
sns.barplot(x='race/ethnicity',y='reading score', data=student)

plt.subplot(133)
plt.title("Writing Score")
sns.barplot(x='race/ethnicity',y='writing score', data=student)


# In[ ]:


#Observation from above plot

#1.Students from group E score more in Math.
#2.Students from group E score more in Reading.
#3.Students from group E score more in Writing.


# In[72]:


plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=0.2)

plt.subplot(131)
plt.title("Math Score")
sns.barplot(x='lunch',y='math score', data=student)


plt.subplot(132)
plt.title("Reading Score")
sns.barplot(x='lunch',y='reading score', data=student)

plt.subplot(133)
plt.title("Writing Score")
sns.barplot(x='lunch',y='writing score', data=student)


# In[ ]:


#Observation from above plot

#1.More students with standard lunch scored more in math.
#2.More students with standard lunch scored more in reading.
#3.More students with standard lunch scored more in writing.


# In[83]:


plt.figure(figsize=(35,8))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=1)

plt.subplot(131)
plt.title("Math Score")
sns.barplot(x='parental level of education',y='math score', data=student)

plt.subplot(132)
plt.title("Reading Score")
sns.barplot(x='parental level of education',y='reading score', data=student)

plt.subplot(133)
plt.title("Writing Score")
sns.barplot(x='parental level of education',y='writing score', data=student)


# In[ ]:


#Observation from above plot
#Students whose parents attented master's degree have scored most in all math, reading and writing.
#Students whose parents attented high score have scored  in least all math, reading and writing.


# In[85]:


plt.figure(figsize=(20,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.5,hspace=1)

plt.subplot(131)
plt.title("Math Score")
sns.barplot(x='test preparation course',y='math score', data=student)

plt.subplot(132)
plt.title("Reading Score")
sns.barplot(x='test preparation course',y='reading score', data=student)

plt.subplot(133)
plt.title("Writing Score")
sns.barplot(x='test preparation course',y='writing score', data=student)


# In[ ]:


#Observation from above plot

#1.Students who have completed test preparation course scored more in Math.
#2.Students who have completed test preparation course scored more in Reading.
#3.Students who have completed test preparation course scored more in Writing.


# In[86]:


plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)
plt.subplot(131)
plt.title('Math Scores')
sns.barplot(hue="gender", y="math score", x="test preparation course", data=student)
plt.subplot(132)
plt.title('Reading Scores')
sns.barplot(hue="gender", y="reading score", x="test preparation course", data=student)
plt.subplot(133)
plt.title('Writing Scores')
sns.barplot(hue="gender", y="writing score", x="test preparation course", data=student)


# In[ ]:


#Observation from above plot

#1.More male who have not taken test preparation course scored more in math
#   More male who have completed taken test preparation course scored more in math

#2.More female who have not taken test preparation course scored more in reading
#   More female who have completed taken test preparation course scored more in reading
 
#3.More female who have not taken test preparation course scored more in writing
#   More female who have completed taken test preparation course scored more in writing
    


# In[87]:


plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)
plt.subplot(131)
plt.title('Math Scores')
sns.barplot(x="race/ethnicity", y="math score", hue="test preparation course", data=student)
plt.subplot(132)
plt.title('Reading Scores')
sns.barplot(hue="test preparation course", y="reading score", x="race/ethnicity", data=student)
plt.subplot(133)
plt.title('Writing Scores')
sns.barplot(hue="test preparation course", y="writing score", x= 'race/ethnicity',data=student)


# In[8]:


#Observation from above plot

#Students from group A who have attented test preparation course have scored more in all subjects than those who haven't.
#Students from group B who have attented test preparation course have scored more in all subjects than those who haven't.
#Students from group C who have attented test preparation course have scored more in all subjects than those who haven't.
#Students from group D who have attented test preparation course have scored more in all subjects than those who haven't.
#Students from group E who have attented test preparation course have scored more in all subjects than those who haven't.


# In[88]:


plt.figure(figsize=(30,15))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)
plt.subplot(251)
plt.title('Test Preparation course Vs Gender',fontsize = 15)
sns.countplot(hue="test preparation course", x="gender", data=student)

plt.subplot(254)
plt.title('Test Preparation course Vs Parental Level Of Education',fontsize = 15)
sns.countplot(hue="test preparation course", y="parental level of education", data=student)

plt.subplot(253)
plt.title('Test Preparation course Vs Lunch',fontsize = 15)
sns.countplot(hue="test preparation course", x="lunch", data=student)

plt.subplot(252)
plt.title('Test Preparation course Vs Ethnicity',fontsize = 15)
sns.countplot(hue="test preparation course", y="race/ethnicity", data=student)


# In[9]:


plt.figure(figsize=(30,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)

plt.subplot(141)
plt.title('Gender Vs Ethnicity',fontsize = 15)
sns.countplot(x="gender", hue="race/ethnicity", data=student)

plt.subplot(142)
plt.title('Gender Vs Parental Level of Education',fontsize = 15)
sns.countplot(x="gender", hue="parental level of education", data=student)


# In[100]:


plt.figure(figsize=(30,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)

plt.subplot(141)
plt.title('Gender Vs Lunch',fontsize = 15)
sns.countplot(x="gender", hue="lunch", data=student)

plt.subplot(142)
plt.title('Gender Vs Test preparation course',fontsize = 15)
sns.countplot(x="gender", hue="test preparation course", data=student)


# In[ ]:


#Observation from above plot

#More females are there who have standard lunch than the females who have free/reduced lunch.
#More males are there better who have standard lunch than the males who have free/reduced lunch.

#More females with test preparation course are there than females who have not attended.
#More males with test preparation course are there than males who have not attended.


# In[102]:


plt.figure(figsize=(30,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)

plt.subplot(141)
plt.title('Ethnicity Vs Parental Level of Education',fontsize = 15)
sns.countplot(x="race/ethnicity", hue="parental level of education", data=student)

plt.subplot(142)
plt.title('Ethnicity Vs Lunch',fontsize = 15)
sns.countplot(x="race/ethnicity", hue="lunch", data=student)


# In[ ]:


#Observation from above table 

#From group A, students whose parent attented :
#1.master's degree is least
#2.some high school is most

#From group B, students whose parent attented :
#1.master's degree is least
#2.high school is most

#From group C, students whose parent attented :
#1.master's degree is least
#2.associates degree is most

#From group D, students whose parent attented :
#1.master's degree is least
#2.some college is most

#From group E, students whose parent attented :
#1.master's degree is least
#2.associates degree is most


# In[15]:


plt.figure(figsize=(30,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)

plt.subplot(141)
plt.title('Ethnicity Vs Test Preparation course',fontsize = 15)
sns.countplot(x="race/ethnicity", hue="test preparation course", data=student)

plt.subplot(142)
plt.title('Parental Level of Education Vs Lunch',fontsize = 15)
sns.countplot(x="parental level of education", hue="lunch", data=student)


# In[66]:


plt.figure(figsize=(50,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)

plt.subplot(141)
plt.title('Parental Level of Education Vs Test Preparation course',fontsize = 25)
sns.countplot(x="parental level of education", hue="test preparation course", data=student)

plt.subplot(142)
plt.title('Lunch Vs Test Preparation course',fontsize = 25)
sns.countplot(x="parental level of education", hue="test preparation course", data=student)


# In[ ]:




