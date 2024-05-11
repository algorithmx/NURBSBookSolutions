import sys
import os

problems = {
    "Ch{ch:02d}".format(ch=c) : ["Q{t:02d}.{x:02d}".format(t=c,x=i+1) for i in range(0,q)] 
    for c,q in [(1,24), (2,9), (3,10), (4,6), (5,5), (6,7), (7,6), (9,3)]
}

joint_md_str = 'Solutions to The NURBS Book (2nd ed.)\n===\n\n'

for ch, qs in problems.items():
    assert os.path.exists(ch)
    for q in qs:
        assert os.path.exists(os.path.join(ch, q))
        assert os.path.exists(os.path.join(ch, q, q+".md"))
        with open(os.path.join(ch, q, q+".md"), "r") as f:
            joint_md_str += f.read()
            joint_md_str += '\n\n'

with open("The_NURBS_Book.md", "w") as f:
    f.write(joint_md_str)
