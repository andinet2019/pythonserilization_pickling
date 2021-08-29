import pickle
x = {'a': 1, 'b': 2}
y=[x, 3, x]
x['c']= y
print('x {} \nBefore pickling: {}'.format(x, y))
# creating a binary file called ptest
fi =open('ptest', 'wb')
pickle.dump(y,fi)
# reading the binary file
fi=open('ptest','rb')
# deserializes the contents of ptest
z=pickle.load(fi)
print("After pickling:",z)