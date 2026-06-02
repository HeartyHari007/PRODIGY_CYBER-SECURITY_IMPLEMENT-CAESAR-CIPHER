Working Principle (Caesar Cipher Analogy)

This Image Encryption Tool works similarly to the famous Caesar Cipher encryption technique.

In a Caesar Cipher, each letter in a message is shifted by a fixed number of positions.

Example

Original Text:

HELLO

Key = 3

Encrypted Text:

KHOOR

Each character is shifted by 3 positions.

Applying the Same Concept to Images

Instead of shifting letters, this project shifts the RGB values of every pixel in the image using a secret key.

Example Pixel

Original Pixel:

(R, G, B) = (120, 200, 50)

Key = 50

Encrypted Pixel:

(R, G, B) = (170, 250, 100)

Each color value is shifted by the key value, similar to how letters are shifted in Caesar Cipher.

Encryption Formula

EncryptedPixel=(OriginalPixel+Key)mod256

The modulo operation ensures that pixel values remain within the valid RGB range (0–255).

Decryption Process

To recover the original image, the same secret key is used in reverse.

Encrypted Pixel:

(170, 250, 100)

Key = 50

Decrypted Pixel:

(120, 200, 50)
Decryption Formula

OriginalPixel=(EncryptedPixel−Key)mod256

Algorithm
Encryption
Load the image.
Read each pixel's RGB values.
Add the secret key to each RGB component.
Apply modulo 256 to keep values within range.
Save the encrypted image.
Decryption
Load the encrypted image.
Read each pixel's RGB values.
Subtract the secret key from each RGB component.
Apply modulo 256.
Save the decrypted image.
Comparison with Caesar Cipher
Caesar Cipher	Image Encryption Tool
Encrypts text characters	Encrypts image pixels
Shifts letters by a key	Shifts RGB values by a key
Uses alphabet positions	Uses pixel color values
Decrypts using reverse shift	Decrypts using reverse pixel shift
Educational cryptography method	Educational image security method
Conclusion

This project demonstrates how the fundamental idea of the Caesar Cipher can be extended from text encryption to image encryption by treating pixel values as data elements and shifting them using a secret key. While simple, it provides a practical introduction to image processing and basic cryptographic concepts.
