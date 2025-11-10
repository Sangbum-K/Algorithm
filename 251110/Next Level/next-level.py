user2_id, user2_level = input().split()
user2_level = int(user2_level)


class user:
    def __init__(self,userid = 'codetree',lv=10):
        self.userid = userid
        self.lv = lv


user1 = user()
print('user',user1.userid,'lv',user1.lv)
user2 = user(user2_id,user2_level)
print('user',user2.userid,'lv',user2.lv)