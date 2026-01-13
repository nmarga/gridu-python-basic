## Web Scraping task

### Prerequisites
Install all the dependencies using pip install
```bash
pip install -r requirements.txt
```

Create .env file on the same directory path as the stock_info.py file. The file should include in the environment variables: the target URL and User Agent. You can see the environment variables names defined in the .env.example file. You can use any valid User Agent string.
```bash
cp .env.example .env
```

### Execution
Run the script from the terminal in the same relative path as stock_info.py file:
```bash
python3 stock_info.py
```

### Optional Arguments
You can clear the cached web responses before running the script by adding the --clear-cache flag:
```bash
python3 stock_info.py --clear-cache
```