### Requirements Check 

##### Clone the FSDL course repo and this repo<br />
!git clone -q https://github.com/full-stack-deep-learning/fsdl-text-recognizer-2021-labs<br />
!git clone -q https://github.com/santhozkumar/fsdl-course<br />


#### Install the requirements.txt file based on gpu/cpu<br />
#GPU<br />
#!pip install -q -r fsdl-course/gpu-requirements.txt -f https://download.pytorch.org/whl/torch_stable.html<br />

#Cpu<br />
!pip install -q -r fsdl-course/cpu-requirements.txt -f https://download.pytorch.org/whl/torch_stable.html<br />


%cd fsdl-text-recognizer-2021-labs<br />
%env PYTHONPATH=.:$PYTHONPATH<br />
%cd lab2<br />




#### To run a sample experiment<br />
!python3 training/run_experiment.py --model_class=MLP --data_class=MNIST --max_epochs=5 --gpus=1<br />  




