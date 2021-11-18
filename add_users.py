from django.contrib.auth import User

def get_input():
    s = input()
    users = []
    while s != "":
        line_array = s.split(',')
        users.append((line_array[0], line_array[1]))

def write_to_db(users):
    for user in users:
        user_object = User.objects.create_user(user[0], user[1])
        user_object.is_superuser = False
        user_object.is_staff = False
        user_object.save()

users = get_input()
write_to_db(users = users)