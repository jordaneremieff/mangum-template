# mangum-template

This is a template for developing [ASGI](https://asgi.readthedocs.io/en/latest/)-compatible Python web apps deployed to [AWS Lambda](https://aws.amazon.com/lambda/). It uses [Mangum](https://github.com/jordaneremieff/mangum) to adapt AWS Lambda events for an example [FastAPI](https://github.com/tiangolo/fastapi) app.

# Usage

- Create an AWS Lambda function with the handler set to `lambda_handler.handler`.
  
- Add your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` secrets to the GitHub project settings.
  
- Change the values of `AWS_REGION` and `LAMBDA_FUNCTION` under the `env` section in the `.github/workflows/deploy.yml` file.

- Push a commit to `main` to run the deployment workflow.

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

The structure of the project and choice of FastAPI as the application framework in this template are just one example and could be substituted with alternative layouts and ASGI frameworks.