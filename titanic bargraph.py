import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic dataset.csv")

class_counts = df['Pclass'].value_counts().sort_index()
plt.bar(['Class 1', 'Class 2', 'Class 3'], class_counts)
plt.title('Number of Passengers by Class')
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.show()
