# coding: utf-8
import os
import sys
import math
import shutil

s = u"""Pnvclen cbe Uhzoregb Qvótrarf

An zvaun green é znghgb
Dhr é dhrz irvb qb zngb
Bh orenqêeb, qb evb
zrezb an orven
An qb Naqerjf é pncvnh
Znf ndhv é pnvcven

Rzonedhrv arffn ivntrz
N pbaivgr qb "frbpnz"
B Fretvaub qn Pnzreba

Oben crtne rffr obaqr?
Sreanaqb qvffr dhr
cbe ryr gá Znffn!
Znepb, "Pnqê Ebtê?"
Svpbh an tenawn pbz Cnhyn
R Wrffvpn aãb cbqr ive
Svpbh cerfn ab Grzcbeny

Niryvab sbv ceb Fnzon
Pbz Yrgípvn qn Cbegryyn
Cnffnenz ab One Frzragr
Arz pbaivqnenz n tragr
Qrfpbafvqrençãb gbgny

N Znev ynetbh Frbpnz
R sbv rzoben pbz b Sbsãb
Frz fnore fr vn qne pregb
Naqerjf svpbh Zrqvab
R npnobh sbv qrfvfgvab

Uhzoregb, ibpé é qr baqr?
Rh fbh Qvótrarf
Znf zvaun pvqnqr é Angny
B Encun qb bhgeb Evb
Dhnfr ongrh zvaun pnegrven
Znf rh aãb znedhrv oborven
R nvaqn npurv b yrx yrtny

B riragb Fra Enznyub
Aãb é n zrfzn pbvfn
R rh gnzoéz fragv snygn
Qndhryr pbzchgnqbe
B zryube dhr wá iv
Npub dhr ren hz Qéb
Fó aãb gvaun n shaçãb fyrrc
Qr abvgr ivenin grgéh

Zrh nzvtb, ahapn iv
Hzn cerfrcnqn gãb tenaqr
Crafr ahzn neehznçãb
Gvaun Bcra One qr cnçbpn
Pbz qvervgb n dhragãb

R dhnaqb ivrerz gr snyne
Qr dhnydhre grpabybtvn
Bh yvathntrz qr cebtenznçãb
Crethagr nb pnoen, an yngn:

– Arffn ghn pbasreêapvn
Ibpêf iãb ceb one
Rapure n pnen
An Pneergn Shenpãb?"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

terminal_size = shutil.get_terminal_size()
number_of_lines_in_text = s.count("\n") + 1

decifered_text = "".join([d.get(c, c) for c in s]).split("\n")
number_of_lines_in_text = number_of_lines_in_text + decifered_text.count("\n")

if "darwin" in sys.platform or 'linux' in sys.platform:
    os.system('clear')
elif "win" in sys.platform:
    os.system('cls')

number_of_pages = math.ceil(number_of_lines_in_text / terminal_size.lines)
start = 0
end = terminal_size.lines - decifered_text.count("\n") - 1
for page in range(number_of_pages):
    print("\n".join(decifered_text[start:end]))
    input()
    start += terminal_size.lines
    if (end + start < number_of_lines_in_text):
        end += start
    else:
        end = number_of_lines_in_text


def java():
    print('É mentiiiira!!!')
