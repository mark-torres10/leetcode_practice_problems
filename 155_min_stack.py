"""Notes:

I had trouble with this one earlier because I was just using
one stack, which makes the getMin operation difficult.

The trick is to use two stacks:
- stack: to store the values
- min_stack: to store the minimum values

When we push a value onto the stack, we also push it onto the min_stack
if it is less than the current minimum (which is the last value in the min_stack).

The min_stack approach works because the min_stack will always have the
minimum values in order.

For example, if you have the stack of [-1, 4, 5, -2],
the min_stack will be [-2, -1].

This works because the min value only changes when the min value
is popped off the stack. Otherwise, the min value returned should be the
same each time. As we pop values off the stack, if we also
pop that value off the min_stack, then the min_stack will always
have the minimum value of the remaining stack.

For example, if you have the stack of [5, -1, -1, 4, -2],
the min_stack will be [5, -1, -1, -2].

As you pop values off the stack, we also pop the min_stack;
- If you pop -2, then you pop -2 off both stacks.
    stack: [5, -1, -1, 4]
    min_stack: [5, -1, -1]
    min_value: -1
- If you pop 4, then you pop off the stack, not the min.
    stack: [5, -1, -1]
    min_stack: [5, -1, -1]
    min_value: -1
- If you pop -1, then you pop off both stacks.
    stack: [5, -1]
    min_stack: [5, -1]
    min_value: -1
- If you pop -1, then you pop off both stacks.
    stack: [5]
    min_stack: [5]
    min_value: 5
- If you pop 5, then you pop off both stacks.
    stack: []
    min_stack: []
    min_value: None

You can also have a simpler implementation where you also have a min_stack,
but you append to the min_stack on each new value, and append either the 
min_stack[-1] value or the new value, whichever is smaller. This is a slightly
cleaner implementation that requires slightly more space, but it's nice.

E.g., let's add the elements for the stack [5, -1, -1, 4, -2]:

- Add 5
    Stack: [5]
    Min_stack: [5]
- Add -1:
    Stack: [5, -1]
    Min-stack: append min(val, min_stack[-1] if min_stack else val)
        min(-1, 5) = -1
    Stack: [5, -1]
    Min_stack: [5, -1]
- Add -1:
    Stack: [5, -1, -1]
    Min_stack: append min(val, min_stack[-1] if min_stack else val)
        min(-1, -1) = -1
    Stack: [5, -1, -1]
    Min_stack: [5, -1, -1]
- Add 4:
    Stack: [5, -1, -1, 4]
    Min_stack: append min(val, min_stack[-1] if min_stack else val)
        min(4, -1) = -1
    Stack: [5, -1, -1, 4]
    Min_stack: [5, -1, -1, -1]
- Add -2:
    Stack: [5, -1, -1, 4, -2]
    Min_stack: append min(val, min_stack[-1] if min_stack else val)
        min(-2, -1) = -2
    Stack: [5, -1, -1, 4, -2]
    Min_stack: [5, -1, -1, -2]

Now, as you pop values off the stack, you can pop from both stacks at the same time.
This'll mean that you have two stacks that are always in sync.

I like this approach better because the interpretation of the min_stack as
"the ith index value is the minimum of the values in the main stack up to
index i" is a little more natural and clear.

For example, in a list, if the min value at index i = 5 is -2, that means that
the min of the stack[:5] values is -2.
"""



class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # add the value to the min stack if (1) it's the first value or
        # (2) if it's <= the current minimum value. The min_stack
        # is guaranteed to always have the minimum value up to that point.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        # add value to the max stack if (1) the stack doesn't exist or
        # (2) if it's >= the current maximum value. The max_stack
        # is guaranteed to always have the maximum value up to that point.
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            if self.stack[-1] == self.max_stack[-1]:
                self.max_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

    def getMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]
