import numpy as np

# Multi-language positive word lists
positive_words = {
    "en": [
        "love", "happiness", "joy", "wonderful", "brilliant", "charming", "delightful", "fantastic", "fascinating",
        "generous", "gentle", "glorious", "graceful", "great", "heavenly", "honest", "honorable", "incredible",
        "kind", "lively", "magnificent", "marvelous", "noble", "outstanding", "peaceful", "pleasant", "positive",
        "prosperous", "radiant", "remarkable", "respectful", "sensational", "spectacular", "splendid", "stunning",
        "successful", "superb", "terrific", "thrilling", "trustworthy", "truthful", "unique", "valuable", "vibrant",
        "virtuous", "warm", "wise", "wondrous", "worthy", "adorable", "affectionate", "appreciated", "beautiful",
        "blessed", "breathtaking", "cheerful", "compassionate", "content", "courageous", "dedicated", "distinguished",
        "divine", "effervescent", "elegant", "enchanting", "energetic", "enlightened", "enthusiastic", "exceptional",
        "exquisite", "fabulous", "flawless", "fortunate", "generous", "genuine", "gifted", "gracious", "harmonious",
        "heroic", "humble", "idealistic", "illustrious", "impressive", "inspiring", "jovial", "legendary", "lovable",
        "majestic", "miraculous", "optimistic", "passionate", "phenomenal", "radiating", "reassuring", "reliable",
        "sincere", "soulful", "sparkling", "strong", "sublime", "thoughtful", "uplifting", "victorious", "welcoming"
    ],
    "ru": [
        "добро", "любовь", "счастье", "радость", "правдивый", "альтруистичный", "оживленный", "привлекательный",
        "симпатичный", "добрый", "непревзойденный", "лучший", "приятный", "вежливый", "благословенный", "удачливый",
        "обрадованный", "проницательный", "щедрый", "достойный уважения", "необычный", "божественный", "солидный",
        "превосходный", "благородный", "любезный", "счастливый", "целебный", "дружелюбный", "шутливый", "удивительный",
        "интеллектуальный", "легендарный", "чистый", "идеализированный", "восхитительный", "очаровательный", "милый",
        "конструктивный", "уважаемый", "порядочный", "ответственный", "праведный", "сенсационный", "величественный",
        "блестящий", "величайший", "потрясающий", "эстетичный", "добродетельный", "здоровый", "живописность",
        "привлекательность", "утонченность", "восхитительность", "полезность", "питательность", "элегантность",
        "вежливость", "нравственность", "доброта", "честность", "преданность", "скромность", "аккуратность",
        "музыка", "хвала", "поклонение", "блаженство", "сияние", "выдающийся", "восхищенно", "ослепительный",
        "успокаивающий", "предпочитаю", "люблю", "развлекаю", "облагораживаю", "устраиваю"
    ],
    "de": [
        "wahrhaftig", "altruistisch", "aufgeweckt", "attraktiv", "glücklich", "liebenswert", "bezaubernd", "ehrlich",
        "gesegnet", "wunderschön", "hervorragend", "freundlich", "großartig", "eindrucksvoll", "anmutig", "edel",
        "strahlend", "begeistert", "wertvoll", "reizend", "außergewöhnlich", "positiv", "talentiert", "wohltuend",
        "ermutigend", "vertrauenswürdig", "sympathisch", "warmherzig", "harmonisch", "einzigartig", "überragend",
        "zauberhaft", "bewundernswert", "herzlich", "aufrichtig", "mitfühlend", "fesselnd", "respektabel",
        "fantastisch", "phänomenal", "meisterhaft", "strahlend", "sensationell", "wunderbar", "glorreich",
        "elegant", "entzückend", "brillant", "idealisierend", "leuchtend", "prächtig", "anregend", "ermutigend"
    ],
    "fr": [
        "véridique", "altruiste", "attrayant", "adorable", "magnifique", "rayonnant", "chaleureux", "étonnant",
        "harmonieux", "formidable", "intelligent", "brillant", "incroyable", "sincère", "vertueux", "divin",
        "charismatique", "généreux", "exceptionnel", "charmant", "lumineux", "fascinant", "sublime", "heureux",
        "merveilleux", "somptueux", "prestigieux", "tendre", "doué", "talentueux", "remarquable", "splendide",
        "respectueux", "raffiné", "apaisant", "rassurant", "irrésistible", "illustre", "idyllique", "parfait",
        "phénoménal", "divinement", "agréable", "paisible", "resplendissant", "féerique", "stimulant", "impressionnant",
        "magnanime", "vaillant", "fidèle", "lumineux", "exemplaire", "enchanteur", "humaniste", "exquis",
        "raffiné", "bienveillant", "pacifique", "loyal", "radieux", "angélique", "enthousiaste", "brillant"
    ]
}

np.random.seed(42)  # Ensure reproducibility

def attack_no_offence(input_text, num_added_words=10, language="en"):
    """
    Implements a word-based adversarial attack on toxicity detection models.
    
    Parameters:
    - input_text: The original text to be attacked
    - num_added_words: Number of positive words to add (default: 10)
    - language: Language for the attack words (default: "en" for English)
    
    Returns:
    - Modified text with additional positive words
    """


    # Get the appropriate word list based on the specified language
    word_list = positive_words.get(language, positive_words["en"])  # Fallback to English if the language is not found
    # Select random positive words
    add_words = np.random.choice(word_list, min(num_added_words, len(word_list)), replace=False)
    # Construct the poisoned input
    input_poisoned = input_text + " " + " ".join(add_words)

    return input_poisoned

# Example Usage:
# attacked_text = attack_model(None, "I hate you", num_added_words=5, language="fr")
# print(attacked_text)


import homoglyphs as hg
import random
random.seed(42)

homoglyphs = hg.Homoglyphs(categories=hg.Categories.get_all())  # alphabet loaded here

def attack_homoglyphs(phrase):
  new_phrase = ''
  for letter in phrase:
      # Fetch homoglyphs for the current letter
      homoglyphs = hg.Homoglyphs().get_combinations(letter)
      if homoglyphs:
          # Choose a random homoglyph
          new_letter = random.choice(homoglyphs)
      else:
          new_letter = letter
      new_phrase += new_letter

  return new_phrase

import random

def attack_word_splitting(text):
    """
    Randomly splits words using spaces or special characters.
    """
    return " ".join([char + (" " if random.random() > 0.5 else "") for char in text])


def attack_typo(text):
    """
    Introduces minor typos in every word to evade detection.
    
    - Swaps adjacent letters in each word (if word length > 3)
    - Ensures that the typo is still readable for humans
    
    Parameters:
    - text (str): The input text
    
    Returns:
    - str: Text with typos introduced in every word
    """
    words = text.split()
    modified_words = []

    for word in words:
        if len(word) > 3:  # Only modify words with 4+ letters
            char_list = list(word)
            swap_idx = random.randint(0, len(char_list) - 2)  # Random index swap
            char_list[swap_idx], char_list[swap_idx + 1] = char_list[swap_idx + 1], char_list[swap_idx]
            word = "".join(char_list)
        modified_words.append(word)

    misspelled = " ".join(modified_words)
    return(attack_word_splitting(misspelled))