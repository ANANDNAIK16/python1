class Node:

# Constructor 
def __init__(self, data):
	self.data = data
	self.next = None


class LinkedList:

	# head function
	def __init__(self):
		self.head = None

	def reverse_Util(self, curr, prev):

		# If last node mark it head
		if curr.next is None:
			self.head = curr


			curr.next = prev
			return

		# Save curr.next node for recursive call
		next = curr.next

		# update next
		curr.next = prev

		self.reverse_Util(next, curr)

	# This function calls reverse_Util()
	# with previous as Null

	def reverse(self):
		if self.head is None:
			return
		self.reverse_Util(self.head, None)

	# To insert the new node at the beginningof the list

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# To print the list
	def printL(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next


# Main function
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)


print "Given linked list"
llist.printL()

llist.reverse()

print "\nReverse linked list"
llist.printL()
 

Output

Given linked list
4 3 2 1 
Reverse linked list
1 2 3 4
 