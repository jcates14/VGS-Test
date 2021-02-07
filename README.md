# VGS-Test

## Overview
A basic app to test inbound and outbound routes with VGS

## Setup
1. There is a pull request waiting approval. 
2. Once PR is approved, clone repo
3. Add virtual environment to project and activate venv
4. pip3 install -r requirements.txt
5. Create an .env file in the root of the project. Add the following credentials to your .env file. See `env.example` for example.
    - HTTPS_PROXY_USERNAME
    - HTTPS_PROXY_PASSWORD
    - VAULT_ID
    - Path to .pem certificate (for outbound routes)
6. Run "python3 app.py"
7. Open browser and navigate to http://127.0.0.1:5000/ to test
