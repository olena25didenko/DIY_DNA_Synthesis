import matplotlib; matplotlib.use("Agent" if False else "Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans","axes.spines.top":False,
    "axes.spines.right":False,"figure.dpi":150,"savefig.dpi":150,"savefig.bbox":"tight"})
COL={"col":"#2166AC","photo":"#B2182B","enz":"#1B7837","diy":"#762A83","paper":"#999999",
     "ours":"#2166AC","ins":"#92C5DE","sub":"#F4A582","del":"#2166AC"}

# ============ FIG 4.4  MASAKI REPRODUCTION (our measured data) ============
fig,ax=plt.subplots(1,3,figsize=(12,3.6))
# A: capping -> G->A
a=ax[0]
cats=["Ac2O\n(standard)","Pac2O\n(reactive)"]; ours=[0.127,1.539]; paper=[0.10,1.33]
x=np.arange(2); w=0.36
a.bar(x-w/2,ours,w,color=COL["col"],label="our reprocessing")
a.bar(x+w/2,paper,w,color=COL["paper"],label="Masaki 2022")
a.set_xticks(x); a.set_xticklabels(cats); a.set_ylabel("G→A per guanine (%)")
a.set_title("(a) Capping drives G→A",fontweight="bold",fontsize=10)
a.text(-0.1,1.30,"12.2×\n(paper 13×)",fontsize=9,fontweight="bold",color=COL["col"],ha="left")
a.legend(fontsize=8,frameon=False)
# B: position-resolved dG suppression
b=ax[1]
gpos=[1,6,9,14,17,20,25,28,32,35,40,43]
pac=[0.338,0.784,0.884,1.080,0.840,0.971,0.605,1.161,0.935,1.442,1.353,1.581]
da7=[0.615,1.288,1.420,0.094,1.655,1.891,1.145,0.173,1.931,2.829,0.275,2.937]
a8 =[0.445,0.822,0.837,0.027,0.936,1.491,0.723,0.021,1.669,2.347,0.030,2.029]
xx=np.arange(len(gpos))
b.plot(xx,pac,"-o",ms=4,color="#2166AC",label="Pac2O (canonical)")
b.plot(xx,da7,"-s",ms=4,color="#F4A582",label="+ 7-deaza-dG")
b.plot(xx,a8,"-^",ms=4,color="#B2182B",label="+ 8-aza-7-deaza-dG")
for i,p in enumerate(gpos):
    if p in (14,28,40): b.axvspan(i-0.35,i+0.35,color="#FFF3B0",zorder=0)
b.set_xticks(xx); b.set_xticklabels(gpos,fontsize=7); b.set_xlabel("guanine position in 48-mer")
b.set_ylabel("G→A (%)"); b.set_title("(b) Non-canonical dG rescue is position-local",fontweight="bold",fontsize=9.5)
b.legend(fontsize=7.5,frameon=False,loc="upper left")
b.text(0.5,-0.30,"shaded = analog-substituted sites 14/28/40 (10× / 59× suppression)",transform=b.transAxes,ha="center",fontsize=8,color="#B2182B",fontweight="bold")
# C: polymerase independence
c=ax[2]
pol=["Q5","Phusion","Ex Taq"]; vals=[3.24,3.01,3.24]
c.bar(pol,vals,color=COL["col"],width=0.55)
c.axhline(np.mean(vals),ls="--",color="#B2182B",lw=1)
c.set_ylabel("total error (per kb)"); c.set_ylim(0,4)
c.set_title("(c) Error is chemistry-, not\nreadout-determined",fontweight="bold",fontsize=9.5)
c.annotate("spread 1.08×\n(no difference)",xy=(1,3.1),xytext=(0.3,3.55),fontsize=8.5,fontweight="bold",color="#B2182B")
fig.suptitle("Figure 4.4  Independent reproduction of Masaki et al. (2022) capping chemistry from raw reads (DDBJ DRA013805)",
    fontweight="bold",fontsize=11,y=1.04)
fig.savefig("fig4_4_masaki_reproduction.png"); plt.close(fig)

