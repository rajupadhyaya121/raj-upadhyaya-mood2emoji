# Kid-Safe Text-Mood Detector

This project is a lightweight web tool that examines a short text input and returns a child-friendly mood output (such as happy, neutral, or sad).  
It is built using Python with Streamlit for the interface and TextBlob for simple sentiment scoring.  
The system also checks for unsafe vocabulary so it can be used comfortably by learners aged 12–16.

---

## 1. Setup and Run Instructions

Follow the steps below to run this application on your system:

1. **Clone the repository**
    ```bash
    git clone https://github.com/rajupadhyaya121/Text-mood-detector-for-kids.git
    cd Text-mood-detector-for-kids
    ```

2. **Install required packages**  
   Make sure you have Python 3.9+ installed, then run:
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

3. **Launch the Streamlit app**
    ```bash
    streamlit run app.py
    ```

---

## 2. What the Project Does and How Students Benefit

**Summary:**  
The app receives a sentence typed by the user and assigns it an emotional score ranging from −1 to +1.  
Depending on this score, the text is categorized into a simple mood class.  
Before evaluation, a small filter checks for sensitive or inappropriate words to keep the experience safe for younger students.

**Key Learning Outcomes (Ages 12–16):**
- How computers analyze written language on a basic level  
- What polarity means and how it relates to sentiment  
- Introduction to rule-based decision methods  
- How numbers can be used to represent feelings or opinions  

---

## 3. Teaching Approach — Approx. 60 Minutes

The session is designed around **Explain → Demonstrate → Explore**.

* **10 min — Introduction**
  * Discuss how machines attempt to interpret text and emotion

* **25 min — Demonstration + Explanation**
  * Show how the app processes input and assigns a mood label  
  * Use Teacher Mode to display polarity values and mapping logic  

* **20 min — Student Activity**
  * Students experiment with their own examples  
  * They try unusual sentences (including sarcastic attempts) and compare results  

* **5 min — Recap**
  * Review the simple rules used in classification  
  * Discuss why the model sometimes makes mistakes and why safety filters matter  

---

## 4. Known Limitations

* **Difficulty detecting sarcasm or indirect meaning:**  
  Because the logic is based on basic polarity scoring, it struggles when the literal text does not reflect the intended emotion.

* **Limited handling of slang or multilingual input:**  
  Expressions that use informal or mixed language may produce inaccurate results.

* **Challenges with nuanced expressions:**  
  Sentences like “I’m not unhappy” can confuse the system because polarity alone cannot capture layered meaning.
