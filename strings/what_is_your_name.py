'''
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
'''
def print_full_name(a, b):
    print(f"Hello {first_name} {last_name}! You just delved into python.")

first_name = input()
last_name = input()
print_full_name(first_name, last_name)