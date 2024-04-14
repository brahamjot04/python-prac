# The ATM program allows a user an indefinite number of attempts to log in . Fix the program so that it displays a popup message that the police will be called after a user has had three successive failures. The program should also disable the login button when this happens.

def atm_program():

    #   Simulates an ATM program with login attempt limit.

    login_attempts = 0
    correct_pin = 1234  # Replace with actual PIN

    while True:
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == correct_pin:
            print("Login successful!")

            break
        else:
            login_attempts += 1
            if login_attempts == 3:
                print(
                    "Incorrect PIN. You have reached the maximum number of attempts. \n \
                    Your account is locked. The police have been notified.")

                break
            else:
                print("Incorrect PIN. Please try again.")


atm_program()
