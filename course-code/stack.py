
class Stack(object):

	def __init__(self):
		self.stack = [];
		self.numOfItems = 0;
		
	def isEmpty(self):
		return self.stack == [];
		
	def push(self, data):
		self.stack.insert(self.numOfItems, data);
		self.numOfItems = self.numOfItems + 1;
		
	def pop(self):
		self.numOfItems = self.numOfItems - 1;
		data = self.stack.pop(self.numOfItems);
		return data;
		
	def size2(self):
		return len(self.stack);
		
		
stack = Stack();

stack.push(10);
stack.push(20);
stack.push(30);

print(stack.pop());
print(stack.pop());
print(stack.size2());
print(stack.pop());
print(stack.size2());
