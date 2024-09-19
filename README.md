# Generative AI System: Text-to-Image & Text-to-Video

This project is focused on developing a **Generative AI System** that converts text inputs into images and videos. It includes the implementation of machine learning models, the creation of a web and mobile application, cloud deployment, and observability tools.

## Project Structure

```
├── .expo                 # React Native configurations
├── .github               # GitHub Actions CI/CD pipeline 
├── .vscode               # VS Code workspace settings
├── cloud_infrastructure  # Terraform for AWS infrastructure
├── data                  # Dataset storage (MS COCO, TDIUC)
├── docs                  # Project documentation
├── mobile_app            # React Native mobile app code
├── web_app               # Flask-based web app code (Frontend & Backend)
├── .gitignore            # Git ignore file
└── README.md             # Project overview (this file)
```

## Steps Breakdown

### 1. Data Collection
- **Text-to-Image (MS COCO Dataset)**: Preprocess and organize the dataset for use in the model.
- **Text-to-Video (TDIUC Dataset)**: Download and preprocess for text-to-video tasks.

### 2. Model Development

#### Text-to-Image Model
- **Model**: [Stable Diffusion](https://github.com/CompVis/stable-diffusion) or a similar model is used for generating images from text.
- **Hardware Requirements**:
  - **CPU**: AMD or Intel CPU
  - **RAM**: Minimum 16 GB
  - **Storage**: 256 GB SSD (minimum)
  - **GPU**: GeForce RTX GPU with 8 GB VRAM (minimum)

#### Text-to-Video Model
- **Model**: [CogVideo](https://github.com/THUDM/CogVideo) or a similar model for generating videos from text.
- **Hardware Requirements**:
  - **GPU**: NVIDIA RTX 3090 or better
  - **RAM**: 16 GB or more
  - **Storage**: Sufficient space for datasets, model weights, and generated videos

### 3. Web Application Development

- **Backend**: Flask server with endpoints to trigger text-to-image and text-to-video generation.
- **Frontend**: HTML/CSS/JavaScript interface for users to input text and view results.
  
#### Example Frontend (index.html):
- Simple input forms for users to generate images or videos.

### 4. Mobile Application Development

- **Framework**: React Native
- **Features**: Mobile app allows users to input text and receive generated images or videos.

### 5. CI/CD Pipeline Setup

- **GitHub Actions**: Automate building, testing, and deploying the models.
- **Pipeline Steps**:
  1. Code checkout
  2. Dependency installation
  3. Testing
  4. Deployment to AWS

### 6. Cloud Infrastructure

- **Services**:
  - **Amazon ECS**: Container orchestration for deploying models.
  - **Amazon S3**: Store generated media (images and videos).
  - **Amazon RDS** (Optional): For storing logs and metadata.
  
- **Terraform**: Scripts for defining and provisioning cloud infrastructure.

### 7. Deployment

- Use the CI/CD pipeline to deploy the application to AWS using **Amazon ECS** and **S3**.

### 8. Observability

- **Amazon CloudWatch**: Monitoring, logging, and alerting.
- **AWS X-Ray**: Tracing for requests and performance analysis.
- **SLI/SLO/SLA**: Define and monitor service level indicators, objectives, and agreements.

### 9. Documentation and Presentation

- **Documentation**: Includes setup instructions, model details, and cloud infrastructure setup. Document code logic, key files, and configuration.
  
## Setup Instructions

### 1. Prerequisites
- Install Python (>=3.8)
- Node.js (for React Native)
- Docker (for containerization)
- AWS CLI (for cloud deployment)
- Terraform (for infrastructure as code)

### 2. Setup Python Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/generative-ai-system.git

# Navigate into the project directory
cd generative-ai-system

# Create a virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Linux/MacOS
# On Windows:
# .\.venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Dataset Preprocessing
Place your datasets in the `data/` folder, and run the preprocessing scripts located in `data_collection/`.

```bash
# For MS COCO
python data_collection/preprocess_coco.py

# For TDIUC
python data_collection/preprocess_tdiuc.py
```

### 4. Run the Web Application
Start the Flask server and access the web app:

```bash
cd web_app
python app.py
```
Access the application at `http://localhost:5000`.

### 5. Run the Mobile Application
To run the mobile app, follow the steps below:

```bash
cd mobile_app
npm install
npx expo start
```

Open the mobile app on an Android or iOS emulator.

### 6. Deploy to AWS

Use the GitHub Actions workflow to trigger the CI/CD pipeline. Ensure your AWS credentials are configured correctly.

```bash
terraform init
terraform apply
```

### 7. Monitoring & Observability

Logs and metrics are accessible via **Amazon CloudWatch**, while request tracing can be analyzed using **AWS X-Ray**.

## License


## Contributors

- Chaphowasit Mahayossanan (chaphowasit.work@gmail.com)

---