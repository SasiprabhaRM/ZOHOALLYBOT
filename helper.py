

# put all my changing info here
# gets imported into app.py

titles = {'portfolio': 'Software World',
          
          'index': "GALAXY",
          
          'blog': 'Data Insights Developer',
          'apps': 'Web apps and Dashboards'
          }
messages = {'portfolio': ['Embark on a journey of innovation and coding excellence as a Software Developer with us.',
                          'Join our dynamic team, where your passion for cutting-edge technology will be nurtured, and your skills will shape the future of software development.'],
          
          'index': [ 'Our innovative employee onboarding designed to provide seamless guidance and support to new team members.', 'We are committed to enhance the onboarding experience, ensuring a smooth transition and empowering employees with the knowledge they need to thrive in our dynamic work environment.'],
          
           'blog': ['Specialized in unlocking meaningful patterns from diverse datasets, employing techniques such as NLP classification, predictive modeling, and geospatial visualization.', 'Transforming raw data into valuable insights, contributing to informed decision-making and strategic data-driven initiatives.'],

         'apps': ['Embark on a journey into web development, where your skills as a developer will shape cutting-edge digital experiences.',
                      'Join a dynamic environment, leveraging your expertise to contribute to innovative and impactful web solutions.'
                      
                      ]
          }

# latest projects
# each article [title, address, image]
blog_posts = [
            ['NLP Classification Using Keras RNN/LSTM',
             'https://levelup.gitconnected.com/painless-classification-model-using-rnn-b90cb0982543',
             'static/images/rnn_project.png', 'Level Up Coding'],
            ['Flask REST API',
             'https://sciencelee.medium.com/13483c2556b?source=friends_link&sk=f689a8286361296030c1504c9eeedb04',
             'static/images/api_blog.png', 'Level Up Coding'],
            ['Baseline Accuracy',
             'https://towardsdatascience.com/calculating-a-baseline-accuracy-for-a-classification-model-a4b342ceb88f#30fd-8213094caad9',
             'static/images/baseline_blog.png', 'Towards Data Science'],
            ['Do Traffic Cameras Make Intersections Safe?',
               'https://towardsdatascience.com/chicago-red-light-cameras-and-traffic-safety-a6c5f08e5c4',
               'static/images/rlc_blog.png', 'Towards Data Science'],
            ['Geocoding with Nomantim',
               'https://levelup.gitconnected.com/simple-geocoding-in-python-fb28ee5272e0',
               'static/images/geo_blog.png', 'Level Up Coding'],
              ['Plots With Pandas Groupby',
               'https://python.plainenglish.io/making-plots-with-the-pandas-groupby-ac492941af28',
               'static/images/groupby_blog.png', 'Python in Plain English'],
              ['Deploy Predictive Model with Flask',
               'https://levelup.gitconnected.com/deploy-a-predictive-model-with-flask-33c1976293cc',
               'static/images/deploy_flask.png', 'Level Up Coding'],
            ['PySpark in Google Colab',
               'https://sciencelee.medium.com/using-pyspark-with-google-colab-8bca09c11f91',
               'static/images/pyspark_blog.png', 'Medium'],
            ['Chain Store Election Modeling',
               'https://towardsdatascience.com/are-you-a-trader-joes-democrat-or-a-walmart-republican-a7b156131435',
               'static/images/election_blog.png', 'Towards Data Science'],
            ['Folium Maps (Housing)',
               'https://levelup.gitconnected.com/visualizing-housing-data-with-folium-maps-4718ed3452c2',
               'static/images/folium_blog.png', 'Level Up Coding'],
            ['Boruta Feature Selection',
               'https://towardsdatascience.com/simple-example-using-boruta-feature-selection-in-python-8b96925d5d7a',
               'static/images/boruta_blog.png', 'Towards Data Science'],
            ['Folium Maps (Earthquakes)',
               'https://levelup.gitconnected.com/plotting-usgs-earthquake-data-with-folium-8f11ddc21950',
               'static/images/earthquake_blog.png', 'Level Up Coding'],
            ['Multivariate Linear Regression',
               'https://medium.com/swlh/multivariable-linear-regression-basics-62425ac4eafa',
               'static/images/linreg_blog.png', 'The Startup'],
            ['Python List Comprehension Essentials',
            'https://sciencelee.medium.com/list-comprehensions-for-beginners-fc4998991419?sk=c0359b92c9ead0f75f6fe8f7808af08e',
             'static/images/comprehension_blog.png', 'Level Up Coding'],

            ['Python Sorting Essentials',
             'https://levelup.gitconnected.com/sorting-in-python-using-keys-d2622edd7a92',
             'static/images/sorting_blog.png', 'Level Up Coding'],
              ]

