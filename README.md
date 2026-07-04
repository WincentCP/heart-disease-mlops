# Workflow-CI: Automated MLOps Pipeline with GitHub Actions

An end-to-end MLOps workflow that automates machine learning training, evaluation, experiment tracking, and Docker image creation using GitHub Actions. This project demonstrates how Continuous Integration (CI) can streamline machine learning development and improve reproducibility.

---

## Overview

This project implements an automated CI pipeline for machine learning using **GitHub Actions**. Every code push or pull request triggers a workflow that prepares the environment, trains a machine learning model, logs experiments with MLflow, evaluates model performance, and optionally builds a Docker image.

The goal is to demonstrate modern MLOps practices by integrating software engineering workflows into machine learning development.

---

## Features

- Automated CI pipeline using GitHub Actions
- Machine learning model training
- MLflow experiment tracking
- Model performance evaluation
- Docker image build automation
- Reproducible Python environment using Conda
- Version-controlled machine learning workflow

---

## Project Structure

```text
Workflow-CI/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│
├── src/
│
├── mlruns/
│
├── MLproject
├── conda.yaml
├── Dockerfile
├── train.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python
- Scikit-learn
- MLflow
- GitHub Actions
- Docker
- Conda
- Git

---

## Workflow

The CI pipeline performs the following steps:

1. Trigger workflow on push or pull request.
2. Set up the Python environment.
3. Install project dependencies.
4. Execute the MLflow Project.
5. Train a Random Forest classification model.
6. Log parameters, metrics, and artifacts with MLflow.
7. Evaluate model performance.
8. Build a Docker image automatically.
9. (Optional) Push the image to Docker Hub.

---

## Machine Learning Pipeline

The project demonstrates a reproducible ML workflow consisting of:

- Data loading
- Data preprocessing
- Train-test split
- Random Forest model training
- Model evaluation
- Experiment tracking with MLflow
- Artifact logging

---

## CI/CD Workflow

```text
Git Push
     │
     ▼
GitHub Actions
     │
     ▼
Install Dependencies
     │
     ▼
Run MLflow Project
     │
     ▼
Train Model
     │
     ▼
Evaluate Performance
     │
     ▼
Log Experiment
     │
     ▼
Build Docker Image
```

---

## Learning Objectives

This project demonstrates knowledge of:

- Continuous Integration (CI)
- MLOps fundamentals
- Experiment tracking
- Machine learning automation
- Docker containerization
- Reproducible ML workflows
- Version control with Git

---

## Future Improvements

- Continuous Deployment (CD)
- Model Registry integration
- Automated model validation
- Unit and integration testing
- Data versioning with DVC
- Cloud deployment (AWS/GCP/Azure)
- Model monitoring and drift detection
