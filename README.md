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

pipenv install

yarn install

cp .env.sample .env # and edit accordingly
```

### Deploying
```shell
sls deploy
```