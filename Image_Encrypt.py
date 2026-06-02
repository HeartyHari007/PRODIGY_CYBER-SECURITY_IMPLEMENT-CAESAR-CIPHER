from PIL import Image

def encrypt_image(input_image, output_image, key):
    try:
        # Open image and convert to RGB
        img = Image.open(input_image).convert("RGB")
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Encrypt pixel values
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

                pixels[x, y] = (r, g, b)

        img.save(output_image)
        print(f"\n✅ Encrypted image saved as: {output_image}")

    except Exception as e:
        print(f"\n❌ Error during encryption: {e}")


def decrypt_image(input_image, output_image, key):
    try:
        # Open image and convert to RGB
        img = Image.open(input_image).convert("RGB")
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Decrypt pixel values
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

                pixels[x, y] = (r, g, b)

        img.save(output_image)
        print(f"\n✅ Decrypted image saved as: {output_image}")

    except Exception as e:
        print(f"\n❌ Error during decryption: {e}")


# ---------------- MAIN PROGRAM ---------------- #

print("===================================")
print("      IMAGE ENCRYPTION TOOL")
print("===================================")

choice = input("Enter E for Encrypt or D for Decrypt: ").strip().upper()

input_file = input("Enter image file path: ").strip().strip('"')
output_file = input("Enter output image name: ").strip().strip('"')

try:
    key = int(input("Enter secret key (0-255): "))

    if key < 0 or key > 255:
        print("❌ Key must be between 0 and 255.")

    elif choice == "E":
        encrypt_image(input_file, output_file, key)

    elif choice == "D":
        decrypt_image(input_file, output_file, key)

    else:
        print("❌ Invalid choice! Enter E or D.")

except ValueError:
    print("❌ Please enter a valid numeric key.")