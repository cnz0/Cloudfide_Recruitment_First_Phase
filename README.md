# Cloudfide_Recruitment_First_Phase
This project was created as part of recrutation process

## Start ##

If you don't have libraries installed, type in console:
```python
pip install -r requirements.txt
```
or
```python
python -m pip install -r requirements.txt
```
When in folder with requirements.txt file

## Using program ##

File "solution.py" includes whole code logic. Line #42 can be removed - if you don't need to see the input every single time, the function is called

File "testing.py" includes testing - including automatic tests, provided in exercise, and manual test part, if it's necessary

## Supported names and operations ##

Initial dataframe name is unrestricted
All column names must consist only of symbols between A-Z a-z with optional uderscores - no numbers or other special characters.
The expression with equation must be in format: column_name1 operator column_name2. Operator is one of the following symbols: "+", "-", "*", column names restrictions are stated one line above. Whitespaces are optional - program strips the expression of them anyway

## Use examples ##

df = add_virtual_column(df, "a*c", "ac") -> returns df with additional column "ac"
add_virtual_column(df, "a --- b", "adad") -> returns empty df ("---" is not valid operator)
add_virtual_column(df, "a+               a", "aa") -> returns df with additional column that is equal to a+a
