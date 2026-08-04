import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"font.family":"DejaVu Sans","axes.spines.top":False,
    "axes.spines.right":False,"figure.dpi":150,"savefig.dpi":150,"savefig.bbox":"tight"})
COL={"col":"#2166AC","photo":"#B2182B","enz":"#1B7837","echem":"#762A83","dep":"#888888","paper":"#BBBBBB"}

# ============ FIG 4.5  MEASURED PHENOTYPES (4 chemistries) ============
fig,ax=plt.subplots(1,2,figsize=(11.5,4.4))
# (a) deletion-rate ladder across measured methods/vendors (log x)
a=ax[0]
rows=[("Twist deposition",0.044,"dep","ours"),
      ("Sigma (column)",0.080,"col","ours"),
      ("IDT (column)",0.207,"col","ours"),
      ("BioSearch (column)",0.382,"col","ours"),
      ("Eurofins (column)",0.491,"col","ours"),
      ("Genscript electrochem.",0.835,"echem","ours"),
      ("Enzymatic TdT (Palluk)",1.3,"enz","pub"),
      ("Photolithographic (Lietard)",3.41,"photo","ours")]
rows=sorted(rows,key=lambda r:r[1])
y=np.arange(len(rows))
a.barh(y,[r[1] for r in rows],color=[COL[r[2]] for r in rows],
       edgecolor=["none" if r[3]=="ours" else "#333" for r in rows],
       hatch=["" if r[3]=="ours" else "//" for r in rows])
a.set_yticks(y); a.set_yticklabels([r[0] for r in rows],fontsize=8.5)
a.set_xscale("log"); a.set_xlabel("deletion rate (%/nt, log scale) — MEASURED")
for i,r in enumerate(rows): a.text(r[1]*1.08,i,f"{r[1]:.3f}",va="center",fontsize=7.5)
a.set_xlim(0.03,6)
a.set_title("(a) Deletion burden spans ~80× across methods",fontweight="bold",fontsize=10)
a.text(0.98,0.02,"solid = our reprocessing · hatched = published (Palluk)",transform=a.transAxes,
       ha="right",fontsize=7,color="#555")
# (b) substitution direction
b=ax[1]
lab=["Column\n(Masaki)","Photolithographic\n(Lietard)"]; ga=[0.11,0.100]; gt=[0.03,0.279]
x=np.arange(2); w=0.36
b.bar(x-w/2,ga,w,color="#2166AC",label="G→A"); b.bar(x+w/2,gt,w,color="#B2182B",label="G→T")
b.set_xticks(x); b.set_xticklabels(lab); b.set_ylabel("substitution rate (%/nt)")
b.set_title("(b) Substitution direction: column G→A vs photolith. G→T",fontweight="bold",fontsize=9.5)
b.legend(fontsize=9,frameon=False); b.set_ylim(0,0.34)
b.annotate("G→A\ndominant",xy=(-w/2,0.11),xytext=(-0.46,0.19),fontsize=8,color="#2166AC",fontweight="bold")
b.annotate("G→T\ndominant",xy=(1+w/2,0.279),xytext=(0.72,0.30),fontsize=8,color="#B2182B",fontweight="bold")
fig.suptitle("Figure 4.5  Four synthesis chemistries, four measured error fingerprints (reproduced from deposited reads)",
             fontweight="bold",fontsize=10.5,y=1.02)
fig.savefig("fig4_5_phenotypes.png"); plt.close(fig)

# ============ FIG 4.6  MEASURED ATTRIBUTION + SCORECARD ============
fig,ax=plt.subplots(1,2,figsize=(11.5,4.4))
a=ax[0]
tasks=["Cross-chemistry\n4-class (atlas)","Masaki capping\nAc2O vs Pac2O","Masaki capping\nmech. (3-cls)","Filges 4-manuf.\n(leave-lot-out)","Filges IDT vs Sigma\n(leave-lot-out)"]
acc=[100,100,76.9,19.4,72.2]; chance=[25,50,33.3,25,50]; sig=["p≈.01","p≈.01","","ns (1 lot ea.)","p≈.05"]
x=np.arange(5)
solid="#2166AC"; weak="#c9a0a0"
bars=a.bar(x,acc,0.62,color=[solid,solid,solid,weak,weak])
for j in (3,4): bars[j].set_hatch("//")
a.plot(x,chance,"_",ms=22,mew=2.5,color="#B2182B",label="chance")
for i in range(5):
    a.text(i,acc[i]+2,f"{acc[i]:.0f}%",ha="center",fontsize=8.5,fontweight="bold")
    a.text(i,6,sig[i],ha="center",fontsize=7,color="#333")
