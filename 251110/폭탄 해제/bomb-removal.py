unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class unlock():
    def __init__(self,code,color,sec):
        self.code = code
        self.color = color
        self.sec = sec

unlock1 = unlock(unlock_code,wire_color,seconds)

print('code :',unlock1.code)
print('color :',unlock1.color)
print('second :',unlock1.sec)