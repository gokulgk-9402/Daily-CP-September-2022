class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.rear = -1
        self.front = 0
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear>=self.length-1:
            self.rear=-1
            
        self.queue[self.rear+1]=value
        self.rear+=1
        return True

    def deQueue(self) -> bool:
        if self.queue[self.front]==-1:
            return False
        if self.front==self.rear:
            self.queue[self.front]=-1
            self.front, self.rear = 0, -1
            return True
        if self.front==self.length-1:
            self.queue[self.front]=-1
            self.front=0
            return True
        
        self.queue[self.front]=-1
        self.front+=1
        return True

    def Front(self) -> int:
        if self.queue[self.front]==-1:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.queue[self.rear]==-1:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front==0 and self.rear==-1:
            return True
        return False
            

    def isFull(self) -> bool:
        if (self.rear - self.front == self.length-1) or (self.front-abs(self.rear)==1):
            return True
        return False