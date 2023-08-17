#  DeepInc 

Constraint solving is a fundamental approach for verifying deep neural networks (DNNs). In the field of AI safety, DNNs often undergo modifications in their structure and parameters for purposes such as repair or attack. In such scenarios, we propose the problem of incremental DNN verification, which aims to determine whether a safety property still holds after the DNN has been modified. To address this problem, we present an incremental satisfiability modulo theory (SMT) algorithm based on the Reluplex framework. Our algorithm, called DeepInc, simulates the key features of the configurations that infer the verification results of the old solving procedure. It heuristically checks whether the proofs remain valid for the modified DNN. Experimental results demonstrate that DeepInc outperforms DeepInc inefficiency in most cases. Moreover, for cases where the property is violated both before and after modification, DeepInc achieves significantly faster acceleration, even when compared to the state-of-the-art verifier $\alpha,\beta$-CROWN.

We build this repo based on [Marabou](https://github.com/NeuralNetworkVerification/Marabou/tree/master).

Build and Dependencies
------------------------------------------------------------------------------

DeepInc depends on the Boost library,
which is automatically downloaded and built when you run make. 

And Gurobi, which need to download yourself.

The DeepInc build process uses CMake version 3.12 (or later).
You can get CMake [here](https://cmake.org/download/).

### Install gurobi
We use Gurobi as an LP solver. Gurobi requires a license (a free
academic license is available), after getting one the software can be downloaded
[here](https://www.gurobi.com/downloads/gurobi-optimizer-eula/) and [here](https://www.gurobi.com/documentation/9.5/quickstart_linux/software_installation_guid.html#section:Installation) are
installation steps, there is a [compatibility
issue](https://support.gurobi.com/hc/en-us/articles/360039093112-C-compilation-on-Linux) that should be addressed.
A quick installation reference:
```
export INSTALL_DIR=/opt
sudo tar xvfz gurobi9.5.1_linux64.tar.gz -C $INSTALL_DIR
cd $INSTALL_DIR/gurobi951/linux64/src/build
sudo make
sudo cp libgurobi_c++.a ../../lib/
```
Next it is recommended to add the following to the .bashrc (but not necessary) 
```
export GUROBI_HOME="/opt/gurobi951/linux64"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"

```

### Build Instructions

To build DeepInc using CMake run:
```
cd path/to/DeepInc/repo/folder
mkdir build 
cd build
cmake .. 
```
For configuring to build a static DeepInc binary, use the following flag
```
cmake .. 
```
To build, run the following:
```
cmake --build . --target DeepInc -j 20
```

To compile in debug mode (default is release)
```
cmake .. -DCMAKE_BUILD_TYPE=Debug
cmake --build .
```

The compiled binary will be in the *build* directory, named _DeepInc_



Getting Started
-----------------------------------------------------------------------------
### To run DeepInc from Command line 
After building DeepInc the binary is located at *build/DeepInc*  The
repository contains sample networks and properties in the *resources* folder.

To run DeepInc, execute from the repo directory, for example：

The first verification process:


```
cd /path/to/repo/build

./DeepInc ../resources/nnet/acasxu/ACASXU_experimental_v2a_1_1.nnet ../resources/properties/acas_property_1.txt --search-tree-file ../resources/nnet/acasxu/1_1.nnet.searchTree 
```

running this command will generate search tree at `../resources/nnet/acasxu/1_1.nnet.searchTree`

to use this search tree for incremental solve, running this:


```
./DeepInc ../resources/nnet/acasxu/ACASXU_experimental_v2a_1_1.nnet ../resources/properties/acas_property_1.txt --search-tree-file ../resources/nnet/acasxu/1_1.nnet.searchTree --incremental-verification
```

note, the nnet file in first run doesn't need to be the same with nnet file in the second run.