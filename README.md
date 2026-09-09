# CS240 Assignment 1: Converter and Pixel System

## Description

This project has a lot of programs that are related to representing information as bits and numbers:

1. Converting ASCII to decimal
2. A number-base converter that supports binary, decimal, octal, and hexadecimal
3. A program that reads an image and converts its pixels
4. A program that consumes pixels and creates an image
5. Tests boundaries for unsigned and two's-complement values

## Requirements

- Python 3
- Pillow (PIL)

Install Pillow with:
```bash
pip3 install Pillow
```

## Files

1. `Assignment 1.py` - Main Python source code
2. `smiley.png` - Input image used for pixel conversion
3. `input.txt` - Pixel data used to rebuild an image
4. `output.txt` - Pixel values generated from input image
5. `output.png` - Image rebuild from the pixel data
6. `output 2.txt` - Additional output generated during testing

## How to Run

### Using VS Code
1. Open the project folder in VS Code
2. Open `Assignment 1.py`
3. Run the program using the Python Run button or the terminal

### Using Terminal
```bash
python3 "Assignment 1.py"
```

## Example: Binary Input

```
Enter a number: 1010
Enter the base (2, 8, 10, or 16): 2

Binary: 0b1010
Decimal: 10
Octal: 0o12
Hexadecimal: 0xa
```

## Author

Akil Shaik
