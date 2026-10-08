def check_role(func):
    def wrapper(username, role):
        if role == "admin":
            func(username)
        else:
            print("Access denied")
    return wrapper
@check_role
def delete_user(username):
    print(username, "deleted")
def main():
    delete_user("John", "admin")
    delete_user("David", "user")


main()