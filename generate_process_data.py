import pandas as pd
import random
from datetime import datetime, timedelta

num_orders = 2000

order_ids = [f"ORD{100001 + i}" for i in range(num_orders)]

start_date = datetime(2025, 1, 1)

order_dates = [
    start_date + timedelta(days=random.randint(0, 364))
    for _ in range(num_orders)
]

payment_times = [
    round(random.uniform(0.5, 4.5), 2)
    for _ in range(num_orders)
]

inventory_times = [
    round(random.uniform(0.5, 2.5), 2)
    for _ in range(num_orders)
]

picking_times = [
    round(random.uniform(1.0, 5.0), 2)
    for _ in range(num_orders)
]

packing_times = [
    round(random.uniform(0.5, 1.5), 2)
    for _ in range(num_orders)
]

shipping_times = [
    round(random.uniform(0.5, 2.5), 2)
    for _ in range(num_orders)
]

queue_wait_times = [
    round(random.uniform(1.5, 3.5), 2)
    for _ in range(num_orders)
]

total_processing_times = [
    round(
        payment_times[i]
        + inventory_times[i]
        + picking_times[i]
        + packing_times[i]
        + shipping_times[i]
        + queue_wait_times[i],
        2
    )
    for i in range(num_orders)
]

inventory_errors = [
    random.random() < 0.08
    for _ in range(num_orders)
]

manual_interventions = [
    random.random() < 0.70
    for _ in range(num_orders)
]

delay_threshold = 14

delayed_orders = [
    total_processing_times[i] > delay_threshold
    for i in range(num_orders)
]

data = {
    "order_id": order_ids,
    "order_date": order_dates,
    "payment_time_hours": payment_times,
    "inventory_time_hours": inventory_times,
    "picking_time_hours": picking_times,
    "packing_time_hours": packing_times,
    "shipping_time_hours": shipping_times,
    "queue_wait_time_hours": queue_wait_times,
    "total_processing_time_hours": total_processing_times,
    "inventory_error": inventory_errors,
    "manual_intervention": manual_interventions,
    "delayed_order": delayed_orders
}

df = pd.DataFrame(data)

df.to_csv("velox_process_data.csv", index=False)

print("VELOX process dataset created successfully!")
print(f"Number of orders: {len(df)}")