# Password Checker and Generator

This Python program generates secure passwords and checks if they have been previously compromised in data breaches using the Pwned Passwords API.

## Features

- **Password Generation:** Utilizes a random selection of characters to create secure passwords of specified lengths.
- **Security Check:** Verifies the generated password against a database of breached passwords.
  
## Prerequisites

- Python 3.x installed.

## Setup

1. Clone this repository to your local machine.
2. Install the required modules:

3. Run the program by executing `main.py` with the desired password length as an argument:

## Usage

The `main.py` script serves as the entry point for the program. It generates a password of specified length and checks its security against known breaches.

Example usage:

`python main.py 12 ` - this generates a password with 12 characters (ascii uppercase, ascii lowercase, digits and punctuation marks)


## Files

- `main.py`: Entry point of the program, generates passwords and checks their security status.
- `password_checker.py`: Contains functions to check passwords against breach databases using the Pwned Passwords API.
- `password_generator.py`: Provides functionality to generate secure random passwords.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository and create your branch from `main`.
2. Make sure your code follows the project's coding style and conventions.
3. Ensure any necessary documentation is updated.
4. Submit a pull request with your changes, detailing the improvements made and any relevant information.

Thank you for contributing to this project!
