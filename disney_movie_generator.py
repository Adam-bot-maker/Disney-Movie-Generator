import random

def generate_disney_movie():
    protagonists = ["a brave princess", "a curious young boy", "a kind-hearted animal", "an adventurous teenager", "a shy inventor"]
    sidekicks = ["a talking snowman", "a magical bird", "a sassy dragon", "a loyal dog", "a comedic genie"]
    villains = ["a wicked sorcerer", "a greedy businessman", "a jealous sibling", "an evil queen", "a cunning thief"]
    magical_elements = ["a spellbook", "a glowing crystal", "a golden lamp", "a magical tree", "an enchanted necklace"]
    settings = ["a bustling kingdom", "a mystical forest", "a peaceful village", "a vast ocean", "a futuristic city"]

    protagonist = random.choice(protagonists)
    sidekick = random.choice(sidekicks)
    villain = random.choice(villains)
    magical_element = random.choice(magical_elements)
    setting = random.choice(settings)

    plot = (f"In {setting}, {protagonist} discovers {magical_element}. "
            f"With the help of {sidekick}, they must stop {villain} and "
            "restore peace to their world.")
    
    return plot

if __name__ == "__main__":
    print("Welcome to the Disney Movie Generator!")
    print("Here's your movie plot:")
    print(generate_disney_movie())