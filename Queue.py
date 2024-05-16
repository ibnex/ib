#  Python program to implement Queue data structure using list

class Queue:
    def __init__(self):
        self.queue = []

    
    def is_empty(self):
        return len(self.queue) == 0


    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.queue)

# Example usage:

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue size:", q.size())
print("Peek:", q.front())
print("Dequeue:", q.dequeue())
print("Queue size:", q.size())
