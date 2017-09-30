
class Queue(object):

	def __init__(self):
		self.queue = [];
		
	def isEmpty(self):
		return self.queue == [];
		
	def enqueue(self, data):
		self.queue.insert(0, data);
		
	def dequeue(self):
		return self.queue.pop();
		
	def size2(self):
		return len(self.queue);
		
queue = Queue();

queue.enqueue("Daniel");
queue.enqueue(12);
queue.enqueue(10.5);

print(queue.dequeue());
print(queue.dequeue());
print(queue.size2());
print(queue.dequeue());
print(queue.size2());
