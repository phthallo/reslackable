# reslackable
Reslackable is a Python app for browsing the Slack messaging platform from a reMarkable e-ink device. 

<p align="center">
  <br>
  <img src="https://github.com/user-attachments/assets/f91fd821-207d-4bcf-a982-926a83c094de" width="300" title="Channel drectory">
  <img src="https://github.com/user-attachments/assets/fd5ec660-6c20-475c-9628-97f924b24502" width="300" title="View messages">
<br>
<img src="https://github.com/user-attachments/assets/436088b2-97e2-4148-aa45-f2f8236b4a29" width="300" title="Channel directory on device">
  <img src="https://github.com/user-attachments/assets/24033c35-5f44-4e0d-906b-969e0f04fb7c" width="300" title="View messages on device">
</p>

> [!NOTE]  
> This is a big work in progress!

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
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3. Add your Slack App token as the `BOT_USER_OAUTH_TOKEN` environment variable. 
4. Start the simulator. Edit the created .resim.sh file to add the `--simulate` flag. 
    ```
    make simulate
    ```

## Roadmap
- [ ] More detailed development instructions
- [ ] Actually installable built version
- [ ] Pagination for fetching channels
- [ ] Pagination for navigating channels and messages
- [ ] Profile picture support
- [ ] Message times
- [ ] Replace user, channel @'s with actual names
- [ ] Better code :tm:
