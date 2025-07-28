import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
file_name = input("Enter CSV file name (like sales_data.csv): ")
data = pd.read_csv(file_name)

# Calculate Revenue
data['Revenue'] = data['Units Sold'] * data['Unit Price']

# Group by Product
summary = data.groupby('Product')['Revenue'].sum().reset_index()

# Sort products by revenue
summary = summary.sort_values(by='Revenue', ascending=False)

# Total and top product
total_revenue = summary['Revenue'].sum()
top_product = summary.iloc[0]['Product']

# Write report to file
with open(r"Day_18_Task/report.txt", "w") as f:
    f.write("Sales Summary\n")
    for i, row in summary.iterrows():
        f.write(f"Product: {row['Product']} – Revenue: {int(row['Revenue'])}\n")
    f.write(f"\nTotal Revenue: {int(total_revenue)}\n")
    f.write(f"Top Product: {top_product}\n")

print("report.txt created!")

# Bar chart
plt.bar(summary['Product'], summary['Revenue'], color='lightgreen')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.savefig("Day_18_Task/revenue_chart.png")
print("revenue_chart.png created!")
