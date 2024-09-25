import requests
import os

def prepare_image(image_path):
    with open(image_path, "rb") as img_file:
        return img_file.read()

def identify_bird(image_path):
    api_url = "https://api.bird-id.com/identify"
    api_key = "your_api_key_here"

    image_data = prepare_image(image_path)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(api_url, headers=headers, data=image_data)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def display_bird_info(bird_info):
    print("Bird identified!")
    print(f"Species: {bird_info['species']}")
    print(f"Migration patterns: {bird_info['migration']}")
    print(f"Physical description: {bird_info['description']}")

def main():
    print("Welcome to the Bird Watcher App!")
    image_path = input("Please enter the path to the bird image: ")

    if os.path.exists(image_path):
        bird_info = identify_bird(image_path)
        if bird_info:
            display_bird_info(bird_info)
        else:
            print("Sorry, no bird identified.")
    else:
        print("Image file not found. Please try again.")

if __name__ == "__main__":
    main()
