import random
import re


def mask_data(key, value):
    masks = {
        "email": mask_email,
        "first-name": mask_first_name,
        "full-name": mask_full_name,
        "phone-number": mask_phone_number,
        "token": mask_token,
    }

    if key in masks:
        return masks[key](value)
    else:
        return f"Unsupported mask key: {key}"


def mask_email(email):
    # Mask email address by replacing a random number of characters in both the local and domain parts with asterisks.
    if "@" in email:
        local_part, domain = email.split("@")

        # Mask local part
        masked_local_part = local_part[0] + "*" * random.randint(5, 20)

        # Mask a random subset of characters in the domain part
        domain_characters = list(domain)
        num_asterisks = random.randint(2, min(len(domain), 10))
        indices_to_mask = random.sample(range(len(domain)), num_asterisks)

        for index in indices_to_mask:
            domain_characters[index] = "*"

        masked_domain = "".join(domain_characters)

        masked_email = f"{masked_local_part}@{masked_domain}"
        return masked_email
    else:
        return f"Invalid email address: {email}"


def mask_first_name(first_name):
    # Mask a first name by replacing all characters except the first one with asterisks.
    if len(first_name) >= 1:
        masked_first_name = vars[0] + "*" * (len(first_name) - 1)
        return masked_first_name
    else:
        return f"Invalid first name: {first_name}"


def mask_full_name(full_name):
    # Mask all characters in both the first and last name except for the first character.
    names = full_name.split()

    if len(names) >= 2:
        masked_first_name = names[0][0] + "*" * (len(names[0]) - 1)
        masked_last_name = names[-1][0] + "*" * (len(names[-1]) - 1)
        masked_full_name = f"{masked_first_name} {masked_last_name}"
        return masked_full_name
    else:
        return f"Invalid full name: {full_name}"


def mask_phone_number(phone_number):
    # Mask all but the last four digits in a phone number
    digits = "".join(char for char in phone_number if char.isdigit())

    if len(digits) >= 4:
        return "******" + digits[-4:]
    else:
        return f"Invalid phone number: {phone_number}"


def mask_token(token):
    # Mask a token by replacing a random subset of characters in each segment with asterisks.
    if not is_valid_token(token):
        return f"Invalid token format: {token}"

    segments = token.split("-")
    masked_segments = []

    for segment in segments:
        num_asterisks = random.randint(
            1, min(len(segment), 5)
        )  # You can adjust the range as needed
        indices_to_mask = random.sample(range(len(segment)), num_asterisks)

        masked_characters = [
            char if i not in indices_to_mask else "*" for i, char in enumerate(segment)
        ]
        masked_segments.append("".join(masked_characters))

    masked_token = "-".join(masked_segments)
    return masked_token


def is_valid_token(token):
    # Check if a token is in the correct format.
    pattern = re.compile(
        r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    )
    return bool(pattern.match(token))
