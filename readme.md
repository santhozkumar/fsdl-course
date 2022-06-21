### Requirements Check 

##### Clone the FSDL course repo
!git clone https://github.com/full-stack-deep-learning/fsdl-text-recognizer-2021-labs
%cd fsdl-text-recognizer-2021-labs

#### "Minimum Requirements given by course"
!pip3 install boltons wandb pytorch_lightning==1.1.4 pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 torchtext==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
%env PYTHONPATH=.:$PYTHONPATH

#### OR use below 
!pip install -q boltons wandb pytorch_lightning torchmetrics toml
!pip install -q torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 torchtext==0.8.1

#### To run a sample experiment
!python3 training/run_experiment.py --model_class=MLP --data_class=MNIST --max_epochs=5 --gpus=1

#### Check for the above with below commands in colab

!pip list | grep torch
!pip list | grep -e boltons -e wandb -e pytorch_lightning -e torch
!pip install -q boltons wandb pytorch_lightning



