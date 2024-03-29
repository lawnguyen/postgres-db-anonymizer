import random
import string
import uuid


def transform_data(key, value):
    transformations = {
        "email": generate_email,
        "first-name": generate_first_name,
        "full-name": generate_full_name,
        "phone-number": generate_phone_number,
        "random": randomize_value,
        "random-free": generate_random_value,
        "number": generate_random_number,
        "address": generate_random_address,
        "address2": generate_random_address2,
        "token": generate_random_token,
    }

    if key in transformations:
        return transformations[key](value)
    else:
        raise Exception(f"Error: Unsupported transformation key: {key}")


def generate_email(value):
    if not value:
        return None
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


def generate_first_name(value):
    if not value:
        return None

    first_names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Harry",
        "Ivy",
        "Jack",
        "Katherine",
        "Leo",
        "Mia",
        "Noah",
        "Olivia",
        "Sophia",
        "Liam",
        "Emma",
        "Aiden",
        "Ava",
        "Jackson",
        "Oliver",
        "Isabella",
        "Sophie",
        "Lucas",
        "Ethan",
        "Amelia",
        "Mason",
        "Harper",
        "Evelyn",
        "Sofia",
        "Mateo",
        "Aaliyah",
        "Mohammed",
        "Jasmine",
        "Yuki",
        "Hiroshi",
        "Sakura",
        "Ravi",
        "Priya",
        "Chen",
        "Mei",
        "Yusuke",
        "Aya",
        "Diego",
        "Ananya",
        "Raj",
        "Lila",
        "Arjun",
        "Maya",
        "Dante",
        "Elena",
        "Luca",
        "Sofija",
        "Nikolai",
        "Jamal",
        "Zara",
        "Omar",
        "Sana",
        "Kai",
        "Aisha",
        "Javier",
        "Isabel",
        "Rahul",
        "Nina",
    ]
    return random.choice(first_names)


def generate_full_name(value):
    if not value:
        return None

    last_names = [
        # English
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        # Chinese
        "Wang",
        "Li",
        "Zhang",
        "Liu",
        "Chen",
        "Yang",
        "Huang",
        # Indian
        "Patel",
        "Sharma",
        "Singh",
        "Kumar",
        "Das",
        "Roy",
        "Mukherjee",
        # Spanish
        "Garcia",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Perez",
        "Gonzalez",
        # Russian
        "Ivanov",
        "Smirnov",
        "Kuznetsov",
        "Popov",
        "Vasilyev",
        "Sokolov",
        "Mikhailov",
        # Japanese
        "Sato",
        "Suzuki",
        "Takahashi",
        "Tanaka",
        "Watanabe",
        "Ito",
        "Yamamoto",
        # French
        "Martin",
        "Dubois",
        "Thomas",
        "Lefevre",
        "Moreau",
        "Simon",
        "Leroy",
        # German
        "Muller",
        "Schmidt",
        "Schneider",
        "Fischer",
        "Weber",
        "Schulz",
        "Becker",
        # Italian
        "Rossi",
        "Russo",
        "Ferrari",
        "Esposito",
        "Bianchi",
        "Romano",
        "Colombo",
        # Korean
        "Kim",
        "Lee",
        "Park",
        "Choi",
        "Jeong",
        "Kang",
        "Yoon",
        # Brazilian
        "Silva",
        "Santos",
        "Oliveira",
        "Souza",
        "Lima",
        "Costa",
        "Pereira",
        # Nigerian
        "Okafor",
        "Ogunjimi",
        "Adebayo",
        "Nwabueze",
        "Obi",
        "Eze",
        "Oluwole",
        # Egyptian
        "Mohamed",
        "Ibrahim",
        "Ali",
        "Hassan",
        "Abdel",
        "Mahmoud",
        "Saeed",
        # South African
        "Nkosi",
        "Zulu",
        "Molefe",
        "Botha",
        "Mthembu",
        "Mokwena",
    ]
    return f"{generate_first_name('foobar')} {random.choice(last_names)}"


def randomize_value(value):
    if not value:
        return None

    # Randomize a string with alphanumeric values while maintaining the same length.
    randomized_string = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(len(value))
    )
    return randomized_string


def generate_phone_number(value):
    if not value:
        return None

    # Country code (you can customize this based on your needs)
    country_code = "+91"  # Example: India

    # Generate a random local area code and phone number
    area_code = str(random.randint(100, 999))
    local_number = "".join(str(random.randint(0, 9)) for _ in range(7))

    # Format the phone number
    phone_number = f"{country_code} ({area_code}) {local_number[:3]}-{local_number[3:]}"

    return phone_number


def generate_random_number(value):
    if not value:
        return None

    # Generate a random integer between 1 and 1000 (inclusive).
    return random.randint(1, 1000)


def generate_random_address(value):
    if not value:
        return None

    states = [
        "Andhra Pradesh",
        "Telangana",
        "Maharashtra",
        "Tamil Nadu",
        "Uttar Pradesh",
    ]
    cities = ["Hyderabad", "Mumbai", "Chennai", "Delhi", "Bangalore"]
    zip_code = str(random.randint(100000, 999999))

    state = random.choice(states)
    city = random.choice(cities)
    street_address = (
        f"{random.randint(1, 999)} {random.choice(['Main', 'Cross', 'Market'])} Street"
    )

    random_address = f"{street_address}, {city}, {state} - {zip_code}, India"

    return random_address


def generate_random_address2(value):
    if not value:
        return None

    # Generate a random address2 part.
    address2_length = random.randint(5, 20)  # You can adjust the length range as needed
    address2 = "".join(
        random.choice(string.ascii_letters + string.digits + " ,.-")
        for _ in range(address2_length)
    )
    return address2


def generate_random_token(value):
    if not value:
        return None

    token = str(uuid.uuid4())
    return token


def generate_random_value(value):
    if not value:
        return None

    # Generate a random string with random length
    random_length = random.randint(5, 20)  # You can adjust the length range as needed
    random_value = "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(random_length)
    )
    return random_value
