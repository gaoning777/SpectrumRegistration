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
	def deserialize(self,string):
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
class TransactionQueues:
	def __init__(self,num=3):
		self.queues=list()
		for i in range(num):
			self.queues.append(TransactionQueue())
	def getSize(self):
		return len(self.queues)
	
	def add_search(self,num,lat,lon,distance):
		if num>=self.getSize():
			print "Ning Warning:TransactionQueues: index out of bound"
			return None
                queue=self.queues[num]
                queue.add_search(lat,lon,distance)
        def add_add(self,num,lat,lon):
		if num>=self.getSize():
                        print "Ning Warning:TransactionQueues: index out of bound"
                        return None
                queue=self.queues[num]
                queue.add_add(lat,lon)
        def add_remove(self,num,lat,lon):
		if num>=self.getSize():
                        print "Ning Warning:TransactionQueues: index out of bound"
                        return None
                queue=self.queues[num]
                queue.add_remove(lat,lon)
        def pop(self,num):
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
	queues=TransactionQueues(3)	
	#queues.add_search(0,5,5,13)
	#queues.add_add(0,7,6)
	queues.add_remove(1,9,8)
	#queues.add_add(3,4,5)
	#numQueues=queues.getSize()
	
	for i in range(numQueues):
		print "Queue"+str(i)
		trans=queues.pop(i)
		while trans!=None:
			trans.toString()
			trans=queues.pop(i)

	trans=queues.pop(1)
	trans.toString()

if __name__ =="__main__":
	main()
'''
