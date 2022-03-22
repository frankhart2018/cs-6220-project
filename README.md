# CS 6220 (DMT) Project

## Team Members

1. Aruvi Puhazhendhi
2. Siddhartha Dhar Choudhury

## Cleaning and filling data

This can be achieved by using the `clean_fill` package and the `clean.py` script. To understand the process of using the `clean_fill` package, we must understand the following files:

1. `clean.py`: This file is used to run the cleaner and filler pipelines on an input CSV file and generate a processed CSV file.
2. `config.json`: Contains the list of cleaners and fillers that are to be applied to an input file. The strings in cleaner and filler lists are the exact names of the classes that are used for cleaning or filling but in <a href="https://en.wikipedia.org/wiki/Snake_case">snake case</a>, while the actual class names (as seen under `clean_fill/clean` and `clean_fill/fill` are in <a href="https://techterms.com/defini tion/pascalcase">Pascal Case</a>). 

### Steps

#### Running the clean and fill script

The clean and fill script takes one required argument and two optional arguments:

1. `input`: The input CSV file that is to be cleaned and filled.
2. `clean`: A flag that turns on cleaning feature, and cleans the input file using the available cleaners in `config.json`.
3. `fill`: A flag that turns on filling feature, and fills the input file using the available fillers in `config.json`.

If you pass only the `input` argument, the script will not perform any processing.

For more information on the clean and fill script, please refer to the help using:

```bash
user@programmer~:$ python clean.py --help
```

To run with all the available options:

```bash
user@programmer~:$ python clean.py --input input.csv --clean --fill
```

#### Adding new cleaners and fillers

1. All cleaners are inherited from `Cleaner` class from `clean_fill/clean/cleaner` module which is the base class for all of them, the same for fillers is in `Filler` class from `clean_fill/fill/filler` module.
2. To add a new cleaner or filler add a new class to the respective sub-package and inherit from the respective base class.
3. Import the class in the `clean.py` script.
4. Finally to use it during cleaning and filling process add the name of the class in snake case in the `config.json` file.
