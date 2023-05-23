import wandb

print(f'Wandb Version {wandb.__version__}')


assert wandb.__version__ == '0.15.3', f'The version of wandb should be 0.15.3 not {wandb.__version__}'
