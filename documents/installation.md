# Installation Guide for SuRFM

## Prerequisites
Before installing the SuRFM package, make sure you have the following prerequisites installed on your system:

- **Python 3.x**: Ensure you have a recent version of Python installed. Python 3.6 or newer is recommended. You can download Python from [the official website](https://www.python.org/downloads/).
- **pip**: Python's package installer. It usually comes with Python, but if you need to install it, follow the instructions on [pip's installation page](https://pip.pypa.io/en/stable/installing/).

## Installation Steps

### 1. Clone the Repository
First, clone the SuRFM repository from GitHub to your local machine. You can do this using the following command:

```bash
git clone https://github.com/arturavagyan2/MA_Group_Project.git
cd SuRFM
```

### 2. Set Up a Virtual Environment (Optional)
It's a good practice to use a virtual environment to isolate package dependencies. To set up a virtual environment, you can use `venv`:

```bash
python -m venv surfm-env
source surfm-env/bin/activate  # On Windows use `surf-env\Scripts\activate`
```

### 3. Install Dependencies
Install all the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This command will install all the libraries needed for the SuRFM package, as specified in the requirements.txt file.

### 4. Install the SuRFM Package
To install SuRFM so that it's usable as a module, run:

```bash
pip install .
```

This command will install the SuRFM package into your Python environment.

## Post-Installation

### Verify Installation
After installation, you can verify that SuRFM is correctly installed by running:

```bash
import surfm
print(surfm.__version__)
```

This command should print the version number of the SuRFM package if it's installed correctly.

## Support
For further assistance, contact the support team through the repository's issues page or via email.
