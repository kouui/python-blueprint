# refactor of rba-algorithm implementation

## background

this is a project to implement (various kinds of) unsupervised SSO log anomaly detection algorithms.

the project is managed by `uv` witten in python. 
- use `uv add [package_name]` to add new package if necessary.
- use `uv run [path/to/script]` to run the script.

## purpose

the current prompt is to refactor an existing implementation of the risk based authentication (rba) algorithm to our package.

## requirements


1. an explaination of rba algorithm is in `external/rba-algorithm/paper/rba-explained.md`. read carefully to make sure you understand the algorithm
2. the original implementation `experiments/kou/rba-algorithm/origin.py`, which is a copy-pasted version of an ipynb notebook. 
    - it is not well-structured and has many global values since ipynb declare variables in the global scope. you should avoid using global variables in your implementation if possible.
    - the original implementation uses pandas as the main data structure. you should use `polars` instead to improve performance.
    - the docstring in the file describes a part of the purpose/usage of the code. you should read it carefully and understand the purpose of each function.
3. functions and classes should be well-structured and modularized in `src/secioss_anomaly_detection/models/risk_based_auth`entication.py`
    - `.py` file in the directory should has filename with leading underscore `_` to indicate that it is a private module.
    - expose the necessary functions/classes in the `__init__.py` file in the directory.
    - seperate the functions/classes into different files if necessary (do not implement everything in a single file).
4. main function should be implemented in `experiments/kou/rba-algorithm/main.py`
5. do not implement all at once. you should implement the code step by step.
    - after each step, use `print` to print out the intermediate variable in `origin.py` and your implementation for comparison
        - for `origin.py`, just add/remove  `print` statements, do not modify the logic code since it provides your the correct result for reference.
    - do not use logging to print the intermediate variable value, to reduce the output size.
    - in both `origin.py` and your current implementation, stop the execution by using assert False after the first iteration. since we are now comparing intermediate result, the full output is redundant

## logging guideline

in the main script, use the following code to setup logger
```python
if __name__ == "__main__":
    from {package_name}.utils.logger import LogUtil as logging
    logging.setup_logger()
```

and then in the library source code,
```python
from {package_name}.utils.logger import LogUtil as logging

def {function_name}(...):
    logging.info(...)
    loggign.debug(...)
```

## else

after finishing your task planning, please save it as `instructions/01_task.md`.

