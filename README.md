# Bottled-Clicker 📜
This Python script uses Selenium to automate the process of logging into the Bottled chat site, locating a specified username's chat, and auto-clicking to scroll to the start of the conversation.
## Features ✨

- Logs into the Bottled chat site automatically.
- Searches for a specified username's chat.
- Auto-clicks to reach the start of the conversation.

## Prerequisites 📋

- Python 3.x 🐍
- pip (Python package installer) 📦
- A web driver compatible with your browser (e.g., [ChromeDriver for Google Chrome](https://developer.chrome.com/docs/chromedriver/downloads))

## Installation 💻

1. **Clone the repository or download as ZIP**

 ```bash
# Option 1: Clone the repository
git clone https://github.com/sevilerdal/Bottled-Clicker.git

cd Bottled-Clicker

# Option 2: Download .zip and extract
wget https://github.com/sevilerdal/Bottled-Clicker/archive/refs/heads/main.zip

unzip main.zip
   
cd Bottled-Clicker-main
```

2. **Install the required packages**

```bash
# Option 1: Install packages individually
pip install selenium

# Option 2: Install packages from requirements.txt
pip install -r requirements.txt
```

3. **Download the web driver**

For Chrome, download ChromeDriver from here and place it in the same directory as your script or in a directory included in your system's PATH.

## Configuration ⚙️

1. **Edit the script to include your login credentials and the target username**

```python
# Change this with your site credentials
email = "yourmail@mail.co" 
passwd = "yourpassword"

# Replace this with the username of the chat you want to locate
chatusername = "targetUsername" 
```

## Usage 🚀
Run the script.
```bash
python bottledclicker.py
```

The script will:
- Open a browser and navigate to the Bottled chat site.
- Log in using the provided credentials.
- Navigate to the chat page.
- Search for the chat with the specified username.
- Auto-click to scroll to the start of the conversation.

## Notes 📝
+ Ensure that your browser version matches the web driver version.
+ This script is written for Chrome Browser. If you want to use another browser, change the code below for your preferred browser. For options and further development, you can refer to the [Selenium Documentation](https://www.selenium.dev/documentation/):

```python
. . .
# Change drive, e.g., "driver = webdriver.Firefox()" to use Firefox Browser
driver = webdriver.Chrome() 
. . .
```
+ Depending on the length of conversation, process may take time.
+ After reaching to the top of the chat, script waits for 10 minutes before shutting down. You can stop the script earlier by closing the tab or keyboard interruption (`Cmd + C` on macOS, `Ctrl + C` on Windows/Linux)
+ If you need more time than 10 minutes, change the code before running the program.
```python
. . .

except WebDriverException as e:
    # You should change 600 to value you need
    # Value = minutes * 60
    time.sleep(600) 
. . .
```
+ The script might need adjustments if the Bottled chat site layout or login process changes.

## Troubleshooting 🛠️

### Common Issues

1. **Web driver not found:**
   Ensure the web driver is in the correct directory or in a directory included in your system's PATH.

2. **Login issues:**
   Verify that your login credentials are correct and that the Bottled chat site has not changed its login process.


If you encounter any other issues, feel free to open an issue on GitHub.

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

