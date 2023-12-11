# Python Intrusion Detection System

This project is an Intrusion Detection System (IDS) developed in Python 3, leveraging the capabilities of the `scapy` library for packet manipulation and analysis, and `sib_api_v3_sdk` for integrating with Sendinblue's email API for alerts.

## Prerequisites

Ensure you have Python 3 installed on your system. Additionally, the following libraries are required:

- `scapy`
- `sib_api_v3_sdk`

You can install these dependencies via pip:

```bash
pip install scapy sib_api_v3_sdk
```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/groupeCyber/projetcyberpython.git
cd projetcyberpython
```

## Usage

To run the Intrusion Detection System, navigate to the `app` folder and execute `main.py`:

```bash
cd app
python main.py
```

## Features

- Packet sniffing and analysis using `scapy`.
- Real-time intrusion detection with customizable rules.
- Alert notifications via email using `sib_api_v3_sdk`.
