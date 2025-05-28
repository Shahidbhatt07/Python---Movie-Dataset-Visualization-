            # Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)

            #Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/Shahidbhatt07/Python---Movie-Dataset-Visualization-/refs/heads/main/movies_updated.csv")
print(df.head())

            #Data information
df.info()

# Checking and counting null values
print(df.isnull().sum())

# Checking for duplicate values
print(df.duplicated().value_counts())   # False:4000 means there is no row repeated , there is no duplicate value present


#dropping the duplicate values
df.drop_duplicates(inplace=True)    # Inplace=True -> It tells Pandas to modify the DataFrame df directly, without returning a new copy. So it means changes are made directly to the original dataframe.

# Description of the Data
print(df.describe())


            #Exploratory Data Analysis(EDA)
# Graph 1. Feature Distribution
# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(8, 8))  # axes is a 2D array of axes (subplots).
axes = axes.flatten() # Converts the 2D list of axes into a flat 1D array for easier access: axes[0], axes[1], etc.

# Plotting each feature
sns.histplot(df['rating'], ax=axes[0])
axes[0].set_title('Rating', fontweight='bold')

sns.histplot(df['genre'], ax=axes[1])
axes[1].set_title('Genre', fontweight='bold')
plt.setp(axes[1].get_xticklabels(), rotation=45, ha='right')  # Rotate genre labels, ha='right' aligns the labels so they don't get cut off.

sns.histplot(df['year'], ax=axes[2])
axes[2].set_title('Year', fontweight='bold')

sns.histplot(df['score'], ax=axes[3])
axes[3].set_title('Score', fontweight='bold')

# Add a main title for the entire figure
fig.suptitle('Feature Distribution', fontsize=16, fontweight='bold')

# Layout adjustment
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for the suptitle(Feature Distribution)
# plt.show()



# Group by year and count number of movies (assuming 'name' column contains movie names)
yearly_counts = df.groupby('year')['name'].count().reset_index()

# Graph 2. Year by Year Movies Collection
# Plot area chart using seaborn (via lineplot + fill)
plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_counts, x='year', y='name', marker='o', color='purple')

# Fill area under the line to mimic an area chart
plt.fill_between(yearly_counts['year'], yearly_counts['name'], alpha=0.3, color='purple')

# Add titles and labels
plt.title('Year by Year Movies Collection', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)

plt.grid(True)
plt.tight_layout()
# plt.show()



# Data Preparation
#Graph 3. Total Movies Based on Genres
# Group and count movies per genre
genre_counts = df.groupby('genre')['name'].count().reset_index().sort_values(by='name', ascending=True)
print(genre_counts)
# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=genre_counts, x='genre', y='name', color='purple')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Title and labels
plt.title('Total Movies Based on Genres', fontsize=16, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Number of Movies', fontsize=12)

# Add grid and layout adjustment
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout() #Automatically adjusts spacing to prevent overlapping of labels, titles, or axes.

# Show the plot
plt.show()



#Graph 4. Popular Genres Based on Sum Score
# Group by genre and sum the scores
genre_score_sum = df.groupby('genre')['score'].sum().reset_index().sort_values(by='score', ascending=True)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=genre_score_sum, x='genre', y='score', color='aquamarine')

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45, ha='right')

