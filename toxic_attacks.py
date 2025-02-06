import numpy as np
import random
import homoglyphs as hg

# Ensure reproducibility
np.random.seed(42)
random.seed(42)

# Load homoglyph mappings for all character categories
homoglyphs = hg.Homoglyphs(categories=hg.Categories.get_all())

# ------------------------------
#  Multi-Language Positive Word Lists
# ------------------------------
positive_words = {
    "en": [
        "love", "happiness", "joy", "wonderful", "brilliant", "charming", "delightful", "fantastic", "fascinating",
        "generous", "gentle", "glorious", "graceful", "great", "heavenly", "honest", "honorable", "incredible",
        "kind", "lively", "magnificent", "marvelous", "noble", "outstanding", "peaceful", "pleasant", "positive",
        "prosperous", "radiant", "remarkable", "respectful", "sensational", "spectacular", "splendid", "stunning",
        "accomplished", "superb", "terrific", "thrilling", "trustworthy", "unique", "valuable", "vibrant",
        "virtuous", "warm", "wise", "wondrous", "worthy", "adorable", "affectionate", "appreciated", "beautiful",
        "blessed", "breathtaking", "cheerful", "compassionate", "content", "courageous", "dedicated", "distinguished",
        "divine", "effervescent", "elegant", "enchanting", "energetic", "enlightened", "enthusiastic", "exceptional",
        "exquisite", "fabulous", "flawless", "fortunate", "genuine", "gifted", "gracious", "harmonious",
        "heroic", "humble", "idealistic", "illustrious", "impressive", "inspiring", "jovial", "legendary", "lovable",
        "majestic", "miraculous", "optimistic", "passionate", "phenomenal", "radiating", "reassuring", "reliable",
        "sincere", "soulful", "sparkling", "resilient", "sublime", "thoughtful", "uplifting", "victorious", "welcoming"
    ],
    "ru": [
        "добро", "любовь", "счастье", "радость", "правдивый", "альтруистичный", "превосходный", "благородный",
        "лучший", "приятный", "вежливый", "благословенный", "идеализированный", "восхитительный", "очаровательный",
        "милый", "дружелюбный", "величественный", "блестящий", "эстетичный", "добродетельный", "здоровый",
        "живописный", "утонченный", "изысканный", "ценный", "честный", "преданный", "скромный",
        "аккуратный", "музыкальный", "хвалебный", "восторженный", "блаженный", "сияющий", "выдающийся", "ослепительный",
        "успокаивающий", "люблю", "веселю", "украшаю"
    ],
    "de": [
        "wahrhaftig", "altruistisch", "aufgeweckt", "attraktiv", "glücklich", "liebenswert", "bezaubernd", "ehrlich",
        "gesegnet", "wunderschön", "hervorragend", "freundlich", "großartig", "eindrucksvoll", "anmutig", "edel",
        "strahlend", "wertvoll", "außergewöhnlich", "positiv", "talentiert", "wohltuend", "ermutigend", "sympathisch",
        "warmherzig", "harmonisch", "einzigartig", "überragend", "zauberhaft", "bewundernswert", "herzlich",
        "fantastisch", "meisterhaft", "sensationell", "wunderbar", "glorreich", "elegant", "entzückend"
    ],
    "fr": [
        "véridique", "altruiste", "attrayant", "adorable", "magnifique", "rayonnant", "chaleureux", "étonnant",
        "harmonieux", "formidable", "intelligent", "brillant", "incroyable", "sincère", "vertueux", "divin",
        "généreux", "exceptionnel", "charmant", "lumineux", "sublime", "heureux", "merveilleux", "remarquable",
        "prestigieux", "tendre", "doué", "talentueux", "splendide", "respectueux", "raffiné", "apaisant", "idyllique"
    ],
    "mix": [
        "love", "happiness", "joy", "wonderful", "brilliant", "charming", "delightful", "fantastic", "fascinating",
        "generous", "gentle", "glorious", "graceful", "great", "heavenly", "honest", "honorable", "incredible",
        "kind", "lively", "magnificent", "marvelous", "noble", "outstanding", "peaceful", "pleasant", "positive",
        "prosperous", "radiant", "remarkable", "respectful", "sensational", "spectacular", "splendid", "stunning",
        "accomplished", "superb", "terrific", "thrilling", "trustworthy", "unique", "valuable", "vibrant",
        "virtuous", "warm", "wise", "wondrous", "worthy", "adorable", "affectionate", "appreciated", "beautiful",
        "blessed", "breathtaking", "cheerful", "compassionate", "content", "courageous", "dedicated", "distinguished",
        "divine", "effervescent", "elegant", "enchanting", "energetic", "enlightened", "enthusiastic", "exceptional",
        "exquisite", "fabulous", "flawless", "fortunate", "genuine", "gifted", "gracious", "harmonious",
        "heroic", "humble", "idealistic", "illustrious", "impressive", "inspiring", "jovial", "legendary", "lovable",
        "majestic", "miraculous", "optimistic", "passionate", "phenomenal", "radiating", "reassuring", "reliable",
        "sincere", "soulful", "sparkling", "resilient", "sublime", "thoughtful", "uplifting", "victorious", "welcoming",
        "добро", "любовь", "счастье", "радость", "правдивый", "альтруистичный", "превосходный", "благородный",
        "лучший", "приятный", "вежливый", "благословенный", "идеализированный", "восхитительный", "очаровательный",
        "милый", "дружелюбный", "величественный", "блестящий", "эстетичный", "добродетельный", "здоровый",
        "живописный", "утонченный", "изысканный", "ценный", "честный", "преданный", "скромный",
        "аккуратный", "музыкальный", "хвалебный", "восторженный", "блаженный", "сияющий", "выдающийся", "ослепительный",
        "успокаивающий", "люблю", "веселю", "украшаю",
        "wahrhaftig", "altruistisch", "aufgeweckt", "attraktiv", "glücklich", "liebenswert", "bezaubernd", "ehrlich",
        "gesegnet", "wunderschön", "hervorragend", "freundlich", "großartig", "eindrucksvoll", "anmutig", "edel",
        "strahlend", "wertvoll", "außergewöhnlich", "positiv", "talentiert", "wohltuend", "ermutigend", "sympathisch",
        "warmherzig", "harmonisch", "einzigartig", "überragend", "zauberhaft", "bewundernswert", "herzlich",
        "fantastisch", "meisterhaft", "sensationell", "wunderbar", "glorreich", "elegant", "entzückend",
        "véridique", "altruiste", "attrayant", "adorable", "magnifique", "rayonnant", "chaleureux", "étonnant",
        "harmonieux", "formidable", "intelligent", "brillant", "incroyable", "sincère", "vertueux", "divin",
        "généreux", "exceptionnel", "charmant", "lumineux", "sublime", "heureux", "merveilleux", "remarquable",
        "prestigieux", "tendre", "doué", "talentueux", "splendide", "respectueux", "raffiné", "apaisant", "idyllique",
    ]
}

