import sys
from PIL import Image



# 1. Build an ASCII-to-decimal converter.
args = sys.argv
 
s = "Dominic"
for c in s:
 print(ord(c))

# 2. Build a number-base converter supporting binary, decimal, octal, and hexadecimal.


number = input("Enter a number: ")
base = int(input("Enter the base (2, 8, 10, or 16): "))

decimal = int(number, base)

print("Binary:", bin(decimal))
print("Decimal:", decimal)
print("Octal:", oct(decimal))
print("Hexadecimal:", hex(decimal))

# 3. Write a program that reads an image and prints its pixel values.

def convert(color):
  # if red
  if color == "(237, 28, 36)":
    return "R"
  # if black 
  elif color == "(0,0,0)":
    return "B"
  # if yellor 
  elif color == "(255,242,0)":
    return "Y"
  else:
    return color
  
output_file = open("output.txt", "w")

image_file = Image.open("./smiley.png")
image_file.load()

width,height = image_file.size

for line in range(height):
 for pixel in range(width):
    color = str(image_file.getpixel((pixel, line)))
    color = convert(color)
    output_file.write(color)
    output_file.write(" ")
    output_file.write("\n")

output_file.close()


#for line in lines:
 #for pixel in line:
  #color = getColor(pixel)
  #print(color)
#print(";\n")

# 4. Write a program that consumes pixel values and creates an image.

def convert(color):
    if color == "R":
        return (237, 28, 36)
    elif color == "B":
        return (0, 0, 0)
    elif color == "Y":
        return (255, 242, 0)
    else:
        return color
input_text_file = open("input.txt", "r")
lines = input_text_file.readlines()

width, height = lines[0].count(" "), len(lines)

output_image_file = Image.new("RGB", (width, height))

output_image_file.save("output.png")

for y in range(height):
  line = lines[y]
  pixels = line.split()
  for x in range(width):
    pixel = pixels[x]
    pixel = convert(pixel)
    output_image_file.putpixel((x,y), pixel)

output_image_file.save("output.png")
input_text_file.close()

# 5. Test boundary cases, including zero, the largest supported unsigned value, and at least one negative two's-complement value.
print("Zero:", bin(0))
print("Largest unsigned value:", bin(255))
print("Negative value:", bin(128))