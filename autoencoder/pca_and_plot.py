import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn import decomposition
from sklearn import datasets

np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
data = np.load('test_data_encoder_output.share_weight.npy')
#data, _ = np.split(data, [1000], axis=0)
print data.shape
y, X = np.split(data, [2], axis=1)
print y.shape
y, _ = np.split(y, [1], axis=1)
y = np.squeeze(y).astype(np.int)
fig = plt.figure(1, figsize=(4, 3))
plt.clf()
plt.cla()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
X = X / np.linalg.norm(X)
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
print X.shape
print y.shape

for name, label in [('male', 1), ('female', 0)]:
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean(),
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
print type(y[0])
y = np.choose(y, [1, 0]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.spectral)

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])


#plt.plot(X[y == 1, 0], X[y == 1, 1], 'bo')
#plt.plot(X[y == 0, 0], X[y == 0, 1], 'go')
plt.show()
