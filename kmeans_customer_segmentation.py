import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load Dataset
data = pd.read_csv('Mall_Customers.csv')

# Step 2: Select Features (e.g., Annual Income & Spending Score)
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 3: Standardize the Data (Optional but recommended)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Find Optimal K using Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8,4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Step 5: Apply K-Means with optimal k (let's say k=5)
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Step 6: Add Cluster to DataFrame
data['Cluster'] = clusters

# Step 7: Visualize the Clusters
plt.figure(figsize=(8,5))
sns.scatterplot(
    x=data['Annual Income (k$)'], 
    y=data['Spending Score (1-100)'], 
    hue=data['Cluster'], 
    palette='Set1', 
    s=100
)
plt.title('Customer Segments based on Annual Income & Spending Score')
plt.show()

# Step 8: Save the Result (optional)
data.to_csv('Clustered_Customers.csv', index=False)
print("Customer Segmentation Complete!")
