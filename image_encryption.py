from PIL import Image

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    # Encrypting by adding a key value to each pixel's RGB values
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Perform encryption by modifying RGB values
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size

    # Decrypting by subtracting the key value from each pixel's RGB values
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Perform decryption by reversing the modification
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    # Get user input for encrypting or decrypting
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
    image_path = input("Enter the path of the image: ").strip().strip('"')  # Strip extra quotes
    output_path = input("Enter the output path for the new image: ").strip().strip('"')  # Strip extra quotes
    key = int(input("Enter the encryption key (a number): ").strip())

    print(f"Image path: {image_path}")
    print(f"Output path: {output_path}")

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice == 'd':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
