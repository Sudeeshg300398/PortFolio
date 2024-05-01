import base64


class PortfolioPage:
    def __init__(self, title, image_path, phone, email, linkedin, github):
        self.title = title
        self.image_path = image_path
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.github = github

    def generate_header(self, education, skills, article_links, certifications, projects):
        # Prepare education HTML
        education_html = ""
        for item in education:
            education_html += f"<p>{item}</p>"

        # Prepare skills HTML
        skills_html = "<ul>"
        for skill, tools in skills.items():
            tools_list = ", ".join(tools)
            skills_html += f"<li><strong>{skill}</strong>: {tools_list}</li>"
        skills_html += "</ul>"

        # Prepare articles HTML
        articles_html = ""
        for article, title in article_links.items():
            articles_html += f"<a href='{article}' target='_blank'>{title}</a><br>"

        # Prepare certifications HTML
        certifications_html = "<ul>"
        for cert in certifications:
            certifications_html += f"<li>{cert}</li>"
        certifications_html += "</ul>"

        # Prepare projects HTML
        projects_html = ""
        for project, details in projects.items():
            project_details_html = "<ul>"
            for detail in details:
                project_details_html += f"<li>{detail}</li>"
            project_details_html += "</ul>"
            projects_html += f"<div class='project'><h3>{project}</h3>{project_details_html}</div>"

        # Encode image to base64
        with open(self.image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

        # Combine all HTML sections
        header = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{self.title}</title>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                .header {{
                    background-color: #007bff;
                    color: #fff;
                    padding: 20px;
                    text-align: center;
                    position: relative;
                    border-bottom-left-radius: 50%;
                    border-bottom-right-radius: 50%;
                }}
                .header img {{
                    position: absolute;
                    top: 20px;
                    right: 20px;
                    border-radius: 50%;
                    border: 3px solid #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                    width: 140px;
                    height: 140px;
                }}
                .header p {{
                    font-size: 14px; /* Reduced font size for additional details */
                    margin: 5px 0; /* Added margin for spacing */
                }}
                .white-text {{
                    color: #fff; /* Set text color to white */
                }}
                .separator {{
                    color: #000; /* Set separator color to black */
                }}
                .education p {{
                    margin: 0; /* Remove margin from paragraphs within education div */
                }}
                .project {{
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>{self.title}</h1>
                <img src="data:image/jpeg;base64,{encoded_image}" alt="Portfolio Image">
                <p><span class="white-text">{self.phone}</span> <span class="separator">|</span> <a href="mailto:{self.email}" class="white-text">{self.email}</a> <span class="separator">|</span> <a href="{self.linkedin}" target="_blank" class="white-text">LinkedIn</a> <span class="separator">|</span> <a href="{self.github}" target="_blank" class="white-text">GitHub</a></p>
            </div>

            <div class="education">
                <h2>Education</h2>
                {education_html}
            </div>

            <div class="skills">
                <h2>Skills & Tools</h2>
                {skills_html}
            </div>

            <div class="articles">
                <h2>Articles</h2>
                {articles_html}
            </div>

            <div class="certifications">
                <h2>Certifications</h2>
                {certifications_html}
            </div>

            <div class="projects">
                <h2>Academic Projects</h2>
                {projects_html}
            </div>

            <div class="container">
        """
        return header

    def generate_footer(self):
        footer = """
            </div>
        </body>
        </html>
        """
        return footer

    def generate_content(self, content):
        return f"{content}"


skills = {
    "Programming Language": ["Python"],
    "Data Management": ["MySQL"],
    "Data Mining & Exploratory Data Analysis": ["Seaborn", "Matplotlib", "Plotly", "Tableau"],
    "Statistical Analysis": ["Descriptive Statistics", "Inferential Statistics", "Hypothesis Testing"],
    "Machine Learning": ["Supervised (Regression, Classification)", "Unsupervised (Clustering)", "NLP"],
    "Web Scraping": ["Requests", "Beautiful Soup"],
    "Tools": ["Jupyter Notebook", "PyCharm"]
}

education = [
    "Post Graduation Program: Data Science & Engineering, Great Lakes Institute, June 2023.",
    "Bachelor of Engineering: Mechanical Engineering, Anna University, India, August 2020."
]

certifications = [
    "Six Sigma White Belt",
    "Data Analytics Using Excel",
    "Data Analytics Using Tableau and PowerBI",
    "Hanker Rank Intermediate (Python and SQL)",
    "The Complete Python Bootcamp- Udemy"
]

article_links = {
    "https://www.linkedin.com/pulse/object-oriented-programming-sudeesh-gandhi-tzokc/?trackingId=dri58FtFTTqGfRlC8%2Fi9eQ%3D%3D": "Object-Oriented Programming",
    "https://www.linkedin.com/pulse/natural-langage-processing-sudeesh-gandhi-k49ae/?trackingId=c4mfEd2dQDO8A2At30mU1g%3D%3D": "Natural Language Processing (NLP) in Python"
}

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

portfolio_page = PortfolioPage("Sudeesh Gandhi",
                               "C:\\Users\\91755\\OneDrive\\Desktop\\GREAT _LAKES\\Sudeesh_RI4JC0XO1E.jpg",
                               +919600957952, "sudeeshg300398@gmail.com", "https://www.linkedin.com/in/sudeeshgandhi/",
                               "https://github.com/Sudeeshg300398")

# Generate header with skills and education
header = portfolio_page.generate_header(education, skills, article_links, certifications, projects)

# Generate footer
footer = portfolio_page.generate_footer()

# Combine all sections to form the complete page
html_content = f"{header}\n{footer}"

# Save HTML content to a file
with open("portfolio.html", "w") as f:
    f.write(html_content)

print("Portfolio page created successfully!")
