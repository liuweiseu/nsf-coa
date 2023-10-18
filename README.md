# NSF-COA
The code is referred [here](https://github.com/timothydmorton/nsf-coa/blob/main/coa.ipynb). It's used for populating [coa-tepmlate.xlsx](https://www.nsf.gov/bfa/dias/policy/coa/coa_template.xlsx) file.

# Install packages
Before running the code, we need to install some packages.
1. Install ads from github
    ```
    https://github.com/andycasey/ads.git
    cd ads
    pip install .
    ```
    ***Note:*** If you use `pip install ads`, you may have some issues.   
2. Install jupyterlab (optional)
    ```
    pip install jupyterlab
    ```
    If you don't want to use jupyterlab, you can copy the code to a .py file, and then run it directly.

# Getting start
1. create an account on [ADS](https://ui.adsabs.harvard.edu/), then get the API token(Accounts-->Settings-->API Token). Then paste the API token to the  notebook:
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