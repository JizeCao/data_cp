import numpy as np
from sklearn import linear_model


# Data requires shape (n_samples, n_features), labels: (n_samples, n_labels)
# Return: defined linear classifier
def LinearRegression(data, labels, ridge=False, lasso=False, alpha=0.1):
    if ridge:
        clf = linear_model.Ridge(alpha=alpha)
    elif lasso:
        clf = linear_model.Lasso(alpha=alpha)
    else:
        clf = linear_model.LinearRegression()

    clf.fit(data, labels)
    print('The coefficient of the classifier', clf.coef_)
    print('The intercept of the classifier', clf.intercept_)
    return clf


if __name__ == '__main__':
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

    y = np.dot(X, np.array([1, 2])) + 3
    # X requires shapes: (n_samples, n_features)
    #
    clf = LinearRegression(X, y, lasso=True, alpha=0.1)


