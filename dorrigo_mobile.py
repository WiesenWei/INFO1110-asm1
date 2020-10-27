"""
 * Dorrigo Mobile Phone Class.
 *
 * INFO1110 Assignment, Semester 2, 2020.
 *
 * dorrigo_mobile
 * In this assignment you will be creating an Dorrigo Mobile Phone as part of a simulation.
 * The Mobile phone includes several attributes unique to the phone and has simple functionality.
 * You are to complete 2 classes. dorrigo_mobile and dorrigo_contact
 *
 * The phone has data
 *  Information about the phone state. 
 *    If it is On/Off
 *    Battery level 
 *    If it is connected to network. 
 *    Signal strength when connected to network
 *  Information about the current owner saved as contact information. 
 *    First name
 *    Last name
 *    Phone number
 *  A list of N possible contacts.
 *    Each contact stores first name, last name, phone number and chat history up to 20 messages
 *  
 * The phone has functionality
 *  Turning on the phone
 *  Charging the phone. Increase battery level
 *  Change battery (set battery level)
 *  Use phone for k units of battery (decreases battery level by k)
 *  Search/add/remove contacts
 *
 * Attribute features
 *  if the phone is off. It is not connected. 
 *  if the phone is not connected there is no signal strength
 *  the attribute for battery life has valid range [0,100]. 0 is flat, 100 is full.
 *  the attribute for signal strength has a valid range [0, 5]. 0 is no signal, 5 is best signal.
 * 
 * Please implement the methods provided, as some of the marking is
 * making sure that these methods work as specified.
 *
 * @author An INFO1110 tutor.
 * @date September, 2020
 *
"""

from dorrigo_contact import dorrigo_contact

