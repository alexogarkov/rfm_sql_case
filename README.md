
# 🧠 RFM & Cohort Analysis Case (SQL + BI + Python)

This project demonstrates how to implement and visualize customer segmentation using **RFM analysis** and **Cohort analysis**, powered by cloud-hosted PostgreSQL, Python, and Power BI.

## 🔍 Use Case

- Segment customers based on Recency, Frequency, and Monetary value (RFM)
- Track cohort-based retention and revenue evolution
- Monitor transitions between RFM segments over time

---

## ⚙️ Tech Stack

| Layer               | Tools Used                                       |
|---------------------|--------------------------------------------------|
| **Database**        | [Neon.tech](https://neon.tech) (serverless PostgreSQL) |
| **SQL Interface**   | DBeaver                                          |
| **Analytics Logic** | PostgreSQL SQL Views (CTE, WINDOW, NTILE)       |
| **BI Platform**     | Microsoft Power BI (Ribbon, Chord, Treemap)     |
| **Custom Viz**      | Python + Matplotlib (3D voxel matrix)           |

---

## 📁 Repo Contents

```
├── data/
│   └── orders.csv                      # Synthetic dataset
│
├── sql/
│   ├── customer_cohort_quarterly.sql  # Assigns cohort per customer
│   ├── rfm_current_segments.sql       # Calculates current RFM segments
│   ├── rfm_historical_segments.sql    # Calculates historical RFM segments
│   └── segment_definitions.sql        # Segment label mapping
│
├── python/
│   └── rfm_voxel_plot.py              # Custom matplotlib 3D visualization
│
├── powerbi/
│   └── rfm_cohort_dashboard.pbix      # Power BI dashboard (optional)
│
└── README.md
```

---

## 🚀 How to Run

1. Load `orders.csv` into Neon PostgreSQL (or local instance).
2. Run SQL scripts to create views.
3. Connect to DB from Power BI or Python.
4. Customize visualizations or extend with your own logic.

---

## 📬 Author

Made by **Aleksei Ogarkov**  
Feel free to connect: [Telegram](https://t.me/aleks_comex) · [LinkedIn](https://www.linkedin.com/in/ogarkovalex/) · [GitHub](https://github.com/alexogarkov)
