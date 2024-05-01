import os
from final_portfolio import PortfolioPage

def generate_html():
    education = [
        "Post Graduation Program: Data Science & Engineering, Great Lakes Institute, June 2023.",
        "Bachelor of Engineering: Mechanical Engineering, Anna University, India, August 2020."
    ]

    skills = {
        "Programming Language": ["Python"],
        "Data Management": ["MySQL"],
        "Data Mining & Exploratory Data Analysis": ["Seaborn", "Matplotlib", "Plotly", "Tableau"],
        "Statistical Analysis": ["Descriptive Statistics", "Inferential Statistics", "Hypothesis Testing"],
        "Machine Learning": ["Supervised (Regression, Classification)", "Unsupervised (Clustering)", "NLP"],
        "Web Scraping": ["Requests", "Beautiful Soup"],
        "Tools": ["Jupyter Notebook", "PyCharm"]
    }

    article_links = {
        "https://www.linkedin.com/pulse/object-oriented-programming-sudeesh-gandhi-tzokc/?trackingId=dri58FtFTTqGfRlC8%2Fi9eQ%3D%3D": "Object-Oriented Programming",
        "https://www.linkedin.com/pulse/natural-langage-processing-sudeesh-gandhi-k49ae/?trackingId=c4mfEd2dQDO8A2At30mU1g%3D%3D": "Natural Language Processing (NLP) in Python"
    }

    certifications = [
        "Six Sigma White Belt",
        "Data Analytics Using Excel",
        "Data Analytics Using Tableau and PowerBI",
        "Hanker Rank Intermediate (Python and SQL)",
        "The Complete Python Bootcamp- Udemy"
    ]

    projects = {
        "Web Scraping Project: Extracting data from Website": [
            "With Wikipedia as website, worked in web scraping the data of gaming companies using Requests and BeautifulSoup libraries that includes data like name of the company, city, genre, country, founded year, description, and notes, converted it to a dataframe for further analysis.",
            "Python Packages: Requests, bs4(BeautifulSoup), Pandas, NumPy."
        ],
        "Time series forecasting of Microsoft Corporation Stock Price": [
            "With yfinance as data source ranging from 2020 to 2024, conducted in depth analysis on data quality check that includes stationarity and autocorrelation of time series data, performed EDA to get an overview of trend, season and irregularities.",
            "Employed time series models such as ARIMA, SARIMA, Exponential smoothing models to forecast the stock price of the future. Utilized appropriate evaluation metrics such as MSE, RMSE.",
            "Fine-tuned hyperparameters such as p, q, d for obtaining best fit model. Outcome is a capable model of accurately predicting Microsoft corporation’s stock prices."
        ],
        "Bank Telemarketing Campaign Success Prediction a Machine Learning Approach": [
            "With UCI as Data Source, conducted Data Quality Check, including Data Pre-Processing, and performed Exploratory Data Analysis to gain insights.",
            "Employed various classification-based models such as Logistic Regression, Decision Tree Classifier, Random Forest Classifier and Support Vector Machine to find potential customers with high probability of subscribing to a Bank’s Product, after model’s fine tuning with defined hyperparameters ended up with a highly capable model with an accuracy of 91%.",
            "Targeting model classified customer will result in high success rate and even results in Cost Reduction and Resource Optimization.",
            "Python Packages Utilized: NumPy, Pandas, Matplotlib, Seaborn, SciPy, Scikit Learn."
        ],
        "Predicting Indian Premier League Final Winner": [
            "With Kaggle as Data Source, conducted Data Quality Check, including Data Pre-Processing, and performed Exploratory Data Analysis to gain raw insights.",
            "Employed various classification-based models such as Logistic Regressor, rule-based Decision Tree Classifier and ensemble learner Random Forest Classifier to classify and find potential teams that has highly capable players to predict the team that has high possibility of taking cup home, after enormous fine tuning of models ended up with capable model that could possibly find the pattern to predict the winner of the season with an accuracy of 82%.",
            "Counter tackling with precise strategies of those teams might higher the chances of winning.",
            "Python Packages Utilized: NumPy, Pandas, Matplotlib, Seaborn, SciPy, Scikit Learn."
        ]
    }

    file_path = os.path.join(os.getcwd(), 'index.html')

    portfolio_page = PortfolioPage('Sudeesh Gandhi',
                                   "C:\\Users\\91755\\OneDrive\\Desktop\\GREAT _LAKES\\Sudeesh_RI4JC0XO1E.jpg",
                                   "+919600957952",
                                   "sudeeshg300398@gmail.com",
                                   "https://www.linkedin.com/in/sudeeshgandhi/",
                                   "https://github.com/Sudeeshg300398")
    header = portfolio_page.generate_header(education, skills, article_links,
                                            certifications, projects)

    footer = portfolio_page.generate_footer()

    html_content = f"{header}\n{footer}"

    # Save the HTML content to a file
    with open(file_path, 'w') as f:
        f.write(html_content)

    print(f"HTML file generated successfully at: {file_path}")


if __name__ == "__main__":
    generate_html()