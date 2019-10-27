class Stack:

    def __init__(self):
        self.stack = []


    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()


    def push(self,val):
        return self.stack.append(val)


    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]


    def size(self):
        return len(self.stack)


    def is_empty(self):
        return self.size() == 0


class BrowserHistory:

    def __init__(self):
        self.History = Stack()
        self.FWDCache = Stack()

    def open(self, URL):
        self.History.push(URL)
        self.FWDCache = 0

    def Back(self):

        Tmp = self.History.peak()
        print (Tmp)
        self.FWDCache.push(Tmp)
        self.History.pop()


    def Forward(self):

        Tmp = self.FWDCache.peak()
        print (Tmp)
        self.History.push(Tmp)
        self.FWDCache.pop()





def main():
    A = Stack()

    A.push(1)
    A.push(2)
    A.push(3)
    A.push(4)

    print (A.peak())

main()


