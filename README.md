RoadIQ

GIS-Based Road Maintenance Intelligence Platform

RoadIQ is an interactive GIS dashboard developed to support data-driven road maintenance and infrastructure management. The application combines geospatial visualization, database analytics, and maintenance prioritization to help authorities identify critical road issues and make informed maintenance decisions.

---

Live Demo

🔗 https://roadiqwe.streamlit.app/

---

 Features

- Interactive GIS map of the Bengaluru road network
- Visualization of pothole complaint locations
- Multiple map layers (Street, Light, Dark)
- Key Performance Indicators (KPIs)
  - Road Segments
  - Pothole Complaints
  - Repair Records
  - Wards Covered
- Analytics Dashboard
  - Top 10 Wards by Complaint Count
  - Complaint Status Distribution
  - Monthly Complaint Trend
- Maintenance Priority Recommendation System
- SQLite-based backend for efficient querying

---

Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| GIS | GeoPandas, Folium |
| Visualization | Plotly |
| Database | SQLite |
| Data Processing | Pandas |

---

Dataset

The project uses publicly available road infrastructure and complaint datasets for Bengaluru.

Data includes:
- Road Network
- Pothole Complaints
- Repair Records
- Ward Information

---

Project Structure

```
RoadIQ/
│
├── app.py
├── analytics.py
├── database.py
├── gis.py
├── priority.py
├── queries.py
├── data_loader.py
├── requirements.txt
├── README.md
│
├── database/
│   └── roadiq.db
│
└── data/
    └── Bengaluru/
```

---

Dashboard Overview

  GIS Map
  Interactive visualization of Bengaluru's road network and pothole complaint locations.

  Analytics
  - Complaint status distribution
  - Monthly complaint trends
  - Top 10 wards with the highest complaint counts

  Maintenance Priority
  Generates maintenance recommendations based on complaint information to support decision-making.

---


Future Improvements

- Multi-city support
- Ward-based filtering
- Real-time complaint integration
- User authentication
- Interactive reporting and exports

---

Author

Vaishnavi Patil

Civil Engineering Undergraduate, NIT Goa

GitHub: https://github.com/v-ai-sh-navi

---
