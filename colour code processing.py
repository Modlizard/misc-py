while True:
	tag = input("Enter tag (if it has spaces do one part at a time without the space):")
	tag = tag.replace("&x", "")
	tag = tag.replace("&", "")
	out = ""
	for x in range(0,len(tag),7):
		out += f'<span style="color:#{tag[x:x+6]};">{tag[x+6]}</span>'

	print(out)

"""
Efficiency
for x in range(1,26):
	print(f"|-\n| {x} || {610-10*x} || ${1000*x} || {round(3600.0/(610-10*x), 2)} || {round(86400.0/(610-10*x), 2)}")

trash reduction
for x in range(0,26):
	print(f"|-\n| {x+1} || {30-x}% || ${500*(x+1)} || {40 + 0.5*x}% || {29 + 0.5*x}% || 1%")

discovery
for x in range(0,9):
	print(f"|-\n| {x+1} || {1+0.5*x}% || ${500*(x+1)} || {30-0.5*x}% || 40% || 29%")

durability 
level | degred/sec | cost | health after 1h | health after 1d | time until 0 
from datetime import timedelta
for x in range(1,10):
	print(f"|-\n| {x} || {round(0.001/x,6)}% || ${750*x} || {round(100-(3600*(0.001/x)),4)}% || {round(100-(86400*(0.001/x)),4)}% || {timedelta(seconds = 100000*x)} ({100000*x}s)") # 100/(0.001/x) = 100000*x

luck
for x in range(1,21):
	print(f"|-\n| {x} || {round(1+0.2*x, 1)}% || ${500*x} || {round(55-0.2*x, 1)}% || 30% || 10% || 4%")

scale
for x in range(1,21):
	print(f"|-\n| {x} || {round(0.02+0.2*x, 2)}% || ${500*x} || {round(20-0.2*x, 2)}% || 40% || 30% || 9.98% ")
"""
# Figure out if luck is 55% common 30% rare or 65% common 20% rare
# Ask about pets not listed on /pets 
# Trap offline rate/restriction