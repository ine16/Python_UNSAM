from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_dataset = load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

# agrego el atributo 'target' de cada flor al dataframe
iris_dataframe['target'] = iris_dataset['target']


iris_dataframe['target'].replace([0], 'Setosa', inplace = True)
iris_dataframe['target'].replace([1], 'Versicolor', inplace = True)
iris_dataframe['target'].replace([2], 'Virginica', inplace = True)

sns.pairplot(data = iris_dataframe, hue = 'target')
plt.show()