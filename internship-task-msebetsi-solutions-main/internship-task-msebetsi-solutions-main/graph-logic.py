import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Income-Expense.xlsx'
df = pd.read_excel(file_path)

month_num = range(1, len(df) + 1)

plt.figure(figsize=(13, 5))
bar_width = 0.4
spacing = 0
font_size = 6

plt.bar([num + spacing for num in month_num], df['Income'], label='Income', color='green', width=bar_width)
plt.bar([num + bar_width + spacing * 2 for num in month_num], df['Expense'], label='Expense', color='red', width=bar_width)

for i, income in enumerate(df['Income']):
    plt.text(month_num[i] + spacing, income, f'{income:.2f}', ha='center', va='bottom', color='black', rotation=0, fontsize=font_size)

for i, expense in enumerate(df['Expense']):
    plt.text(month_num[i] + bar_width + spacing * 2, expense, f'{expense:.2f}', ha='center', va='bottom', color='black', rotation=0, fontsize=font_size)

plt.xlabel('Month')
plt.ylabel('Amount (Rands)')
plt.title('Income and Expenses in the Last 12 Months')
plt.legend()

plt.xticks([num + bar_width + spacing for num in month_num], df['Month'], rotation=45)

plt.tight_layout()
plt.grid(True)
plt.show()
