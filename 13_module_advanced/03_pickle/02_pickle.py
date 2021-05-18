import pickle
dic = {'name':'admin', 'password':123}
pickle.dump(dic, open('d.data', mode='wb'))

print(pickle.load(open('d.data', mode='rb')))
