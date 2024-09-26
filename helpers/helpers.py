import yaml
import random

PASSWORD_EXCLUDED = open("./helpers/dictionary.yaml", 'r')
def enter_password_length() -> int:
    return (int(input("Longeur souhaité du mot de passe : ")))

def verify_password_length(length: int) -> bool:
    return length >= 12

def check_in_exclusion(password: str) -> bool:
    with PASSWORD_EXCLUDED as file:
        exclusion_data = yaml.safe_load(file)
    excluded_pass = exclusion_data['exclusion']
    if password in excluded_pass:
        raise Exception('Mot de passe trop simple')
    return True

def generate_password(length: int) -> str:
    char_list = "azertyuipqsdfghjklmwxcvbnAZERTYUIPQSDFGHJKLMWXCVBN&É(-_)=$*!:&~#{[|]}+=12346546789+,?./§"
    password = ''.join(random.choice(char_list) for _ in range(length))
    if check_in_exclusion(password=password):
        return password