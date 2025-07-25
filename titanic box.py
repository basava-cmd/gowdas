import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
titanic = titanic.dropna(subset=['age', 'survived'])
sns.boxplot(x='survived', y='age', data=titanic)

plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Age')
plt.title('Boxplot of Age by Survival on the Titanic')
plt.show()
