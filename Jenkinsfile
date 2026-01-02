pipeline {
    agent any 
    environment {
        DB_ADDRESS = "192.168.1.9"
        USERNAME = "DB_USER_1"
        SERVER_CREDS = credentials('server_creds')
        }
    // options {
    //     skipDefaultCheckout true
    // }
    stages {
        // Checkout Stage
        stage("Checkout Code") {
            steps {
                // sh "git clone https://github.com/amandev-x/Jenkins-flask-app.git"
                echo "The IP Address of the DB is ${DB_ADDRESS} and username is ${USERNAME}"
                echo "My Creds: ${SERVER_CREDS}"
                echo "Username: ${SERVER_CREDS_USR}"
                echo "Password: ${SERVER_CREDS_PSW}"
            }
        }

        stage("Build Stage") {
            steps {
                echo "Building the application..."
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        // // Build Stage
        // stage() 
    }
}