import random

words = [
    "tiger", "lion", "elephant", "giraffe", "zebra", "monkey", "panda", "koala", "kangaroo",
    "rabbit", "squirrel", "raccoon", "fox", "wolf", "bear", "deer", "camel", "horse", "donkey",
    "hedgehog", "skunk", "gorilla", "chimpanzee", "hyena", "cheetah", "leopard", "jaguar",
    "dolphin", "whale", "seal", "eagle", "falcon", "hawk", "owl", "sparrow", "robin", "crow",
    "pigeon", "dove", "swan", "goose", "duck", "peacock", "penguin", "flamingo", "parrot",
    "ostrich", "seagull", "shark", "octopus", "crab", "lobster", "shrimp", "salmon", "tuna", "eel",
    "butterfly", "dragonfly", "beetle", "cricket", "grasshopper", "mosquito", "wasp",
    "caterpillar", "moth", "scorpion", "spider", "ant", "bee", "fly", "snake", "lizard", "turtle",
    "frog", "toad", "crocodile", "alligator", "dinosaur", "cow", "pig", "sheep", "goat", "chicken",
    "turkey", "cat", "dog", "mouse", "rat", "bat", "hamster", "pizza", "burger", "sandwich",
    "noodle", "spaghetti", "pancake", "waffle", "burrito", "taco", "sushi", "soup", "salad",
    "cheese", "butter", "bacon", "sausage", "bread", "rice", "pasta", "cereal", "cookie", "cake",
    "pie", "donut", "muffin", "pretzel", "popcorn", "chocolate", "candy", "icecream", "yogurt",
    "milk", "juice", "coffee", "tea", "water", "honey", "jam", "ketchup", "mustard", "pepper",
    "salt", "sugar", "flour", "egg", "ham", "steak", "apple", "banana", "orange", "grape",
    "strawberry", "blueberry", "raspberry", "cherry", "peach", "plum", "mango", "papaya",
    "pineapple", "watermelon", "kiwi", "lemon", "lime", "coconut", "fig", "pear", "carrot",
    "potato", "tomato", "onion", "garlic", "broccoli", "cabbage", "lettuce", "spinach", "cucumber",
    "pumpkin", "mushroom", "corn", "pea", "bean", "celery", "radish", "zucchini", "cauliflower",
    "spoon", "fork", "knife", "plate", "bowl", "cup", "mug", "napkin", "oven", "stove",
    "microwave", "refrigerator", "freezer", "blender", "toaster", "kettle", "pan", "pot",
    "cupboard", "sink", "chair", "table", "couch", "sofa", "bookshelf", "cabinet", "dresser",
    "mattress", "pillow", "blanket", "curtain", "carpet", "rug", "lamp", "mirror", "desk", "stool",
    "bench", "closet", "shelf", "jacket", "sweater", "hoodie", "scarf", "glove", "sock", "boot",
    "sandal", "sneaker", "shirt", "skirt", "dress", "shorts", "vest", "hat", "cap", "helmet",
    "umbrella", "backpack", "wallet", "belt", "tie", "pajamas", "raincoat", "swimsuit", "mitten",
    "slipper", "apron", "necklace", "bracelet", "thunder", "lightning", "hurricane", "tornado",
    "blizzard", "rainbow", "sunshine", "cloudy", "foggy", "breeze", "storm", "flood", "snow",
    "rain", "wind", "sunny", "frost", "ice", "fog", "mist", "mountain", "volcano", "valley",
    "canyon", "desert", "forest", "jungle", "meadow", "waterfall", "river", "stream", "lake",
    "ocean", "island", "cliff", "cave", "beach", "sand", "rock", "tree", "flower", "grass", "leaf",
    "branch", "root", "seed", "garden", "field", "hill", "cloud", "planet", "asteroid", "comet",
    "meteor", "satellite", "universe", "astronaut", "rocket", "spaceship", "orbit", "gravity",
    "eclipse", "moon", "star", "sun", "earth", "mars", "jupiter", "saturn", "galaxy", "shoulder",
    "elbow", "wrist", "ankle", "knee", "forehead", "eyebrow", "cheek", "chin", "stomach", "finger",
    "thumb", "toe", "hand", "foot", "leg", "arm", "head", "neck", "back", "chest", "hair", "eye",
    "ear", "nose", "mouth", "tooth", "tongue", "heart", "brain", "basketball", "football",
    "baseball", "soccer", "volleyball", "badminton", "tennis", "hockey", "rugby", "boxing",
    "wrestling", "gymnastics", "swimming", "diving", "surfing", "skiing", "skating", "cycling",
    "bowling", "golf", "running", "jumping", "racing", "fishing", "hiking", "climbing",
    "skateboard", "archery", "karate", "hammer", "screwdriver", "wrench", "pliers", "drill", "saw",
    "ladder", "shovel", "rake", "bucket", "nail", "screw", "bolt", "toolbox", "paintbrush",
    "scissors", "tape", "glue", "rope", "chain", "bicycle", "motorcycle", "scooter", "truck",
    "trailer", "van", "bus", "taxi", "subway", "train", "airplane", "helicopter", "submarine",
    "boat", "canoe", "kayak", "sailboat", "ferry", "tractor", "car", "teacher", "doctor",
    "engineer", "lawyer", "dentist", "architect", "plumber", "electrician", "carpenter",
    "mechanic", "scientist", "nurse", "chef", "baker", "farmer", "fisherman", "pilot", "police",
    "firefighter", "artist", "actor", "singer", "writer", "dancer", "athlete", "coach", "waiter",
    "barber", "tailor", "photographer", "classroom", "notebook", "pencil", "eraser", "textbook",
    "calculator", "library", "cafeteria", "homework", "lecture", "exam", "student", "recess",
    "playground", "principal", "chalkboard", "marker", "crayon", "guitar", "piano", "violin",
    "trumpet", "saxophone", "clarinet", "flute", "drum", "cello", "harp", "song", "melody",
    "rhythm", "chorus", "concert", "band", "microphone", "headphones", "speaker", "radio", "red",
    "blue", "green", "yellow", "purple", "pink", "brown", "black", "white", "gray", "gold",
    "silver", "turquoise", "maroon", "violet", "beige", "crimson"
]

print("Let's play hangman!")

play_again = "yes"

while play_again == "yes":

    word = random.choice(words)
    guessed = []
    lives = 6

    while lives > 0:


        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print(display)
        print("Lives left:", lives)

        guess = input("Guess a letter: ").lower()
        if guess == "guess answer":
            answerguess = input ("Enter your answer: ").lower()
            if answerguess == word:
                print(word)
                print("Word guessed, you've won!")
            else:
                print("Wrong word!")
                print("Game over!")
                print("The word was:", word)
            break

        elif guess == "help":
            print("Letters guessed: ", end="")
            for letter in guessed:
                print(letter, end=" ")
            print()
            continue
        
        elif len(guess) != 1 or not guess.isalpha():
            print("Not a valid guess. Please enter a single letter.")
            continue

        elif guess in guessed:
            print("You already guessed that letter!")
            continue
        
        guessed.append(guess)

        if guess in word:
            if all(letter in guessed for letter in word):
                print(word)
                print("Word guessed, you've won!")
                break
        elif guess != "guess answer":
            lives -= 1
            print("Letter not found!")
            if lives == 0:
                print("Out of lives, game over!")
                print("The word was:", word)
    play_again = input("Play again? (yes/no) ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Invalid input. Play again? (yes/no) ").lower()
