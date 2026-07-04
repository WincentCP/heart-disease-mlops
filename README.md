# Heart Disease MLOps Pipeline

An end-to-end MLOps pipeline for heart disease prediction using a Random Forest classifier. This project demonstrates how machine learning models can be trained, tracked, containerized, and automatically deployed through a CI/CD workflow.

## Overview

Built on the processed heart disease dataset, this repository automates the machine learning lifecycle—from model training and experiment tracking to Docker image creation and deployment using GitHub Actions.

## Features

* Random Forest classifier
* Automated model training
* Hyperparameter tuning
* MLflow experiment tracking
* DagsHub remote experiment logging
* GitHub Actions CI/CD
* Docker containerization
* Automated Docker Hub deployment

## Tech Stack

* Python
* scikit-learn
* MLflow
* DagsHub
* GitHub Actions
* Docker

## Project Structure

```text
.
├── .github/
│   └── workflows/          # CI/CD workflow
├── MLProject/              # Training pipeline and MLflow project
├── .workflow/
├── .gitignore
└── README.md
```

## Workflow

1. Load the processed dataset.
2. Train a Random Forest classifier.
3. Perform hyperparameter tuning.
4. Track experiments with MLflow and DagsHub.
5. Automatically trigger GitHub Actions on every push.
6. Evaluate the model.
7. Build a Docker image.
8. Push the image to Docker Hub (when credentials are configured).

## Highlights

* End-to-end automated machine learning workflow
* Experiment reproducibility with MLflow
* CI/CD pipeline using GitHub Actions
* Containerized deployment with Docker
* Easily extendable to production environments

