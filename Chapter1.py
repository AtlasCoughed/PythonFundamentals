record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

print(phone_numbers)

##################################
#DeQue - keep last N items
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q # 1, 2, 3
deque([1, 2, 3], maxlen=3)
q.append(4)
q

deque([2, 3, 4], maxlen=3)
q.append(5)
q
deque([3, 4, 5], maxlen=3)

# Commands: Append, AppendLeft, pop, popLeft()

##################################
# Finding Largest/ Smallest number

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

heap = list(nums)
heapq.heapify(heap)
print(heap)
//Ordered list

heapq.heappop(heap) # smallest value in heap

# Only good for smaller lists
