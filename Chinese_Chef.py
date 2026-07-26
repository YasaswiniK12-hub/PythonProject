from Chef import Chef
class Chinese_Chef(Chef):

# I can also do method overriding
    def make_special_dish(self):
        print("Chinese Chef makes orange chicken")
    def make_fried_rice(self):
        print("Chinese chef makes fried rice.")
