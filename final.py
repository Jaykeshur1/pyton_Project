import random
import tkinter as tk
from tkinter import messagebox

def randomgenre():
    genre_list = ["fantasy", "mystery", "science fiction"]
    select_random = random.choice(genre_list)
    return select_random

def generate_story(genre, num_words):
    if genre == "fantasy":
        story = generate_fantasy_story(num_words)
    elif genre == "mystery":
        story = generate_mystery_story(num_words)
    elif genre == "science fiction":
        story = generate_science_fiction_story(num_words)
    else:
        genre = randomgenre()
        if genre == "fantasy":
            story = generate_fantasy_story(num_words)
        elif genre == "mystery":
            story = generate_mystery_story(num_words)
        elif genre == "science fiction":
            story = generate_science_fiction_story(num_words)
    return story

def generate_fantasy_story(num_words):
    characters = ["wizard", "elf", "dwarf", "princess", "dragon", "knight", "sorceress"]
    places = ["castle", "forest", "cave", "mountain", "enchanted land", "underwater kingdom"]
    actions = ["cast a spell", "embark on a quest", "fight against evil", "find a hidden treasure", "rescue a captured ally", "confront a dark prophecy"]
    objects = ["magic wand", "enchanted amulet", "ancient artifact", "flying broomstick", "magical potion"]

    story = []
    current_words = 0
    while current_words < num_words:
        character = random.choice(characters)
        place = random.choice(places)
        action = random.choice(actions)
        object = random.choice(objects)

        sentence = f"a {character} ventured into the {place}. With bravery and wisdom, the {character} {action} using a {object}."
        words = sentence.split()
        if current_words + len(words) <= num_words:
            story += words
            current_words += len(words)
        else:
            break

    if num_words == 1:
        story = random.choice(story)  # Choose a random word
    else:
        story += ["Along", "the", "way,", "the", "character", "encountered", "mythical", "creatures", "and", "overcame", "perilous", "challenges,", "proving", "their", "worth", "and", "unlocking", "their", "true", "potential."]

    return " ".join(story)


def generate_mystery_story(num_words):
    characters = ["detective", "police officer", "journalist", "sleuth", "private investigator", "forensic expert"]
    places = ["mansion", "crime scene", "city", "small town", "abandoned warehouse", "luxury hotel"]
    actions = ["solve a murder", "unravel a conspiracy", "find a missing person", "uncover a secret", "decode a cryptic message", "expose a corrupt organization"]
    clues = ["mysterious note", "hidden document", "bloodstained knife", "cryptic symbol", "surveillance footage", "missing diary"]

    story = []
    current_words = 0
    while current_words < num_words:
        character = random.choice(characters)
        place = random.choice(places)
        action = random.choice(actions)
        clue = random.choice(clues)

        sentence = f"a {character} set out to {action}. As clues were pieced together, the {character} discovered a {clue}."
        words = sentence.split()
        if current_words + len(words) <= num_words:
            story += words
            current_words += len(words)
        else:
            break

    if num_words == 1:
        story = random.choice(story)  # Choose a random word
    else:
        story += ["Each", "revelation", "deepened", "the", "mystery,", "leading", "the", "character", "closer", "to", "the", "truth,", "but", "also", "placing", "their", "own", "life", "in", "danger."]

    return " ".join(story)


def generate_science_fiction_story(num_words):
    characters = ["space explorer", "robot", "alien", "scientist", "cyborg", "telepath"]
    places = ["spaceship", "distant planet", "cybernetic world", "future Earth", "asteroid colony", "virtual reality realm"]
    actions = ["save humanity", "uncover the secrets of the universe", "battle against rogue AI", "discover a new dimension", "defend against an alien invasion", "hack into a high-security network"]
    technology = ["advanced AI", "time-travel device", "nanotechnology", "augmented reality implants", "hyperspace engine"]

    story = []
    current_words = 0
    while current_words < num_words:
        character = random.choice(characters)
        place = random.choice(places)
        action = random.choice(actions)
        tech = random.choice(technology)

        sentence = f"a {character} embarked on a journey to {action} in the vast expanse of the {place}. Equipped with {tech}, the {character} faced unimaginable challenges and encountered extraterrestrial civilizations, pushing the boundaries of human understanding."
        words = sentence.split()
        if current_words + len(words) <= num_words:
            story += words
            current_words += len(words)
        else:
            break

    if num_words == 1:
        story = random.choice(story) 

    return " ".join(story)

def generate_and_display_story():
    try:
        genre = genre_var.get()
        num_words = int(num_words_entry.get())
        if num_words < 1:
            raise ValueError("Number of words should be greater than 0.")

        user_name = name_entry.get().strip()
        greeting_message = f"Hello {user_name}!"

        story = generate_story(genre, num_words)
        story_text.delete("1.0", tk.END)
        story_text.insert(tk.END, greeting_message + "\n\n" + story)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("Story Generator")

# Create the GUI components
name_label = tk.Label(app, text="Hello Reader")
name_label.pack()

name_label = tk.Label(app, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

genre_label = tk.Label(app, text="Enter a genre:")
genre_label.pack()

genre_var = tk.StringVar()
genre_var.set("fantasy")  # Set default value
genre_option_menu = tk.OptionMenu(app, genre_var, "fantasy", "mystery", "science fiction")
genre_option_menu.pack()

num_words_label = tk.Label(app, text="Enter the number of lines you want in the story:")
num_words_label.pack()

num_words_entry = tk.Entry(app)
num_words_entry.pack()

generate_button = tk.Button(app, text="Generate Story", command=generate_and_display_story)
generate_button.pack()

# Add a scroll bar to the story text area
scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

story_text = tk.Text(app, wrap=tk.WORD, width=40, height=10, yscrollcommand=scrollbar.set)
story_text.pack()

# Configure the scrollbar to work with the text area
scrollbar.config(command=story_text.yview)

# Start the main event loop
app.mainloop()
