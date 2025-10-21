# Python 3.11.9 Installation Guide (Windows 64-bit)

This document provides step-by-step instructions for installing [Python 3.11.9 (64-bit)](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe) on a Windows operating system.

## 1. Download the Installer

Click the link below to download the Python 3.11.9 installer:

🔗 [python-3.11.9-amd64.exe](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)

## 2. Launch the Installer

Double-click the downloaded file `python-3.11.9-amd64.exe` to start the installation process.

## 3. Installation Options

On the installation screen, follow these steps:

- ✅ **Check the box that says "Add Python 3.11 to PATH".** (This is very important!)
- 🔘 Choose between **"Install Now"** or **"Customize installation"**:
  - For a quick setup, **Install Now** is recommended.
  - Advanced users can choose **Customize installation** to select a custom install directory and options.

## 4. Complete the Installation

The installation process may take a few minutes. Once it’s finished, you should see a message that says “Setup was successful.”

## 5. Verify the Installation

To verify that Python is installed correctly, open the Command Prompt (CMD) and type:

```bash
python --version
```

If the installation was successful, you’ll see:

```
Python 3.11.9
```

To start the interactive Python shell:

```bash
python
```

## 6. (Optional) Update pip

`pip` is Python’s package manager. You can update it with the following command:

```bash
python -m pip install --upgrade pip
```

## 7. Python is Ready to Use!

You now have Python 3.11.9 installed and ready to use.