#!/usr/bin/env python3
# if not in the 'src' folder cd into it: '/work/cds-lang/assignment-1---linguistic-analysis-using-nlp-NiGitaMyrGit/src'
# setup
import spacy
nlp = spacy.load("en_core_web_sm")
import os
import pandas as pd
import sys
import fileinput
import pathlib
from pathlib import Path
import csv
import fnmatch

# Set the main directory 'main_dir' (USEcorpus) where the files are located
main_dir = os.path.join("in", "USEcorpus")

def run():
    # Specifying that we are looking at the subdirectories 'dir' (a1-c1) within the main directory
    for subdir in os.listdir(main_dir):
        # making a sub path list
        subdir_path = os.path.join(main_dir, subdir)
        # creating a results list to be used for appending the results
        subdir_results = []

        for filename in os.listdir(subdir_path):
            #  creating empty lists for the parts-of-speech (POS)
            verb_count = 0
            noun_count = 0
            adj_count = 0
            adv_count = 0
            per_count = 0
            loc_count = 0
            org_count = 0
            # creating empty sets, since sets inherently only include unique values
            per_set = set()
            loc_set = set()
            org_set = set()
            # making a list that specifies looking at the files inside the sub directory path
            file_path = os.path.join(subdir_path, filename)

            #opening the files
            with open(file_path, 'r', encoding='latin-1') as file:
                #creating a doc object
                contents = file.read()
                # Remove "< >" and the doc-id
                remove_pattern = ['<', ">", "doc\.id=[0-9]*\.[abc][0-9]"]
                lines = contents.split('\n')
                filtered_lines = []
                for line in lines:
                    if not any(fnmatch.fnmatch(line, pattern) for pattern in remove_pattern):
                        filtered_lines.append(line)
                contents = ''.join(filtered_lines)
                
                #creating a doc object¨
                doc = nlp(contents)

            #counting the POS
            for token in doc:
                if token.pos_ == 'VERB':
                    verb_count += 1
                if token.pos_ == 'NOUN':
                    noun_count += 1
                if token.pos_ == 'ADJ':
                    adj_count += 1
                if token.pos_ == 'ADV':
                    adv_count += 1

            #counting the unique entities
            for ent in doc.ents:
                if ent.label_ == 'PER':
                    per_set.add(ent.text)
                elif ent.label_ == 'LOC':
                    loc_set.add(ent.text)
                elif ent.label_ == 'ORG':
                    org_set.add(ent.text)
            per_count = len(per_set)
            loc_count = len(loc_set)
            org_count = len(org_set)
            # counting the relative frequency of POS per 10000 words
            rel_noun_freq = (noun_count / len(doc)) * 10000
            rel_verb_freq = (verb_count / len(doc)) * 10000
            rel_adj_freq =  (adj_count / len(doc)) * 10000
            rel_adv_freq =  (adv_count / len(doc)) * 10000
            # splitting filename into tuple containing basename of the file.txt without directory path
            filename_only = os.path.splitext(os.path.basename(file_path))[0]
            # gathering the output and appending it to the subdir_results list
            output = [subdir, filename_only, rel_noun_freq, rel_verb_freq, rel_adj_freq, rel_adv_freq, per_count, loc_count, org_count]
            subdir_results.append(output)
        #creating the CSV datatables in the out-folder
        data = pd.DataFrame(subdir_results, columns=['Subdirectory', 'Filename', 'RelFreq NOUN', 'RelFreq VERB', 'RelFreq ADJ', 'RelFreq ADV', 'Unique PER', 'Unique LOC', 'Unique ORG'])
        csv_path = os.path.join("out", subdir + '_table.csv')
        data.to_csv(csv_path, index=False)

# calling main function
if __name__== "__main__":
    run()