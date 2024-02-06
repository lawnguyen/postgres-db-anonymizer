import random
import string


def mask_data(key, value):
    masks = {
        "email": mask_email,
        "first-name": mask_first_name,
        "full-name": mask_full_name,
        "phone-number": mask_phone_number,
    }

    if key in masks:
        return masks[key](value)
    else:
        return f"Unsupported mask key: {key}"


def mask_email(value):
    # Mask all characters in the local part of an email address except the first character.
    if "@" in value:
        local_part, domain = value.split("@")
        masked_local_part = local_part[0] + "*" * (len(local_part) - 1)
        masked_email = f"{masked_local_part}@{domain}"
        return masked_email
    else:
        return f"Invalid email address: {value}"


def mask_first_name(value):
    # Mask a first name by replacing all characters except the first one with asterisks.
    if len(value) >= 1:
        masked_first_name = vars[0] + "*" * (len(value) - 1)
        return masked_first_name
    else:
        return f"Invalid first name: {value}"


def mask_full_name(value):
    # Mask all characters in both the first and last name except for the first character.
    names = value.split()

    if len(names) >= 2:
        masked_first_name = names[0][0] + "*" * (len(names[0]) - 1)
        masked_last_name = names[-1][0] + "*" * (len(names[-1]) - 1)
        masked_full_name = f"{masked_first_name} {masked_last_name}"
        return masked_full_name
    else:
        return f"Invalid full name: {value}"


def mask_phone_number(value):
    digits = "".join(char for char in value if char.isdigit())

    if len(digits) >= 4:
        masked_digits = "*" * (len(digits) - 4) + digits[-4:]
        masked_phone_number = "".join(
            masked_digits[i] if char.isdigit() else char for i, char in enumerate(value)
        )
        return masked_phone_number
    else:
        return f"Invalid phone number: {value}"
