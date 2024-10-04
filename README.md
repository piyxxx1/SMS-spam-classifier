# SMS Spam Classification System

This project is a **Natural Language Processing (NLP)** application that classifies SMS messages as **spam** or **ham** (non-spam). The system leverages **TfidfVectorizer** and the **Bag of Words** algorithm to extract features from text data, with a simple and interactive user interface built using **Streamlit**, along with some custom **HTML** and **CSS** for styling.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to develop an SMS spam classifier that can distinguish between spam and non-spam messages using NLP techniques. The classifier is built using the **TfidfVectorizer** technique for transforming text data into numerical format and the **Bag of Words** algorithm to create a vectorized representation of the SMS messages.

The project comes with a **Streamlit-based user interface**, making it easy for users to test the classification system by inputting new SMS messages and instantly seeing whether the message is classified as spam or not.

## Features

- **Text Preprocessing**: Cleans the SMS messages by removing punctuation, converting to lowercase, and tokenizing.
- **Text Vectorization**: Utilizes **TfidfVectorizer** for feature extraction.
- **Classification Algorithm**: Implements a machine learning model using **Bag of Words** (BoW) algorithm to classify messages as spam or ham.
- **User Interface**: Simple and interactive web interface built with **Streamlit** for easy message input and result display.
- **Customization**: Additional custom HTML and CSS elements for enhanced UI/UX.
  
## Technologies Used

- **Python**: Core programming language.
- **NLP**: TfidfVectorizer and Bag of Words for text vectorization.
- **Machine Learning**: For classification of spam vs ham messages.
- **Streamlit**: Web framework for building the user interface.
- **HTML/CSS**: Basic front-end styling.

## Installation

To run the project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/piyuxx1/SMS-spam-classifier.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SMS-spam-classifier
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

Once the application is running, you can input any SMS text message into the web interface, and the model will classify it as **Spam** or **Ham**.

### Example

- **Input**: "Congratulations! You've won a $1000 Walmart gift card."
- **Output**: **Spam**

## Dataset

You can find the dataset used for training and testing the model here: [SMS Spam Dataset](dataset_link_here). The dataset contains labeled examples of both spam and non-spam SMS messages.

## Contributing

Feel free to open issues or submit pull requests if you want to contribute to the project. All contributions are welcome!

## License

This project is licensed under the MIT License.

---

You can customize the placeholders like the dataset link and project repository URL according to your project setup. Let me know if you'd like any changes!
