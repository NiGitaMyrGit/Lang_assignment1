# Assignment 1 - Extracting linguistic features using spaCy
This is the repository for the first assignment in the course Language Analytics from the bachelors elective Cultural Data Science at Aarhus University.
## 1. Contributions
The code was written by me independently.
**I had help from the following sources**:
#TODO find the help soruces 
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
The script ```extract_features.py``` located in the folder [src](https://github.com/NiGitaMyrGit/Lang_assignment1/tree/e4ee062a0a23ffa7ba3717f330c92bbe2f22da8e/src) extracts linguistic feautures with ```spacy```.
The data is loaded, and preprocessed. By using the package ```fnmatch``` the doc-id and other meta-data contained in pointed brackets ```<>``` are removed from the text files with regex pattern matching and substitution. 
The script loops over the textfiles located in the subfolders of the data folder ```in/USECorpus```. The linguistic features are saved as datatables stored in CSV-files: one for each subfolder with the same name as the subfolder. 
## 4. Usage
The script is written in python 3.10.7. Make sure this is the python version you have installed on your device.
From the command line clone this GitHub repository to your current location (this can be changed with the `cd path/to/desired/location`) by running the command `git clone https://github.com/NiGitaMyrGit/Lang_assignment1.git".` 
### 4.1 Installing packages
From the commandline, located in the main directory, run the command `bash setup.sh`. This will install all required packages from the `requirements.txt` file.
### 4.2 Retrieve data
**The Uppsala Student English Corpus (USE)** 
The data is located in the folder [in]() as a zip-file.
In order to unzip the data, from the commandline, located in the folder [in](), run the command `unzip USEcorpus.zip`
This will unpack a folder called [USEcorpus] with 14 subfolder names [a1]-[a5], [b1]-[b8] and [c1].
The zip.file was retrived from [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).
More information can be found in the [readme.md] located in the [in] folder.
### 4.3 Run the script
From the command line, located in the main directory, run the command `python3 src/extract_features`.

## 5. Results
The script produces a table for each subfolder, showcasing the relative frequency per 10.000 words of nouns (RelFreq NOUN), verbs (RelFreq VERB), adjectives (RelFreq ADJ) and adverbs (RelFreq ADV). Furthermore it showcases the total number of unique persons (Unique PER) locations (Unique LOC) and organisations (Unique ORG).
An example from the first table named a1_table.csv:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

|Subdirectory|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|---|
|a1|0100.a1 |1455.0641940085593|1283.8801711840229|798.8587731811697|556.3480741797432|0|0|0|
|a1|2049.a1|1496.5517241379312|1144.8275862068965|531.0344827586207|717.2413793103448|0|1|3|

The relative frequency per 10.000 of the nouns of the filde ```0100.a1.txt``` are 1283.88, which in percentage means that approximately 12.8 % of the words are nouns. The same can be analysed from the relative frequency of verbs, adjectives and adverbs. The amount of unique person, location and organisation entities are 0, although "the US" is actually mentioned in the text. How come this is not counted as a location is unknown. 
Looking at the line for the file ```2049.a1.txt``` some unique locations and organisations are accounted for. In the text-file a person "Inga" is mentioned, but this is not counted as a person, probably because it is not a well-known person such as "Barack Obama". On the other ahnd "James Bond" is mentioned, who is definitely a well known person. When going through all the output tables, it seems that no person entitites are counted, which is rather odd.
The unique organisations is probably Sky Channel, Sky One and Fun Factory, which maskes sense. Since the code for the unique entities of organisations and persons are produced in the same way, there should, in theory, be no problem, but somehow there is anyway. 


