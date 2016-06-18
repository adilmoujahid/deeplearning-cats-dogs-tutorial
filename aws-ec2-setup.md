# Installation Guide - Caffe and Anaconda on AWS EC2

## Update the package lists

```
sudo apt-get update
```

## Installing general dependencies

```
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
```

## Installing CUDA

Create a downloads folder.

```
mkdir downloads
```

# Download and install Nvidia CUDA

```
cd downloads

wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb

sudo apt-get upgrade -y
sudo apt-get install -y opencl-headers build-essential protobuf-compiler \
    libprotoc-dev libboost-all-dev libleveldb-dev hdf5-tools libhdf5-serial-dev \
    libopencv-core-dev  libopencv-highgui-dev libsnappy-dev libsnappy1 \
    libatlas-base-dev cmake libstdc++6-4.8-dbg libgoogle-glog0 libgoogle-glog-dev \
    libgflags-dev liblmdb-dev git python-pip gfortran
    
sudo apt-get clean
sudo apt-get install -y linux-image-extra-`uname -r` linux-headers-`uname -r` linux-image-`uname -r`
sudo apt-get install -y cuda
sudo apt-get clean
```

Add CUDA to ```.bashrc```

```
echo 'export PATH=$PATH:/usr/local/cuda-7.5/bin' >> ~/.bashrc 
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-7.5/lib64' >> ~/.bashrc 

source ~/.bashrc
```

## Installing cuDNN

```
wget https://s3-eu-west-1.amazonaws.com/poc-ocr-caffe/cudnn-7.0-linux-x64-v4.0-prod.tgz
tar -zxf cudnn-7.0-linux-x64-v4.0-prod.tgz
cd cuda
sudo cp lib64/* /usr/local/cuda/lib64/
sudo cp include/cudnn.h /usr/local/cuda/include/
```

## Download Caffe

```
cd
git clone https://github.com/BVLC/caffe.git
```

## Installing Caffe

```
cd caffe

sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev

cp Makefile.config.example Makefile.config

sed -i '/^# USE_CUDNN := 1/s/^# //' Makefile.config
sed -i '/^# WITH_PYTHON_LAYER := 1/s/^# //' Makefile.config
sed -i '/^PYTHON_INCLUDE/a    /usr/local/lib/python2.7/dist-packages/numpy/core/include/ \\' Makefile.config
```

Build Caffe 

```
make all -j8
make test -j8
make runtest
```

## Installing Anaconda

Download Anaconda

``` 
cd ~/downloads
wget http://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh
```
Install Anaconda

```
bash ./Anaconda2-4.0.0-Linux-x86_64.sh
```

## Installing additional dependencies

```
sudo apt-get install graphviz
sudo apt-get install python-opencv
conda install opencv
pip install lmdb
pip install pydot
```


## Installing Pycaffe

```
cd /home/ubuntu/caffe/python
for req in $(cat requirements.txt); do pip install $req; done

cd /home/ubuntu/caffe
make pycaffe
```

## Add the Caffe and PyCaffe paths to .bashrc

```
echo 'export CAFFE_ROOT=/home/ubuntu/caffe' >> ~/.bashrc
echo 'export PYTHONPATH=/home/ubuntu/caffe/python:/home/ubuntu/anaconda2/bin/python' >> ~/.bashrc
source ~/.bashrc
```

## Execute the command below to solve libdc1394 error
```
sudo ln /dev/null /dev/raw1394
```

## References
* [Installing Caffe the right way](http://installing-caffe-the-right-way.wikidot.com/start)
* [libdc1394 error](http://stackoverflow.com/questions/12689304/ctypes-error-libdc1394-error-failed-to-initialize-libdc1394)



