#Decorators
def admin_only(dashboard):
    def wrapper(username):
        if username == 'admin':
            print("Access granted")
            dashboard(username)
        else:
            print("Access Denied")
    return wrapper

@admin_only
def dashboard(username):
    print(f"Welcome to the dashboard, {username}")
dashboard("admin") # Access granted
dashboard("user1") # Access Denied