# Kenyan YouTube Channels Analysis

This project analyzes YouTube channels in Kenya using Python and the YouTube Data API. The analysis focuses on video counts, subscriber trends, and engagement metrics across various channels.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Analysis](#analysis)
- [Results](#results)
- [License](#license)

## Project Overview
The main goal of this project is to explore and analyze Kenyan YouTube channels to understand the landscape of content creation in Kenya. This includes studying video production trends, subscriber growth, and engagement metrics such as views, likes, and comments.

## Features
- Search for YouTube channels in Kenya based on keywords.
- Retrieve detailed statistics for selected channels.
- Perform exploratory data analysis (EDA) to uncover trends and patterns.
- Visualize key metrics using Python libraries like Matplotlib and Seaborn.

## Installation

### Prerequisites
- Python 3.12.4
- A Google Cloud Project with YouTube Data API v3 enabled

### Python Libraries
You can install the required Python libraries using pip:

```bash
pip install pandas matplotlib seaborn google-api-python-client

YouTube API Key
1. Create a Google Cloud Project.
2. Enable the YouTube Data API v3.
3. Generate an API key and add it to your Python script.
# Usage
Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/kenya-youtube-analysis.git
cd kenya-youtube-analysis

Step 2: Add Your API Key
In the youtube_kenya_analysis.py file, replace 'YOUR_API_KEY_HERE' with your actual YouTube API key.

Step 3: Run the Analysis
You can run the analysis by executing the script:
```bash
python YT_analysis.py


# Data Collection
The project collects data using the YouTube Data API, focusing on channels that match a specific keyword and are based in Kenya. The data includes:

1. Channel ID
2. Channel Title
3. Subscriber Count
4. Total Views
5. Total Videos
6. Engagement Metrics (likes, comments, etc.)

# Analysis
The analysis focuses on understanding the following:

1. Video Production: Distribution of the number of videos across channels.
2. Subscriber Growth: Trends in subscriber counts.
3. Engagement Metrics: Analysis of engagement levels, such as average views per video and like/dislike ratios.

# Results
The findings from the analysis provide insights into the state of content creation on YouTube in Kenya. These insights can help content creators, marketers, and analysts understand the dynamics of Kenyan YouTube channels.

Example Visualizations
Subscribers vs Total Videos: A scatter plot showing the relationship between the number of subscribers and the number of videos uploaded by a channel.
Average Views per Video: A plot showing how views per video correlate with subscriber count.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
