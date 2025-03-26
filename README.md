# Classification of Amazon Fine Food Reviews using LSTM  

##  Team Members  
- **Aashka Chhabra**  
- **Anchi Kansal**  
- **Anubha Sharma**  
- **Ansh Shekokar**  
- **Anushka Verma**  

---

##  Model Architecture  

###  Embedding Layer  
The **Embedding Layer** converts words into dense vectors of fixed size, allowing the model to learn relationships between words.  

**Example:**  
- Words like **"king"** and **"queen"** might be positioned near each other in vector space, capturing semantic similarity.  

---

###  LSTM Layer (Long Short-Term Memory)  
The **LSTM Layer** is responsible for processing sequences while retaining context over long sentences.  

 **Why LSTM?**  
- Unlike traditional neural networks, LSTMs handle long-term dependencies.  
- It remembers important contextual information, e.g., **"not good"** has a different sentiment than **"good"**.  

---

###  Dense Layer  
The **Dense Layer** is the output layer responsible for making predictions based on learned patterns.  

 Fully connected neurons aggregate information from the previous layers.  

 The number of neurons depends on the output requirement (e.g., 1 neuron for binary classification).  

---

###  Sigmoid Activation Function  
The **Sigmoid Activation Function** is used in the final layer to output probabilities between 0 and 1.  

 **Why Sigmoid?**  
- Since this is a binary classification problem (**positive** or **negative** sentiment), sigmoid helps interpret the model's confidence in a particular class.  

 **Formula:**  
\[
sigma(x) = 1/(1 + e^(-x))
\]  
where \( x \) is the input from the previous layer.  

---

###  Dropout Regularization  
The **Dropout Layer** is used to prevent overfitting by randomly disabling neurons during training.  

 **Why Dropout?**  
- Forces the network to learn redundant patterns, improving generalization.  
- Helps in reducing model complexity and preventing over-reliance on specific neurons.  

---

##  Training and Testing the Model  
The model will be trained and tested using the **Amazon Fine Food Reviews Dataset** from Kaggle.  

###  Steps:  
1. **Data Preprocessing:**  
   - Remove punctuation, numbers, and stop words.  
   - Normalize uppercase and lowercase letters.  
2. **Tokenization & Padding:**  
   - Convert text into numerical sequences.  
   - Apply padding to ensure uniform input sizes.  
3. **Model Training:**  
   - Train using LSTM with different hyperparameters.  
4. **Evaluation:**  
   - Compare performance using accuracy and loss metrics.  

---

##  Dataset Information  
- **Dataset:** [Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)  
- **Total Reviews:** 568,454  
- **Timeframe:** Oct 1999 – Oct 2012  
- **Total Products:** 74,258  

---

##  Summary  
This project implements sentiment analysis using LSTMs to classify customer reviews as **positive** or **negative**. By using **embedding layers**, **LSTMs**, **dense layers**, and **dropout regularization**, the model learns contextual relationships in text data.  

 **Key Benefits:**  
- Improved sentiment classification using deep learning.  
- Context-aware feature extraction via LSTM.  
- Robust performance with dropout regularization.  

---

