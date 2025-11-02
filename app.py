{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "de57e484-7624-4491-80de-88536c2b4bee",
   "metadata": {},
   "source": [
    "# Import necessary libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6435c952-02d2-49a5-9a24-9b9e45642bae",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0a51e116-a5a0-43c6-afa9-fbbe997b553a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: textblob in c:\\users\\acer\\anaconda3\\lib\\site-packages (0.19.0)\n",
      "Requirement already satisfied: nltk>=3.9 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from textblob) (3.9.1)\n",
      "Requirement already satisfied: click in c:\\users\\acer\\anaconda3\\lib\\site-packages (from nltk>=3.9->textblob) (8.1.8)\n",
      "Requirement already satisfied: joblib in c:\\users\\acer\\anaconda3\\lib\\site-packages (from nltk>=3.9->textblob) (1.4.2)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from nltk>=3.9->textblob) (2024.11.6)\n",
      "Requirement already satisfied: tqdm in c:\\users\\acer\\anaconda3\\lib\\site-packages (from nltk>=3.9->textblob) (4.67.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\acer\\anaconda3\\lib\\site-packages (from click->nltk>=3.9->textblob) (0.4.6)\n",
      "Finished.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package brown to\n",
      "[nltk_data]     C:\\Users\\ACER\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package brown is already up-to-date!\n",
      "[nltk_data] Downloading package punkt_tab to\n",
      "[nltk_data]     C:\\Users\\ACER\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt_tab is already up-to-date!\n",
      "[nltk_data] Downloading package wordnet to\n",
      "[nltk_data]     C:\\Users\\ACER\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package wordnet is already up-to-date!\n",
      "[nltk_data] Downloading package averaged_perceptron_tagger_eng to\n",
      "[nltk_data]     C:\\Users\\ACER\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package averaged_perceptron_tagger_eng is already up-to-\n",
      "[nltk_data]       date!\n",
      "[nltk_data] Downloading package conll2000 to\n",
      "[nltk_data]     C:\\Users\\ACER\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package conll2000 is already up-to-date!\n",
      "[nltk_data] Downloading package movie_reviews to\n",
      "[nltk_data]     C:\\Users\\ACER\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package movie_reviews is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "!pip install textblob\n",
    "!python -m textblob.download_corpora"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "26062756-3c66-4dbb-b30c-952b67b02551",
   "metadata": {},
   "outputs": [],
   "source": [
    "from textblob import TextBlob"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef78a6df-eeb0-4db3-8bda-81124905336b",
   "metadata": {},
   "source": [
    "# List of banned words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1a662454-799e-4fe3-b915-735add942a22",
   "metadata": {},
   "outputs": [],
   "source": [
    "banned_words=['fuck','bitch','ass','mf','hell','shit','nigga'] # here we can put all banned words "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44d6a00b-eab0-4991-ab77-e4bdd3227f86",
   "metadata": {},
   "source": [
    "# Check if word is not banned"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "098212cb-9dc1-4d34-8d86-88b3e1a18e0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def safe_word(word):\n",
    "    for word in banned_word:\n",
    "        if word in text.lower(): # convert word into lower\n",
    "            return False # check if the word is a banned word\n",
    "        return True"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51a535be-4aa4-436d-a703-89771e78b99b",
   "metadata": {},
   "source": [
    "# Function to detect mood"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d78b88a5-baec-4803-8bec-99670ee2d21a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_mood(word):\n",
    "    blob=TextBlob(word)\n",
    "    polarity=blob.sentiment.polarity # checing the polarity of word\n",
    "    if polarity>0.3:\n",
    "        return '😀','the sentence sounds happy'\n",
    "    elif polarity<-0.3:\n",
    "        return '😞','the sentence sounds sad'\n",
    "    else:\n",
    "        return '😞','the sentence sounds neutral'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4538912-07c7-4f89-8d22-efb4cefe0565",
   "metadata": {},
   "source": [
    "# Setup streamlit environment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "477ecbb1-7d91-4cbd-9b84-75fa645a5cee",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-02 17:04:42.153 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.160 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.161 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.162 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.163 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.164 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.165 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.166 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.168 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.168 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.169 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.170 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:42.172 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.title('kid safe text mood detector') #title of hosting site\n",
    "# taking input from user\n",
    "sentence=st.text_input('enter a word')\n",
    "# setup button that runs when user enters\n",
    "if st.button('click me'):\n",
    "    # if no input provided warn user\n",
    "    if sentence.strip()=='':\n",
    "        st.write('please enter a word')\n",
    "    # if word is a safe word we proceed\n",
    "    elif safe_word(sentence):\n",
    "        emote,definition=get_mood(sentence)\n",
    "        st.write(f\" Output : {emote} & {explanation}\")\n",
    "    else:\n",
    "        st.write(\"Inappropirate word detected\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "173b0398-ce53-42c0-9e9f-39d546842df7",
   "metadata": {},
   "source": [
    "# Teacher Mode to visualize how app works"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "bb16101f-090f-4bcc-8dcc-505c1863132b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-02 17:04:43.150 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:43.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:43.157 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:43.159 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-02 17:04:43.160 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.checkbox('teacher_mode'):#displaying a teacher mode checkbox\n",
    "    st.write('This app is analyzing simple word sentiment')\n",
    "    st.write(' if polarity >0.3-- :), happy sentiment')\n",
    "    st.write(' if polarity <-0.3-- :(, negative sentiment')\n",
    "    st.write(' if neutral polarity-- \\-/, neutral sentiment')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cbdaf00-1791-4a84-8359-e79a0a69d70f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
