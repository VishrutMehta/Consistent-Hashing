import bisect
import hashlib

l = []
def get_machine(key):

    h = my_hash(key)
    if h > l[-1][2]: 
    	return l[0][0]
    hash_values = map(lambda y: y[2],l)
    #print hash_values
    index = bisect.bisect_left(hash_values,h)
    return l[index][0]

def my_hash(key):
	ans = (int(hashlib.md5(key).hexdigest(),16) % 1000000)/1000000.0
	return ans

def allocate(mac, rep):
	global l
	for i in range(mac):
		for j in range(rep):
			l.append((i,j,my_hash((str(i)+"_"+str(j)))))

	l.sort(lambda x,y: cmp(x[2],y[2]))

def add_machine(mac, rep):
	global l
	for i in range(rep):
		l.append((mac-1,i,my_hash((str(mac-1)+"_"+str(i)))))

	l.sort(lambda x,y: cmp(x[2],y[2]))

	for (i,j,k) in l:
		print "(%s,    %s,    %s)" % (i,j,k)
	print "\n"	

mac = raw_input("Enter the number of Machines")
rep = raw_input("Enter the number of Replicas")
print "(machine,replica,hash value):"
allocate(int(mac), int(rep))
for (i,j,k) in l: 
	print "(%s,    %s,    %s)" % (i,j,k)
print "\n"	
while True:
	key = raw_input("Please enter a key, or (a) to add machine:")	
	if key == "a":
		mac = int(mac) + 1
		print "New Hash Has Been Alloted"
		add_machine(int(mac), int(rep))
	else:
		print "hash(Key: %s) = %s, Goes to machine %s\n" % (key, my_hash(key), get_machine(key))
