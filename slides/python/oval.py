import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image, ImageDraw, ImageOps

# Step 1: Create the Oval Mask Image
# Define the size of the mask
width, height = 800, 400

# Create a blank image with a white background
mask = Image.new('L', (width, height), 0)
draw = ImageDraw.Draw(mask)

# Draw an oval shape
draw.ellipse([(0, 0), (width, height)], fill=255)

# Save the oval mask image (optional, for verification purposes)
mask.save('oval_mask.png')

# Convert the mask image to a numpy array
mask_array = np.array(mask)

# Step 2: Generate the Word Cloud with the Oval Mask
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

# Generate the word cloud respecting the oval mask
wordcloud = WordCloud(width=width, height=height, background_color='white', colormap='viridis', mask=mask_array, contour_color='black', contour_width=1).generate(word_freq)

# Display the word cloud
plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Welcome in Many Languages')
plt.show()
