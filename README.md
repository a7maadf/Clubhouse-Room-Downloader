# Clubhouse Room Downloader

Clubhouse Room Downloader is a tool that allows users to download Clubhouse rooms as MP3 files. It consists of a browser userscript (`violentMonkeyScript.js`) and a Python script (`main.py`) that work in conjunction to achieve this functionality.

## Requirements

- Python 3.x
- Violentmonkey or compatible userscript manager for your browser.

## How to Use

### Step 1: Install the Userscript

1. **Install a Userscript Manager**: Make sure you have a userscript manager like Violentmonkey installed in your browser. You can find it in the browser's extension store.

2. **Access the Userscript**: Go to the GitHub repository and find the `violentMonkeyScript.js` file.

3. **View the Raw Code**: Click on the file and then click on the 'Raw' button. This will open the raw version of the JavaScript file.

4. **Install the Script**: Copy the URL of the raw script. Open Violentmonkey (or your chosen userscript manager) and choose to add a new script from a URL. Paste the copied URL and follow the prompts to install the script.

5. **Verify Installation**: Ensure that the script is enabled in Violentmonkey (or your chosen userscript manager).

6. **Refresh Clubhouse Room**: Refresh the Clubhouse room in your browser.

After following the above steps, you should see a blue button in the top left corner of the Clubhouse room that says 'download'. If the button doesn't appear, double-check the previous steps, especially that the script is enabled in your userscript manager.

### Step 2: Download the Clubhouse Room

1. Click the blue 'download' button.
2. A file will be downloaded to your system.

### Step 3: Convert to MP3

1. Open a terminal or command prompt on your computer.
2. Navigate to the directory containing the `main.py` file.
3. Run the following command, replacing `path/to/downloaded/file` with the actual path to the downloaded file:

   ```bash
   python main.py --file path/to/downloaded/file
   ```

4. The script will export the Clubhouse room as an MP3 file.

## Troubleshooting

If you encounter any issues, please check that you have all the necessary dependencies installed and that you are following the steps in the correct order. For more specific help, please open an issue on this repository.

## License

This project is available under the MIT License. See the LICENSE file for more details.

