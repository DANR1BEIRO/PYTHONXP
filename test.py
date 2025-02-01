import re


def email_pattern(email):
    pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
    return bool(pattern.match(email))


def is_valid_email(email):
    if email_pattern(email):
        print("E-mail válido!")
    else:
        print("E-mail inválido!")


email_input = input("Digite o e-mail para validação: ")

is_valid_email(email_input)