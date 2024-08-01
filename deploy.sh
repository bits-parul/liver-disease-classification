#!/bin/bash

# Variables
REMOTE_USER="ec2-user"
REMOTE_HOST="16.171.44.242"
REMOTE_PATH="/home/ec2-user"
MODEL_PATH="/home/ec2-user/model-deployment/models"
APP_PATH="/home/ec2-user/model-deployment/app"
KEY_PATH="/home/ec2-user/testing-key.pem"

# Copy the model file to the EC2 instance
scp -i "$KEY_PATH" "models/liver_disease_randomforest_model.joblib" $REMOTE_USER@$REMOTE_HOST:$MODEL_PATH

# Copy the Flask application files to the EC2 instance
scp -i "$KEY_PATH" "src/app.py" $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH

# SSH into the EC2 instance and start the Flask application
ssh -i "$KEY_PATH" $REMOTE_USER@$REMOTE_HOST << 'EOF'
    cd /home/ec2-user/model-deployment/app
    sudo yum update -y
    sudo yum install python3 -y
    pip3 install flask joblib requests jsonify
    nohup python3 app.py &
EOF