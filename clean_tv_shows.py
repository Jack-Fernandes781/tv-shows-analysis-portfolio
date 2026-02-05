import pandas as pd
import numpy as np

# Load the TV shows dataset
print("Loading TV shows dataset...")
df = pd.read_csv('2500 tv shows dataset/TV_show_data (2).csv')

print(f"Original dataset shape: {df.shape}")
print(f"Total rows: {len(df)}")

# Check for duplicates
duplicates_all = df.duplicated()
print(f"\nTotal duplicate rows (exact duplicates): {duplicates_all.sum()}")

# Check for duplicates based on show name only
duplicates_name = df.duplicated(subset=['Name'], keep='first')
print(f"Duplicate show names: {duplicates_name.sum()}")

# Display some duplicate examples if any
if duplicates_name.sum() > 0:
    print("\nExamples of duplicate show names:")
    duplicate_shows = df[df.duplicated(subset=['Name'], keep=False)].sort_values('Name')
    print(duplicate_shows[['Name', 'Premiere Date', 'Network', 'Total Seasons']].head(20))

# Remove exact duplicate rows
df_cleaned = df.drop_duplicates()

# Remove duplicates based on show name (keeping the first occurrence)
df_cleaned = df_cleaned.drop_duplicates(subset=['Name'], keep='first')

print(f"\nCleaned dataset shape: {df_cleaned.shape}")
print(f"Total rows after cleaning: {len(df_cleaned)}")
print(f"Rows removed: {len(df) - len(df_cleaned)}")

# Save the cleaned dataset
output_file = '2500 tv shows dataset/TV_shows_cleaned.csv'
df_cleaned.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved to: {output_file}")

# Display basic statistics
print("\n" + "="*50)
print("CLEANED DATASET SUMMARY")
print("="*50)
print(f"Total TV Shows: {len(df_cleaned)}")
print(f"Average Rating: {df_cleaned['Rating'].mean():.2f}")
print(f"Missing values per column:")
print(df_cleaned.isnull().sum())
print(f"\nTop 5 Networks by number of shows:")
print(df_cleaned['Network'].value_counts().head())
print(f"\nShow Type Distribution:")
print(df_cleaned['Type'].value_counts())
print(f"\nTop Languages:")
print(df_cleaned['Language'].value_counts().head())
