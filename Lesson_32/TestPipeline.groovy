pipeline {
    agent { label 'master' }
    environment {
        TEST_VAL = "15"
        WEB_UI_TEST_PATH = "/tmp"
    }
    parameters {
        string(name: 'NAME', defaultValue: 'John', description: 'Some description')
        booleanParam(name: 'FLAG', defaultValue: true, description: '')
    }

    stages {
        stage('hillel_git') {
            steps {
                checkout([
                $class: 'GitSCM',
                branches: [[name: '*/main']],
                extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'hillel']],
                userRemoteConfigs: [[credentialsId: 'my-git',
                                     url: 'git@github.com:antohaUa/hillel_aqa_301123.git']]])
            }
        }

        stage('Start') {
            steps {
                script {
                    dir('test_dir') {
                        sh """
                        echo "TestVal = ${TEST_VAL}"
                        echo "NAME = ${NAME}"
                        echo "FLAG = ${FLAG}"
                        ls -la
                        """
                    }
                }
            }
        }

        stage('env-install') {
            steps {
                script {
                    dir('hillel'){
                        withPythonEnv('python3') {
                            sh """
                                pip install requests pytest allure-pytest

                                python ./Lesson_24/01_example.py

                                # pytest has exit code 1 if tests fail. We return true to be able continue flow.
                                pytest -s -v ./Lesson_25/01_pytest --alluredir=${WORKSPACE}/allure-results | true
                            """
                        }
                    }
                }
            }
            post {
                always {
                        allure includeProperties:
                        false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                }
            }
        }
    }
}