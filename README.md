🚀 Databricks Data Processing Pipeline

📌 Project Overview

This project is a data processing pipeline built in Databricks using PySpark. The pipeline processes transactional data, applies transformations, and exports results to both Delta Tables and DBFS (Databricks FileStore) for further analysis.

📊 Features

Ingest transaction data from Databricks Catalog.
Apply transformations using PySpark.
Filter customers who purchased AirPods after buying an iPhone.
Join with customer data for enriched insights.
Export results to:
✅ Delta Table for scalable storage and querying.
✅ DBFS (as CSV/Parquet) for external access.
🛠️ Tech Stack

Databricks (Workspace & DBFS)
Apache Spark (PySpark)
Python
Delta Lake (for efficient storage)
Factory Design Pattern (for flexible data handling)
📂 Project Structure

databricks-project/
│── notebooks/                # Databricks Notebooks
│   ├── ingestion.py          # Loads raw data from Databricks Catalog
│   ├── transformation.py     # Processes and filters data
│   ├── export.py             # Saves processed data to Delta Table & DBFS
│── scripts/                  # Python scripts
│── data/                     # Sample input data (if needed)
│── README.md                 # Project documentation
│── .gitignore                # Files to ignore in Git
🛠️ Low-Level Design (LLD) - Factory Pattern

This project follows the Factory Pattern to manage data ingestion and data export efficiently.

Data Source Factory:
Dynamically handles different data sources (CSV, Parquet, Delta Tables) based on input type.
Ensures flexibility when adding new data formats without modifying existing logic.
Data Sink Factory:
Supports multiple output formats, allowing easy switching between Delta Table, DBFS (CSV/Parquet).
Standardizes the process of saving data without modifying core transformation logic.
Benefits of Using Factory Pattern:
✅ Encapsulation: Abstracts the logic for reading and writing data.
✅ Extensibility: Allows adding new data formats without changing existing code.
✅ Reusability: Standardizes input/output handling across the pipeline.
⚙️ Setup Instructions

1️⃣ Clone the Repository
Go to GitHub and clone the repository.
Navigate to the project folder.
2️⃣ Load Data from Databricks Catalog
Ensure the required data tables exist in Databricks Catalog before running the pipeline.

3️⃣ Apply Transformations
Run the transformation process in Databricks notebooks.

4️⃣ Export Transformed Data
Saved to Delta Table for structured querying.
Stored in DBFS (CSV & Parquet) for external access.
📢 Contributing

If you'd like to contribute:

Fork the repository.
Create a feature branch.
Commit your changes.
Push and open a Pull Request.
🔗 Useful Links

Databricks Docs
Apache Spark
Factory Pattern Design Principles
📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Your Name
GitHub
LinkedIn
