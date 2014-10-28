class Transaction:
	# three kinds of transactions:1:range_query, 2: add access point, 3: remove access point
	# 1. range_query
	#	required: lon, lat, distance
	# 2. add_query
	#	required: lon, lat
	# 3. rm_query
	#	required: lon, lat
	
	def __init__(self, lat, lon, kind):
		self.lat = lat
		self.lon = lon
		self.kind = kind
	def getKind(self):
		return self.kind
	def toString(self):
                print "Update Query: lat= "+str(self.lat)+", lon= "+str(self.lon)+", kind(2:add, 3:remove)= "+str(self.getKind())
	#serialize and deserialize is to send bytes at the network because the class is not serializable
	def serialize(self):
		return str(self.kind)+","+str(self.lat)+","+str(self.lon)
	@staticmethod
	def deserialize(string):
		fields=string.split(',')
		if int(fields[0]) != 1: 
			return int(fields[0]),float(fields[1]),float(fields[2])
		else:
			return int(fields[0]),float(fields[1]),float(fields[2]),float(fields[3])

class Search_Transaction(Transaction):
	def __init__(self, lat, lon, distance, kind=1):
		Transaction.__init__(self,lat,lon,kind)
		self.distance=distance
	def toString(self):
		print "Search Query: lat= "+str(self.lat)+", lon= "+str(self.lon)+", distance= "+str(self.distance)
	def serialize(self):
		return str(self.kind)+","+str(self.lat)+","+str(self.lon)+","+str(self.distance)


class Add_Transaction(Transaction):
	def __init__(self, lat, lon, kind=2):
		Transaction.__init__(self,lat,lon,kind)

class Remove_Transaction(Transaction):
	def __init__(self, lat, lon, kind=3):
		Transaction.__init__(self,lat,lon,kind)

# Use List to implement a queue of transactions
class TransactionQueue:
	def __init__(self):
		self.transactions=list()
	def getSize(self):
		return len(self.transactions)

	def add_search(self,lat,lon,distance):
		trans=Search_Transaction(lat,lon,distance)
		self.transactions.append(trans)
	def add_add(self,lat,lon):
		trans=Add_Transaction(lat,lon)
		self.transactions.append(trans)
	def add_remove(self,lat,lon):
		trans=Remove_Transaction(lat,lon)
		self.transactions.append(trans)
	def pop(self):
		if not self.transactions:
			return None
		else:
			trans=self.transactions.pop()
			return trans.serialize()

# manipulate several queues
# it assumes there's file called servermap in current directory telling the IP addresses of the servers
# function with toothers is to add transactions to all the queues except the argv[1] IP
class TransactionQueues:
	def __init__(self):
		servermapFile=open('servermap','r')
		i=0
		# index of ip in servermap corresponds to the index of its queue in queues
		self.servermap=list()
		for line in servermapFile:
			self.servermap.append(line.strip())
		
		num=len(self.servermap)
		self.queues=list()
		for i in range(num):
			self.queues.append(TransactionQueue())
		

	def getSize(self):
		return len(self.queues)
	
	def add_search(self,ip,lat,lon,distance):
		num=self.servermap.index(ip)
		if num>=self.getSize():
			print "Ning Warning:TransactionQueues: index out of bound"
			return None
                queue=self.queues[num]
                queue.add_search(lat,lon,distance)

	def add_search_toothers(self,ip,lat,lon,distance):
		num=self.servermap.index(ip)
		if num>=self.getSize():
			print "Ning Warning:TransactionQueues: index out of bound"
			return None
		for i in range(self.getSize()):
			if i==num:
				continue;
			queue=self.queues[i]
			queue.add_search(lat,lon,distance)


        def add_add(self,ip,lat,lon):
		num=self.servermap.index(ip)
		if num>=self.getSize():
                        print "Ning Warning:TransactionQueues: index out of bound"
                        return None
                queue=self.queues[num]
                queue.add_add(lat,lon)

	def add_add_toothers(self,ip,lat,lon):
		num=self.servermap.index(ip)
		if num>=self.getSize():
			print "Ning Warning:TransactionQueues: index out of bound"
			return None
		for i in range(self.getSize()):
			if i==num:
				continue;
			queue=self.queues[i]
			queue.add_add(lat,lon)

        def add_remove(self,ip,lat,lon):
		num=self.servermap.index(ip)
		if num>=self.getSize():
                        print "Ning Warning:TransactionQueues: index out of bound"
                        return None
                queue=self.queues[num]
                queue.add_remove(lat,lon)

	def add_remove_toothers(self,ip,lat,lon):
		num=self.servermap.index(ip)
		if num>=self.getSize():
			print "Ning Warning:TransactionQueues: index out of bound"
			return None
		for i in range(self.getSize()):
			if i==num:
				continue;
			queue=self.queues[i]
			queue.add_remove(lat,lon)

        def pop(self,ip):
		num=self.servermap.index(ip)
		if num>=self.getSize():
                        print "Ning Warning:TTransactionQueues: index out of bound"
                        return None
                queue=self.queues[num]
                return queue.pop()
# Concoord Test Object
'''
class UpdateQueue:
	def __init__(self, value=0):
		self.value = value

	def decrement(self):
		self.value -= 10

	def increment(self):
		self.value += 10

	def getvalue(self):
		return self.value

	def __str__(self):
		return "The counter value is %d" % self.value
'''
# test Transaction Queue Class

'''
def main():
	queues=TransactionQueues()	
	queues.add_search("192.168.3.210",5,5,13)
	queues.add_add("192.168.3.215",7,6)
	queues.add_remove("192.168.3.216",9,8)
	queues.add_add_toothers("192.168.3.210",4,5)
	numQueues=queues.getSize()
	
	print "Queue"+"192.168.3.210"
	trans=queues.pop("192.168.3.210")
	while trans!=None:
		print trans
		trans=queues.pop("192.168.3.210")
	print "Queue"+"192.168.3.215"
	trans=queues.pop("192.168.3.215")
	while trans!=None:
		print trans
		trans=queues.pop("192.168.3.215")
	print "Queue"+"192.168.3.216"
	trans=queues.pop("192.168.3.216")
	while trans!=None:
		print trans
		trans=queues.pop("192.168.3.216")

if __name__ =="__main__":
	main()
'''
