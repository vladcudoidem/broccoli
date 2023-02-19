# Scripting file with help functions and classes

def pr_ret(msg):
    print(msg)
    return msg

class Helper:
    def __init__(self, val):
        self.val = val
    
    def getInstance():
        return Helper()
        