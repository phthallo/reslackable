# reslackable

Reslackable is a Python app for browsing the Slack messaging platform from a reMarkable e-ink device. 

## Development
### Requirements
1. [Carta](https://github.com/jayy001/carta)
2. [Requests](https://github.com/psf/requests) 


### Instructions
1. Clone the repository
    ```
    git clone https://github.com/phthallo/reslackable && cd reslackable
    ```
2. Install dependencies (in a virtual environment)
    ```
    pip install -r requirements.txt
    ```
3. Add your Slack App token as the `BOT_USER_OAUTH_TOKEN` environment variable. 
4. Start the simulator. Edit the created .resim.sh file to add the `--simulate` flag. 
    ```
    make simulate
    ```