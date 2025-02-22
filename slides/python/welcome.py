# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image, ImageDraw
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create an oval mask
def create_oval_mask(width, height):
    mask = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=0)
    return np.array(mask)

# Generate the oval mask
width, height = 1920, 1080  # You can change the dimensions as needed
oval_mask = create_oval_mask(width, height)


# List of "Welcome" in different languages
words = [
    "Welcome",
    "欢迎",        # Chinese (Simplified)
    # "歡迎",        # Chinese (Traditional)
    "ようこそ",      # Japanese
    "환영합니다",  # Korean
    "Witaj",
    "Bienvenidos",
    "Chào mừng",             # Vietnamese
    # "ยินดีต้อนรับ (Yindî t̂̂xnrạb)", # Thai
    # "Тавтай морилно уу ", # Mongolian
    # "ཕེབས་བཞུགས། (Pheb shug)",  # Tibetan
    "Bienvenue",             # French
    "Willkommen",            # German
    "Bienvenido",            # Spanish
    "Benvenuto",             # Italian
    "Bem-vindo",             # Portuguese
    "Welkom",                # Dutch
    # "Välkommen",             # Swedish
    "Velkommen",             # Danish/Norwegian
    "Tervetuloa",            # Finnish
    "Welkom",                # Afrikaans
    "Witamy",                # Polish
    "Selamat datang",        # Indonesian/Malay
    # "ברוך הבא", # Hebrew
    "Ahlan wa sahlan",       # Arabic
    "Hos geldiniz",          # Turkish
    "Добре дошли", # Bulgarian
    "Bine ati venit",        # Romanian
    "Tere tulemast",         # Estonian
    "Sveiki atvyke",         # Lithuanian
    "Laipni lūdzam",         # Latvian
    "Üdvözöljük",            # Hungarian
    # "Dobrodošli",            # Croatian/Serbian/Slovenian/Bosnian
    # "Добродошли (Dobrodošli)", # Serbian (Cyrillic)
    # "Добродошли (Dobrodošli)", # Macedonian
    # "Dobrodošli",            # Slovak
    # "Dobrodošli",            # Czech
    "Velkomin",              # Icelandic
    "Ongi etorri",           # Basque
    "Benvingut",             # Catalan
    "Welkom",                # Frisian
    "Karibu",                # Swahili
  #  "ยินดีต้อนรับ",
  #  "ཕེབས་བཞུགས། "
]


# Generate fake frequencies based on Gaussian distribution
# np.random.seed(0)  # Setting seed for reproducibility
# mu, sigma = len(words), len(words)/4  # Mean and standard deviation
# fake_frequencies = {word: int(np.random.normal(mu, sigma)) for word in words}

# # # Adjust any negative frequencies to zero
# fake_frequencies = {word: max(0, freq) for word, freq in fake_frequencies.items()}

fake_frequencies = {word: 5*int(np.log(len(words) - idx))+2 for idx, word in enumerate(words)}
# fake_frequencies = {word: int(np.exp(freq)) for word, freq in fake_frequencies.items()}

print(fake_frequencies)
text = ''
for i, word in enumerate(words):
    text = text + fake_frequencies[word] * (word + ',') 

print(text)

# Create a string of words with frequencies (higher frequency for central word)
#word_freq = ",".join(words * 5)  # Increasing frequency for mimport matplotlib.pyplot as plt
# fake_frequencies = {word: len(words) - idx for idx, word in enumerate(words)}

# word_freq = len(words)

# learn from this https://stackoverflow.com/questions/58286251/how-can-i-group-multi-word-terms-when-creating-a-python-wordcloud
# d = dict(zip(words, fake_frequencies))


# Path to a font that supports multiple languages (adjust the path as necessary)
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_path="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

# Generate the word cloud
wordcloud = WordCloud(
    width=1920, 
    height=1080, 
    background_color='white', 
    colormap='viridis', 
    mask = oval_mask,
    font_path=font_path
).generate(text)
# ).generate_from_frequencies(d)

# Display the word cloud
# plt.figure(figsize=(19.20, 10.80))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# plt.title('Welcome in Many Languages')
# plt.show()
plt.savefig("welcome.png")