# ============ FIG 4.5  MEASURED PHENOTYPES (sourced + reproduced) ============
fig,ax=plt.subplots(1,2,figsize=(11,4.2))
# A: error-class balance (normalised del/ins/sub), our data + Palluk published
a=ax[0]
methods=["Column\nphosphoramidite","Photolithographic\n(light-directed)","Enzymatic\n(TdT)"]
# rates (%/nt): Filges IDT (ours), Lietard normal (ours), Palluk (published)
raw={"del":[0.207,3.41,1.3],"ins":[0.013,0.001,1.0],"sub":[0.018,1.23,0.09]}
tot=[raw["del"][i]+raw["ins"][i]+raw["sub"][i] for i in range(3)]
dl=[100*raw["del"][i]/tot[i] for i in range(3)]
ins=[100*raw["ins"][i]/tot[i] for i in range(3)]
sub=[100*raw["sub"][i]/tot[i] for i in range(3)]
y=np.arange(3)
a.barh(y,dl,color=COL["del"],label="deletion")
a.barh(y,ins,left=dl,color=COL["ins"],label="insertion")
a.barh(y,sub,left=[dl[i]+ins[i] for i in range(3)],color=COL["sub"],label="substitution")
for i in range(3):
    if dl[i]>8: a.text(dl[i]/2,i,f"{dl[i]:.0f}%",ha="center",va="center",color="white",fontsize=9,fontweight="bold")
    if ins[i]>8: a.text(dl[i]+ins[i]/2,i,f"{ins[i]:.0f}%",ha="center",va="center",fontsize=8)
    if sub[i]>8: a.text(dl[i]+ins[i]+sub[i]/2,i,f"{sub[i]:.0f}%",ha="center",va="center",fontsize=8)
a.set_yticks(y); a.set_yticklabels(methods)
a.set_xlim(0,100); a.set_xlabel("error-class composition (normalised, %)")
a.set_title("(a) Error-class balance differs by method",fontweight="bold",fontsize=10)
a.legend(fontsize=8,loc="upper center",bbox_to_anchor=(0.5,1.14),ncol=3,frameon=False); a.invert_yaxis()
# B: substitution direction G->A vs G->T
b=ax[1]
lab=["Column\n(Masaki)","Photolithographic\n(Lietard)"]; 
ga=[0.11,0.100]; gt=[0.03,0.279]
x=np.arange(2); w=0.36
b.bar(x-w/2,ga,w,color="#2166AC",label="G→A")
b.bar(x+w/2,gt,w,color="#B2182B",label="G→T")
b.set_xticks(x); b.set_xticklabels(lab); b.set_ylabel("substitution rate (%/nt)")
b.set_title("(b) Substitution direction is the fine discriminator",fontweight="bold",fontsize=10)
b.legend(fontsize=9,frameon=False)
b.annotate("G→A\ndominant",xy=(0-w/2,0.11),xytext=(-0.45,0.20),fontsize=8,color="#2166AC",fontweight="bold")
b.annotate("G→T\ndominant",xy=(1+w/2,0.279),xytext=(0.75,0.30),fontsize=8,color="#B2182B",fontweight="bold")
b.set_ylim(0,0.36)
fig.suptitle("Figure 4.5  Measured error phenotypes discriminate synthesis method (reproduced from deposited data, not illustrative)",
    fontweight="bold",fontsize=10.5,y=1.02)
fig.text(0.5,-0.03,"Column = Filges IDT desalted + Masaki (our reprocessing). Photolithographic = Lietard normal (our reprocessing). "
    "Enzymatic = Palluk 2018 (published). Absolute rates not directly comparable across studies; the discriminative signal is profile SHAPE + substitution direction.",
    ha="center",fontsize=7.5,color="#555")
fig.savefig("fig4_5_phenotypes.png"); plt.close(fig)

