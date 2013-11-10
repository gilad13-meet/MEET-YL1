a = raw_input("word?")
v=0
list= []
for x in xrange(len(a)):
	list.append(a[x])
	v+=1
if v/2!=v/2.0:
	v-=1
bool = True
print v
for l in xrange(v/2):
	if list[l] != list[-l-1]:
		bool = False
print bool
