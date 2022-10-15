# ternstay

TernStay - Code to run the TernStay recon tasks

## Installing

1. Create a Python virtual environment and activate it.

    i. If you do not have virtualenv install it

    ```pip3 install virtualenv```

    ii. Initialise your virtual environment

    ```
    virtualenv -p python3 debite_venv
    source debite_venv/bin/activate
    ```

  2a. Install the package and all of its requirements.

      pip install -e .
     
  2b.  Install the package and all of its requirements for testing and development.
  
      pip install -e ".[dev]"
