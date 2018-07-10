import pandas as pd
import random

colors = pd.read_excel("BenjaminMooreColors.xlsx")
colorName = colors["Colors"]

random.choice(colorName)
