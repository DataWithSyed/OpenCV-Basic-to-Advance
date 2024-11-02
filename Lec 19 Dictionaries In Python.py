d = {'name': 'Taha', 'age': 14, 'Year': 2004}
print(d)
print(d['name'])
print(d["Year"])
# you can store any data type in Key
e = {'name': "Sohail", 'age': 15, 15.56: 'x', 'y' :5**2, 8: (5,8,7,9,3), 'Are u a liar': True}
print(e)
print(e[8])
print(e['y'])
print(e['Are u a liar'])
print(len(e))
print(d.get('name'))
# if you want to assign a key and ots value into a dictionary
e['Boolean']= False
print(e)
# if you want to remove any key from a dictionary
d.pop('name')
print(d)
# if you want to clear the values
print(e.clear())
# update the key of a dictionary
d['Year'] = 2006
print(d)
d.update({'age' : 11})
print(d)
# Keys to list out all the keys of a dictionary
print(d.keys())
# Values to list out all the value of a dictionary
print(d.values())
#if you want to get dictionary value and key in pairs
print(d.items())
# popitem() will remove the last item what you added or updated
print(d.popitem())