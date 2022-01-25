# Interview-Scheduler

## Overview
An application that can optimally schedule interviews for candidates based on their preferences and available slots.

The program is given an input of interview slots and how each candidate ranks their top preferred slot timings. The output will be an optimal scheduling of the candidates in their interview slots. 

This means candidates get their preferred slots as much as possible. However, if necessary, some candidates will be scheduled outside (but close to) their preferences.

## Usage
The program was implemented in Python, and the core libraries used in this implementation are Pandas for the data processing and output. As such, this script is run from the CLI. The input is two CSV files, one for available timings and another for candidate preferences. The output is a CSV of the optimal scheduling.

## General input constraints
* There exists as many interview slots as candidates.
* All candidates have the same number of preferences, though this number can be less than the slots available (i.e. candidates can give the top `X` out of `N` available slots).
* Each candidate is, for the sake of avoiding ambiguity, identified by an ID.

## Format of the two CSV inputs:
* `slots.csv` - a CSV that is a table of available interview slots. The columns for this CSV must be the start time and the end time, in this order. Headers **shouldn't** be provided. For a sample, please examine sample_slots.csv, provided in `/sample_inputs` above.
* `preferences.csv` - a CSV table of the candidate preferences of the interview slots. Supposing we had `N` candidates and `K` preferences per candidate, the dimension of this table must be `N` rows and `K + 1` columns.\ \
   Thus, for each row, there must be the candidate ID column, followed by the `X <= N` preferences (in order of **highest to lowest**) for that candidate. This `X` must be constant amongst all candidates. Again, headers **shouldn't** be provided.
* **Both CSV inputs must be in a folder called `inputs`.**

## Format of the CSV output:
`schedule.csv` is the name of the output CSV, created under `outputs`. It will contain, **without headers**, the slot timing column followed by the matched candidate (using ID) column. Thus, each row is a scheduled interview for one of the `N` candidates.

## To execute:
Simply run the bash script (`final_program.bash`) provided above.
