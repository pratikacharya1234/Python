# Random Password Generator

A simple Python script that generates random passwords using a mix of lowercase letters, uppercase letters, numbers, and special symbols.

## Overview

This script creates an 8-character random password by selecting characters from a predefined set of lowercase letters, uppercase letters, numbers, and special symbols. It's a basic implementation of a password generator that can be used for creating secure passwords.

## Features

- Generates 8-character random passwords
- Includes a mix of:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Special symbols (!,@,#,$,%,^,&,*,(,),_,-,+,=,?,/)
- Simple and easy to use

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `random` module)

## Usage

1. Run the script:
   ```
   python password_generator.py
   ```
2. The script will output an 8-character random password to the console

## How It Works

1. The script defines character sets for lowercase letters, uppercase letters, numbers, and special symbols
2. It combines all these sets into a single pool of characters
3. It then randomly selects characters from this pool until the password reaches 8 characters in length
4. The generated password is printed to the console

## Implementation Notes

- The character sets are defined as comma-separated strings
- The `random.choice()` function is used to select random characters
- The script always generates an 8-character password

## Potential Improvements

- Allow customization of password length
- Ensure the password contains at least one character from each set
- Add command-line arguments for configuration
- Implement a function to generate multiple passwords
- Add an option to copy the password to the clipboard
- Improve the way character sets are defined (using lists instead of comma-separated strings)