import shelve

s = shelve.open("test")
s['key'] = "ishaan"
print s['key']
s['key'] = "ishaan1111"
print s['key']
s.close()
