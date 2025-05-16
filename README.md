# Triforcer

**Triforcer** is a multi-protocol brute force testing tool designed for educational and penetration testing purposes. It currently supports **web login brute forcing**, with plans to extend support for **FTP** and **SSH** authentication attacks. The project also includes test servers for safe local testing and experimentation.

## Features

- Web login brute force module
- Easy to configure test web server with login page
- Modular design for adding FTP and SSH brute forcing
- Safe and controlled environment for testing

## Getting Started

### Prerequisites

- Python 3.x
- Required packages listed in `requirements.txt` (Flask, paramiko, pyftpdlib)

### Running Test Servers

You can run the included test server to simulate the target services:

```bash
python test_server.py
