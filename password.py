def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least 1 uppercase letter.")

    if not any(char.islower() for char in password):
        errors.append("Password must contain at least 1 lowercase letter.")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least 1 digit.")

    if errors:
        print("Password is invalid:")
        for error in errors:
            print(error)
        return False
    else:
        print("Password is valid.")
        return True

def main():
    password = input("Enter your password: ")
    check_password(password)

if __name__ == "__main__":
    main()
