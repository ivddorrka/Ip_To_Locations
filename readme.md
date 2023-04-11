# Files description

## Python Files

### ip_to_locations.py 

running example via cmd: 

```
python ip_to_locations.py arg1 arg2 arg3
```
, where: 
* arg1 - relative path from the current directory to the input file. To make life easier - move the input file to the same directory where this python file is and run the script from there

* arg2 - name of the ip-addresses columns. rename it to something 1-word-simple name as IP

* arg3 - api-key from here:  https://ipstack.com/plan

### synchronization.py 
running example via cmd: 

```
python synchronization.py arg1  
```
, where: 

* arg1 - relative path from the current directory to the input file. To make life easier - move the input file to the same directory where this python file is and run the script from there


## TXT files 

### requirements.txt 

Consists of all necessary libraries for correct program execution.
Before running the program for the first time in the root directory execute this: 

```
pip install -r requirements.txt 
```

### my_key_file.txt

It should contain exactly one line - api-key from here:  https://ipstack.com/plan


# Other files 

If you want to make yours work as fast and easy as possible: 

* move your xlsx file with ip addresses (input file) in this directory where all other files are
* rename the column with ip addresses to "IP"
* add the api key to my_key_file.txt 
* run synchronization.py file as described above.