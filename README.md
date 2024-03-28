# Game-Guesser

## Run 

Install `requests`
```
pip install requirements.txt
```
Run `main.py`
```
python main.py
```

## Examples

### Mode 1, Game with uknown symbols:
Game: `Balatro`

Only known: `*a*at**`, result: `['Cavatus', 'ZaBaTa!', 'Lakatos', 'Balatro', 'NARATHA']`

### Mode 2, Word in the name:
Game: `Balatro`

Only known: `latro`, result: `['Balatro']`

### Mode 3, Words in the name begin with:
Game: `Far Cry® 6`

Only known: `F, C, 6`, result: `['Far Cry® 6']`

