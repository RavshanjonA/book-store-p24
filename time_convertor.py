# import datetime
#
# # Convert Unix timestamp to readable datetime
# timestamp = 1730040612
# readable_time = datetime.datetime.utcfromtimestamp(timestamp)
#
# print(readable_time)


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        # fname, lname = full_name.split(" ") "ali" "  valiyev"
        fname, lname = full_name.split()  # "ali" "valiyev"
        return cls(first_name=fname, last_name=lname)


if __name__ == '__main__':
    u1 = User(first_name="ali", last_name="valiyev")
    u2 = User.from_full_name("ali   valiyev")
    print(u1.first_name)
    print(u1.last_name)
    print(u2.first_name)
    print(u2.last_name)
