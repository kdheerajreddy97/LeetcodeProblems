class PhoneDirectory:

    def __init__(self, size):
        self.count = 0
        self.phoneNumbers = set()
        self.size = size

        for i in range(self.size):
            self.phoneNumbers.add(self.count) #available phone number
            self.count += 1

    def get(self):
        if self.phoneNumbers:
            return self.phoneNumbers.pop()
        else:
            return -1

    def check(self, var):
        if var in self.phoneNumbers:
            return True
        else:
            return False

    def release(self,var):
        if var in range(self.size) and var not in self.phoneNumbers:
            self.phoneNumbers.add(var)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)