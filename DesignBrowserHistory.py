class BrowserHistory(object):

    def __init__(self, homepage):
        self.history = [homepage]
        self.curr_idx = 0

    def visit(self, url):
        while (len(self.history) != self.curr_idx+1):
            self.history.pop()
        self.history.append(url)
        self.curr_idx += 1

    def back(self, steps):
        next_idx = max(0, self.curr_idx - steps)
        self.curr_idx = next_idx
        return self.history[self.curr_idx]

    def forward(self, steps):
        next_idx = min(self.curr_idx + steps, len(self.history)-1)
        self.curr_idx = next_idx
        return self.history[self.curr_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)