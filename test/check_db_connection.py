from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list = db.get_group_list()
    for item in list:
        print(item)
    print(len(list))
finally:
    pass
