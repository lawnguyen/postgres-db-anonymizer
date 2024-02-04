import re
import random
import string


def transform_data(key, value):
    transformations = {
        "email": generate_email,
        "first-name": generate_first_name,
        "phone-number": generate_phone_number,
        "random": randomize_value,
        "keep-first-char": keep_first_char,
        "credit-card": generate_credit_card,
        "redacted": obfuscate_data,
    }

    if key in transformations:
        return transformations[key](value)
    else:
        return f"Unsupported transformation key: {key}"


def generate_email():
    # List of common email domains
    email_domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "example.com",
        "company.com",
    ]

    # Generate a random username
    username = "".join(random.choices(string.ascii_letters + string.digits, k=8))

    # Choose a random email domain
    domain = random.choice(email_domains)

    # Create the email address
    email_address = f"{username}@{domain}"

    return email_address


def generate_first_name():
    # Replace first name logic with your own logic
    return "John Doe"


def generate_phone_number():
    # Replace phone number logic with your own logic
    # This is just a placeholder
    return "123-456-7890"


def randomize_value(value):
    # Randomize value but keep the same length
    return "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in value)


def keep_first_char(value):
    # Keep only the first character of the column
    return value[0]


def generate_credit_card():
    # Replace credit card logic with your own logic
    return "424****************"


def obfuscate_data(value):
    # Obfuscate sensitive data
    return re.sub(r"\d", "*", value)
