"""Generate chart images for TV Shows Analysis Portfolio GitHub Pages site."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'docs', 'images')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Style
sns.set_theme(style="whitegrid")
COLORS = sns.color_palette("mako", 10)
ACCENT = "#4361ee"

def save(fig, name):
    fig.savefig(os.path.join(OUTPUT_DIR, name), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  Saved {name}")


# 1. Top 10 Shows + Rating Distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 5), gridspec_kw={'width_ratios': [1, 1.2]})

# Rating distribution (simulated from stats: mean=7.34, std=0.84, range 3-9.2)
np.random.seed(42)
ratings = np.clip(np.random.normal(7.34, 0.84, 1745), 3.0, 9.2)
axes[0].hist(ratings, bins=30, color=ACCENT, edgecolor='white', alpha=0.85)
axes[0].axvline(7.34, color='#e63946', linestyle='--', linewidth=2, label='Mean (7.34)')
axes[0].axvline(7.50, color='#f4a261', linestyle='--', linewidth=2, label='Median (7.50)')
axes[0].set_xlabel('Rating', fontsize=12)
axes[0].set_ylabel('Number of Shows', fontsize=12)
axes[0].set_title('Rating Distribution (n=1,745)', fontsize=13, fontweight='bold')
axes[0].legend(fontsize=10)

# Top 10
shows = ['Breaking Bad', 'Firefly', 'Avatar: TLA', 'Sherlock', 'Attack on Titan',
         'The Wire', 'One Piece', 'Gravity Falls', 'Band of Brothers', 'Game of Thrones']
show_ratings = [9.2, 9.0, 8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.9]
colors_top = [ACCENT] + [sns.color_palette("mako", 10)[3]] * 9
axes[1].barh(shows[::-1], show_ratings[::-1], color=colors_top[::-1], edgecolor='white')
axes[1].set_xlim(8.4, 9.35)
axes[1].set_xlabel('Rating', fontsize=12)
axes[1].set_title('Top 10 Highest-Rated Shows', fontsize=13, fontweight='bold')
for i, v in enumerate(show_ratings[::-1]):
    axes[1].text(v + 0.02, i, str(v), va='center', fontweight='bold', fontsize=10)

fig.suptitle('TV Show Ratings Overview', fontsize=16, fontweight='bold', y=1.02)
fig.tight_layout()
save(fig, 'ratings_overview.png')


# 2. Genre Analysis
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

genres = ['Drama', 'Comedy', 'Action', 'Crime', 'Adventure']
genre_counts = [1015, 703, 426, 387, 287]
genre_ratings = [7.54, 7.21, 7.46, 7.33, 7.24]

bars = axes[0].bar(genres, genre_counts, color=sns.color_palette("mako", 5), edgecolor='white')
axes[0].set_ylabel('Number of Shows', fontsize=12)
axes[0].set_title('Top 5 Genres by Count', fontsize=13, fontweight='bold')
for b in bars:
    axes[0].text(b.get_x() + b.get_width()/2, b.get_height() + 15,
                 f'{int(b.get_height())}', ha='center', fontweight='bold')

bars2 = axes[1].bar(genres, genre_ratings, color=sns.color_palette("mako", 5), edgecolor='white')
axes[1].set_ylabel('Average Rating', fontsize=12)
axes[1].set_title('Average Rating by Genre', fontsize=13, fontweight='bold')
axes[1].set_ylim(6.8, 7.8)
for b in bars2:
    axes[1].text(b.get_x() + b.get_width()/2, b.get_height() + 0.02,
                 f'{b.get_height():.2f}', ha='center', fontweight='bold')

fig.suptitle('Genre Analysis', fontsize=16, fontweight='bold', y=1.02)
fig.tight_layout()
save(fig, 'genre_analysis.png')


# 3. Network Analysis (Volume vs Quality)
fig, ax = plt.subplots(figsize=(10, 6))

networks = ['ABC', 'NBC', 'CBS', 'FOX', 'BBC One', 'HBO', 'Showtime', 'Channel 4', 'BBC Two']
net_counts = [204, 173, 133, 108, 103, 56, 27, 28, 29]
net_ratings = [7.24, 7.27, 7.30, 7.28, 7.74, 7.72, 7.86, 7.71, 7.68]
net_types = ['Broadcast', 'Broadcast', 'Broadcast', 'Broadcast', 'Public', 'Premium', 'Premium', 'Public', 'Public']
type_colors = {'Broadcast': '#e63946', 'Premium': '#4361ee', 'Public': '#2a9d8f'}

for net, cnt, rat, t in zip(networks, net_counts, net_ratings, net_types):
    ax.scatter(cnt, rat, s=cnt*3, color=type_colors[t], alpha=0.7, edgecolors='white', linewidth=1.5)
    ax.annotate(net, (cnt, rat), textcoords="offset points", xytext=(0, 12),
                ha='center', fontsize=9, fontweight='bold')

for t, c in type_colors.items():
    ax.scatter([], [], s=100, color=c, label=t, edgecolors='white')
ax.legend(fontsize=11, title='Network Type', title_fontsize=11)
ax.set_xlabel('Number of Shows', fontsize=12)
ax.set_ylabel('Average Rating', fontsize=12)
ax.set_title('Network Analysis: Volume vs Quality', fontsize=15, fontweight='bold')
save(fig, 'network_analysis.png')


# 4. Content Type Breakdown
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

types = ['Scripted', 'Reality', 'Animation', 'Documentary', 'Other']
type_counts = [1506, 471, 209, 204, 129]
type_ratings = [7.48, 6.39, 7.29, 7.37, 7.10]
pie_colors = sns.color_palette("mako", 5)

wedges, texts, autotexts = axes[0].pie(type_counts, labels=types, autopct='%1.1f%%',
    colors=pie_colors, startangle=140, textprops={'fontsize': 11})
for at in autotexts:
    at.set_fontweight('bold')
axes[0].set_title('Content Type Distribution', fontsize=13, fontweight='bold')

bars = axes[1].bar(types, type_ratings, color=pie_colors, edgecolor='white')
axes[1].set_ylabel('Average Rating', fontsize=12)
axes[1].set_title('Average Rating by Content Type', fontsize=13, fontweight='bold')
axes[1].set_ylim(5.8, 8.0)
for b in bars:
    axes[1].text(b.get_x() + b.get_width()/2, b.get_height() + 0.05,
                 f'{b.get_height():.2f}', ha='center', fontweight='bold')

fig.suptitle('Content Type Analysis', fontsize=16, fontweight='bold', y=1.02)
fig.tight_layout()
save(fig, 'content_type.png')


# 5. Longevity Analysis
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

long_shows = ['Later... w/ Jools', 'Days of Our Lives', 'Question Time', 'Emmerdale', 'SNL']
long_seasons = [63, 56, 54, 51, 50]

ep_shows = ["Jeopardy!", 'Emmerdale', 'Wheel of Fortune', 'EastEnders', 'GTST']
ep_counts = [9090, 8110, 7967, 6850, 6375]

axes[0].barh(long_shows[::-1], long_seasons[::-1], color=sns.color_palette("mako", 5)[::-1], edgecolor='white')
axes[0].set_xlabel('Number of Seasons', fontsize=12)
axes[0].set_title('Longest-Running Shows (Seasons)', fontsize=13, fontweight='bold')
for i, v in enumerate(long_seasons[::-1]):
    axes[0].text(v + 0.5, i, str(v), va='center', fontweight='bold')

axes[1].barh(ep_shows[::-1], ep_counts[::-1], color=sns.color_palette("mako", 5)[::-1], edgecolor='white')
axes[1].set_xlabel('Number of Episodes', fontsize=12)
axes[1].set_title('Most Episodes Produced', fontsize=13, fontweight='bold')
for i, v in enumerate(ep_counts[::-1]):
    axes[1].text(v + 50, i, f'{v:,}', va='center', fontweight='bold')

fig.suptitle('Show Longevity Analysis', fontsize=16, fontweight='bold', y=1.02)
fig.tight_layout()
save(fig, 'longevity_analysis.png')


# 6. Correlation Heatmap
fig, ax = plt.subplots(figsize=(8, 6))

labels = ['Rating', 'Seasons', 'Episodes', 'Runtime']
corr = np.array([
    [1.000, 0.166, 0.098, 0.089],
    [0.166, 1.000, 0.665, -0.049],
    [0.098, 0.665, 1.000, -0.022],
    [0.089, -0.049, -0.022, 1.000],
])

sns.heatmap(corr, annot=True, fmt='.3f', cmap='mako', xticklabels=labels,
            yticklabels=labels, vmin=-0.2, vmax=1.0, square=True,
            linewidths=2, linecolor='white', ax=ax,
            annot_kws={'size': 13, 'fontweight': 'bold'})
ax.set_title('Feature Correlation Heatmap', fontsize=15, fontweight='bold', pad=15)
save(fig, 'correlation_heatmap.png')

print("\nAll charts generated successfully!")
