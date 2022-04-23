# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/


class MinStack:
    def __init__(self):
        self.stack_q = []

    def push(self, val: int) -> None:
        m = self.getMin()
        if (m is None) or (val < m):
            m = val
        self.stack_q.append((val, m))

    def pop(self) -> None:
        self.stack_q.pop()

    def top(self) -> int:
        l = len(self.stack_q)
        return self.stack_q[-1][0]

    def getMin(self) -> int:
        l = len(self.stack_q)
        if l == 0:
            return None
        else:
            return self.stack_q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
