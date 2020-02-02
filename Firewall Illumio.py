import csv

#Created by Matthew Davin Kuangga
#github: davrminator
#Made in 2 hours from 4:30pm to 6:30pm on Feb/1/2020 
#Execution of these classes and useful comments start at line 100

class Firewall:
	def __init__(self, path):
	  self.array = []
	  with open(path, 'r') as file:
	  	reader = csv.reader(file)

	  	for line in reader:
	  		self.array.append(line)


	def accept_packet(self, direction, protocol, port, ip):
		self.direction = direction
		self.protocol = protocol
		self.port = port
		self.ip = ip
		#print(self.direction, self.protocol, self.port, self.ip)

		#print(len(self.array))
		index = 0
		for row in self.array:
			if self.direction == row[0] and self.protocol == row[1]:
				part = self.parse_port(row[2])
				if len(part) == 2:
					if self.port >= part[0] and self.port <= part[1]:
						#print("I am here")
						part2 = self.parse_ip(row[3])
						part3 = self.parse_ip(self.ip)
						#print "Yhis is part 2 ", self.ip
						final = self.ip_check(part2,part3)
						#print(part2)
						#print("the end")
						return final
				else:
					if(self.port == row[2]):
						part2 = self.parse_ip(row[3])
						part3 = self.parse_ip(self.ip)
						final = self.ip_check(part2,part3)
						#check for
						return final
			
			index += 1
			if index >= 4:
				return False


	def parse_port(self, port):
		#self.port = port
		parts = []
		if port.find("-") != -1:
			#print("dash found")
			parts.append(port[0:port.find("-")])
			parts.append(port[port.find("-") + 1:])
			return parts
		else:
			parts.append(port)
			return parts


	def parse_ip(self, ip):
		parts2 = []
		if ip.find("-") != -1:
			ip1 = ip[0:ip.find("-")]
			ip2 = ip[ip.find("-") + 1:]
			
			ip1 = ip1.replace('.','')
			ip2 = ip2.replace('.','')

			parts2.append(int(ip1))
			parts2.append(int(ip2))
			return parts2
		else:
			ip = ip.replace('.','')
			parts2.append(int(ip))
			return parts2


	def ip_check(self, csvip, argip):
		if len(csvip) == 2:
			if argip >= csvip[0] and argip <= csvip[1]:
				return True
			else:
				return False
		else:
			if argip == csvip:
				return True
			else:
				return False





#enter your input in "arguments" this variable or on the console
#print(arguments)
arguments = input("Enter input in exactly this format: 'direction,protocol,port,ip)': ") 
args = arguments.split(",")
#print(args)


#this will create the instance f1 of class object Firewall
#you can replace 'fw.csv' with the desired path to your CSV file
f1 = Firewall('fw.csv')
#print(f1.array)


#the lines below should not be changed because it is how I will call the class function
final = f1.accept_packet(args[0], args[1], args[2], args[3])
print(final)