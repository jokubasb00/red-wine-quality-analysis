Red wine quality analysis



Author: Jokubas Banaitis



Python analysis of the relationships between chemical measurements and quality scores in the UCI red Wine Quality dataset.



Tested operating system: \*\*Windows 11\*\*. Tested Python version: \*\*3.14.7\*\*



\## Software dependencies



The code requires Python 3 and these libraries:



pandas

matplotlib



The libraries are listed in requirements.txt. The pathlib module used in the code comes with Python.



\## Dataset



The dataset file must be located at:

data/raw/winequality-red.csv



Keep the Python script in the main project folder, alongside requirements.txt and the data folder.



Dataset source: UCI Wine Quality.

Citation: Cortez, P., Cerdeira, A., Almeida, F., Matos, T., and Reis, J. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T. Dataset licence: CC BY 4.0.



\## How to run



Download and extract the repository.

Open the project folder in VS Code.

Open a terminal in that folder.



Install the required libraries:

python -m pip install -r requirements.txt



Run the analysis:



python MAT2007.projectanalysis.py



The script displays the quality distribution, correlations with quality, and boxplots of alcohol and volatile acidity by quality score. Close a graph window to allow the script to continue if it pauses at that graph.

