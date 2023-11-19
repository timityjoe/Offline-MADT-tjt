#!/bin/bash

# See https://github.com/PKU-MARL/Multi-Agent-Transformer
# conda create --name conda39-mat python=3.9
echo "Setting up Multi-Game Decision Transformer Environment..."
source activate base	
conda deactivate
conda activate conda39-mat
echo "$PYTHON_PATH"
