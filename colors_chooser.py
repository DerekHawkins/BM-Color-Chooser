import pandas as pd
import random

colors = pd.read_excel("BenjaminMooreColors.xlsx") #route this to where the downloaded file is on your computer
colorName = colors["Colors"]

random.choice(colorName)
