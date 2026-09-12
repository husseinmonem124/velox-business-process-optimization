import pandas as pd

df = pd.read_csv("velox_process_data.csv")

print(df.head())

average_processing_time = df["total_processing_time_hours"].mean()

print(f"Average processing time: {average_processing_time:.2f} hours")

average_payment = df["payment_time_hours"].mean()
average_inventory = df["inventory_time_hours"].mean()
average_picking = df["picking_time_hours"].mean()
average_packing = df["packing_time_hours"].mean()
average_shipping = df["shipping_time_hours"].mean()
average_queue_wait = df["queue_wait_time_hours"].mean()

print(f"Average payment time: {average_payment:.2f} hours")
print(f"Average inventory check time: {average_inventory:.2f} hours")
print(f"Average picking time: {average_picking:.2f} hours")
print(f"Average packing time: {average_packing:.2f} hours")
print(f"Average shipping time: {average_shipping:.2f} hours")
print(f"Average queue/waiting time: {average_queue_wait:.2f} hours")

inventory_error_rate = df["inventory_error"].mean() * 100
manual_intervention_rate = df["manual_intervention"].mean() * 100
delayed_order_rate = df["delayed_order"].mean() * 100

print(f"Inventory error rate: {inventory_error_rate:.2f}%")
print(f"Manual intervention rate: {manual_intervention_rate:.2f}%")
print(f"Delayed order rate: {delayed_order_rate:.2f}%")

stage_averages = {
    "Payment": average_payment,
    "Inventory Check": average_inventory,
    "Warehouse Picking": average_picking,
    "Packing": average_packing,
    "Shipping": average_shipping
}

bottleneck_stage = max(stage_averages, key=stage_averages.get)

print(f"Main bottleneck: {bottleneck_stage}")
print(f"Bottleneck average time: {stage_averages[bottleneck_stage]:.2f} hours")

picking_share = (average_picking / average_processing_time) * 100

print(f"Warehouse picking share of total processing time: {picking_share:.2f}%")

import matplotlib.pyplot as plt

stages = [
    "Payment",
    "Inventory Check",
    "Warehouse Picking",
    "Packing",
    "Shipping"
]

times = [
    average_payment,
    average_inventory,
    average_picking,
    average_packing,
    average_shipping
]

plt.figure(figsize=(10, 6))

plt.bar(stages, times)

plt.title("VELOX Average Processing Time by Stage")
plt.xlabel("Process Stage")
plt.ylabel("Average Time (Hours)")

plt.tight_layout()
plt.savefig("velox_process_stage_times.png")

inventory_error_count = df["inventory_error"].sum()
manual_intervention_count = df["manual_intervention"].sum()
delayed_order_count = df["delayed_order"].sum()

print(f"Orders with inventory errors: {inventory_error_count}")
print(f"Orders requiring manual intervention: {manual_intervention_count}")
print(f"Delayed orders: {delayed_order_count}")

improved_picking_time = 1.50

picking_time_saved = average_picking - improved_picking_time

print(f"Potential picking time saved per order: {picking_time_saved:.2f} hours")

improved_total_time = average_processing_time - picking_time_saved

print(f"Current average processing time: {average_processing_time:.2f} hours")
print(f"Improved average processing time: {improved_total_time:.2f} hours")
print(
    f"Potential total time reduction: "
    f"{((average_processing_time - improved_total_time) / average_processing_time) * 100:.2f}%"
)

plt.show()