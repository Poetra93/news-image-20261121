#!/usr/bin/env python3
"""Draw front-page.png: a newspaper front page summing up the world news
of Saturday 21 November 2026. Every story was verified against dated
reports for that day (see README.md). Build-time only; main.py just copies
the finished PNG."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
NAVY = (20, 36, 61)
GOLD = (201, 162, 39)
RED = (178, 34, 34)
TEAL = (14, 92, 92)
GREY = (90, 86, 78)
RULE = (180, 172, 155)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, xy, text, fnt, max_w, fill=INK, leading=None):
    x, y = xy
    lh = leading or int(fnt.size * 1.22)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def hline(draw, y, x0=24, x1=1000, fill=RULE, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead ------------------------------------------------------------
d.rectangle([0, 0, W, 118], fill=NAVY)
d.text((512, 14), "THE WORLD IN ONE DAY", font=font(SERIF_B, 46),
       fill=(250, 248, 240), anchor="ma")
d.text((512, 66), "SATURDAY 21 NOVEMBER 2026", font=font(SANS_B, 26),
       fill=GOLD, anchor="ma")
d.text((512, 96), "A front page of the day's world news  •  Every story happened or was first reported today",
       font=font(SANS, 14), fill=(200, 205, 215), anchor="ma")

# ---- Lead story ----------------------------------------------------------
d.text((24, 130), "LEAD  —  THE GULF", font=font(SANS_B, 15), fill=RED)
d.text((24, 152), "Iran says it struck US bases in Bahrain",
       font=font(SERIF_B, 38), fill=INK)
draw_wrapped(d, (24, 200),
             "Bahrain says the attack hit a civilian industrial site and started a fire; "
             "no injuries were reported and air defences intercepted other attacks. "
             "Tehran also claims it downed a US drone near Qeshm Island; Washington "
             "denies an F-16 was hit. President Trump says he wants a permanent deal.",
             font(SANS, 17), 976, leading=21)
hline(d, 272)

# ---- Second row: two stories ---------------------------------------------
def story_box(x, y, w, kicker, colour, headline, body, hsize=21):
    d.text((x, y), kicker, font=font(SANS_B, 14), fill=colour)
    y = draw_wrapped(d, (x, y + 20), headline, font(SERIF_B, hsize), w, leading=25)
    draw_wrapped(d, (x, y + 4), body, font(SANS, 15), w, leading=19)


story_box(24, 284, 478, "MEXICO  —  CARTELS", RED,
          "Mexico captures cartel boss \u201cEl Chapo Isidro\u201d",
          "Forces seized Fausto Isidro Meza Flores, one of the FBI's 10 most "
          "wanted, in Guasave, Sinaloa. At least 11 people died in the backlash.",
          hsize=20)
story_box(522, 284, 478, "UKRAINE  —  WAR", RED,
          "Russian missile hits Zelenskyy's hometown",
          "A ballistic strike on Kryvyi Rih killed a boy aged 7 and a woman aged "
          "20, and wounded about 60. Two Russian missiles had landed in Poland "
          "the day before.", hsize=20)
hline(d, 420)

# ---- Third row: three stories --------------------------------------------
story_box(24, 432, 312, "CLIMATE  —  COP31, ANTALYA", TEAL,
          "Climate talks run into overtime",
          "COP31 passed its deadline with no deal; the draft omits fossil fuels.",
          hsize=19)
story_box(356, 432, 312, "MARKETS  —  NEW YORK", TEAL,
          "US stocks slide into correction",
          "The AI sell-off deepened: the S&P 500 and Dow entered correction.",
          hsize=19)
story_box(688, 432, 312, "POLITICS  —  SHENZHEN", TEAL,
          "Trump defends Putin ties",
          "After a summit with Xi, Trump defended calling Putin a friend; "
          "Zelenskyy: \u201ca killer\u201d.",
          hsize=19)
hline(d, 566)

# ---- The day in brief -----------------------------------------------------
d.text((24, 574), "THE DAY IN BRIEF", font=font(SERIF_B, 22), fill=NAVY)
d.text((1000, 578), "24 more stories from Saturday", font=font(SANS, 14),
       fill=GREY, anchor="ra")
hline(d, 602, width=3)

BRIEFS = [
    ("POLAND", "Missiles land on NATO soil; Warsaw calls it an \u201cintentional provocation\u201d."),
    ("BALTIC SEA", "Drones hit Russian cargo ship Sparta II; it drifts into Finnish waters."),
    ("GAZA", "Israeli strike kills three people in a food vehicle in Gaza City."),
    ("YEMEN", "Houthis and the Saudi-led coalition trade strikes; 71 strikes claimed."),
    ("BREXIT", "UK and EU sign three deals on food, emissions trading and youth travel."),
    ("TRADE", "EU and Indonesia sign a deal cutting 98.5% of tariffs on EU goods."),
    ("TECH TAX", "Trump threatens a tax on firms building AI data centres abroad."),
    ("CYBER", "FBI crime database reportedly hacked; the bureau is investigating."),
    ("AI WEAPONS", "UN talks agree to keep working on rules for autonomous weapons."),
    ("DENMARK", "Russian diplomat expelled over an alleged plot to kill rapper Kyivstoner."),
    ("FRANCE", "Cost-of-living protests continue; 144 arrests on a sixth Saturday."),
    ("PARIS", "Three police sentenced over the racist 2020 beating of Michel Zecler."),
    ("LOS ANGELES", "Man convicted of starting the 2025 Palisades fire, in which 12 died."),
    ("BRAZIL", "Wolbachia mosquitoes cut dengue among children, a study finds."),
    ("SPACE", "BepiColombo enters orbit around Mercury after an eight-year journey."),
    ("BRASILIA", "Bolsonaro in intensive care with a bowel obstruction; he is stable."),
    ("NIGERIA", "Funeral boat capsizes in Bayelsa State; at least 24 people dead."),
    ("ENERGY", "Saudi Arabia and Japan agree an oil stockpile deal: 24m barrels."),
    ("ARGENTINA", "Bonds fall into distressed territory for the first time in two years."),
    ("TURKEY", "State takes control of Sozcu TV, the last big independent channel."),
    ("TANZANIA", "Opposition leader Tundu Lissu convicted of sedition."),
    ("UGANDA", "Gatherings restricted as the Ebola outbreak spreads."),
    ("QUAKES", "Magnitude 6.7 shakes Peru; a 6.8 quake strikes off Timor-Leste."),
    ("RUGBY", "England rout the All Blacks 37\u201312 at Twickenham, a record win."),
]

COL_W, COL_X = 312, (24, 356, 688)
ROW_H = 47
y0 = 614
f_kick = font(SANS_B, 13)
f_body = font(SANS, 13)
for i, (kick, text) in enumerate(BRIEFS):
    col, row = divmod(i, 8)
    x = COL_X[col]
    y = y0 + row * ROW_H
    # First line: bold kicker + start of text, wrapped to two lines total.
    full = kick + " \u2014 " + text
    lines = wrap(d, full, f_body, COL_W)
    # Redraw first line with the kicker in bold red.
    first = lines[0]
    klen = len(kick) + 3  # kicker + " — "
    prefix = first[:klen]
    rest = first[klen:]
    d.text((x, y), prefix, font=f_kick, fill=RED)
    d.text((x + d.textlength(prefix, font=f_kick), y), rest, font=f_body, fill=INK)
    if len(lines) > 1:
        d.text((x, y + 16), lines[1], font=f_body, fill=INK)
    if len(lines) > 2:
        # Squeeze a third line in only if it fits the row; it should not occur.
        d.text((x, y + 32), lines[2], font=f_body, fill=INK)

hline(d, 996)
d.text((24, 1004), "All 30 stories above happened or were first reported on Saturday 21 November 2026.",
       font=font(SANS, 13), fill=GREY)
d.text((1000, 1004), "Sources: AP, Reuters, BBC, AFP, ESA, national wires",
       font=font(SANS, 13), fill=GREY, anchor="ra")

img.save("front-page.png", optimize=True)
print("saved front-page.png", img.size)
