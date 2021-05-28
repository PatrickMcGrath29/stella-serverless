# Stella Serverless

## Setup Instructions
### Dependencies
```shell
brew install serverless yarn pyenv mongodb-community
```

### Repository Setup
```shell
pyenv virtualenv 3.8.0 stella-serverless
pyenv local stella-serverless

pip install -r requirements.txt
pip install -r test_requirements.txt

yarn install

cp .env.sample .env # and edit accordingly
```