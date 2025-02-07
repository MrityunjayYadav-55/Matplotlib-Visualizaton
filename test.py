import numpy as np
import matplotlib.pyplot as plt

m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
p1 = [250, 270, 300, 310, 290, 330]
p2 = [300, 340, 400, 380, 350, 420]
p3 = [200, 210, 250, 230, 220, 270]
p4 = [220, 260, 280, 300, 310, 330]
p5 = [180, 190, 200, 220, 240, 260]

fig, ar = plt.subplots(2, 2, figsize=(10, 8))

# for 0, 0 : 
ar[0, 0].plot(m, p1, marker='o', linestyle="-", color='r', label="Product_1")
ar[0, 0].plot(m, p2, marker='s', linestyle=":", color='b', label="Product_2")
ar[0, 0].plot(m, p3, marker='D', linestyle="-.", color='g', label="Product_3")
ar[0, 0].plot(m, p4, marker='x', linestyle="--", color='orange', label="Product_4")
ar[0, 0].plot(m, p5, marker='.', linestyle=":", color='cyan', label="Product_5")
ar[0, 0].set_title("Sales Distribution")
ar[0, 0].set_xlabel("Months")
ar[0, 0].set_ylabel("Sales")
ar[0, 0].legend()
ar[0, 0].grid(True)

# for 0, 1 :
total_sales = [sum(p1), sum(p2), sum(p3), sum(p4), sum(p5)]
products = ["p1", "p2", "p3", "p4", "p5"]

ar[0, 1].bar(products, total_sales, color=("r", "g", "b", "purple", "cyan"))
ar[0, 1].set_title("Total Sales For Each Product")
ar[0, 1].set_xlabel("Products")
ar[0, 1].set_ylabel("Total Sales")
ar[0, 1].grid(True)

# for 1, 0 :
all_sales = p1 + p2 + p3 + p4 + p5
ar[1, 0].hist(all_sales, bins=15, color='r', edgecolor='black', label="Sales Distribution")
ar[1, 0].set_title("All Sales Histogram Distribution")
ar[1, 0].set_xlabel("Sales value")
ar[1, 0].set_ylabel("Frequency")
ar[1, 0].legend()
ar[1, 0].grid(True)

# for 1, 1 :
p = [p1, p2, p3, p4, p5]
ar[1, 1].boxplot(p, labels=["p1", "p2", "p3", "p4", "p5"])
ar[1, 1].set_title("Sales Variability per Product")
ar[1, 1].set_xlabel("Products")
ar[1, 1].set_ylabel("Sales")
ar[1, 1].grid(True)

plt.tight_layout()
plt.savefig("Sales_analysis.png", dpi=300, bbox_inches="tight")
plt.show()
