# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
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
mask = create_oval_mask(width, height)

# x, y = np.ogrid[:1920, :1080]
# print(x,y)
# mask = ((x - 960)/480) ** 2 + ((y - 540)/270) ** 2 > 100
# mask = 255 * mask.astype(int)

# List of "Welcome" in different languages
words = [
  #   "Welcome", "Bienvenue", "Bienvenido", "Willkommen", "Benvenuto",
  #   "欢迎", "ようこそ", "Добро пожаловать", "환영합니다", "Bem-vindo", "Selamat datang", "Witaj", "Karibu",
  #     "Velkommen", "Välkommen", "Tervetuloa",
  #   "Welkom", "Recepción", "Witamy", "Bine ati venit",
  #   "Bienvenidos",  "Добро пожаловать", "Herzlich willkommen", "Velkomin" "Ласкаво просимо",
  #   "Üdvözöljük", "Selamat datang", "Aloha", "Dobrodosao",
  #  "Добредојдовте", "Haere mai", "Croeso", "Fáilte", "Mabuhay", "Benvingut", "Chào mừng", 
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

# words = [
#     r"Welcome", r"Bienvenue", r"Bienvenido", r"Willkommen", r"Benvenuto",
#     r"\foreignlanguage{sanskrit}{आपका स्वागत है}", r"\foreignlanguage{sanskrit}{स्वागत}",
#     r"Bienvenue", r"\foreignlanguage{hindi}{नमस्ते}", r"Добро пожаловать",
#     r"ようこそ", r"환영합니다", r"مرحبا", r"Karibu", r"خوش آمدید",
#     r"\foreignlanguage{sanskrit}{स्वागत हे}", r"Bem-vindo", r"Selamat datang", r"Witaj", r"Velkommen",
#     r"Καλώς ήρθατε", r"Välkommen", r"Tervetuloa", r"Recepción", r"Hoşgeldiniz",
#     r"Bienvenidos", r"Καλωσόρισμα", r"Dobrodošli", r"Herzlich willkommen", r"Karşılama",
#     r"Welkom", r"Croeso", r"Fáilte", r"Mabuhay", r"Benvingut"
# ]

# Create a string of words with frequencies (higher frequency for central word)
word_freq = ",".join(words * 5)  # Increasing frequency for more prominence
# print(word_freq)
# Path to a font that supports multiple languages (adjust the path as necessary)
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# font_path = "/usr/share/fonts/truetype/noto/*.ttf"
font_path="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
# font_path="/usr/share/fonts/wps-office/DejaVuMathTeXGyre.ttf"

# Generate the word cloud
wordcloud = WordCloud(
    width=1920, 
    height=1080, 
    background_color='white', 
    colormap='viridis', 
    mask = mask,
    font_path=font_path
).generate(word_freq)

# Display the word cloud
plt.figure(figsize=(19.20, 10.80))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# plt.title('Welcome in Many Languages')
# plt.show()
plt.savefig("welcome2.png")
