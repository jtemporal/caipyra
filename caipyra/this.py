# coding: utf-8
import sys
import webbrowser

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
        d[chr(i + c)] = chr((i + 13) % 26 + c)

s_list = s.split('\n\n')

for index, verse in enumerate(s_list):
    print("\n" + "".join([d.get(c, c) for c in verse]))
    if index < len(s_list) - 1:

        # Checks Python major version to accepting data from user
        if sys.version_info.major == 2:
            next = raw_input('\nContinue (Y/n)? ')
        else:
            next = input('\nContinue (Y/n)? ')

        if next.lower() == 'n':
            break


def link():
    webbrowser.open('https://www.youtube.com/watch?v=BNmNSHu9bMU')
