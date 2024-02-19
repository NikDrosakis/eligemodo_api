import random
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from fimg import search_unsplash_image


def trivial():
    filename = 'dataset/'++'.csv'
    concap = pd.read_csv(filename)
    n = len(concap.index)
    df = pd.read_csv(filename).to_dict()
    chosen = random.randint(0, n-1)
    chosencountry = df['CountryName'][chosen]
    # Give three more choices
    print("Which is the capital of: " + chosencountry + "?")
    # Create a dict without chosen adding chosen
    others = list(range(0, n-1))
    others.remove(chosen)
    otherchoices = random.sample(others, 3)
    otherchoices.append(chosen)
    random.shuffle(otherchoices)

    # Create a dictionary with choices
    choices_dict = {}
    for index, value in enumerate(otherchoices):
        choices_dict[index+1] = df['CapitalName'][value]

    # Shuffle the choices
    shuffled_choices = {str(key): value for key, value in choices_dict.items()}
    # Include the correct answer in the response
    correct_answer = df['CapitalName'][chosen]
    #get img from unsplash
    imageUrl = search_unsplash_image(correct_answer)
    # Return a JSON response
    response = {
        "question": f"Which is the capital of: {chosencountry}?",
        "choices": shuffled_choices,
        "correct": correct_answer,
        "imageUrl": imageUrl,
    }

    return response

# Example usage:

#print(result)
