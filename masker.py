import random


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
    # Mask email address by replacing a random number of characters in both the local and domain parts with asterisks.
    if "@" in value:
        local_part, domain = value.split("@")

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


def mask_phone_number(phone_number):
    # Mask all but the last four digits in a phone number
    digits = "".join(char for char in phone_number if char.isdigit())

    if len(digits) >= 4:
        return "******" + digits[-4:]
    else:
        return f"Invalid phone number: {phone_number}"
