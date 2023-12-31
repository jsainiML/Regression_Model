# Following is creation of dataset with some random values.  

wieghts = 0.4
bias = 0.2 
start = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim=1)              # We are just adding extra dimnension with .unsqueeze(dim=1)
y = wieghts*X + bias


# creating split Train/Test data set with 80-20 ratio

train_split = int(0.8 * len(X))
X_train,  y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:],   y[train_split:]

len(X_train), len(y_train), len(X_test), len(y_test)
