# Security Monitor

A Python-based cybersecurity monitoring tool that processes Linux authentication logs, detects potentially suspicious login activity, and stores security alerts for investigation.

## Overview

Security monitoring helps identify suspicious activity by collecting and analyzing system events. This project demonstrates the basics of security monitoring using Python, Linux authentication logs, SQLite, and Grafana.

The system reads log entries, converts recognized messages into structured security events, applies detection rules, stores alerts in a database, and displays them in a Grafana dashboard.

**Project status:** Core features implemented; final testing and documentation in progress.

## Objectives

- Learn how Linux authentication logs work.
- Build a Python log reader and parser.
- Convert raw log messages into structured security events.
- Detect repeated failed authentication attempts.
- Store security alerts in an SQLite database.
- Test parsing and detection logic with automated tests.
- Display security alerts in Grafana.
- Document and demonstrate the complete monitoring workflow.

## Architecture

```text
Linux Authentication Logs
          |
          v
      Log Reader
          |
          v
        Parser
          |
          v
   Detection Engine
          |
          v
     SQLite Database
          |
          v
    Grafana Dashboard
```

Each component has a separate responsibility. This makes the system easier to understand, test, and maintain.

## Features

### Log Collection

Reads Linux authentication logs from `/var/log/auth.log` or a specified sample log file and provides individual log entries for processing.

### Log Parsing

Extracts structured information from supported log messages, including:

- Timestamp
- Service name
- Username
- Source IP address
- Event type

The parser recognizes selected SSH authentication events and `sudo` command events.

### Rule-Based Detection

The detection engine identifies repeated failed login attempts from the same source IP address.

The current rule generates an alert when at least five failed login events occur within a 120-second window.

A detection indicates potentially suspicious activity. It does not automatically prove that an attack occurred.

### Alert Storage

Uses SQLite to store security alerts for later retrieval.

Alert records include:

- Alert type
- Source IP address
- Attempt count
- Description
- Creation timestamp

### Grafana Dashboard

Grafana displays stored security alerts in a table so they can be reviewed and investigated.

### Automated Testing

Uses `pytest` to test the parser and detection logic with representative input data, including failed logins, successful logins, and invalid log entries.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Log processing and detection |
| Linux Mint | Development environment |
| Regular expressions | Extracting information from log messages |
| SQLite | Persistent alert storage |
| pytest | Automated testing |
| Git and GitHub | Version control and project documentation |
| Grafana | Security alert dashboard |

## Project Structure

```text
Security-monitor/
├── collector/
│   ├── log_reader.py
│   └── python_practice.py
├── parser/
│   └── log_parser.py
├── detection/
│   └── detection_engine.py
├── database/
│   └── alert_storage.py
├── tests/
│   ├── test_parser.py
│   └── test_detection.py
├── run_monitor.py
├── sample_auth.log
└── README.md
```

The repository folder may still have its original name, `ai-security-monitor`. The project itself is called **Security Monitor**.

## Getting Started

### Prerequisites

- Python 3
- Linux environment
- Access to authentication logs if testing with real system logs
- `pytest` for automated testing
- Grafana for dashboard visualization

SQLite is available through Python's standard library.

### 1. Clone the repository

Replace the example URL with your actual GitHub repository URL.

```bash
git clone <YOUR_REPOSITORY_URL>
cd Security-monitor
```

If you renamed the repository or local folder, use the correct URL and folder name.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install testing dependencies

```bash
python3 -m pip install pytest
```

### 4. Run the monitor with sample data

From the project root, run:

```bash
python3 run_monitor.py sample_auth.log
```

The program processes the sample log, detects repeated failed logins, and saves any generated alerts to the configured SQLite database.

### 5. Run the monitor with system logs

```bash
python3 run_monitor.py
```

The program uses `/var/log/auth.log` by default. Depending on the system, access permissions may be required.

### 6. Run the automated tests

```bash
python3 -m pytest
```

### 7. View the alerts

Open your Grafana dashboard and review the alerts retrieved from the SQLite database.

The database must be accessible through the configured database path, and Grafana must be connected to the correct data source.

## Example Detection Scenario

The following is synthetic test data, not evidence of a real attack.

Five failed login events occur from the same source IP address within 120 seconds.

Example alert:

```text
Alert type: repeated_failed_logins
Source IP: 192.0.2.25
Attempt count: 5
Description: 5 failed login attempts from 192.0.2.25 within 120 seconds
```

The alert provides evidence for further investigation. Legitimate users can also make repeated login mistakes, so additional context is needed before drawing conclusions.

## Security and Privacy

- Only access systems and log data you are authorized to use.
- Use synthetic events when testing detection rules.
- Never commit passwords, API keys, or other secrets.
- Review log files and database contents before publishing them.
- Avoid publishing personal information or sensitive authentication records.
- Treat alerts as indicators for investigation, not definitive proof of an attack.

The repository is an educational prototype and is not intended to replace a production Security Information and Event Management (SIEM) platform.

## Current Limitations

- The parser supports selected log formats, not every Linux authentication event.
- The monitor processes a log file when run; continuous monitoring is not implemented.
- The initial detection rule focuses on repeated failed logins from a single source IP address.
- Real failed SSH login events have not been confirmed in the development environment, so synthetic events are used for detection testing.
- Re-running the sample can create duplicate alerts because alert deduplication has not been implemented.
- The dashboard displays stored alerts but does not provide a complete enterprise investigation workflow.

## Roadmap

- [x] Read Linux authentication logs
- [x] Parse selected authentication events
- [x] Implement a repeated failed-login detection rule
- [x] Store alerts in SQLite
- [x] Add initial automated tests
- [x] Display alerts in Grafana
- [x] Improve parser coverage and error handling
- [x] Improve detection tests and alert deduplication
- [x] Complete end-to-end testing and documentation

## Learning Outcomes

This project provides practical experience with:

- Linux authentication and security logging
- Python programming and regular expressions
- Structured event processing
- Rule-based threat detection
- SQL and SQLite
- Automated testing
- Modular software development
- Security alert investigation
- Git and GitHub

## Disclaimer

This project was developed for educational purposes. It is a learning prototype and has not been validated as a production security monitoring solution.

## Author

Developed as a cybersecurity learning project focused on Linux security monitoring, Python programming, and security alert investigation.