a.set_xticks(x); a.set_xticklabels(tasks,fontsize=7.0); a.set_ylabel("leave-group-out balanced accuracy (%)"); a.set_ylim(0,112)
a.set_title("(a) Attribution from error phenotype — measured",fontweight="bold",fontsize=9.5)
a.legend(fontsize=8,frameon=False,loc="upper right")
a.text(0.5,-0.30,"Solid = significant. Hatched = within-column vendor tasks under leakage-safe leave-one-lot-out:\n4-vendor is data-limited (Eurofins/BioSearch have 1 lot each); IDT-vs-Sigma ~72% is borderline. Cross-chemistry is the strong result.",
       transform=a.transAxes,ha="center",fontsize=6.6,color="#555")
# (b) scorecard ours/paper
b=ax[1]
names=["Masaki\ncapping","Masaki\nda7G","Masaki\na8da7G","Lietard\ncap→G→T","Filges IDT\ndel","Gimpel\ndeposition del","Gimpel\ne/d ratio"]
ours=[12.2,10,59,3.6,0.207,0.044,18.8]; paper=[13,10,50,4.5,0.20,0.06,23]
rel=[ours[i]/paper[i] for i in range(len(ours))]
xx=np.arange(len(names))
b.axhspan(0.8,1.2,color="#DFF0D8",zorder=0); b.axhline(1,ls="--",color="#333",lw=1)
b.bar(xx,rel,0.55,color="#B2182B")
for i in range(len(names)): b.text(i,rel[i]+0.03,f"{ours[i]:g}\nvs {paper[i]:g}",ha="center",fontsize=7)
b.set_xticks(xx); b.set_xticklabels(names,fontsize=7); b.set_ylabel("our value ÷ published"); b.set_ylim(0,1.5)
b.set_title("(b) Reproduction scorecard: measured vs published",fontweight="bold",fontsize=9.5)
fig.suptitle("Figure 4.6  From proof-of-concept to proof: measured attribution and reproduced rates across four chemistries",
             fontweight="bold",fontsize=10,y=1.02)
fig.savefig("fig4_6_measured.png",bbox_inches="tight",dpi=150); plt.close(fig)

# ============ FIG 4.7  GIMPEL electrochemical vs deposition ============
fig,ax=plt.subplots(1,2,figsize=(11,3.8))
a=ax[0]
x=np.arange(2); w=0.36
ours=[0.835,0.044]; paper=[1.35,0.06]
a.bar(x-w/2,ours,w,color=["#762A83","#888888"],label="our reprocessing")
a.bar(x+w/2,paper,w,color="#CCCCCC",label="Gimpel 2023")
a.set_yscale("log"); a.set_xticks(x); a.set_xticklabels(["electrochemical\n(Genscript)","deposition\n(Twist)"])
a.set_ylabel("deletion rate (%/nt, log)"); a.set_ylim(0.02,3)
a.legend(fontsize=8,frameon=False,loc="upper right")
a.set_title("(a) Deletion rate: electrochemical ≫ deposition",fontweight="bold",fontsize=9.5)
a.text(0.5,0.86,"18.8× class ratio\n(paper ~23×)",transform=a.transAxes,ha="center",fontsize=9,fontweight="bold",color="#762A83")
# (b) positional gradient
b=ax[1]
ech=np.array([39241,52775,50193,46791,53594,69300,65848,71080,83921,37041],dtype=float)
ech_n=ech/ech.sum()
xx=np.arange(10)
b.plot(xx,ech_n,"-o",ms=4,color="#762A83",label="electrochemical (Genscript)")
b.plot(xx,[0.1]*10,"-s",ms=4,color="#888888",label="deposition (Twist), ~flat")
b.axvspan(8.5,9.5,color="#FFF3B0",zorder=0)
b.set_xticks(xx); b.set_xlabel("position decile (design 3'→5')"); b.set_ylabel("fraction of deletions")
b.set_title("(b) Electrochemical 5'-ward deletion gradient",fontweight="bold",fontsize=9.5)
b.legend(fontsize=7.5,frameon=False,loc="upper left")
b.text(4.5,0.083,"electrochemical rises toward 5'\n(2.1× peak/first-decile)",fontsize=8,color="#762A83",fontweight="bold",ha="center")
b.text(9,0.02,"3' primer\n(PCR-clean)",fontsize=6.5,ha="center",color="#555")
fig.suptitle("Figure 4.7  Electrochemical vs material-deposition synthesis (Gimpel et al. 2023, ENA PRJEB65931)",
             fontweight="bold",fontsize=10.5,y=1.05)
fig.savefig("fig4_7_gimpel.png"); plt.close(fig)
print("wrote fig4_5, fig4_6, fig4_7")
