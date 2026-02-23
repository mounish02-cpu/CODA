# 🚀 CODA  
## Cross-Platform Observation and Detection Assistant  

CODA is an Explainable AI-based misinformation intelligence system designed to analyze news statements and detect potential manipulation indicators using linguistic analysis and real-time global news verification.

Unlike traditional black-box models, CODA provides transparent reasoning, confidence scoring, and structured verdicts to promote responsible digital information consumption.

---

# 🌍 Project Overview

Misinformation spreads rapidly across digital platforms using emotional manipulation, urgency bias, symbolic cues (emojis), and sensational language.

CODA addresses this challenge by combining:

- Rule-based Natural Language Processing (NLP)
- Emoji semantic analysis
- Personal information detection
- Manipulation detection
- Confidence-based risk scoring
- Real-time global news verification via Google News RSS

The system outputs a multi-level verdict:

🟢 Safe  
🟡 Warning  
🔴 High Risk  

---

# 🧠 Core Features

### 🔍 Linguistic Analysis
- Detects sensational and manipulative language
- Identifies emotional framing
- Recognizes urgency bias

### 😀 Emoji Influence Detection
Interprets psychological signals from emojis such as:
- 🔥 Hype amplification
- 👇 Attention redirection
- 🚨 Urgency signaling
- 😱 Fear induction

### 🔐 Personal Information Detection
- Identifies phone numbers
- Detects email addresses
- Recognizes identity phrases ("my name is", "I am")
- Warns users about privacy risks

### 📊 Confidence Scoring
Risk score calculated based on:
- Manipulative language
- Emoji usage
- Personal information presence
- News validation

### 🌐 Global News Verification
- Extracts keywords from input
- Queries Google News RSS
- Displays matching global news sources
- Filters unrelated articles

### 🟢🟡🔴 Traffic-Light Verdict UI
Interactive dashboard blocks show:
- Verdict
- Confidence percentage
- Warnings
- Matched news links

---

# 🏗 System Architecture
