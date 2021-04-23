# Stella Serverless

## Local Development

### Debugging
To enable local debugging of the Python lambda functions on PyCharm, execute the following bash script.

```shell
FILE_NAME=node_modules/serverless-offline/dist/lambda/handler-runner/python-runner/invoke.py
echo "pydevd.settrace('localhost', port=50059, stdoutToServer=True, stderrToServer=True, suspend=False)" | cat - $FILE_NAME > temp && mv temp $FILE_NAME
echo "import pydevd" | cat - $FILE_NAME > temp && mv temp $FILE_NAME
```