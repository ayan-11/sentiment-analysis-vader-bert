# sentiment-analysis-vader-bert

# Sentiment Analysis with VADER and BERT

This project implements advanced sentiment analysis on textual data using VADER and BERT models. It classifies sentiments into seven categories and visualizes the results with pie charts and bar plots. The BERT model is integrated with TensorFlow to handle text inputs up to 512 tokens.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Visualization](#visualization)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project aims to provide a comprehensive sentiment analysis tool that leverages both the VADER sentiment analysis tool and the BERT model for multilingual sentiment classification. It includes data preprocessing, sentiment classification, and result visualization.

## Installation

### Prerequisites
- Python 3.7+
- TensorFlow
- Transformers
- Pandas
- Matplotlib
- Seaborn
- OpenPyXL

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/ayan-11/sentiment-analysis-vader-bert.git
   cd sentiment-analysis-vader-bert
   ```

2. Install the required packages:
   ```sh
   pip install tensorflow transformers pandas matplotlib seaborn openpyxl vaderSentiment
   ```

## Usage
1. Place your data file (`Output.xlsx`) in the project directory.
2. Run the Jupyter Notebook `AnalysisV2.ipynb` to perform sentiment analysis and visualization.

## Data
The project uses an Excel file (`Output.xlsx`) with a column named 'Content' containing the text entries for sentiment analysis.

## Visualization
The results are visualized using pie charts and bar plots to show the distribution of sentiments as classified by both VADER and BERT models.
Example:
![Screenshot 2024-07-30 100101](https://github.com/user-attachments/assets/38720a2a-063a-4018-a6f6-749167818d49)
![Screenshot 2024-07-30 100247](https://github.com/user-attachments/assets/9f7d1529-5d52-4ecc-a280-c1990eea1382)
![Screenshot 2024-07-30 100140](https://github.com/user-attachments/assets/6e6850fb-0cd5-4d78-b4b9-de1d333c350d)


## Results
The tool classifies sentiments into categories ranging from Very Negative to Very Positive and provides visual insights into the sentiment distribution of the analyzed texts.

## Final Output
![Screenshot 2024-07-30 100401](https://github.com/user-attachments/assets/cb090b24-3cb2-4767-b6e4-64dee9bafe7c)

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

## License
This project is licensed under the MIT License.
