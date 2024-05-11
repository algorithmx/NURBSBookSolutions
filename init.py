import sys
import os

problems = {
    "Ch{ch:02d}".format(ch=c) : ["Q{t:02d}.{x:02d}".format(t=c,x=i+1) for i in range(0,q)] 
    for c,q in [(1,24), (2,9), (3,10), (4,6), (5,5), (6,7), (7,6), (9,3)]
}

for ch, qs in problems.items():
    if not os.path.exists(ch):
        os.mkdir(ch)
    for q in qs:
        if not os.path.exists(os.path.join(ch, q)):
            os.mkdir(os.path.join(ch, q))
        if not os.path.exists(os.path.join(ch, q, q+".md")):
            with open(os.path.join(ch, q, q+".md"), "w") as f:
                f.write("# {q}\n\n".format(q=q))
                f.write("## Question\n\n")
                f.write("## Solution\n\n")
                f.write("## Reference\n\n")