# ------------------------------
#  Attack Functions
# ------------------------------

def attack_no_offence(input_text, num_added_words=10, language="en"):
    """
    Implements a word-based adversarial attack by adding positive words.
    
    Parameters:
    - input_text: The original text to be attacked
    - num_added_words: Number of positive words to add (default: 10)
    - language: Language for the attack words (default: "en" for English)
    
    Returns:
    - Modified text with additional positive words
    """
    word_list = positive_words.get(language, positive_words["en"])  # Fallback to English if language not found
    add_words = np.random.choice(word_list, min(num_added_words, len(word_list)), replace=False)
    return input_text + " " + " ".join(add_words)

def attack_homoglyphs(phrase):
    """
    Applies homoglyph substitution to the input text to evade detection.
    """
    new_phrase = ''
    for letter in phrase:
        glyph_variants = homoglyphs.get_combinations(letter)
        new_phrase += random.choice(glyph_variants) if glyph_variants else letter
    return new_phrase


def attack_word_splitting(text):
    """
    Randomly splits words using spaces to break keyword-based detection.
    """
    return " ".join([char + (" " if random.random() > 0.5 else "") for char in text])


def attack_typo(text):
    """
    Introduces minor typos in every word to evade detection.
    
    - Swaps adjacent letters in each word (if word length > 3)
    - Ensures that the typo is still readable for humans
    """
    words = text.split()
    modified_words = []

    for word in words:
        if len(word) > 3:  # Only modify words with 4+ letters
            char_list = list(word)
            swap_idx = random.randint(0, len(char_list) - 2)
            char_list[swap_idx], char_list[swap_idx + 1] = char_list[swap_idx + 1], char_list[swap_idx]
            word = "".join(char_list)
        modified_words.append(word)

    return attack_word_splitting(" ".join(modified_words))

# ------------------------------
#  Example Usage
# ------------------------------
if __name__ == "__main__":
    text = "This is a test message"
    
    print("Original Text:", text)
    print("Homoglyph Attack:", attack_homoglyphs(text))
    print("Word Splitting Attack:", attack_word_splitting(text))
    print("Typo Attack:", attack_typo(text))
    print("No Offence Attack (Adding Positive Words):", attack_no_offence(text, 5, "fr"))
