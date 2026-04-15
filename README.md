# Trading-Bot
This project is a Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

# Binance Futures Trading Bot (Testnet)

## Overview

This project is a Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

It includes:

- Market order support
- Limit order support
- BUY and SELL operations
- CLI input validation
- Logging system
- Error handling
- Modular project structure

---

## Project Structure

trading_bot/

bot/
- client.py
- orders.py
- validators.py
- logging_config.py

cli.py  
requirements.txt  
README.md  

---

## Setup Instructions

### Install dependencies

pip install -r requirements.txt

### Create .env file

Add:

API_KEY=your_api_key  
API_SECRET=your_secret  

---

## Run MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

---

## Run LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

---

## Logging

Logs are saved in:

trading.log

This includes:

- Order requests
- Responses
- Errors

---

## Assumptions

- Binance Futures Testnet is used
- API keys are valid
- Test USDT balance is available
