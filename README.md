# 🛍️ Customer Segmentation using K-Means

Customer segmentation project using **K-Means clustering** on mall customers dataset. The model groups customers based on **Annual Income** and **Spending Score**, helping businesses design targeted marketing strategies.

---

## 📂 Dataset

The project uses the **Mall\_Customers.csv** dataset with the following columns:

* `CustomerID` – Unique customer ID
* `Gender` – Male/Female
* `Age` – Age of the customer
* `Annual Income (k$)` – Annual income in thousands
* `Spending Score (1-100)` – Score assigned by the mall based on customer behavior

---

## ⚙️ Workflow

1. **Data Loading** – Import dataset using `pandas`.
2. **Feature Selection** – Use `Annual Income` and `Spending Score` for clustering.
3. **Standardization** – Scale features using `StandardScaler`.
4. **Elbow Method** – Determine optimal number of clusters (`k`).
5. **K-Means Clustering** – Train model with chosen `k`.
6. **Visualization** – Plot customer clusters with `matplotlib` & `seaborn`.
7. **Save Results** – Export dataset with cluster labels to `Clustered_Customers.csv`.

---

## 📊 Results

* **Elbow Method Graph** – To find the optimal `k`.
* **Scatter Plot** – Visualizes customer segments.
* **Clustered Dataset** – Saved as `Clustered_Customers.csv`.

---

## 🚀 Installation & Usage

Clone the repository and run the script:

```bash
# Clone repo
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation

# Install dependencies
pip install -r requirements.txt

# Run script
python customer_segmentation.py
```

---

## 📦 Requirements

* Python 3.x
* pandas
* matplotlib
* seaborn
* scikit-learn

(You can create a `requirements.txt` with these inside 👆)

---

## 📌 Applications

* Market segmentation for targeted marketing
* Customer behavior analysis
* Loyalty program personalization
* Business strategy & decision-making

---

## 🖼️ Example Output

### Elbow Method

*(screenshot of the elbow plot here)*

### Customer Segments

*(screenshot of the scatter plot here)*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or submit an issue.


