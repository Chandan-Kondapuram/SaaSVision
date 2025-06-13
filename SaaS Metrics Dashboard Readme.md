# 🚀 SaaS Metrics Dashboard — Real-Time Analytics Pipeline

A fully integrated real-time SaaS analytics dashboard that captures, processes, models, and visualizes critical KPIs across a customer lifecycle. Built using **Kafka, Spark, BigQuery, dbt, and Power BI** on Microsoft Fabric.

---

## 📊 Live Dashboard Preview

<img src="dashboard-preview.png" alt="SaaS Metrics Dashboard" width="800"/>

---

## 🛠️ Tech Stack

* **Data Simulation & Ingestion**: Python + Faker + Kafka
* **Stream Processing**: Apache Spark (Structured Streaming)
* **Data Warehouse**: Google BigQuery
* **Transformation Layer**: dbt (Data Build Tool)
* **Data Modeling & Viz**: Power BI (Microsoft Fabric) using Lakehouse
* **Automation & Refresh**: Power BI Dataflow Gen2

---

## 🔁 Real-Time Pipeline Flow

Kafka → Spark → BigQuery → dbt → Power BI (Lakehouse) → Dashboard

---

## 📈 KPIs Tracked

| KPI                                | Description                              |
| ---------------------------------- | ---------------------------------------- |
| 📦 Monthly Recurring Revenue (MRR) | Monthly subscription-based revenue       |
| 💵 Average Revenue Per User (ARPU) | Total revenue ÷ active users             |
| 📉 Churn Rate                      | % of users who stopped using the service |
| 📈 Upgrade Rate                    | % of users who moved to a higher plan    |
| 💳 Payment Volume                  | Total \$ across plans                    |
| 🔁 Signup Conversion               | Trial → Paid user ratio                  |
| 👤 Daily Active Users (DAU)        | Number of unique daily users             |
| 🌍 Active Users by Region          | Geo-based engagement                     |
| 🧝 Plan Distribution               | % users by Basic / Pro / Enterprise      |
| 🔍 Trial Users Active              | Trials still engaged                     |
| 🔐 Customer Lifetime Value (CLV)   | Total expected revenue/user              |
| ⌛ Average Session Frequency        | Avg logins/user/week                     |
| 🧾 Monthly Signups                 | New signups each month                   |
| 💬 Revenue by Region               | Geo-specific revenue impact              |

---

## 📂 Project Structure

📁 kafka-producer/        → Real-time data simulator
📁 spark-streaming/       → Kafka consumer + BigQuery writer
📁 dbt/                   → Models for transforming KPIs
📁 powerbi/               → Dashboard + visuals
📁 credentials/           → GCP service account keys

---

## 📷 Screenshots

* KPI cards (MRR, ARPU, DAU)
* Line chart for MRR trend
* Geo-map of users by region
* Bar charts for plan/payment breakdown
* Conversion trendlines & spark visuals

---

## 🚀 How to Run This Project

1. `python kafka_producer.py` – Starts event stream
2. `spark-submit spark_stream.py` – Real-time processing
3. `dbt run` – Load and model BigQuery data
4. Connect **Power BI to BigQuery or Lakehouse**
5. Build dashboard with visual KPIs

---

## 💼 Use Case

Designed for product managers, growth teams, or SaaS founders who want to **monitor metrics that matter**, **identify churn risk**, and **drive subscription growth** in real time.

---

## 🤝 Connect with Me

If this project resonates with you, feel free to connect on [LinkedIn](https://linkedin.com/in/your-profile), or reach out to collaborate or chat about data engineering or analytics.

---

## 📢 Hiring Managers & Recruiters

This dashboard demonstrates:

* Real-time event stream processing
* End-to-end data pipeline design
* Business-focused KPI development
* Visual storytelling using Power BI

Let’s talk!