# ============ FIG 4.6  MEASURED ATTRIBUTION (real classifiers) ============
fig,ax=plt.subplots(1,2,figsize=(11,4.2))
a=ax[0]
tasks=["Masaki capping\nAc2O vs reactive\n(binary)","Masaki capping\nmechanism family\n(3-class)","Filges\nIDT vs Sigma\n(leave-batch-out)"]
acc=[100,76.9,72.2]; chance=[50,33.3,50]; shuf=[7.7,7.7,50.0]
x=np.arange(3)
a.bar(x,acc,0.55,color=COL["col"],label="leave-group-out accuracy")
a.plot(x,chance,"_",ms=28,mew=2.5,color="#B2182B",label="chance")
a.plot(x,shuf,"x",ms=9,mew=2,color="#555",label="label-shuffle control")
for i in range(3): a.text(i,acc[i]+2,f"{acc[i]:.0f}%",ha="center",fontsize=9,fontweight="bold")
a.set_xticks(x); a.set_xticklabels(tasks,fontsize=8); a.set_ylabel("accuracy (%)"); a.set_ylim(0,110)
a.set_title("(a) Attribution from error phenotype — measured",fontweight="bold",fontsize=9.5)
a.legend(fontsize=8,frameon=False,loc="upper right")
# B: reproduction scorecard ours vs paper
b=ax[1]
names=["Masaki\ncapping ratio","Masaki\nda7G suppr.","Masaki\na8da7G suppr.","Lietard\ncapping→G→T","Filges IDT\ndel rate"]
ours=[12.2,10,59,3.6,0.207]; paper=[13,10,50,4.5,0.20]
# normalise each to paper=1 for a single-axis "agreement" view
rel_o=[ours[i]/paper[i] for i in range(5)]
xx=np.arange(5)
b.bar(xx,rel_o,0.5,color=COL["photo"])
b.axhline(1.0,ls="--",color="#333",lw=1)
b.axhspan(0.8,1.2,color="#DFF0D8",zorder=0)
for i in range(5): b.text(i,rel_o[i]+0.03,f"{ours[i]:g}\nvs {paper[i]:g}",ha="center",fontsize=7.5)
b.set_xticks(xx); b.set_xticklabels(names,fontsize=7.5); b.set_ylabel("our value ÷ published value")
b.set_ylim(0,1.5); b.set_title("(b) Reproduction scorecard (all within ~±20%)",fontweight="bold",fontsize=9.5)
fig.suptitle("Figure 4.6  Proof-of-concept becomes proof: attribution and per-condition rates reproduced on deposited data",
    fontweight="bold",fontsize=10.5,y=1.02)
fig.savefig("fig4_6_measured.png"); plt.close(fig)

# ============ FIG 4.3  ATTRIBUTION TIERS (clean redraw) ============
fig,ax=plt.subplots(figsize=(10,4.6)); ax.axis("off")
tiers=[("Tier 1 — proves DIY method","needs error + equipment + supply forensics (equipment/supply not developed, §5)","LR > 1000","aspirational","#E8A0A0"),
       ("Tier 2 — consistent with DIY","error phenotype suggests DIY; method not pinned","LR 10–1000","near-term","#F3D28C"),
       ("Tier 3 — rules out commercial","exclusion — most defensible & publishable now (cf. Crook X99/X95)","LR < 1 vs commercial","realistic now","#A7D3A6"),
       ("Tier 4 — uninformative","error-corrected / assembled construct","LR ≈ 1","n/a","#C8CED6")]
y=0.80
for t,d,lr,flag,c in tiers:
    box=FancyBboxPatch((0.03,y-0.03),0.62,0.15,boxstyle="round,pad=0.008",
        linewidth=0,facecolor=c,transform=ax.transAxes); ax.add_patch(box)
    ax.text(0.055,y+0.075,t,fontsize=11,fontweight="bold",transform=ax.transAxes,va="center")
    ax.text(0.055,y+0.02,d,fontsize=8.2,transform=ax.transAxes,va="center",color="#333")
    ax.text(0.70,y+0.06,lr,fontsize=10.5,fontweight="bold",transform=ax.transAxes,va="center",color="#B2182B")
    ax.text(0.70,y+0.005,flag,fontsize=8.5,transform=ax.transAxes,va="center",style="italic",color="#333")
    y-=0.185
ax.text(0.03,0.97,"Figure 4.3  Attribution tiers by likelihood ratio — exclusion is the realistic near-term output",
    fontsize=11.5,fontweight="bold",transform=ax.transAxes)
ax.text(0.03,-0.02,"LR tiers per ENFSI 2015 / NRC 2014. Tier 1 relies on equipment/supply-chain forensics that are NOT developed (§5). "
    "Tier 3 exclusion mirrors Crook et al. 2022 (X99=177 vs 299 winner).",fontsize=7.5,transform=ax.transAxes,color="#555")
fig.savefig("fig4_3_tiers.png"); plt.close(fig)
print("figures written:")
import os
for f in sorted(os.listdir(".")):
    if f.endswith(".png"): print("  ",f, os.path.getsize(f)//1024,"KB")
