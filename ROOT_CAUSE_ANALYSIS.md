# VELOX — Root Cause Analysis

## 1. Purpose

The purpose of this analysis is to identify the underlying causes of the bottlenecks found in the current VELOX order fulfillment process.

Instead of only describing the visible problems, the analysis looks at why these problems occur.

## 2. Root Cause Overview

| Problem                   | Root Cause                                         | Business Impact                 | Improvement Opportunity             |
| ------------------------- | -------------------------------------------------- | ------------------------------- | ----------------------------------- |
| Slow payment verification | Manual payment confirmation                        | Orders remain on hold           | Automated payment confirmation      |
| Slow inventory checks     | Employees manually verify stock                    | Orders wait before picking      | Real-time inventory validation      |
| Warehouse queues          | Orders are processed in a largely sequential queue | Long fulfillment times          | Automated order prioritization      |
| Inventory discrepancies   | Inventory data is not updated consistently         | Rework and order delays         | Real-time inventory synchronization |
| Slow packing              | Manual product verification                        | Additional processing time      | Barcode scanning                    |
| Slow communication        | Departments rely on manual messages                | Waiting and coordination delays | Centralized workflow system         |

## 3. Root Cause 1 — Manual Payment Verification

### Visible Problem

Orders can remain in the payment verification stage for several hours.

### Root Cause

The process depends on employees manually checking and confirming payment information.

### Business Impact

Paid orders cannot continue immediately, increasing the total order processing time.

### Proposed Direction

Introduce automated payment confirmation so successfully paid orders can automatically proceed to the next stage.

---

## 4. Root Cause 2 — Manual Inventory Verification

### Visible Problem

Orders wait before warehouse picking can begin.

### Root Cause

Inventory availability is manually checked rather than being automatically validated when an order is placed.

### Business Impact

This creates unnecessary waiting time and increases employee workload.

### Proposed Direction

Use automated real-time inventory validation when an order is received.

---

## 5. Root Cause 3 — Warehouse Queue Management

### Visible Problem

Orders spend significant time waiting before being picked.

### Root Cause

Warehouse orders are not automatically prioritized according to factors such as order age, shipping priority, or customer requirements.

### Business Impact

Some orders remain in the queue longer than necessary.

### Proposed Direction

Introduce an automated order-prioritization system.

---

## 6. Root Cause 4 — Inventory Data Accuracy

### Visible Problem

Approximately 8% of orders experience an inventory discrepancy.

### Root Cause

Inventory information is not consistently synchronized with actual warehouse stock.

### Business Impact

Employees must investigate discrepancies, causing rework and delays.

### Proposed Direction

Synchronize warehouse and inventory data in real time and introduce regular stock validation.

---

## 7. Root Cause 5 — Manual Packing Verification

### Visible Problem

Packing requires additional manual verification.

### Root Cause

Employees manually compare products with order information.

### Business Impact

The process takes longer and is vulnerable to human error.

### Proposed Direction

Introduce barcode scanning to automatically verify products before shipment.

---

## 8. Root Cause 6 — Fragmented Communication

### Visible Problem

Employees sometimes need to wait for information from another department.

### Root Cause

Order-related communication is distributed across different employees and departments rather than being managed through one centralized workflow.

### Business Impact

Employees spend time waiting for responses and manually communicating order status.

### Proposed Direction

Create a centralized workflow where order status and required actions are automatically visible to the relevant teams.

## 9. Overall Root Cause

The analysis indicates that the main underlying issue is **process fragmentation**.

VELOX relies heavily on manual verification, manual communication, and disconnected process steps.

As a result, employees spend significant time moving information between stages instead of directly processing customer orders.

The proposed TO-BE process should therefore focus on:

1. Automation
2. Real-time data synchronization
3. Centralized workflow management
4. Automated prioritization
5. Reduced manual verification
6. Better process visibility
