import glob
f = open("images.json", "w")
a = glob.glob("*.png")
a.sort()
for i in a[9:]: print('  {\n    "id": "'+i[:4]+'",\n    "val": "'+i+'"\n  },', file=f)
