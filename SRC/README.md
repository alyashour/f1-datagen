# F1 Datagen
## Usage
### Config
Config for the generator can be edited in `SRC/data_generator/config.py`  
DB config must be entered into `SRC/data_writer/config.py`  
Input your password into a `secrets.py` file placed in the SRC directory  
```python
# SRC/secrets.py
# example:
db_pswd = 'my_password'
```

### Installation
#### Pipenv
Run `pipenv install` to install all dependencies.
### Pip
I have not tested this but I have frozen a requirements.txt file for use.  
Run `pip install -r requirements.txt` to install dependencies.

### To Run
- You can run `data_generator/generate.py` to view example data.  
- Automatically run datagen and output to db by running `SRC/main.py`
  - For example:
    ```shell
    # cd into SRC
    cd SRC
    
    # run
    pipenv run python main.py
    ```

Uses `faker` and `mysql-connect`.
