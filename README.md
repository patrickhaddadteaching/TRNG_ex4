In this exercise, you can analyze the impact of the Monobit test parameters on the test results.

You can launch the application and observe how the threshold and the block size  affect  Type 1 and 2 errors that are introduced in Section 1.6 of this chapter.

This test triggers an alarm if the number of bits equal to 1 is bigger than $\frac{Number\ of\ input\ bits}{2}+relative\ threshold$ or is smaller than $\frac{Number\ of\ input\ bits}{2}-relative\ threshold$.

Your goal is to find the the lowest $relative\ threshold$ that makes it possible for $\alpha$ to be bigger than $10^{-6}$ and you should note the highest Shannon entropy ($H_{1}$) for which $\beta$ is smaller than $10^{-6}$.

This $H_{1}$ will be the lowest entropy rate at the TRNG output that will not trigger the alarm.

You should repeat the procedure for $Block\ sizes=4096, 8192, 16384, 32768$.

Now, can you answer the following question? Which parameter values of the Monobit test are required by the AIS31 and FIPS 140-1 test suites?

## How to launch the exercise ?
* We can execute this exercise on [Colab](https://colab.research.google.com/github/patrickhaddadteaching/TRNG_ex4/blob/main/TRNG_ex4_nb.ipynb)
    * Then press Ctrl+F9 or click on Runtime/Run All
* The exercise is a jupyter notebook compatible with voila.
The following libraries are required:
    * numpy
    * matplotlib
    * scipy
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
        conda install scipy
        conda install matplotlib
        conda install -c conda-forge voila    
      ```
    
    * Now, you can either launch the notebook by executing the folowing command in the directory where you cloned this repositorie.
    ```
    jupyter-notebook.exe .\TRNG_ex4_nb.ipynb
    ```
    
    * Or, you can directly launch it with voila  by executing the folowing command in the directory where you cloned this repositorie.
    ```
    voila.exe .\TRNG_ex4_nb.ipynb
    ```
2. Linux
3. Mac OS X
