import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
df["species"] = iris.target

print(df.head())

X = df.drop("species", axis=1)
y = df["species"]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)

X_pca = pca.fit_transform(X_scaled)
pca_df = pd.DataFrame(
    X_pca,
    columns=["PC1", "PC2", "PC3"]
)
pca_df["species"] = y

print("\n=== Dados transformados ===")
print(pca_df.head())

print("\n=== Variância explicada ===")

print(pca.explained_variance_ratio_)

print("\nVariância total preservada:", sum(pca.explained_variance_ratio_))

plt.figure(figsize=(8, 6))

cores = ["red", "green", "blue"]

for especie, cor in zip(range(3), cores):

    subset = pca_df[pca_df["species"] == especie]

    plt.scatter(
        subset["PC1"],
        subset["PC2"],
        c=cor,
        label=iris.target_names[especie]
    )

plt.xlabel("Componente Principal 1 (PC1)")
plt.ylabel("Componente Principal 2 (PC2)")

plt.title("PCA aplicado ao Dataset IRIS")
plt.legend()
plt.grid(True)
plt.show()