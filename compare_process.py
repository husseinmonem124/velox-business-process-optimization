import matplotlib.pyplot as plt

stages = [
    "Payment",
    "Inventory Check",
    "Warehouse Picking",
    "Packing",
    "Shipping",
    "Queue / Waiting"
]

current_times = [
    2.52,
    1.52,
    2.99,
    1.01,
    1.50,
    2.47
]

improved_times = [
    0.25,
    0.25,
    1.50,
    0.50,
    1.50,
    0.50
]

x = range(len(stages))

plt.figure(figsize=(10, 6))

plt.bar(
    [i - 0.2 for i in x],
    current_times,
    width=0.4,
    label="AS-IS"
)

plt.bar(
    [i + 0.2 for i in x],
    improved_times,
    width=0.4,
    label="TO-BE"
)

plt.xticks(x, stages)
plt.ylabel("Average Time (Hours)")
plt.title("VELOX AS-IS vs. TO-BE Process Time")
plt.legend()

plt.tight_layout()
plt.savefig("velox_as_is_vs_to_be.png")

cost_per_order_before = 8.50
cost_per_order_after = 6.00

cost_saving_per_order = cost_per_order_before - cost_per_order_after
monthly_orders = 2000

monthly_savings = cost_saving_per_order * monthly_orders
annual_savings = monthly_savings * 12

print(f"Cost saving per order: €{cost_saving_per_order:.2f}")
print(f"Potential monthly savings: €{monthly_savings:,.2f}")
print(f"Potential annual savings: €{annual_savings:,.2f}")

plt.show()