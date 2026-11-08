import matplotlib.pyplot as plt
import pandas as pd

# Read sales data
df = pd.read_csv("sales.csv")

# Display sales data
print("SALES DATA")
print(df)

# Calculate revenue
df["revenue"] = df["quantity"] * df["unit_price"]

print("\nSALES WITH REVENUE")
print(df)
# 1. Calculate Total Revenue

total_revenue = df["revenue"].sum()

print("\nTOTAL REVENUE")
print(total_revenue)


# 2. Find Best-Selling Product by Quantity

product_sales = df.groupby("product")["quantity"].sum()

best_selling_product = product_sales.idxmax()

print("\nBEST-SELLING PRODUCT")
print(best_selling_product)


# 3. Find Highest Revenue Product

product_revenue = df.groupby("product")["revenue"].sum()

highest_revenue_product = product_revenue.idxmax()

print("\nHIGHEST REVENUE PRODUCT")
print(highest_revenue_product)


# 4. Calculate Average Revenue

average_revenue = df["revenue"].mean()

print("\nAVERAGE REVENUE")
print(round(average_revenue, 2))
# 5. Product Performance Summary

product_summary = df.groupby("product").agg(
    total_quantity=("quantity", "sum"),
    total_revenue=("revenue", "sum")
)

product_summary = product_summary.sort_values(
    by="total_revenue", ascending=False
)

print("\nPRODUCT PERFORMANCE SUMMARY")
print(product_summary)
# 6. Sales Revenue Bar Chart

plt.figure(figsize=(10, 5))

plt.bar(
    product_summary.index,
    product_summary["total_revenue"]
)

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (£)")
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("sales_revenue_chart.png")
plt.show()