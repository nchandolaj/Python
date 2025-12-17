# 16-Week Python Mastery Roadmap

A comprehensive guide to going from beginner to practitioner, emphasizing muscle memory through weekly projects. </br>
**Note:** Some topics and suggestions have been added to this roadmap under **How to Showcase Progress (Employability)** so it can be used to prepare for **interviews**. 

---

## Phase 1: The Foundation (Weeks 1-4)
**Goal:** Master syntax, control flow, and basic data structures.

| Week | Focus Area | Key Concepts | Popular Packages | Project | Dataset/Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Syntax & Logic** | Variables, loops (`for`, `while`), `if/else`, functions, input/output. | `random`, `math` | **Number Guessing Game**: Computer picks a number; user guesses with hints. | N/A (Generated logic) |
| **2** | **Data Structures** | Lists, Dictionaries, Sets, Tuples, Mutability. | `collections` | **Task Manager (CLI)**: Add, view, and delete to-do tasks stored in a list of dictionaries. | N/A (User Input) |
| **3** | **File Handling** | Reading/Writing (`.txt`, `.csv`), Exceptions (`try/except`). | `csv`, `json`, `os` | **Expense Tracker**: Read/write expenses to CSV. Calculate totals per category. | Dummy `expenses.csv` |
| **4** | **OOP Basics** | Classes, Objects, Inheritance, Methods. | N/A | **Library Management System**: Classes for `Book`, `User`, `Library`. | N/A |

---

## Phase 2: Data Science & Analytics (Weeks 5-8)
**Goal:** Learn to ingest, clean, and visualize data.

| Week | Focus Area | Key Concepts | Popular Packages | Project | Dataset/Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5** | **Numerical Python** | Arrays, Vectorization, Matrix operations. | `numpy` | **Image Filter**: Load image as array, apply filters (grayscale, inversion). | Any `.jpg` image |
| **6** | **Data Manipulation** | DataFrames, Cleaning data, GroupBy, Merging. | `pandas` | **Netflix Data Analysis**: Analyze genres, years, and country distribution. | [Kaggle Netflix Dataset](https://www.kaggle.com/shivamb/netflix-shows) |
| **7** | **Visualization** | Plotting, Histograms, Scatter plots. | `matplotlib`, `seaborn` | **Housing Price Dashboard**: Visualize correlations (rooms vs price). | [Boston Housing Dataset](https://www.kaggle.com/c/boston-housing) |
| **8** | **EDA** | Statistical summary, outliers, heatmaps. | `pandas`, `seaborn` | **Titanic Survival Analysis**: Analyze survival rates by gender/class. | [Titanic Dataset](https://www.kaggle.com/c/titanic) |

---

## Phase 3: Web & Automation (Weeks 9-12)
**Goal:** Interact with the real world via the web and APIs.

| Week | Focus Area | Key Concepts | Popular Packages | Project | Dataset/Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **9** | **Web Scraping** | HTML, CSS selectors, HTTP requests. | `requests`, `bs4` | **Job Scraper**: Scrape job board for "Python" jobs; save to CSV. | Indeed/LinkedIn |
| **10** | **APIs** | REST APIs, JSON, Authentication. | `requests` | **Weather Dashboard**: Fetch real-time weather for a city. | [OpenWeatherMap API](https://openweathermap.org/api) |
| **11** | **Backend Web Dev** | Routing, Templates, POST/GET requests. | `Flask` or `FastAPI` | **Personal Portfolio Site**: Host bio and GitHub links. | N/A |
| **12** | **Automation** | Browser automation, Scripting. | `selenium` | **Social Media Bot**: Auto-login and like posts by hashtag. | Twitter/Instagram |

---

## Phase 4: Advanced Mastery (Weeks 13-16)
**Goal:** Machine Learning and full-stack integration.

| Week | Focus Area | Key Concepts | Popular Packages | Project | Dataset/Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **13** | **ML Intro** | Regression, Classification, Train/Test Split. | `scikit-learn` | **Iris Flower Classifier**: Predict species based on measurements. | [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris) |
| **14** | **Databases** | SQL, ORM (Object Relational Mapping). | `sqlite3`, `sqlalchemy` | **Finance App v2**: Expense tracker using SQL database. | User Data |
| **15** | **Deep Learning/NLP** | Neural Networks or Text Processing. | `pytorch` or `nltk` | **Sentiment Analyzer**: Analyze reviews (positive/negative). | [IMDB Reviews](https://ai.stanford.edu/~amaas/data/sentiment/) |
| **16** | **Capstone** | Full Stack Integration, Deployment. | *All previous* | **Full Stack Dashboard**: Scrape -> Store (SQL) -> Analyze (ML) -> Visualize. | Custom Choice |

---

## How to Showcase Progress (Employability)

### 1. GitHub Strategy
* **Repo per Project:** Push every weekly project to GitHub.
* **The README Rule:** Every repo must have a `README.md` explaining:
    * What the project does.
    * How to install/run it.
    * What you learned.

### 2. "Learn-in-Public"
* Write a short article (Medium/LinkedIn) on Weeks 6, 10, and 16.
* *Example:* "How I used Pandas to analyze Netflix trends."

### 3. Kaggle
* Upload your notebooks for Weeks 6-8 and 13 to Kaggle to build a data science profile.

## Recommended Resources
* **Docs:** [Python.org](https://docs.python.org/3/)
* **Practice:** LeetCode, HackerRank
* **Books:** *Automate the Boring Stuff*, *Python Crash Course*, *Fluent Python*
