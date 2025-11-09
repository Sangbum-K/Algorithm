secret_code, meeting_point, time = input().split()
time = int(time)

class secret:
    def __init__(self,code,point,time):
        self.code = code
        self.point = point
        self.time = time




secret1 = secret(secret_code,meeting_point,time)

print('secret code :',secret1.code)
print('meeting point :',secret1.point)
print('time :',secret1.time)