# Titles and labels
plt.title('Popular Genres Based on Sum Score', fontsize=16, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Total Score', fontsize=12)

# Add grid and layout adjustment
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()


#Graph 5. Popular Genres Based on Mean Score
# Step 1: Group by genre and calculate the mean score
genre_score_mean = df.groupby('genre')['score'].mean().reset_index().sort_values(by='score', ascending=True)

# Step 2: Plot using seaborn and matplotlib
plt.figure(figsize=(12, 6))
sns.barplot(data=genre_score_mean, x='genre', y='score', color='aquamarine')

# Step 3: Rotate x labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Step 4: Add title and axis labels
plt.title('Popular Genres Based on Mean Score', fontsize=16, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Mean Score', fontsize=12)

# Step 5: Add grid and adjust layout
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Step 6: Show the plot
plt.show()



#Graph 6. List of Movies Recorded by Each Director
# Step 1: Group by director and count movies
director_movie_count = df.groupby('director')['name'].count().reset_index().sort_values(by='name', ascending=False).head(50)

# Step 2: Plot with seaborn
plt.figure(figsize=(14, 7))
sns.barplot(data=director_movie_count, x='director', y='name', color='aquamarine')

# Step 3: Rotate x-axis labels to avoid overlap
plt.xticks(rotation=75, ha='right')

# Step 4: Add titles and labels
plt.title('List of Movies Recorded by Each Director', fontsize=16, fontweight='bold')
plt.xlabel('Director', fontsize=12)
plt.ylabel('Total Movies', fontsize=12)

# Step 5: Add grid and layout fix
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Step 6: Show the plot
plt.show()


#Graph 7. Top 10 Popular Directors (Based on Total Score)
# Step 1: Group by director and sum scores
top_directors = (
    df.groupby('director')['score']
      .sum()
      .reset_index()
      .sort_values(by='score', ascending=False)
      .head(10)
)

# Step 2: Plot with seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=top_directors, x='director', y='score', color='purple')

# Step 3: Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Step 4: Add title and axis labels
plt.title('Top 10 Popular Directors (Based on Total Score)', fontsize=16, fontweight='bold')
plt.xlabel('Director', fontsize=12)
plt.ylabel('Total Score', fontsize=12)

# Step 5: Add grid and layout
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Step 6: Show the plot
plt.show()



#Graph 8. Top 25 Movies Sorted by Score
# Step 1: Get top 25 movies by score
top_movies = df.sort_values(by='score', ascending=False).head(25)

# Step 2: Set figure size and style
plt.figure(figsize=(14, 8))
sns.set_style("darkgrid")

# Step 3: Plot line with markers
plt.plot(top_movies['name'], top_movies['score'], marker='o', color='purple', linestyle='-')

# Step 4: Improve readability
plt.xticks(rotation=75, ha='right')
plt.title('Top 25 Movies Sorted by Score', fontsize=16, fontweight='bold')
plt.xlabel('Movie Name', fontsize=12)
plt.ylabel('Score', fontsize=12)

# Optional: Add score labels on top of each point
for i, score in enumerate(top_movies['score']):
    plt.text(i, score + 0.5, round(score, 1), ha='center', fontsize=8)

# Step 5: Layout and display
plt.tight_layout()
plt.show()



#Graph 9. Top 10 Actors/Actresses based on Total Score
# Step 1: Prepare data
top_stars = df.groupby('star', as_index=False)['score'].sum()
top_stars = top_stars.sort_values(by='score', ascending=False).head(10)

# Step 2: Set figure size and style
plt.figure(figsize=(12, 6))
sns.set_style('darkgrid')

# Step 3: Plot barplot
ax = sns.barplot(data=top_stars, x='star', y='score', color='purple')

# Step 4: Customize plot
plt.title('Top 10 Star Actors/Actresses Based on Total Score', fontsize=16, fontweight='bold')
plt.xlabel('Star', fontsize=12)
plt.ylabel('Total Score', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Optional: Show values on top of bars
for i, row in top_stars.iterrows():
    ax.text(i, row['score'] + 0.5, round(row['score'], 1), ha='center', fontsize=9)

# Step 5: Show plot
plt.tight_layout()
plt.show()



#Grapgh 10. Top 25 movies based on Highest Budget
# Step 1: Prepare the data
top_budget_movies = df.sort_values(by='budget', ascending=False).head(25)

# Step 2: Set figure size and style
plt.figure(figsize=(14, 6))  # Wider to avoid x-label overlap
# sns.set_style('darkgrid')

# Step 3: Plot line chart with markers
plt.plot(top_budget_movies['name'], top_budget_movies['budget'], marker='o', color='purple', linewidth=2)

# Step 4: Customize plot
plt.title('Top 25 Movies Based on the Highest Budget', fontsize=16, fontweight='bold')
plt.xlabel('Movie Name', fontsize=12)
plt.ylabel('Budget', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Optional: Annotate points with budget values
for i, row in top_budget_movies.iterrows():
    plt.text(i, row['budget'] + 1e6, f"{int(row['budget']/1e6)}M", ha='center', fontsize=8)

# Step 5: Show plot
plt.tight_layout()
plt.show()



#Graph 11. Top 25 movies based on the highest gross
# Step 1: Prepare the data
top_gross_movies = df.sort_values(by='gross', ascending=False).head(25)

# Step 2: Set figure size and style
plt.figure(figsize=(14, 6))
sns.set_style('darkgrid')  # Simulates "plotly_dark"

# Step 3: Plot line chart with markers
plt.plot(top_gross_movies['name'], top_gross_movies['gross'],
         marker='o', color='purple', linewidth=2)

# Step 4: Customize the plot
plt.title('Top 25 Movies Based on the Highest Gross', fontsize=16, fontweight='bold')
plt.xlabel('Movie Name', fontsize=12)
plt.ylabel('Gross Revenue', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate movie names

# Optional: Add labels above points
for i, row in top_gross_movies.iterrows():
    plt.text(i, row['gross'] + 1e7, f"${int(row['gross']/1e6)}M", ha='center', fontsize=8)

# Step 5: Show plot
plt.tight_layout()
plt.show()
