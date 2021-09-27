'''
Version A (efficient push):

push:
enqueue in queue1
pop:
while size of queue1 is bigger than 1, pipe dequeued items from queue1 into queue2
dequeue and return the last item of queue1, then switch the names of queue1 and queue2
Version B (efficient pop):

push:
enqueue in queue2
enqueue all items of queue1 in queue2, then switch the names of queue1 and queue2
pop:
deqeue from queue1


"Stack"
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+

Queue A                Queue B
+---+---+---+---+---+  +---+---+---+---+---+
|   |   |   |   |   |  |   |   |   |   |   |
+---+---+---+---+---+  +---+---+---+---+---+


"Stack"
+---+---+---+---+---+
| 1 |   |   |   |   |
+---+---+---+---+---+

Queue A                Queue B
+---+---+---+---+---+  +---+---+---+---+---+
| 1 |   |   |   |   |  |   |   |   |   |   |
+---+---+---+---+---+  +---+---+---+---+---+

"Stack"
+---+---+---+---+---+
| 2 | 1 |   |   |   |
+---+---+---+---+---+

Queue A                Queue B
+---+---+---+---+---+  +---+---+---+---+---+
|   |   |   |   |   |  | 2 | 1 |   |   |   |
+---+---+---+---+---+  +---+---+---+---+---+

"Stack"
+---+---+---+---+---+
| 3 | 2 | 1 |   |   |
+---+---+---+---+---+

Queue A                Queue B
+---+---+---+---+---+  +---+---+---+---+---+
| 3 | 2 | 1 |   |   |  |   |   |   |   |   |
+---+---+---+---+---+  +---+---+---+---+---+
'''

