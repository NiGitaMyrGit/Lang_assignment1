# Assignment 1 - Extracting linguistic features using spaCy
This is the repository for the first assignment in the course Language Analytics from the bachelors elective Cultural Data Science
## 1. Contributions
The code was written by me independently.
## 2. Assignment description from instructor
This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

For this exercise, you should write some code which does the following:

- Loop over each text file in the folder called ```in```
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

### 2.1 Objective

This assignment is designed to test that you can:

1. Work with multiple input data arranged hierarchically in folders;
2. Use ```spaCy``` to extract linguistic information from text data;
3. Save those results in a clear way which can be shared or used for future analysis

### 2.2 Some notes

- The data is arranged in various subfolders related to their content (see the [README](in/README.md) for more info). You'll need to think a little bit about how to do this. You should be able do it using a combination of things we've already looked at, such as ```os.listdir()```, ```os.path.join()```, and for loops.
- The text files contain some extra information that such as document ID and other metadata that occurs between pointed brackets ```<>```. Make sure to remove these as part of your preprocessing steps!
- There are 14 subfolders (a1, a2, a3, etc), so when completed the folder ```out``` should have 14 CSV files.

### 2.3 Additional comments

Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.

For this assignment, you are welcome to submit your code either as a Jupyter Notebook, or as ```.py``` script. If you do not know how to write ```.py``` scripts, don't worry - we're working towards that!

Lastly, you are welcome to edit this README file to contain whatever informatio you like. Remember - documentation is important!

## 3. Methods
The script `extract_features.py` located in the folder [src](https://github.com/NiGitaMyrGit/Lang_assignment1/tree/e4ee062a0a23ffa7ba3717f330c92bbe2f22da8e/src)

## 4. Usage
The script is written in python 3.10.7. Make sure thsi is the python version you have installed.
### 4.1 Installing packages
From the commandline, located in the main directory (use `cd path/to/Lang_assignment1`), run the command `bash setup.sh`. This will install all required packages from the `requirements.txt`file.
### 4.2 Retrieve data
**The Uppsala Student English Corpus (USE)** 
The data is located in the folder [in]() as a zip-file.
In order to unzip the data, from the commandline, located in the folder [in](), run the command `unzip USEcorpus.zip`
This will unpack a folder called [USEcorpus] with 14 subfolder names [a1]-[a5], [b1]-[b8] and [c1].
The zip.file was retrived from [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).
More information can be found in the [readme.md] located in the [in] folder.
### 4.3 Run the script
From the command line, located in the main directory, run the command `python3 src/extract_features`
The script produces a table for each subfolder, showcasing the relative frequency of relative frequency of nouns 
## 5. Results
The