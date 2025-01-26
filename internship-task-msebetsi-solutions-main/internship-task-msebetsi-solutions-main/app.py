import os
from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI environments
import matplotlib.pyplot as plt
import json
from io import BytesIO
import base64
from numpy import int64, float64

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_data_for_month(df, month):
    month_data = df[df['Month'] == month]
    if not month_data.empty:
        income = month_data['Income'].iloc[0]
        expense = month_data['Expense'].iloc[0]
        return income, expense
    else:
        return None, None


def generate_temporal_graph(df):
    month_num = range(1, len(df) + 1)

    # Plot the data as a double bar graph
    plt.figure(figsize=(13, 5))
    bar_width = 0.4
    spacing = 0
    font_size = 6

    plt.bar([num + spacing for num in month_num], df['Income'], label='Income', color='green', width=bar_width)
    plt.bar([num + bar_width + spacing * 2 for num in month_num], df['Expense'], label='Expense', color='red',
            width=bar_width)

    for i, income in enumerate(df['Income']):
        plt.text(month_num[i] + spacing, income, f'{income:.2f}', ha='center', va='bottom', color='black', rotation=0,
                 fontsize=font_size)

    for i, expense in enumerate(df['Expense']):
        plt.text(month_num[i] + bar_width + spacing * 2, expense, f'{expense:.2f}', ha='center', va='bottom',
                 color='black', rotation=0, fontsize=font_size)

    plt.xlabel('Month')
    plt.ylabel('Amount (Rands)')
    plt.title('Income and Expenses in the Last 12 Months')
    plt.legend()

    plt.xticks([num + bar_width + spacing for num in month_num], df['Month'], rotation=45)

    # Save the graph to a bytes buffer and convert it to a base64 string
    buffer = BytesIO()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    # highest income and expense months
    highest_income_month = df.loc[df['Income'].idxmax(), 'Month']
    highest_expense_month = df.loc[df['Expense'].idxmax(), 'Month']

    # lowest income and expense months
    lowest_income_month = df.loc[df['Income'].idxmin(), 'Month']
    lowest_expense_month = df.loc[df['Expense'].idxmin(), 'Month']

    # average income and expense for the whole dataset
    average_income = df['Income'].mean()
    average_expense = df['Expense'].mean()

    # Get the data for each month as a dictionary
    months_data = df.to_dict(orient='list')

    return graph_data, highest_income_month, highest_expense_month, lowest_income_month, lowest_expense_month, average_income, average_expense, months_data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return "No selected file"

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            df = pd.read_excel(file_path)

            app.config['uploaded_df'] = df

            graph_data, highest_income_month, highest_expense_month, lowest_income_month, lowest_expense_month, average_income, average_expense, months_data = generate_temporal_graph(df)

            return render_template('graph.html',
                                   graph_data=graph_data,
                                   highest_income_month=highest_income_month,
                                   highest_expense_month=highest_expense_month,
                                   lowest_income_month=lowest_income_month,
                                   lowest_expense_month=lowest_expense_month,
                                   average_income=average_income,
                                   average_expense=average_expense,
                                   months_data=months_data)


@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        data = request.get_json()
        selected_month = data.get('month')

        df = app.config['uploaded_df']

        income, expense = get_data_for_month(df, selected_month)

        income = int(income) if isinstance(income, (int64, int)) else float(income)
        expense = int(expense) if isinstance(expense, (int64, int)) else float(expense)

        return jsonify({'income': income, 'expense': expense})


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=False)  # Set debug=False to avoid threading issues
