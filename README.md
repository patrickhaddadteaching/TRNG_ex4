In this exercise, you can analyze the impact of the Monobit test parameters on the test results.
You can execute the last cell of this notebook and observe how the threshold and the block size affect Type 1 and 2 errors.

You can launch the application and observe how the the amount of input data and the threesholds affect test black box test accuracy. 

## How to launch the exercise ?
* We can execute this exercise on [Colab](https://colab.research.google.com/github/patrickhaddadteaching/TRNG_ex4/blob/main/TRNG_ex4_nb.ipynb)
    * Then press Ctrl+F9 or click on Runtime/Run All
* The exercise is a jupyter notebook compatible with voila.
The following libraries are required:
    * numpy
    * matplotlib
## Examples of procedures to execute the exercise with different systems.
1. Windows
    * First of all, Let clone this repositorie
    ```
     git clone https://github.com/patrickhaddadteaching/TRNG_ex4
    ```
    * [Download and install the latest Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links).
    * Open the Anaconda Powershell Prompt associated to Miniconda3 and type the following commands to install  to install all the dependencies required by this exercise.
     ```
        conda install jupyter
        conda install numpy
        conda install matplotlib
        conda install scipy                
        conda install -c conda-forge voila    
    ```
    * Now, you can either launch the notebook by executing the folowing command in the directory where you cloned this repositorie.
    ```
    jupyter-notebook.exe .\TRNG_ex1_nb.ipynb
    ```
    
    * Or, you can directly launch it with voila  by executing the folowing command in the directory where you cloned this repositorie.
    ```
    voila.exe .\TRNG_ex1_nb.ipynb
    ```
2. Linux
3. Mac OS X
## Solutions
* [Click here](https://github.com/patrickhaddadteaching/TRNG_ex4/blob/main/solution.md) to see the solutions
