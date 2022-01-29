# Slot Matcher

## Overview
This is an application that uses stable matching to optimally match slots to individuals based on their preferences and available slots.

The program is given an input of time slots and how each individual ranks their top preferred slot timings. The output will be an optimal scheduling of the individuals in their time slots. 

This means individual get their preferred slots as much as possible. However, if necessary, some individuals will be scheduled outside (but close to) their preferences.

## Development
The program was implemented in Python, and the core libraries used in this implementation are Pandas for the data processing and output. The main algorithm used was Gale-Shapley's stable matching algorithm, with the candidates as the "proposers" to ensure individual-optimal matching. 

## Usage
This script is run from the CLI. The input is two CSV files, one for available timings and another for individual preferences. The output is a CSV of the optimal scheduling.

## General input constraints
* There exists as many interview slots as candidates.
* All individuals have the same number of preferences, though this number can be less than the slots available (i.e. candidates can give the top `X` out of `N` available slots). These preferences must be ordered and unique within the context of a single individual.
* Each individual is, for the sake of avoiding ambiguity, identified by an ID.
* All slots are the same duration and none overlap.

## Format of the two CSV inputs:
* `slots.csv` - a CSV that is a table of available time slots. The columns for this CSV must be the start time and the end time, in this order. Headers **shouldn't** be provided. For a sample, please examine sample_slots.csv, provided in `/sample_inputs` above. Times must be in 24-hour, HH:MM string format.
* `preferences.csv` - a CSV table of the candidate preferences of the time slots. Supposing we had `N` individuals and `K` preferences per individual, the dimension of this table must be `N` rows and `K + 1` columns. Each preference is one of the N **start times only** in an HH:MM string format.\
  Thus, for each row, there must be the individual ID (name or some string or integer) column, followed by the `X <= N` preferences (in order of **highest to lowest**) for that individual. This `X` must be constant amongst all individuals. Again, headers **shouldn't** be provided.
* **Both CSV inputs must be in a folder called `inputs`.**

## Format of the CSV output:
`schedule.csv` is the name of the output CSV, created under `outputs`. It will contain, **without headers**, the slot start and end time columns, followed by the matched individual (using ID) column. Thus, each row is a scheduled slot for one of the `N` individuals.

## To execute:
Simply run `python main.py`.
