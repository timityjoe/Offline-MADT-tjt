
# MADT: Offline Pre-trained Multi-Agent Decision Transformer

A link to our paper can be found on [Arxiv](https://arxiv.org/abs/2112.02845).

## Overview

Official codebase for Offline Pre-trained Multi-Agent Decision Transformer.
Contains scripts to reproduce experiments.

![image info](./architecture.png)

## Instructions

It may be necessary to add the respective directories to your PYTHONPATH.

The offline smac dataset for this repo is available at [here](https://reinholdm.cowtransfer.com/s/7c8545dca1e043), expired.
```shell
## password is xvsma7
```

```shell
New download link [here](https://cowtransfer.com/s/3785a6a9e5d044)
```

## How to run experiments
1. setup python environment with `pip install -r requirements.txt`
2. to install StarCraft II & SMAC, you could run `bash install_sc2.sh`. Or you could install them manually to other path you like, following the official link: https://github.com/oxwhirl/smac.
2. enter the `./sc2/` folder.
3. set hyper-parameters in `run_madt_sc2.py` line 19-49 according to appendix.
4. select a maps to test in `envs/config.py` line 142
5. run the `run_madt_sc2.py` script

```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113^C
pip install -r requirements.txt
pip install pyOpenSSL --upgrade
pip install --upgrade pip

python3 run_madt_sc2.py
python3 run_madt_sc2.py --offline_epochs 1
python3 run_madt_sc2.py --offline_epochs 10

python3 run_rware.py
python3 run_rware.py --eval_episodes 1
python3 run_rware.py --eval_episodes 32

python3 run_robot_warehouse.py
```


