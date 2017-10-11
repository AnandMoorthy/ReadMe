#!groovy

pipeline {
  try {
    stage 'Test'
      sh 'source /home/anand/Dev/virtual_env/readme/bin/activate'
      sh 'echo "Hello Test"'

    stage 'Deploy'
      sh 'python manage.py makemigraions'
      sh 'python manage.py migrate'
      sh 'echo "Hello Deploy"'
  }
  catch (err) {
    sh 'echo "Error Occured By Anand"'
  }
}
