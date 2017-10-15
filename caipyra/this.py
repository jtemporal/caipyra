# coding: utf-8
import webbrowser
import pydoc
from vigenere import decrypt

s = u"""Rybwmep ivf Wsfiseim Kwóvcglg

Lt avcft hrgpt é bymbhb
Onl é onla kcbv qd fhhb
Mn prgywêfb, wv exm
tsebm uo qcbyo
Cy kc Plwysjh é qnegtb
Zpq hehx é qnxnbyo

Cfioefsxp atqlh ixyzla
P vvbixrx rb "llcppk"
C Hcknwawm ko Ryflfbc

Icep ilung xzgr zhurr?
Ylfaplwv qxqll djc
wce cel gá Fhgfp!
Toerm, "Ppbê Fbvê?"
Sxahb ap zyoayy jcz Ntbzn
C Qsfhgvh aãm wcqt opf
Ugvvi epxzo cm Aszemkhz

Yolzvcm mcv nkv Fpkuh
Pdk Ssgíabh qp Ivfgtjeh
Cpqlhfnb gv Opp Zsztlml
Atk jcakgwhfnb t urcrx
Rrhahugvsckhçãd mvhna

H Zppb zngehb Ftmvha
T yvw tkuvfn aht b Dhmãb
Qxt fpzxy ft bh qpp jseim
Hbqgcpz sxahb Ztbbuc
T tjoods mcv bxzwfiggv

Wsfiseim, jbré é qt hurr?
Xb fds Kwóvcglg
Byl avcft qvsywl é Ltaoy
M Yocwy kc dsmyc Ggh
Ehpqx pnicn avcft qngrxpfn
Ktz rj gãc bykxirx uvprxpt
S pggko paalw d ely aczhz

M ljrcrh Grc Khanafh
Bãd é o bclto rmbzo
T xb gpkuéa hcgaw uyeao
Syjbsyt vvacjrtkce
M tsywmk eht cá ix
Tjvb onl rgy ba Séh
Gó lãv gxlah n dnuçãd lssre
Wl adgml ixptco icméi

Kxb nbgzv, csgjo kg
Ban nklgreywh gãm nfncbx
Drcqx bhby hfejktçãb
Rbuvn Milb Qyk rr ntçcpp
Vva sgklwgd t ehtlmãc

C xincbh jvtpxt gt yhzng
Wl djyexirg mlqadjhnwn
Mn zvcenhurb wl cgmzyozpçãv
Ctpzbbgt tv ppzkh, cy sogp:

– Cclzo ist qbcdxyêargt
Jbrêl jãd iyc qyk
Sarfxy n atyo
Cy Joegcmh Sjptjãb?"""


pydoc.pager(decrypt('python', s))


def link():
    webbrowser.open('https://www.youtube.com/watch?v=BNmNSHu9bMU')
