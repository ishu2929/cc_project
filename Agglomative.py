#agglomerative
data = []
with open("distance_matrix.txt", "r") as file:
    for line in file:
        values = line.strip().split()
        int_values = []
        for value in values:
            int_values.append(int(value))
        data.append(int_values)

n = len(data)
clusters = [[i] for i in range(n)]
#print(f"Initial Clusters: {[c+1 for c in clusters]}")
while len(clusters) > 1:
    min_distance = 9999 
    to_merge = (-1, -1) 
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            current_min_distance = 9999  

            for a in clusters[i]:
                for b in clusters[j]:
                    distance = data[a][b]
                    if distance < current_min_distance:
                        current_min_distance = distance
            if current_min_distance < min_distance:
                min_distance = current_min_distance
                to_merge = (i, j)
    c1, c2 = to_merge
    new_cluster = clusters[c1] + clusters[c2]
    clusters = [clusters[k] for k in range(len(clusters)) if k != c1 and k != c2]
    clusters.append(new_cluster)
    print(f" Current clusters: {[c + 1 for c in clusters]}")
print(f"Final cluster: {[x + 1 for x in clusters[0]]}")