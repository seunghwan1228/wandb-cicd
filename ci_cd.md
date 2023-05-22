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




