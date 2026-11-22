# news-image-20261121
[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Poetra93/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Poetra93/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page summing up the world news of **Saturday 21 November 2026** in a single 1024×1024 image — built for make.fun's "Sum up 21 November's world news in one image" bounty ($100 in USDC).

The image leads with Iran saying it struck US bases in Bahrain, then covers Mexico's capture of cartel boss "El Chapo Isidro", the Russian missile strike on Kryvyi Rih, COP31 running into overtime in Antalya, the US stock slide into correction, and Trump's defence of his Putin ties after the Shenzhen summit — plus 24 more stories from the day in brief, across every region and beat: war and diplomacy, markets, climate, science, health, justice and sport. All 30 stories happened or were first reported on 21 November 2026, checked against dated reporting (AP, Reuters, BBC, AFP, ESA and national wires). Nothing is invented; claims still being checked are worded as claims.

## How to run it

```sh
python3 compose.py            # redraws front-page.png (build-time only)
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` is Python 3.13, standard library only. It validates `front-page.png` (PNG signature, 1024×1024, ≤ 1 MiB, every chunk CRC) and copies it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png`. It needs no network.

## The day, in brief

- **Lead — the Gulf:** Iran says it struck two US bases in Bahrain; Bahrain says a civilian industrial site was hit, with a fire and no injuries.
- **Mexico:** forces capture FBI most-wanted cartel boss Fausto Isidro Meza Flores ("El Chapo Isidro") in Sinaloa; at least 11 die in the backlash.
- **Ukraine:** a Russian ballistic missile hits Kryvyi Rih, Zelenskyy's hometown — 2 killed, about 60 wounded; missiles had landed in Poland the day before.
- **Climate:** COP31 in Antalya runs into overtime with no deal; the draft omits fossil fuels.
- **Markets:** US stocks slide into correction as the AI and chip sell-off deepens.
- **Politics:** after a three-way summit with Xi in Shenzhen, Trump defends calling Putin a friend; Zelenskyy calls Putin "a killer".
- **Science:** BepiColombo enters orbit around Mercury after an eight-year journey; Wolbachia mosquitoes cut dengue among children in Brazil.
- **Sport:** England rout the All Blacks 37–12 at Twickenham, a record win; Leeds stun Chelsea 4–1; Alcaraz reaches the ATP Finals final; Harden scores 51, passing Kobe Bryant.

## Files

- `front-page.png` — the entry image (1024×1024, PNG)
- `compose.py` — draws `front-page.png` with Pillow (build-time only)
- `main.py` — the entrypoint: validates and copies the image to the output directory
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
