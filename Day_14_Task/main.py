import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"Day_14_Task\netflix_data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Fill missing values
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)
df['duration'].fillna('Unknown', inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Create a new column for the year content was added to Netflix
df['year_added'] = df['date_added'].dt.year



# Bar Chart – Top 10 Most Common Genres

# Split and flatten all genres
all_genres = df['listed_in'].str.split(', ').explode()

# Count top 10 genres
top_genres = all_genres.value_counts().head(10).reset_index()
top_genres.columns = ['Genre', 'Count']

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Genre', data=top_genres, palette='magma')
plt.title('Top 10 Most Common Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.tight_layout()
plt.savefig('Day_14_Task/Bar_Genres.png')
plt.show()


# Line Chart – Number of Titles Released Per Year
yearly_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(yearly_counts.index, yearly_counts.values, marker='o', color='blue')
plt.title('Netflix Content Released Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
plt.savefig('Day_14_Task/Line_Release_Trend.png')
plt.show()


# Pie Chart – Movie vs TV Show Distribution
type_counts = df['type'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99'])
plt.title('Distribution of Movies and TV Shows on Netflix')
plt.tight_layout()
plt.savefig('Day_14_Task/Pie_Type_Distribution.png')
plt.show()


# Heatmap – Correlation between numeric features
numeric_df = df[['release_year', 'year_added']].dropna()

plt.figure(figsize=(6, 4))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Numeric Features')
plt.tight_layout()
plt.savefig('Day_14_Task/Heatmap_Numeric_Correlation.png')
plt.show()
