# Expected results

| Fixture | What was generated | Must report |
|---------|--------------------|-------------|
| `noise` | Independent ratings: no factors, no segments | no valid segmentation |
| `one-population` | One skewed trait moving every rating: correlated, no segments | no valid segmentation |
| `planted` | Three segments of 75 / 60 / 45, each underserved on every third outcome | k = 3, agreement with `planted-segments.csv` at ARI ≥ 0.8, each segment's top needs from its own third |

For the two without segments there must also be no segment profiles and no
Differentiated or Discrete strategy. Both would have passed the old
silhouette > 0.25 rule.
