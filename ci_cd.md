ML
The CI/CD is triggered by change to 
- code
- data
- model performance
- [Important] Non-linear deployment process

- Focus on "GitOps"

In traditional, CI/CD is for testing, deployments


Common mistake
- using traditional CI/Cd as your orchestratior or central point of observation for ML

Tips
- orchestrat runs with a ML workflow system
- Use experiment tracking for general observability
- If do model runs in GitHub Actions, had it off to your workflow system, and log with WandB



Using WandB in CI/CD workflow (W&B)
- Using Github Action
- The CI/CD query to wandb to return results per SHA

(run-full-test or deploy-"runid")

the deploy action will deploy to gcp-cloud-function


## Pre-requisites
- Github
- YAML (Github Action)
- shell scripting
- Python
- ML




## Store Secret to Repo, not as code
github -> setting  -> secrets and variables -> actions


## Github Action Triggers
- pull_request (PR)
  - PR and Issue (Github contributes PR = Issue)
  - workflow_dispatch = manually trigger workflow available


## Basic Boilerplate (Setting up Dev environment)
  1. actions/checkout@v3
  2. pip install environment


## Emit Output from github action steps
  https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs

  