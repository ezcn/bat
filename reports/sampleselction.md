### Selection of samples for whole-genome sequencing 

We leveraged RNA sequencing data from 105 Glossophaga soricina bats to conduct an initial relatedness inference analysis, which revealed distinct kinship patterns between two colonies and guided the strategic selection of 20 representative individuals for comprehensive long-read genome sequencing, ensuring optimal coverage of the population's genetic diversity while minimizing redundancy in closely related specimens.

- [Colony Comparisons](img/colonies.png)


With the following algorithm we choose 20 bats to be sequenced. We consider:
 
 - Sex balance.
 - Picking from different colonies.
 - Maximizing genetic diversity through PCA analysis and kmeans clustering.
 - Check that selected bats are not related.
 - Show it in two dimensional PCA.

For this, we will use metadata file, and genenetwork.csv file, with the genetic information from the bats.

```python 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

genetic_data = bats_df.iloc[:, 4:].transpose()

genetic_data_filled = genetic_data.fillna(genetic_data.median())

scaled_data = StandardScaler().fit_transform(genetic_data_filled)

pca = PCA(n_components=2) 
principal_components = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['Animal_ID'] = genetic_data.index
pca_df.head()
```

- [PCA](https://github.com/MarsicoFL/batPed/assets/55600771/5072c38c-96ef-4173-b36c-f606f1b6e376)

The selection!

|       PC1 |       PC2 | Animal_ID | Colony | Sex |
|----------:|----------:|:----------|:-------|:----|
| -23.9876  | -18.286   | GSO-12-p  | GC     | M   | 
|  13.498   | -13.1921  | GSO-138-d | GC     | M   | 
|  27.143   |  22.4251  | GSO-97-c  | GC     | M   |
|  37.656   |  -4.86746 | GSO-143-p   | GC     | F   | 
|  52.8923  | -20.8896  | GSO-63-g  | GC     | M   | 
|   2.14418 |   2.47417 | GSO-116-b | GC     | F   |
|  25.0437  |  -3.15348 | GSO-111-c  | GC     | M   | 
|  31.3515  | -39.149   | GSO-45-k  | GC     | F   | 
|  40.4481  | -30.7723  | GSO-59-c  | GC     | F   | 
|  43.2621  |  27.6184  | GSO-58-f  | GC     | F   | 
| -53.6469  | -29.3207  | GSO-79-p  | LC     | M   |
| -48.7845  |  11.1514  | GSO-129-b | LC     | M   |
| -39.8911  |  19.5242  | GSO-90-n  | LC     | M   |
| -29.414   |  31.7277  | GSO-133-h | LC     | M   |
| -26.9571  |  -9.0733  | GSO-33-k  | LC     | M   | 
| -50.4741  | -20.2984  | GSO-88-c  | LC     | F   |
| -33.6347  |  10.1725  | GSO-6-d   | LC     | F   | 
| -26.4434  | -48.3378  | GSO-112-n | LC     | F   |
| -13.7882  | -26.2434  | GSO-70-p  | LC     | F   |
|  -1.48976 | -27.0941  | GSO-25-p  | LC     | M   | 

(*) Indicate that this individuals could be changed and are released from gender balance definition.

- [Selection](https://github.com/MarsicoFL/batPed/assets/55600771/7d6671eb-4b8c-4915-9748-4dee1e5e22a7)

We also check it with previously performed clustering (available on the bat dropbox):
- [clustering](https://github.com/MarsicoFL/batPed/assets/55600771/497eac72-ac6f-46dd-8aa5-ce1a4133b1ec)

