import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic dataset.csv")
sex_counts = df['Sex'].value_counts()
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.2f%%')
plt.title('fare Distribution on Titanic')
plt.show()