class dorrigo_mobile:

	def __init__(self, max_contacts):
		"""
		Every phone manufactured has the following attributes
		 
		 # the phone is off
		 # the phone has battery life 25
		 # the phone is not connected
		 # the phone has signal strength 0
		 Each of the contacts stored in the array contacts has a None value
		 
		 # the owner first name "Dorrigo"
		 # the owner last name is "Incorporated"
		 # the owner phone number is "180076237867"
		 # the owner chat message should have only one message 
		         "Thank you for choosing Dorrigo products"	
		"""
		self.power = False
		self.battery = 25
		self.network = False
		self.signal = 0
		self.owner = dorrigo_contact("Dorrigo", "Incorporated", "180076237867")
		self.owner.chat_history.append("Dorrigo: Thank you for choosing Dorrigo products")
		self.contacts = [None] * max_contacts

	def get_copy_of_owner_contact(self):
		"""  returns a copy of the owner contact details
		  	 return None if the phone is off
			 datatype of returned object is dorrigo_contact or None
		"""
		if self.power == False:
			return None
		else:
			copy = dorrigo_contact("Dorrigo", "Incorporated", "180076237867")
			copy.chat_history.append("Dorrigo: Thank you for choosing Dorrigo products")
			return copy

	def add_contact(self, contact): 
		""" only works if phone is on
		   will add the contact in the array only if there is space and does not exist
		   The method will find an element that is None and set it to be the contact.
		   returns True if successful
		"""
		if self.power == False:
			return False
		else:
			i = 0
			while i < len(self.contacts):
				if self.contacts[i] == contact:
					return False
				if self.contacts[i] == None:
					self.contacts[i] = contact
					return True
				i += 1
			return False

	def remove_contact(self, contact): 
		""" only works if phone is on
		   find the dorrigo_contact object and set the array element to None
	 	   return True on successful remove
		"""
		if self.power == False:
			return False
		i = 0
		if contact == None:
			return False
		else:
			while i < len(self.contacts):
				if contact == self.contacts[i]:
					self.contacts[i] = None
					return True
				i += 1
			return False

	def get_number_of_contacts(self): 
		""" only works if phone is on
		    returns the number of contacts, or -1 if phone is off
		"""
		if self.power == False:
			return -1
		else:
			i = 0
			n = 0
			while i < len(self.contacts):
				if self.contacts[i] != None:
					n += 1
				i += 1
			return n

	def search_contact(self, name): 
		""" only works if phone is on
		   returns a list of all contacts that match first name OR last name
		   if phone is off, or no results, None is returned
		"""
		if self.power == False:
			return
		else:
			i = 0
			ls = []
			while i < len(self.contacts):
				if self.contacts[i] != None:
					if name == self.contacts[i].fname or name == self.contacts[i].lname:
						ls.append(self.contacts[i])
				i += 1
			if ls == []:
				return
			return ls

	def is_phone_on(self): 
		""" returns True if phone is on
		"""
		if self.power == True:
			return True
		else:
			return False

	def set_phone_on(self, on): 
		"""
			set the on status based on the boolean input
			when phone turns on, it costs 5 battery for startup. network is initially disconnected
			when phone turns off it costs 0 battery, network is disconnected
			always return True if turning off
			return False if do not have enough battery level to turn on
			return True otherwise
		"""
		if on == True:
			if self.battery >= 6:
				self.power = True
				self.battery -= 5
				self.network = False
				return True
			else:
				self.network = False
				return False
		elif on == False:
			self.power = False
			self.network = False
			return True
	
	def get_battery_life(self): 
		""" Return the battery life level as an integer. if the phone is off, zero is returned.
		"""
		if self.power == False:
			return 0
		else:
			return self.battery
	
	def change_battery(self, new_battery_level): 
		""" Change battery of phone.
		   On success. The phone is off and new battery level adjusted and returns True
		   If new_battery_level is outside manufacturer specification of [0,100], then 
		   no changes occur and returns False.
		"""
		if 0 <= new_battery_level <= 100:
			self.battery  = new_battery_level
			self.power = False
			self.battery_level = new_battery_level
			return True
		else:
			return False
	
	def is_connected_network(self): 
		""" only works if phone is on. 
		    returns True if the phone is connected to the network
		"""
		if self.power == False:
			self.network = False
			return False
		elif self.network == True:
			return True
		else:
			return False
	
	def disconnect_network(self): 
		""" only works if phone is on. 
		    when disconnecting, the signal strength becomes zero
		    always returns True
		"""
		if self.power == False:
			self.network = False
			return True
		else:
			self.network = False
			self.signal = 0
			return True
	
	def connect_network(self):
		""" only works if phone is on. 
		   Connect to network
		   if already connected do nothing and return True
		   if connecting:
		    1) signal strength is set to 1 if it was 0
		    2) signal strength will be the previous value if it is not zero
		    3) it will cost 2 battery life to do so
		   returns the network connected status
		"""
		if self.power == False:
			return False
		else:
			if self.network == True:
				return self.network
			else:
				if self.signal == 0:
					self.signal = 1
					self.network = True
					self.use_phone(2)
					return self.network
				else:
					self.network = True
					self.use_phone(2)
					return self.network
	
	def get_signal_strength(self): 
		""" only works if phone is on. 
		   returns a value in range [1,5] if connected to network
		   otherwise returns 0
		"""
		if self.power == False:
			return 0
		elif self.network == False:
			return 0
		else:
			return self.signal

	def set_signal_strength(self, new_strength): 
		""" only works if phone is on. 
		   sets the signal strength and may change the network connection status to on or off
		   signal of 0 disconnects network
		   signal [1,5] can connect to network if not already connected
		   if the signal is set outside the range [0,5], nothing will occur and will return False
		   if the phone is not connected to a network and n > 0, it will connect to a network 
		   and reduce the battery life by 2
		   returns True on success
		"""
		if self.power == False:
			return False
		else:
			if new_strength >= 1 and new_strength <= 5:
				if self.network == False:
					self.use_phone(4)
				else: 
					self.use_phone(2)
				self.network = True
				self.signal = new_strength
				return True
			elif new_strength == 0:
				self.network = False
				self.signal = 0
				return True
			else:
				return False
	
	def charge_phone(self): 
		""" each charge increases battery level by 10
		   the phone has overcharge protection and cannot exceed 100
		   returns True if the phone was charged by 10, otherwise False
		"""
		if self.battery > 90:
			self.battery = 100
			return False
		elif 0 <= self.battery <= 90:
			self.battery += 10
			return True
	
	def use_phone(self, k):
		""" Use the phone which costs k units of battery life.
		   if the activity exceeds the battery life, the battery automatically 
		   becomes zero and the phone turns off.
		   returns True on successful use (not partial)
		"""
		try:
			units = k
			if units < self.battery:
				self.battery -= units
				return True
			elif units == self.battery:
				self.battery = 0
				self.power = False
				self.network = False
				return True
			else:
				self.battery = 0
				self.power = False
				self.network = False
				return False
		except TypeError:
			pass