# agent-development

## Getting started

This is a template project for getting started with agentic AI development

## Contents

### agent.py

This is where the agent code can start. Other files from the template depend on this to be where the agent is
initialized, but more files can be added to support proper programming hygiene.

### agent_entry.py

This provides the API entrypoint for the agent through the decorator.

### api_manager.py

This creates the decorator

### entrypoint.py

This is the entrypoint to running the agent using the API. You can run it locally with `python entrypoint.py`. It's also
what the Dockerfile uses as the `CMD`.

### Dockerfile

The Dockerfile is a skeleton Dockerfile that should have most of the features you already need. You may have to update
the python version used in the base image.

### requirements.txt

This file has the python requirements needed to use the agent. It is an empty file and will need to be filled as the
agent is developed and new libraries are added. Rather than running `pip install $LIBRARY`, it is suggested to put the
library in the `requirements.txt`, with its version, and run `pip install -r requirements.txt` during development.

### deployment.yaml

This file is to allow you to deploy your agent into the Kubernetes environment. You will need to update the $IMAGE_NAME
to the correct format for the registry.

### .github/workflows/build-and-push.yaml

This file tells Github to build and push the agent into Github container registry.

## How to use

- Create an empty Github repo
- Create
  a [Github token](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry)
  for pulling from Github Container Registry.
- Create a service account for your agent `kubectl create service account agent-serviceaccount`
- Create a docker secret in kubernetes for this token: `kubectl create secret docker-registry ghcr-login-secret --docker-server=https://ghcr.io --docker-username=$YOUR_GITHUB_USERNAME --docker-password=$YOUR_GITHUB_TOKEN --docker-email=$YOUR_EMAIL`
- Add the secret to your service account `kubectl patch serviceaccount agent-serviceaccount -p '{"imagePullSecrets": [{"name": "ghcr-login-secret"}]}'`
- Git clone this repository
- Develop your agent starting in `agent.py`. Make sure to add any requirements to `requirements.txt` along the way.
- Git commit and git push this repo to the Github repo
- Github will automatically build your agent and produce the `IMAGE_PATH` needed for the `deployment.yaml`.
- Update the `IMAGE_PATH` in `deployment.yaml` and `kubectl apply -f deployment.yaml` into your Kubernetes environment.
- Your agent should deploy and start.
- `kubectl port-forward svc/agent 8000`
- Send a request to `localhost:8000` and it should be processed by your agent.
