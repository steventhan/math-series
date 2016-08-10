# math-series
Paired Assignment for Python 401d4 Tuesday August 9, 2016
This module defines functions that implement mathematical series

# Instructions
Clone this repo, start create new virtual env, install required plugins using:
```
pip install -r requirements.pip
```
To find out what the module does, and see examples, run:
```
python src/series.py
```
To use the module:
```python
import series

series.fibonacci(5) # Return 5th value in the fibonacci series
series.lucas(10) # Return 5th value in the lucas series
series.sum_series(10) # Return 10th value in the fibonacci series because 2nd and 3rd parameters weren't used
series.sum_series(4, 4, 7) # Return 29 as the 4th value of the series[4, 7, 11, 18, 29, ...], the 2nd and 3rd arguments specify index 0 and index 1 of the series respectively
```

To run tests, type in command line:
```
py.test or ptw
```
