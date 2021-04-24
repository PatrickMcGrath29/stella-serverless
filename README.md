# Stella Serverless

## Setup Instructions
### Dependencies
```shell
brew install serverless
brew install yarn
brew install pyenv
```

### Repository Setup
```shell
pyenv virtualenv 3.8.0 stella-serverless
pyenv local stella-serverless

pip install -r requirements.txt
pip install -r test_requirements.txt

yarn install
```

## Local Development
### Local Testing
To test the Lambda functions locally you can use the `serverless-offline` plugin. To start a local webserver running
the Lambda endpoints run `sls offline` in your terminal.

### Debugging
To enable local debugging of the Python lambda functions on PyCharm, execute the following bash script.

```shell
FILE_NAME=node_modules/serverless-offline/dist/lambda/handler-runner/python-runner/invoke.py
echo "pydevd_pycharm.settrace('localhost', port=50059, stdoutToServer=True, stderrToServer=True)" | cat - $FILE_NAME > temp && mv temp $FILE_NAME
echo "import pydevd_pycharm" | cat - $FILE_NAME > temp && mv temp $FILE_NAME
```