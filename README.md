# Grade Classifier

This is a simple grade calculator in Python. You type in a score from 0.00 to 100.00, and it shows your letter grade (A, B, or C).

## Setup

conda activate aigc5005  
pip install -r requirements.txt

## Run

python grade_calculator.py

## Example

Enter a grade: 95
95 is A

Enter a grade: abc
abc is not a number. Please enter a number

## Known limitations

This program uses a very basic grade scheme, so it does not reflect different grading systems used by various schools.

This program does not round decimal grades, so grades with many decimal places may make the result less readable.