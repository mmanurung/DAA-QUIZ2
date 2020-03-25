import networkx as nx
import matplotlib.pyplot as plt
import sys

#Fungsi utility -> mengembalikan vertex jarak minimum
def minDistance(dist, sptSet, V): #cari minimum dist
  min = sys.maxsize #taro nilai numerik terbesar ke min, nanti diupdate trs sampe dpt minimum
  for v in range(V): #shortest path tree
    if dist[v] <= min and sptSet[v] == False:
      min = dist[v]
      min_index = v
  return min_index

#fungsi dijkstra pada grafik G, dengan sumber (src) vertex sebagai sumber
def dijkstra(G, src, pos):
  V = len(G.nodes()) #V = jmlh simpul dlm grafik G
  dist = [] #dist[i] utk jarak terdekat dari sumber ke i
  parent = [None]*V #parent[i] nyimpan node drmn i dicapai di jalur terpendek dari sumber
  sptSet = [] #sptSet[i] -> True jika node i termasuk dalam tree jalur terpendek
  for i in range(V): #inisial awal untuk setiap node
    dist.append(sys.maxsize) #dist[] kasih nilai max
    sptSet.append(False) #sptSet[] kasih False
  dist[src] = 0
  parent[src]= -1 #src = root dan tdk punya induk
  for count in range(V-1):
    u = minDistance(dist, sptSet, V) #pilih titik jarak min dari set vertex
    sptSet[u] = True
    #update vrtex2 yang berdekatan dengan vertex yang dipilih
    for v in range(V):
      if (u, v) in G.edges():
        if sptSet[v] == False and dist[u] != sys.maxsize and dist[u] + G[u][v]['length'] < dist[v]:
          dist[v] = dist[u] + G[u][v]['length']
          parent[v] = u
	#tandai jalur terpendek dari sumber ke tiap vertex dgn warna merah pake parent[]
  for X in range(V):
    if parent[X] != -1: #abaikan induk
      if (parent[X], X) in G.edges():
        nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
  return

#ambil input dari file utk buat grafik
def CreateGraph(): #BRT MASIH ADO SALAH DI SINI!!!
  G = nx.DiGraph()
  f = open('/content/drive/My Drive/input.txt') #simpen di drive
  n = int(f.readline())
  wtMatrix = []
  for i in range(n):
    list1 = list(map(int, (f.readline()).split())) # ERROR DONE DI SINI
    wtMatrix.append(list1)
  src = int(f.readline()) #sumber vertex untuk algoritma dijkstra
  #tambahkan egdes beserta bobotnya ke grafik
  for i in range(n) :
    for j in range(n) :
      if wtMatrix[i][j] > 0 :
        G.add_edge(i, j, length = wtMatrix[i][j]) 
  return G, src

#gambar grafik dan tampilkan bobot
def DrawGraph(G):
  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels = True)  #with_labels = true -> menampilkan nomor vertex dalam grafik
  edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #print weight
  return pos

#main function
if __name__ == "__main__":
  print("Visualizing a Dijkstra's Graph")
  print("Here the red edges denote the shortest path from source node to the rest of the nodes: ")
  G, src = CreateGraph() #??? ERROR MASIH
  pos = DrawGraph(G)
  dijkstra(G, src, pos)
  plt.show()