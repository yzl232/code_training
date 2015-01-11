#记录下下一个值。实现一个带有peek() 的iterator. 写test case
class SequenceIterator:
	def __init__(self,sequence):
		self._seq=sequence	
		self._k=-1
		self._peek=0
	def next(self):	
		if self.hasNext():
			self._k+=1
			return (self._seq[self._k])
		else:
			raise StopIteration()
	def hasNext(self):
		return self._k+1<len(self._seq)
	def peek(self):
		self._peek=self._k+1
		if self._peek<len(self._seq):
			return (self._seq[self._peek])
		else:
			raise StopIteration()
	def __iter__(self):
		return self
#merge sorted stream
class MergeIterator:
	def __init__(self,iters):
		self.pq=[]
		for i in iters:
			if i.hasNext():
				item=i.next()
				heapq.heappush(self.pq,(item,i))
	def next(self):
		if self.hasNext():
			item,curriter=heapq.heappop(self.pq)
			if curriter.hasNext():
				newItem=curriter.next()
				heapq.heappush(self.pq,(newItem,curriter))
			return item
		else:
			raise StopIteration()
	def hasNext(self):
		if self.pq:
			return True
		else:
			return False
	def __iter__(self):
		return self
#iterator of a list of iterators
def FlattenIterator(iters):
	listIters=iters
	curr=initialization()
	def initialization():
		tmp=null
		while listIters.hasNext():
			tmp=listIters.next()
			if tmp.hasNext():
				break
		return tmp
	def hasNext():
		if curr.hasNext():
			return True
		else:
			curr=initialization()
			if curr is None:
				return False
			return curr.hasNext()
	def next():
		if not hasNext(): raise StopIteration()
		return curr.next()
'''
public static Iterator<String> flatten(final Iterator<Iterator<String>> iters) {
		return new Iterator<String>() {	
            private Iterator<String> curIter=null;
            private String nextItem=advanceItem();
            private String advanceItem(){
                if(iters==null&&curIter==null) throw new NullPointerException();
                while((iters!=null&&iters.hasNext())||(curIter!=null&&curIter.hasNext())){
                    if((curIter==null||!curIter.hasNext())){
                        if(iters!=null&&iters.hasNext()){
                            curIter=iters.next();
                        }
                    }
                    if(curIter==null){
                        continue;
                    }
                    while(curIter.hasNext()){
                        String result=curIter.next();
                        if(result!=null){
                            return result;
                        }
                    }
                }
                return null;
            }
			public boolean hasNext() {
				return nextItem!=null;
			}

			public String next() {
				if(!hasNext())
                    throw new NullPointerException();
                String oldItem=nextItem;
                nextItem=advanceItem();
                return oldItem;
			}

			public void remove() {
				throw new UnsupportedOperationException();
			}
		};
}
'''
#fibonacci generator
def fib():
    a,b = 1,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b
#write a rotate iterator
class RotateIterator:
	def __init__(iters):
		self.iters=iters
		self.length=len(iters)
		self.count=0
	def next(self):
		if self.hasNext():
			item=self.iters[self.count+1].next()
			self.count+=1
			return item
		else:
			raise StopIteration()
	def hasNext(self):
		originalCount=self.count
		while not self.iters[self.count+1].hasNext():
			self.count=(self.count+1)%self.length
			if self.count==originalCount:
				return False
		return True
	def __iter__(self):
		return self
#write a jump iterator
class JumpIterator:
	def __init__(self,seq):
		self.seq=seq
	def next(self):
		if self.hasNext():
			return self.seq.next()
		else:
			raise StopIteration()
	def hasNext(self):
		if self.seq.hasNext():
			return True
		else:
			return False
	def nextNext(self):
		if self.hasNext():
			self.seq.next()
			if self.hasNext():
				return self.seq.next()
			else:
				raise StopIteration()
		else:
			raise StopIteration()
	def __iter__(self):
		return self
#write an even iterator
class EvenIterator:
	def __init__(self,seq):
		self.seq=seq
	def hasNext(self):
		return self.seq.hasNext()
	def next(self):
		while self.hasNext():
			item=self.seq.next()
			if item%2==0:
				return item
		raise StopIteration()
	def __iter__(self):
		return self