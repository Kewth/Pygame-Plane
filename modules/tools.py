'''
其他组件
'''

'''计数器'''
class Counter:
    def __init__ (self, freq):
        self.freq = freq
        self.count = 0
        self.tot = 0
    def run (self):
        self.count += 1
        if self.count >= self.freq:
            self.tot += 1
            self.count = 0
            return True
        return False
