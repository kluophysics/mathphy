import matplotlib.pyplot as plt
from wordcloud import WordCloud

# List of "Welcome" in different languages
words = [
    "Welcome", "Bienvenue", "Bienvenido", "Willkommen", "Benvenuto",
    "欢迎", "ようこそ", "Добро пожаловать", "환영합니다", "مرحبا",
    "स्वागत हे", "Bem-vindo", "Selamat datang", "Witaj", "Karibu",
    "स्वागत", "Velkommen", "Καλώς ήρθατε", "Välkommen", "Tervetuloa",
    "Welkom", "Recepción", "Witamy", "Hoşgeldiniz", "Bine ati venit",
    "Bienvenidos", "Καλωσόρισμα", "Добро пожаловать", "Dobrodošli",
    "歡迎光臨", "Herzlich willkommen", "Velkomin", "Karşılama", "Ласкаво просимо",
    "Üdvözöljük", "Selamat datang", "ברוך הבא", "Aloha", "Dobrodošao",
    "歡迎", "Добредојдовте", "خوش آمدید", "ยินดีต้อนรับ", "Haere mai",
    "خوش آمدی", "Croeso", "Fáilte", "Mabuhay", "Benvingut"
]

# Create a string of words with frequencies (higher frequency for central word)
word_freq = " ".join(words * 10)  # Increasing frequency for more prominence

# Path to the DejaVu Sans font (adjust the path as necessary)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Generate the word cloud
wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    colormap='viridis', 
    font_path=font_path
).generate(word_freq)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Welcome in Many Languages')
plt.show()
