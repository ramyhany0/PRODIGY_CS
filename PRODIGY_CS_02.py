import numpy as np
from PIL import Image

def encrypt_image(image_path, operation, key):
    """
    Encrypts an image using pixel manipulation.

    Args:
        image_path (str): The path to the image file.
        operation (str): The encryption operation to perform (e.g., 'swap', 'add', 'multiply').
        key (int): The encryption key.

    Returns:
        np.ndarray: The encrypted image data.
    """
    image = Image.open(image_path)
    image_data = np.array(image)

    if operation == 'swap':
        encrypted_data = swap_pixels(image_data, key)
    elif operation == 'add':
        encrypted_data = add_to_pixels(image_data, key)
    elif operation == 'multiply':
        encrypted_data = multiply_pixels(image_data, key)
    else:
        raise ValueError("Invalid operation")

    return encrypted_data

def decrypt_image(encrypted_data, operation, key):
    """
    Decrypts an encrypted image using pixel manipulation.

    Args:
        encrypted_data (np.ndarray): The encrypted image data.
        operation (str): The decryption operation to perform (e.g., 'swap', 'add', 'multiply').
        key (int): The decryption key.

    Returns:
        np.ndarray: The decrypted image data.
    """
    if operation == 'swap':
        decrypted_data = swap_pixels(encrypted_data, -key)
    elif operation == 'add':
        decrypted_data = add_to_pixels(encrypted_data, -key)
    elif operation == 'multiply':
        decrypted_data = multiply_pixels(encrypted_data, 1 / key)
    else:
        raise ValueError("Invalid operation")

    return decrypted_data

def swap_pixels(image_data, key):
    """
    Swaps pixel values with a specified offset.

    Args:
        image_data (np.ndarray): The image data.
        key (int): The offset value.

    Returns:
        np.ndarray: The modified image data.
    """
    rows, cols, _ = image_data.shape
    for i in range(rows):
        for j in range(cols):
            image_data[i, j] = image_data[(i + key) % rows, (j + key) % cols]
    return image_data

def add_to_pixels(image_data, key):
    """
    Adds a specified value to each pixel.

    Args:
        image_data (np.ndarray): The image data.
        key (int): The value to add.

    Returns:
        np.ndarray: The modified image data.
    """
    image_data += key
    return image_data

def multiply_pixels(image_data, key):
    """
    Multiplies each pixel by a specified value.

    Args:
        image_data (np.ndarray): The image data.
        key (int): The value to multiply.

    Returns:
        np.ndarray: The modified image data.
    """
    image_data *= key
    return image_data

def main():
    while True:
        print("Image Encryption Tool")
        print("---------------------")
        print("1. Encrypt image")
        print("2. Decrypt image")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("Enter the image path: ")
            operation = input("Enter the encryption operation (swap, add, multiply): ")
            key = int(input("Enter the encryption key: "))
            encrypted_data = encrypt_image(image_path, operation, key)
            encrypted_image = Image.fromarray(encrypted_data)
            encrypted_image.save("encrypted_image.png")
            print("Encrypted image saved as encrypted_image.png")
        elif choice == "2":
            encrypted_image_path = input("Enter the encrypted image path: ")
            operation = input("Enter the decryption operation (swap, add, multiply): ")
            key = int(input("Enter the decryption key: "))
            encrypted_image = Image.open(encrypted_image_path)
            encrypted_data = np.array(encrypted_image)
            decrypted_data = decrypt_image(encrypted_data, operation, key)
            decrypted_image = Image.fromarray(decrypted_data)
            decrypted_image.save("decrypted_image.png")
            print("Decrypted image saved as decrypted_image.png")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()