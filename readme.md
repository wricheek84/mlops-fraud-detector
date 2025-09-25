# End-to-End MLOps Fraud Detection Pipeline

This project demonstrates a full, end-to-end MLOps pipeline for a real-world fraud detection use case. The pipeline covers everything from data preprocessing and model training to containerization, CI/CD, and preparation for cloud deployment.

## Features
- **Model Development:** Trained and evaluated a high-performance XGBoost model on a highly imbalanced credit card fraud dataset.
- **API Server:** Built a robust REST API using FastAPI to serve model predictions in real-time.
- **Containerization:** Packaged the entire application (API and model) into a portable, lightweight Docker image.
- **CI/CD Automation:** Implemented a complete CI/CD pipeline with GitHub Actions that automatically builds the Docker image and pushes it to a container registry (Docker Hub) on every commit to the main branch.

## Tech Stack
- **Languages:** Python
- **Data Science:** Pandas, Scikit-learn, SMOTE, XGBoost
- **API:** FastAPI, Uvicorn
- **Containerization:** Docker
- **CI/CD:** Git, GitHub Actions
- **Cloud (Planned):** AWS, Kubernetes (EKS)

## Project Status
This project is fully developed and containerized, with a CI/CD pipeline that automatically builds and publishes the application to Docker Hub. The final deployment to a live Kubernetes cluster is currently on hold due to the resource limitations of cloud provider free tiers, which are insufficient for a stable EKS cluster. The Kubernetes `deployment.yml` and `service.yml` manifest files are complete and included in the repository.

## How to Run Locally
1. Ensure you have Docker installed and running.
2. Pull the image from Docker Hub:
   ```bash
   docker pull your-wricheek01/mlops-fraud-detector:latest