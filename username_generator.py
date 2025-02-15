import random
import string


adjectives = ["Happy", "Brave", "Cool", "Clever", "Lucky", "Fierce", "Witty", "Jolly", "Swift", "Bold"]
nouns = ["Tiger", "Dragon", "Eagle", "Wizard", "Knight", "Panther", "Fox", "Lion", "Ninja", "Samurai"]

def generate_username(user_name, fav_letter, add_number=False, add_special_char=False, custom_length=None):
    """Generates a random username based on user preferences."""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

   
    if fav_letter and fav_letter.isalpha():
        fav_letter = fav_letter.upper()
        possible_names = [word for word in adjectives + nouns if word.startswith(fav_letter)]
        if possible_names:
            first_word = random.choice(possible_names)
        else:
            first_word = adjective 
    else:
        first_word = adjective  

    username = first_word + noun 

   
    if user_name:
        username = user_name.capitalize() + username

    if add_number:
        username += str(random.randint(10, 99))  

    if add_special_char:
        username += random.choice("!@#$%^&*") 

   
    if custom_length:
        username = username[:custom_length] 

    return username

def save_to_file(username, filename="usernames.txt"):
    """Saves the generated username to a text file."""
    with open(filename, "a") as file:
        file.write(username + "\n")
    print(f"✅ Username '{username}' saved to {filename}")

def main():
    """Main function to interact with the user and generate usernames."""
    print("🎮 Welcome to the Personalized Username Generator! 🎮\n")

  
    user_name = input("Enter your name: ").strip().capitalize()
    fav_letter = input("Enter your favorite alphabet (A-Z): ").strip().upper()

    num_usernames = int(input("How many usernames would you like to generate? "))

    add_number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special_char = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    custom_length = input("Enter max username length (or press Enter for default): ").strip()
    custom_length = int(custom_length) if custom_length.isdigit() else None

   
    usernames = [generate_username(user_name, fav_letter, add_number, add_special_char, custom_length) for _ in range(num_usernames)]

    print("\n🎉 Generated Usernames:")
    for name in usernames:
        print(f"🔹 {name}")
        save_to_file(name)

if __name__ == "__main__":
    main()
