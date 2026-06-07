# Coffee Machine

A command-line coffee machine simulator built in Python. Handles drink ordering, coin-based payments, resource tracking, and change calculation.

## How to Run

Requires Python 3.

```bash
python main.py
```

## Usage

| Input | Action |
|---|---|
| `espresso` / `latte` / `cappuccino` | Order a drink |
| `report` | Print current resource and money levels |
| `off` | Shut down the machine |

## Menu

| Drink | Water | Milk | Coffee | Cost |
|---|---|---|---|---|
| Espresso | 50ml | — | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 100ml | 24g | $3.00 |

## Coin Denominations

| Coin | Value |
|---|---|
| Quarter | $0.25 |
| Dime | $0.10 |
| Nickel | $0.05 |
| Penny | $0.01 |
