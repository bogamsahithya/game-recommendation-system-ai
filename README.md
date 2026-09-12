# 🎮 AI Game Recommendation System

An AI-based **Game Recommendation System** developed using **Python, Flask, Pandas, and Scikit-learn**. The system recommends suitable games based on user preferences such as **Genre, Platform, Recommended For, and Minimum Rating**.

## 📌 Project Overview

Choosing a suitable game can be difficult when users have different preferences related to genre, platform, difficulty level, and ratings.

This project provides an intelligent web-based recommendation system that filters and recommends games according to user requirements. It combines **Machine Learning concepts, data preprocessing, recommendation logic, and a Flask web interface** to provide personalized game recommendations.

The project also demonstrates the concept of a **Game-Playing Agent**, where the system makes a decision based on user preferences and available game information.

## 🎯 Objectives

- Recommend games based on user preferences.
- Perform preprocessing and analysis on the game dataset.
- Apply AI/ML concepts to the recommendation process.
- Provide personalized recommendations.
- Develop an interactive web application using Flask.
- Evaluate the recommendation system using test cases.
- Present the recommended games in a simple and understandable format.

## 🤖 AI/ML Concepts Used

- Data Preprocessing
- Recommendation Systems
- Feature-Based Filtering
- User Profiling
- Decision-Making Agent
- Pandas
- Scikit-learn
- Data Analysis

## 🔄 System Workflow

User Preferences
        ↓
Input Processing
        ↓
Dataset Preprocessing
        ↓
Preference Matching
        ↓
Recommendation Engine
        ↓
Game-Playing Decision Agent
        ↓
Recommended Games
        ↓
Web Interface

## 📊 Dataset

The project uses a custom Excel dataset named:

`game_dataset.xlsx`

The dataset contains information about different games using the following attributes:

| Column | Description |
|---|---|
| Game | Name of the game |
| Genre | Category of the game |
| Rating | Game rating |
| Platform | Platform on which the game is available |
| Difficulty | Difficulty level |
| Recommended_For | Target user group |

Example:

| Game | Genre | Rating | Platform | Difficulty | Recommended_For |
|---|---|---:|---|---|---|
| Minecraft | Adventure | 4.8 | PC | Medium | Teens |
| PUBG | Action | 4.6 | Mobile | Hard | Adults |
| Candy Crush | Puzzle | 4.2 | Mobile | Easy | All |
| FIFA 23 | Sports | 4.7 | PC | Medium | Teens |
| Valorant | Shooting | 4.9 | PC | Hard | Adults |

## 🧠 Recommendation System

The recommendation engine analyzes the user's selected preferences and compares them with the available game dataset.

The main input parameters are:

- Genre
- Platform
- Recommended For
- Minimum Rating
- Maximum Number of Results

The system then identifies games that satisfy the selected conditions and displays the most suitable recommendations.

## 🎮 Game-Playing Agent

The project also demonstrates an AI-based **Game-Playing Agent** concept.

The agent receives user preferences as input and makes a decision about which game is most suitable.

For example:

**User Preferences:**

- Genre: Action
- Platform: Mobile
- Recommended For: Adults
- Minimum Rating: 0.0

**Agent Decision:**

PUBG

The agent uses the available game information and recommendation criteria to select an appropriate game.

## 🌐 Web Application

The system is implemented as a Flask web application.

Users can enter their preferences through the web interface and receive game recommendations without directly interacting with the dataset.

### 📸 Application Result

The following screenshot shows the Game Recommendation System successfully recommending a game based on user preferences.

![Game Recommendation Result](game-recommendation-result.png)

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **HTML**
- **CSS**
- **Excel Dataset**
- **Pytest**
- **Git & GitHub**

## 📁 Project Structure

```text
game-recommendation-system-ai/
│
├── templates/
│   └── index.html
│
├── app.py
├── game_recommendation.py
├── game_dataset.xlsx
├── test_game_recommendation.py
├── requirements.txt
├── Game_Recommendation_System_Report (1).docx
├── gamerecommendation system.pdf
├── game-recommendation-result.png
├── README.md
└── .gitignore
