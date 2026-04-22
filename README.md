# 🚀 Trading Bot CLI (Binance Futures Testnet)

## Introduction

Trading Bot CLI is a lightweight Python-based command-line application that simulates and executes trading orders on Binance Futures Testnet.  
The project is designed to demonstrate clean backend architecture, robust input validation, structured logging, and resilient API handling.

It supports **MARKET**, **LIMIT**, and **STOP-LIMIT** orders with a modular and production-style design.

---

## Project Overview

- CLI-based trading execution tool  
- Supports:
  - MARKET orders  
  - LIMIT orders  
  - STOP-LIMIT orders (trigger + limit)  
- Handles BUY and SELL operations  
- Modular architecture with clear separation of concerns:
  - CLI layer (input/output)
  - Validation layer
  - Order execution layer (with retry logic)
  - API client layer (mock + real support)
- Provides structured JSON outputs  
- Logs all operations to file

---

## Features

### CLI-Based Execution
Execute trades directly from terminal using structured arguments.

### Input Validation
Ensures correctness of:
- symbol  
- side (BUY/SELL)  
- order type  
- quantity  
- price and stop price

### Multiple Order Types
Supports:
- MARKET  
- LIMIT  
- STOP-LIMIT (with stop trigger)

### Mock + Real API Support
- Default: Mock mode (safe execution)  
- Optional: Real Binance Futures Testnet integration

### Retry Mechanism
Retries failed order execution automatically.

### Structured Logging
Logs all inputs, outputs, and errors to `logs/app.log`.

### JSON Output
Returns clean, structured responses for both success and failure cases.

---

## Tech Stack

- Python 3.11  
- argparse (CLI parsing)  
- logging (built-in)  
- python-binance (API integration, optional)  
- pytest (basic testing)

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client (mock + real support)
│   ├── orders.py          # Order execution + retry logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   └── cli.py             # CLI entry point
│
├── logs/
│   └── app.log
│
├── tests/
│   └── test_validators.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone repository

```bash
git clone <your-repo-link>
cd trading_bot
```

---

### 2. Create virtual environment

```bash
python3.11 -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### ▶️ MARKET Order

```bash
python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```

---

### ▶️ LIMIT Order

```bash
python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 60000
```

---

### ▶️ STOP-LIMIT Order

```bash
python bot/cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.01 --price 60000 --stop-price 60500
```

---

## Sample Output

```json
{
  "success": true,
  "data": {
    "symbol": "BTCUSDT",
    "status": "FILLED",
    "orderId": 12345,
    "executedQty": 0.01
  }
}
```

---

## Error Example

```json
{
  "success": false,
  "error": "stop_price is required for STOP_LIMIT"
}
```

---

## Logging

Logs are stored in:

```text
logs/app.log
```

Includes:

- input parameters
- execution results
- errors and retries

---

## Mock vs Real Mode

### Default (Mock Mode)

- No API keys required
- Safe simulation of order execution

### Real Mode (Optional)

To enable real Binance Futures Testnet:

1. Generate API keys
2. Update client initialization:

```python
BinanceClient(api_key, api_secret, use_mock=False)
```

---

## ⚠️Important Note

Due to Binance testnet API key generation restrictions (KYC enforcement in some cases), the application runs in **mock mode by default**.

The real API integration is fully implemented and can be enabled when valid credentials are available.

---

## Testing

Run tests:

```bash
pytest
```
