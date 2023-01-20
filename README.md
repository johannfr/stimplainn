# stimplainn

Apparat til að stimpla sig inn, já.

## Uppsetning

Mæli með uppsetningu gegnum pipX:
```bash
pip3 install --user pipx
```

Og svo setja inn pakkann sjálfan:

```bash
pipx install git+https://github.com/johannfr/stimplainn.git
```

## Notkun

```bash
Usage: stimplainn [OPTIONS] EMPLOYEE_NUMBER

Options:
  -j, --jobtype INTEGER   [default: 0]
  -d, --description TEXT
  -u, --update
  --help                  Show this message and exit.
```

Tegundir eru þær sem sýnilegar eru í listanum á skráningarsíðunni, talið frá 0:
```
  0. Vinna
  1. Frí
  2. Veikindi
  3. Veikindi barns
```

### Dæmi

#### Stimpla inn/út í vinnu
```bash
stimplainn 1234567
```
#### Skrá veikindi
```bash
stimplainn 1234567 -j 2
```
