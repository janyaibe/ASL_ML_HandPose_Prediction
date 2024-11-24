# ASL Machine Learning Hand Pose Prediction

## Overview
This project uses machine learning (ML) techniques to predict and analyze hand poses for American Sign Language (ASL). It aims to differentiate between expert and novice hand motions by leveraging TensorFlow, MediaPipe, and OpenCV.

The primary objective is to create a scalable pipeline that processes video data, extracts hand landmarks, and predicts skill levels based on hand motion accuracy.

---

## Features
- Hand pose detection using MediaPipe.
- Video data preprocessing using OpenCV.
- Machine Learning prediction using TensorFlow.
- SQLite database integration for efficient data storage.
- Optimized pipelines for large-scale data using TensorFlow `tf.data`.

---

## Installation

### Prerequisites
- Python 3.8+
- SQLite (pre-installed in most Python distributions)
- Git

### Clone the Repository
```bash
git clone https://github.com/your-username/ASL_ML_HandPose_Prediction.git
cd ASL_ML_HandPose_Prediction
