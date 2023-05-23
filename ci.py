import wandb

print(f'Wandb Version {wandb.__version__}')

assert wandb.__version == '2.2.2', f'The version of wandb should be 2.2.2 not {wandb.__version__}'
