import sys
import pandas as pd

OUT = sys.stdout

df = pd.read_csv(sys.argv[1])
df.to_csv(OUT, index=False, line_terminator='\n')

for i in sys.argv[2:]:
    df = pd.read_csv(i)
    df.to_csv(OUT, index=False, mode='a', header=False, line_terminator='\n')
