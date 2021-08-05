from TransformerLib import *
TransLib=TransformerLib()
#print(TransLib.EMF)
#print(TransLib.Eff)
#print(TransLib.Regulation)


TransLib.TransformerEMF(50, 200, 1)
print(f'EMF = {TransLib.EMF:.2f}')

TransLib.TransformerRegulation(4, 1)
print(f'Regulation = {TransLib.Regulation:.2f}')


TransLib.TransformerEfficiency(4, 1, 2)
print(f'Efficiency = {TransLib.Eff:.2f}')
