# AWS Polly Audio Generator
==========================

A simple web application that converts text to speech in Hindi using Amazon Polly.

## Project Description
-------------------

This project is a Streamlit application that allows users to input text and generate an MP3 audio file using AWS Polly.

## Badges
---------

| Badge | Value | Target |
| --- | --- | --- |
| Python | 3.8 | Python 3.8 |
| Streamlit | 0.84.0 | Streamlit 0.84.0 |
| Boto3 | 1.24.22 | Boto3 1.24.22 |

## Overview and Key Features
---------------------------

* Convert text to speech in Hindi using AWS Polly
* Generate MP3 audio files
* User-friendly web interface using Streamlit

## Technology Stack
-----------------

* **Languages:** Python
* **Frameworks:** Streamlit
* **Libraries:**
	+ Boto3 (AWS SDK for Python)
	+ OpenAI
	+ Python-dotenv
* **Infrastructure:** AWS Polly, AWS S3 (for storing generated audio files)

## Architecture
-------------

```mermaid
graph LR
    User-->|Input Text| Streamlit App
    Streamlit App-->|Call AWS Polly| backend/polly_service.py
    backend/polly_service.py-->|Generate Audio| AWS Polly
    AWS Polly-->|Store Audio| generated_audio/
    Streamlit App-->|Display Audio| User
```

## Project Structure
------------------

```markdown
aws-polly-audio-generator/
├── backend/
│   ├── __init__.py
│   ├── polly_service.py
│   └── ...
├── configuration/
│   ├── __init__.py
│   ├── config.py
│   └── ...
├── frontend/
│   ├── __init__.py
│   ├── streamlit_app_polly.py
│   └── ...
├── generated_audio/
├── project demo images/
└── requirements.txt
```
![aws-polly-audio-generator](./project%20demo%20images/polly01.png)

![aws-polly-audio-generator](./project%20demo%20images/polly02.png)

![aws-polly-audio-generator](./project%20demo%20images/polly04.png)

![aws-polly-audio-generator](./project%20demo%20images/polly03.png)

## Prerequisites
--------------

* AWS account with AWS Polly setup
* Python 3.8 installed
* `pip install -r requirements.txt`

## Installation and Setup
-------------------------

1. Install the required dependencies using `pip install -r requirements.txt`
2. Set up your AWS environment variables
3. Run the application using `streamlit run frontend/streamlit_app_polly.py`

## Environment Variables
----------------------

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_REGION`

## How to Run the Application
-----------------------------

1. Install the required dependencies using `pip install -r requirements.txt`
2. Set up your AWS environment variables
3. Run the application using `streamlit run frontend/streamlit_app_polly.py`

## API Endpoints and Usage Examples
---------------------------------

* The application uses the AWS Polly API to generate audio files
* The application has a UI feature to input text, generate audio, and display the generated audio file

## Database or AI/RAG Workflow
-----------------------------

* The application uses AWS Polly, which is an AI-powered text-to-speech service
* The application stores generated audio files in the `generated_audio/` directory, which is not a database

## Testing Instructions
----------------------

There are no tests in the repository.

## Docker or Deployment Instructions
---------------------------------

There are no deployment scripts or infrastructure configuration in the repository.

## Security Notes
----------------

* The application assumes that the user has an AWS account and has set up the necessary environment variables for AWS Polly
* The application assumes that the user has installed the required dependencies using `pip install -r requirements.txt`

## Limitations and Future Improvements
--------------------------------------

* The application does not have any tests
* The application does not have any deployment scripts or infrastructure configuration
* Future improvements:
	+ Add tests for the application
	+ Add deployment scripts and infrastructure configuration

## Contribution and License
-------------------------

This project is not open-sourced.
