# NSF-COA
The code is referred [here](https://github.com/timothydmorton/nsf-coa/blob/main/coa.ipynb). It's used for populating table-4 in [coa-tepmlate.xlsx](https://www.nsf.gov/bfa/dias/policy/coa/coa_template.xlsx) file.   
Feel free to modify the code to populate other tables. 

# Install packages
Before running the code, we need to install some packages.
1. Install ads from github
    ```
    git clone https://github.com/andycasey/ads.git
    cd ads
    pip install .
    ```
    ***Note:*** If you use `pip install ads`, you may have some issues.   
2. Install nameparser
    ```
    pip install nameparser
    ```
4. Install jupyterlab (optional)
    ```
    pip install jupyterlab
    ```
    If you don't want to use jupyterlab, you can copy the code to a .py file, and then run it directly.

# Getting start
You have 2 options: python script or notebook. I suggest you use the python script.
## Use the python script
1. create an account on [ADS](https://ui.adsabs.harvard.edu/), then get the API token(Accounts-->Settings-->API Token).   
   Then you need to copy the token to `token.txt`.
2. use `nsf-coa.py` to populate the table. (Currently, I only populate table-4.)
    ```
    ./nsf-coa.py --author 'horowitz, p.' --year '2018-2023' --verbose
    ```
    If everything goes well, you will see the paper number, paper list and the compared names. A csv file will be generated automatically.  
    More options can be seen here:
    ```(python)
    (jupyter) ➜  nsf-coa git:(main) ./nsf-coa.py -h                                                  
    usage: nsf-coa.py [-h] [--author AUTHOR] [--year YEAR] [--fn FN] [--verbose]

    Usage for NSF COA file population

    optional arguments:
    -h, --help       show this help message and exit
    --author AUTHOR  author name
    --year YEAR      year range. For example, 2018-2023
    --fn FN          output file name. By default, it's `coa_table_4.cvs`.
    --verbose        print out information
    ```
## Use the notebook
1.  Then paste the API token to the  notebook:
    ```
    ads.config.token = 'xxxxxxxx'
    ```
2. Export the paper list in AASTeX format. It should be like this:
    ```
    \bibitem[Korzoun et al.(2023)]{2023arXiv230809607K} ...   
    \bibitem[Maire et al.(2022)]{2022SPIE12184E..8BM} ...
    ...
    ```
    ***TO-DO***: We should be able to do the query with ads.SearchQuery().
3. copy the paper list to the notebook.
4. run the notebook, and get the coa.csv