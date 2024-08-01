#!/bin/bash

# Variables
REMOTE_USER="ec2-user"
REMOTE_HOST="13.60.59.177"
REMOTE_PATH="/home/ec2-user"
KEY_PATH="C:\\Users\\parularo\\testing-key.pem"

# Copy the model file to the EC2 instance
scp -i "$KEY_PATH" "F:\\Docs\\per\\Edu\\MTech\\Course\\Course 3\\MLOPS\\Assignment\\Assignment1\\liver-disease-classification\\models\\liver_disease_randomforest_model.joblib" $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH

# Copy the Flask application files to the EC2 instance
scp -i "$KEY_PATH" "F:\\Docs\\per\\Edu\\MTech\\Course\\Course 3\\MLOPS\\Assignment\\Assignment1\\liver-disease-classification\\src\\app.py" $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH

# SSH into the EC2 instance and start the Flask application
ssh -i "$KEY_PATH" $REMOTE_USER@$REMOTE_HOST << 'EOF'
    cd /home/ec2-user
    sudo yum update -y
    sudo yum install python3 -y
    pip3 install flask joblib
    nohup python3 app.py &
EOF