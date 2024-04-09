#class syntax

class member:
    not_allowed_name = ["bdea","sad", "asd"]
    users = 0
    @classmethod
    def show_users_count(cls):
        return f"users = {cls.users}"
    def __init__(self, firsT_name, sname, tname, sex): # self point to instance when created (for every instance)
        self.name = firsT_name
        self.sname = sname
        self.tname = tname
        self.Sex = sex
        member.users += 1
    def full_name(self):
        return f"{self.name} {self.sname} {self.tname}"
    def hello(self):
        if self.Sex == "male":
            return f"hello mr {self.name}"
        else:
            return f"hello ms {self.name}"
    def del_user(self):
        member.users -= 1
        del self
			
print(member.users)
member1 = member("shadi","mahmody","alu","male")
member2 = member("aser","mahmody","alu","male")
# member2 = member("osama")
# member3 = member("ahmed")
# member4 = member("saied")
# print(member1.__class__)
# print(dir(member))
# print(member1.hello())
print(member2.hello())
print(member.users)
member1.del_user()
print(member1.hello())
print(member2.hello())
print(member.users)
print(member1.hello())
print(member2.hello())
print(member.show_users_count())
print(member.users)
print ("@" * 30)