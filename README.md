# Genomic Variant Classification for MECP2 Mutation Pathogenicity

## Overview
This project applies **machine learning** techniques to classify **MECP2 gene mutations** as **benign** or **pathogenic**. MECP2 mutations are associated with **Rett Syndrome** and other **neurodevelopmental disorders**, making their accurate classification crucial for diagnosis and targeted therapies.

## Motivation
Despite advancements in genomic sequencing, the **functional impact** of novel mutations remains **challenging** to determine. Traditional **wet-lab validation** is expensive and time-consuming. This study aims to **bridge the gap** by using **ML models** that integrate **genomic sequence context, mutation type, and transition/transversion ratios** for enhanced classification accuracy.

## Dataset
- **Source:** ClinVar database
- **Size:** 802 MECP2 gene variants
- **Preprocessing:**
  - Applied filters for **germline classification** (Pathogenic, Likely Pathogenic, Benign, Likely Benign)
  - Included only **Single Nucleotide Variants (SNVs)**
  - Converted raw data into **structured CSV format**
  - Feature extraction based on **mutation type, nucleotide context, and molecular consequences**
  - Encoded categorical variables using **one-hot encoding**
  - Normalized numerical features using **Min-Max scaling**
  - Split into **80% training and 20% testing**

## Machine Learning Models
We employed two classification models:
1. **Random Forest (RF)**
   - Utilizes **ensemble learning** to improve classification accuracy
   - Feature selection based on **Gini impurity**
   - Hyperparameter tuning: **100 trees, depth = 10**
   - Accuracy: **93.1%**
  
2. **XGBoost (Extreme Gradient Boosting)**
   - **Boosting-based** learning for complex feature interactions
   - Uses **gradient boosting** to optimize classification performance
   - Hyperparameter tuning: **Tree depth, learning rate, regularization**
   - Accuracy: **97.5% (best performer)**

## Results
- **XGBoost outperformed Random Forest** with:
  - **Accuracy:** 97.5%
  - **Precision:** 98% (Pathogenic) / 97% (Benign)
  - **Recall:** 93% (Pathogenic) / 99% (Benign)
- **5-Fold Cross-Validation Results:**
  - XGBoost: **95.5% ± 1.28%**
  - Random Forest: **93.3% ± 1.29%**
- Transition-to-transversion ratio and molecular consequences played a key role in pathogenicity classification.

## Key Contributions
- First study to apply **ML-based classification** for **MECP2 gene mutations**.
- Developed a **highly accurate** classifier for genomic variant interpretation.
- Reduced reliance on **wet-lab validation** with **computational insights**.
- Identified **missense mutations** as the most influential in disease outcomes.
- Proposed an **efficient data preprocessing pipeline** for genomic datasets.

## Future Work
- Expand dataset to include **insertions, deletions, and structural variants**.
- Explore **deep learning models** (e.g., CNNs, RNNs) for improved classification.
- Improve model interpretability using **SHAP/LIME**.
- Validate results using **larger clinical datasets**.
- Develop a **web-based tool** for real-time MECP2 mutation classification.

## Citation
If you use this work, please cite:
> **Sravya Sri Mallampalli**, Chandra Mohan Dasari, *Genomic Variant Classification for MECP2 Mutation Pathogenicity*, Indian Institute of Information Technology, Sri City, Andhra Pradesh, India.
