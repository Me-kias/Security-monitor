# AI-Assisted Cybersecurity Monitoring

A Python-based cybersecurity monitoring prototype that processes Linux authentication logs, identifies potentially suspicious login activity, and stores security alerts for investigation.

## Overview

Security monitoring helps organizations identify suspicious activity by collecting and analyzing system events. This project explores the fundamentals of that process by building a small, modular monitoring system using Python and Linux authentication logs.

The system reads authentication-related log entries, converts recognized events into structured data, applies rule-based detection, and stores generated alerts in an SQLite database.

The long-term goal is to add AI-assisted alert explanations to help users understand why an alert was generated and what to investigate next.

**Project status:** In development

## Objectives

- Learn how Linux authentication logs work.
- Build a Python log reader and parser.
- Convert raw log messages into structured security events.
- Detect repeated failed authentication attempts.
- Store security alerts in an SQLite database.
- Test parsing and detection logic with automated tests.
- Develop a dashboard for reviewing alerts.
- Explore AI-assisted security alert explanations.

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
    Security Dashboard
          |
          v
 AI-Assisted Explanation
       (Planned)
```

The system is designed as separate components so that log collection, parsing, detection, storage, and presentation can be developed and tested independently.

## Current Features

### Log Collection

Reads Linux authentication logs from `/var/log/auth.log` and passes individual log entries to the parser.

### Log Parsing

Extracts structured information from recognized log messages, including:

- Timestamp
- Service name
- Username
- Source IP address
- Event type

The parser currently recognizes selected SSH authentication events and `sudo` command events.

### Rule-Based Detection

The detection engine includes a rule for identifying repeated failed login attempts from the same source IP address.

The current test rule triggers when at least five failed login events occur within a 120-second window.

A detection indicates potentially suspicious activity; it does not, by itself, prove that an attack occurred.

### Alert Storage

Uses SQLite to store security alerts for later retrieval and analysis.

Alert records include fields such as:

- Alert type
- Source IP address
- Attempt count
- Description
- Creation timestamp

### Automated Testing

Uses `pytest` to test components and verify expected behavior with representative input data.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Log processing and detection logic |
| Linux Mint | Development and log source environment |
| Regular expressions | Extracting information from log messages |
| SQLite | Persistent alert storage |
| pytest | Automated testing |
| Git and GitHub | Version control and project documentation |
| Grafana | Planned alert visualization |
| AI / LLM API | Planned alert explanation and investigation support |

## Project Structure

```text
Ai-security-monitor/
├── collector/
│   └── log_reader.py
├── parser/
│   └── log_parser.py
├── detection/
│   └── detection_engine.py
├── database/
│   └── alert_storage.py
├── tests/
├── run_monitor.py
├── datetime_test.py
├── security_alerts.db
└── README.md
```

The exact files and directories may evolve as the project develops.

## Getting Started

### Prerequisites

- Python 3
- Linux environment with access to authentication logs
- SQLite support through Python's standard library
- `pytest` for running automated tests

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Ai-security-monitor
```

Replace `<YOUR_REPOSITORY_URL>` with the URL of your GitHub repository.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install testing dependencies

```bash
python3 -m pip install pytest
```

Install any additional dependencies required by the current version of the project.

### 4. Run the monitor

From the project root:

```bash
python3 run_monitor.py
```

The program requires read access to the configured authentication log. Depending on the system, elevated permissions may be necessary.

### 5. Run the tests

```bash
python3 -m pytest
```

## Example Detection Scenario

The following is illustrative test data, not evidence of a real attack:

```text
Event 1: Failed login from 10.0.2.20
Event 2: Failed login from 10.0.2.20
Event 3: Failed login from 10.0.2.20
Event 4: Failed login from 10.0.2.20
Event 5: Failed login from 10.0.2.20
```

If all five events fall within the configured 120-second window, the detection rule can generate an alert similar to:

```text
Alert type: repeated_failed_logins
Source IP: 10.0.2.20
Attempt count: 5
Description: 5 failed login attempts within 120 seconds
```

The alert provides evidence for further investigation. Legitimate users can also make repeated mistakes, so additional context is needed before drawing conclusions.

## AI-Assisted Analysis

AI-assisted analysis is a planned extension of the project.

The intended functionality is to provide explanations of existing alerts, summarize the evidence behind a detection, and suggest investigation steps.

The detection engine remains rule-based. AI is intended to support human investigation rather than replace detection rules or independently determine whether an incident is malicious.

## Security and Privacy

- Use only systems and log data you are authorized to access.
- Use synthetic events when testing detection rules.
- Do not commit passwords, API keys, access tokens, or other secrets.
- Review log files and database contents before publishing them.
- Avoid publishing personal information or sensitive authentication records.
- Treat alerts as indicators that require investigation, not definitive proof of an attack.

The repository is an educational prototype and is not intended to replace a production Security Information and Event Management (SIEM) platform.

## Current Limitations

- The parser supports selected log formats rather than every Linux authentication event.
- The current log reader processes the configured log file when run; continuous monitoring is not yet implemented.
- The initial detection logic focuses on repeated failed logins from a single source IP.
- Real failed SSH login events have not yet been confirmed in the development environment; synthetic events are used for detection testing.
- Dashboard integration and AI-assisted explanations are planned extensions.

## Roadmap

- [x] Read Linux authentication logs
- [x] Parse selected authentication events
- [x] Implement a repeated failed-login detection rule
- [x] Store alerts in SQLite
- [x] Add initial automated tests
- [ ] Improve parser coverage and error handling
- [ ] Improve detection tests and alert deduplication
- [ ] Visualize alerts in a dashboard
- [ ] Add AI-assisted alert explanations
- [ ] Complete end-to-end testing and documentation

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
- AI-assisted security analysis

## Disclaimer

This project is developed for educational purposes. It is a learning prototype and has not been validated as a production security monitoring solution.

## Author

Developed as a cybersecurity learning project focused on Linux security monitoring, Python automation, and AI-assisted investigation.
