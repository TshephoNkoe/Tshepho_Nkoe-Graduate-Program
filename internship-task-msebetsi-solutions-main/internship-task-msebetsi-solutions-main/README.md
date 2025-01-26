# internship-task - Msebetsi Solutions

# Financial Data Visualization

This is a Flask web application that allows users to upload an Excel file containing financial data for the past 12 months. The app generates a temporal graph displaying income and expense trends and provides summary statistics based on the uploaded data.

### Folder Structure  
- app.py: The main Flask application file containing the routes and functions to handle file uploads and data processing.  

- uploads/: The folder where uploaded Excel files are saved.

- templates/: Contains the HTML templates for rendering the web pages.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contact](#contact)

## Description

The Financial Data Visualization App is built using Flask, a Python web framework. It allows users to analyze their financial data visually and gain insights into their income and expenses over the past year. The app supports data in the form of an Excel file, and it automatically generates a graph showing the income and expense trends for each month. Additionally, the app calculates summary statistics such as the highest and lowest income and expense months and the average income and expense for the entire dataset.

## Features

- Upload Excel file containing financial data.
- Generate a temporal graph displaying income and expense trends.
- Calculate highest and lowest income and expense months.
- Calculate average income and expense for the entire dataset.
- Select a specific month to view detailed income and expense data.

## Installation

To run the app locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command in the project directory:

```bash
pip install -r requirements.txt
```

3. Start the Flask app by running:

```bash
python app.py
```

The app will be accessible at `http://localhost:5000/` in your web browser.

## Usage

1. Open your web browser and go to `http://localhost:5000/`.
2. Fill in the required information in the form, including the first name, last name, date of birth, and upload an Excel file containing financial data for the past 12 months.
3. Click the "Upload" button to submit the form and view the temporal graph along with summary statistics.
4. Use the dropdown menu to select a specific month and click the "Get Data" button to view detailed income and expense data for that month.

## Demo

A video demonstration called demo.mp4 has been provided to show how it works

## Contact

- Email: [tshephonkoe@gmail.com](mailto:tshephonkoe@gmail.com)
---
