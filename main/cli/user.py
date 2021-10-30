import sys
import getpass
from passlib.hash import sha256_crypt as crypt
from sqlalchemy.exc import IntegrityError


def input_loop(message, password=False):
    while True:
        if not password:
            data = input(message)
        else:
            data = getpass.getpass(message)
        if data or data is None:
            break
    return data


def createsuperuser(User):
    print("<<< Create superuser >>>\n")
    try:
        username = input_loop("Enter username: ")
        email = input_loop("Enter your email: ")
        password = input_loop("Enter password: ", password=True)
        password_confirm = input_loop("Confirm password: ", password=True)
        if password != password_confirm:
            print(">>> Passwords do not match. Aborted.")
            sys.exit()
        password_hash = crypt.hash(password)
        new_user = User(
            username=username, email=email, password=password_hash, superuser=True
        )
        new_user.save()
    except KeyboardInterrupt:
        print("\n>>> Interrupt by user")
        sys.exit()
    except IntegrityError as err:
        if f"({username}) already exists" in str(err.orig):
            print(">>> [ERROR] This user already exists.")
        elif f"({email}) already exists" in str(err.orig):
            print(">>> [ERROR] Cannot have more than one user with the same email.")
