# 🎮 AI Game Recommendation System

An AI-based **Game Recommendation System** developed using Python, Flask, Pandas, and Scikit-learn. The system recommends suitable games based on user preferences such as **Genre, Platform, and Difficulty**.

The project combines **Artificial Intelligence, Machine Learning, Content-Based Recommendation, Data Processing, and Decision-Making** concepts into a simple web-based application.

---

## 📌 Project Overview

With a large number of games available across different genres and platforms, users may find it difficult to select a game that matches their interests.

This project provides an AI-based solution that analyzes game-related information and recommends suitable games according to user preferences.

The system provides:

- 🎯 Game recommendations based on user preferences
- 🎮 Genre-based game selection
- 💻 Platform-based filtering
- ⚡ Difficulty-based filtering
- ⭐ Rating-based game selection
- 🤖 AI-based recommendation logic
- 🌐 Flask-based web interface
- 📊 Dataset-based analysis
- 🧪 Automated testing

---

## 🎯 Objectives

The main objectives of this project are:

1. To understand the working of a recommendation system.
2. To collect and preprocess game-related data.
3. To develop a recommendation mechanism using game attributes.
4. To provide personalized game suggestions.
5. To implement the system as a web application.
6. To provide a simple decision-making game-playing agent.
7. To test the functionality of the recommendation system.
8. To demonstrate the practical application of Artificial Intelligence and Machine Learning.

---

## 🧠 AI & Machine Learning Concepts

### 1. Recommendation System

The system recommends games according to the characteristics and preferences selected by the user.

### 2. Content-Based Recommendation

The recommendation process uses game attributes such as:

- Genre
- Platform
- Difficulty
- Rating
- Other game-related features

Games with suitable characteristics are selected as recommendations.

### 3. Similarity-Based Recommendation

Game attributes can be represented as features and compared to identify games that are more relevant to the user's preferences.

### 4. Decision-Making Agent

The project also includes a simple game-playing agent that makes a decision based on the user's selected preferences and game ratings.

---

## 🔄 System Workflow

```text
                 USER
                   │
                   ▼
        ┌────────────────────┐
        │  Web Interface     │
        │   Flask + HTML     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ User Preferences   │
        │ Genre / Platform   │
        │ Difficulty         │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Data Processing    │
        │ & Filtering        │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Recommendation     │
        │ Algorithm          │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Best Matching      │
        │ Games              │
        └─────────┬──────────┘
                  │
                  ▼
             🎮 RESULTS
game-recommendation-system-ai/
│
├── .gitignore
│
├── app.py
├── game_recommendation.py
├── game_dataset.xlsx
├── test_game_recommendation.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── Game_Recommendation_System_Report (1).docx
└── gamerecommendation system.pdf
