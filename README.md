# mangum-template

This is a template for developing [ASGI](https://asgi.readthedocs.io/en/latest/)-compatible Python web apps deployed to [AWS Lambda](https://aws.amazon.com/lambda/) with [Mangum](https://github.com/jordaneremieff/mangum). 

The example app was created using [FastAPI](https://github.com/tiangolo/fastapi).

# Usage

- Create an AWS Lambda function with the handler set to `lambda_handler.handler`.
  
- Add your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` secrets to the GitHub project settings.
  
- Change the value of `LAMBDA_FUNCTION` under the `env` section in the `.github/workflows/deploy.yml` file to your function's name.

- Push a commit to `main`. 

Assuming everything is otherwise configured correctly in AWS, you should be able to visit the URL to your deployment and see the output from the example included in the template. Since this uses FastAPI, you may additionally visit `/docs` to see the generated API documentation.

# Testing

- Create a local Python virtual environment.

    `python -m venv .venv`
- Activate the virtual environment.

    `. .venv/bin/activate`
- Install the dev requirements.

    `python -m pip install requirements/dev.txt`

- Run the tests using `pytest`:

    `python -m pytest`

The test settings can be adjusted in the `pyproject.toml` file.

# Notes

The structure of the project and choice of FastAPI as the application framework in this template are just one example. This could look very different and use any other ASGI-compliant framework or app so long as the Mangum adapter instance is configured to handle the invocations.