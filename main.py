from password_checker import pwned_api_check
from password_generator import password_generator

def main():
    password = password_generator(12)
    print(f'Password generated successfully. The suggested password is {password}')

    count = pwned_api_check(password)
    if count:
        print(f'The suggested password was hacked {count} times. Consider changing it.')
    else:
        print('The suggested password was not found in the breach database. You can proceed.')

if __name__ == "__main__":
    main()