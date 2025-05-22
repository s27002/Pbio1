from Bio import Entrez, SeqIO
import pandas as p, matplotlib.pyplot as m

i=input
Entrez.email=i("email: ")
Entrez.api_key=i("api-key: ")
t=i("taxid: ")
a,b=map(int,(i("min len: "),i("max len: ")))
n=int(i("max rec: "))
s=Entrez.esearch(db="nucleotide",term=f"txid{t}[Organism]",usehistory="y")
d=Entrez.read(s)
c=int(d["Count"])
print(c,"rec")
w,q=d["WebEnv"],d["QueryKey"]
r=[]
x=500
for s in range(0,min(c,n),x):
 h=Entrez.efetch(db="nucleotide",rettype="gb",retmode="text",retstart=s,retmax=min(x,n-s),webenv=w,query_key=q)
 r+=[{"a":z.id,"l":len(z.seq),"d":z.description}for z in SeqIO.parse(h,"genbank")if a<=len(z.seq)<=b]
df=p.DataFrame(r)
df.to_csv(f"t{t}.csv",index=0)
df=df.sort_values("l",ascending=0)
m.figure(figsize=(12,6))
m.plot(df["a"],df["l"],marker='o')
m.xticks(rotation=90,fontsize=8)
m.tight_layout()
m.savefig(f"t{t}.png")
