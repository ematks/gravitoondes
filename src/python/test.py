import ROOT
import numpy as np
import matplotlib.pyplot as plt


ROOT.ROOT.EnableImplicitMT()

root_file = ROOT.TFile("/home/ducoin/gravitational-waves.git/data/GW150914/h1.data.00.root","open")
#print("root_file =", root_file)

Tgraph = root_file.Get("data")
#Tgraph = ROOT.Tgraph("/home/ducoin/gravitational-waves.git/data/GW150914/h1.data.00.root")
#print("Tgraph =", Tgraph)


x_buff = Tgraph.GetX()
y_buff = Tgraph.GetY()
#print("x_buff =", x_buff)
#print("y_buff =", y_buff)

#N = Tgraph.GetN()
#x_buff.SetSize(N)
#y_buff.SetSize(N)

x_arr = np.array(x_buff)
y_arr = np.array(y_buff)

print("x_arr =", x_arr)
print("y_arr =", y_arr)



plt.plot(x_arr,y_arr)
plt.show()


