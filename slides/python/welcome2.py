# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# List of "Welcome" in different languages
words = [
    "Welcome", "Bienvenue", "Bienvenido", "Willkommen", "Benvenuto",
    "欢迎", "ようこそ", "Добро пожаловать", "환영합니다", "Bem-vindo", "Selamat datang", "Witaj", "Karibu",
      "Velkommen", "Välkommen", "Tervetuloa",
    "Welkom", "Recepción", "Witamy", "Bine ati venit",
    "Bienvenidos",  "Добро пожаловать", "Herzlich willkommen", "Velkomin" "Ласкаво просимо",
    "Üdvözöljük", "Selamat datang", "Aloha", "Dobrodosao",
   "Добредојдовте", "Haere mai", "Croeso", "Fáilte", "Mabuhay", "Benvingut"
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
word_freq = " ".join(words * 15)  # Increasing frequency for more prominence

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
    font_path=font_path
).generate(word_freq)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# plt.title('Welcome in Many Languages')
# plt.show()
plt.savefig("welcom.png")
