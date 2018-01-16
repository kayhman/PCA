import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
labels = ['sepal length', 'sepal width', 'petal length', 'petal width']
for xx in range(4):
    for yy in range(4):
        if yy > xx:
            print xx, yy
            plt.xlabel(labels[xx])
            plt.ylabel(labels[yy])            
            plt.scatter(iris.data[y==0][:, xx], iris.data[y==0][:,yy])
            plt.scatter(iris.data[y==1][:, xx], iris.data[y==1][:,yy])
            plt.scatter(iris.data[y==2][:, xx], iris.data[y==2][:,yy])
            plt.show()

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Percentage of variance explained for each components
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')

plt.show()