# each project [title, address, image, whet2lookfor]
projects = [['Chicago Red Light Camera Accident Study',
                'https://github.com/sciencelee/chicago_rlc',
                'static/images/rlc_project.png',
                '''In this impactful data engineering initiative, data from over nine diverse sources is harmonized into a cohesive SQLite database. The project employs statistical methodologies like t-tests, Logistic Regression, Linear Regression, and Random Forest to craft robust predictive and inferential models, contributing to a comprehensive and insightful data analysis.'''],

            ['Pediatric X-ray classification',
                'https://github.com/sciencelee/xray-pneumonia-ML',
                'static/images/xray_project.png',
                '''Employing a Convolutional Neural Network (CNN), this advanced project demonstrates a precision rate surpassing 98% in predicting the occurrence of pneumonia. Notably, the model seamlessly operates within the Google Colab framework, highlighting adept utilization of cutting-edge deep learning methodologies for accurate and efficient medical diagnostics.'''],

            ['Chain Store Voting Habits',
                'https://github.com/sciencelee/chainstore-election-model',
                'static/images/vote_project.png',
                '''Significant data engineering to combine 2018 congressional election results with state and county information, 
                combined with the presence of more than 20 store chains including: Starbucks, Target, Cracker Barrel, WalMart etc.  
                Web scraping with Beautiful Soup was used to get many store locations.  GeoPandas used to place stores inside voting
                districts.  XGBoost and Random Forest models used to predict party voting habits by presence of stores at > 70% accuracy.  
                Use of Folium and Mapbox with Plotly.'''],

            ['King County Housing Model',
                'https://github.com/sciencelee/seattle-housing-model',
                'static/images/king_project.png',
                '''Significant feature engineering including addition of school districts and other proximity features
                to mapped locations.  A linear Regression model created with only 5 features and an r2 score of 0.70'''],

            ['Twitter Sentiment Evaluator',
                'https://github.com/sciencelee/twitter-sentiment-evaluator',
                'static/images/twitter_project.png',
                '''Utilizing Natural Language Processing techniques with nltk and GloVe vectors, this project analyzes a labeled dataset containing Twitter reviews focusing on Apple and Google products. The approach combines advanced linguistic processing to extract insights from user sentiments, offering a nuanced examination of opinions on these technology giants.'''],

            ['College Recommendation System',
             'https://github.com/sciencelee/college_api',
             'static/images/college_project.png',
             '''Built on Flask, this project features a RESTful API driving a content-based college recommendation system tailored for students. The system leverages advanced algorithms to deliver personalized recommendations, offering a concise and efficient tool for guiding college-bound individuals in their decision-making process.'''],

            ]

# each project [title, address, image, whet2lookfor]
apps = [
            ['Red Light Camera Web App (Plotly Dash)',
                'https://rlc.sciencelee.com/',
                'static/images/RLC_webapp.png',
                '''This project utilizes API queries to gather live data from various databases on the Chicago Data Portal. The data is visualized using Plotly, including line, scatter, and Mapbox plots, within a Dash application hosted on Heroku. The application streamlines the exploration of 150+ intersections and over 8,000 red light crashes, providing an easily navigable map interface for efficient data analysis.'''],

            ['FIRST Tech Challenge Team Maps Web App (Plotly Dash)',
                'http://ftcapp.sciencelee.com//',
                'static/images/ftc-app.png',
                '''This dashboard, integrates data from The Orange Alliance API. Utilizing Plotly in a Dash application on Heroku, it provides an interactive exploration of high scores for over 3,000 teams and 75,000 matches worldwide, offering insights at the city, state, and country levels.'''],

            ['X-ray Classification Web App (Flask)',
                'https://xray.sciencelee.com/',
                'static/images/xray_webapp.png',
                '''Flask web application that classifies user loaded image using an h5 stored CNN model hosted on Heroku.'''],

            ['This Portfolio Website! (Flask and Bootstrap CSS)',
              'https://www.sciencelee.com/apps',
              'static/images/website.png',
              '''This portfolio website employs a template and Jinja notation to dynamically showcase information from a static Python file. The design, featuring Bootstrap and custom CSS, prioritizes a clean and consistent look for straightforward updates.
              '''
             ],

            ['College Recommendation API and web app',
              'https://www.collegereco.com/',
              'static/images/college_reco.png',
              '''This project involves creating a RESTful API to deliver results from a content-based recommendation system. This system empowers student users to discover colleges similar to those they have already identified as potential targets, enhancing the efficiency of their exploration and decision-making process. '''
             ]
          ]

