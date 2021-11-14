import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def my_autopct(pct):
    return ('%.2f%%' % pct) if pct > 2 else ''

df = pd.read_csv('aug_test.csv')

print(df['gender'].value_counts()/df['gender'].count()*100)   #Gender statistics


print(df.groupby('education_level')['training_hours'].mean())  #Average of training hours by education level

eduLvl = df.groupby('education_level')['training_hours'].mean() #Bar Chart to compare training averages
eduSorted = ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd']
eduLvl.plot(kind = 'bar', color = 'orange')
plt.ylabel('Training Hours Avg')
plt.title('Education Level Average Training Hours')

plt.show()


print(df['city_development_index'].value_counts().nlargest(3)) #Top 3 city indexs with applicants

cityPie = df['city'].value_counts() #Pie Chart setup for see city relevance in data
cityPie.plot(kind='pie', subplots=True, autopct=my_autopct, shadow=True, startangle=270)
plt.title("Percentages of Most Common Cities")
plt.legend(df['city'].value_counts().nlargest(10), loc = 'right',bbox_to_anchor=(1.35, 0.5), frameon=False)
plt.ylabel("")

plt.show()




