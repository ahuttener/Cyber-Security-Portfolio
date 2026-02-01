# 🏦 CyberSec Portfolio: Vulnerable Bank API & PyAudit Tool

This repository showcases a complete **Offensive Security Simulation**, demonstrating skills in Python scripting, API vulnerability exploitation (IDOR/BOLA), and password auditing.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Framework:** Flask (API Simulation)
- **Concept:** Broken Object Level Authorization (BOLA) / IDOR
- **Tools:** Custom Python Scripts (CLI)

---

## 🚩 Project 1: The "Billion Dollar" Bank Hack (Simulation)
**Scenario:** A controlled environment simulating a Digital Bank API hosted on a local server. The goal was to compromise high-value assets by exploiting logic flaws.

### 1. The Target
A REST API endpoint `/api/balance/<id>` was identified. The application failed to validate if the requester had ownership of the requested object ID.

### 2. The Vulnerability (IDOR)
By manipulating the `user_id` parameter, I was able to bypass authorization controls.
- **My User ID:** `1002` (Balance: $50.00)
- **Target ID:** `1001` (Admin Account)

**Vulnerable Code Snippet:**
```python
# NO TOKEN VALIDATION
@app.route('/api/balance/<user_id>')
def get_balance(user_id):
    return database.get(user_id) # Returns data to anyone who asks


### 3. The Result
Full exfiltration of the administrative account balance (**$1.5 Billion** - fictional).

<img width="2817" height="1497" alt="print_bank png" src="https://github.com/user-attachments/assets/c7c8213d-c9c2-4db3-b9b3-336690f829d0" />



🔐 Project 2: PyAudit - Elite Password Cracker
I developed a custom CLI tool for Red Team operations to audit weak password policies via dictionary attacks.

<img width="2817" height="1475" alt="print_tool png" src="https://github.com/user-attachments/assets/325c1fc8-0ce2-4f3a-b78a-b7be02e78ace" />


Features:

🚀 Multi-Algorithm: Supports MD5 and SHA-256.

🎨 Visual Interface: Custom ASCII Art banner and color-coded logs (Colorama).

⚡ Performance: Optimized file reading for wordlist processing.

Usage

Bash
python3 pyaudit.py -hash [HASH] -w wordlist.txt -t sha256

Execution Proof
⚠️ Disclaimer
This project was developed for educational purposes and security research only. The vulnerabilities demonstrated here are intentional simulations running in a local environment.
