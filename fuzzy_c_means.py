
import random

def create_membership_matrix(pixels: list[int], c):
    deg = []
    target = 1.0

    for _ in pixels:
        cluster = []
        reste = target

        for _ in range(c - 1) :
            deg_c = random.uniform(0, reste)
            cluster.append(deg_c)
            reste =reste - deg_c

        cluster.append(reste)
        deg.append(cluster)
    return deg

def calculate_centroids(test, m, pixels, c):
    cluster_result =[]
    if m <= 1:
         raise ValueError("m doit etre > 1")
    
    
    for x in range(c):
        num = 0.0
        denum = 0.0
        for i in range(len(test)): 
            num += (test[i][x])**m * pixels[i]
            denum += (test[i][x])**m
            
        total = num / denum 
        cluster_result.append(total)
    return cluster_result


def update_matrix(pixels, test2, m):
    result = []

    for i in range(len(pixels)):
        distances = []

        for center in test2:
            d = abs(pixels[i] - center)
            distances.append(d)



        if distances[0] == 0:
            u1 = 1 
            u2 = 0
        elif distances[1] == 0:
            u1 = 0 
            u2 = 1
        else:
            u1 = 1 / (1 + (distances[0]/distances[1])**(2/(m-1)))
            u2 = 1 - u1
        
        result.append((u1,u2))
    return result


def stop_criteria(u_old, u_new):
    diff = []
    for i in range(len(u_old)):

        for e in range(len(u_new[i])):
            r = abs(u_old[i][e] - u_new[i][e])
            diff.append(r)
    return max(diff)

def fuzzy_c_means(pixels,c, m=2, epsilon=0.01):
    U = create_membership_matrix(pixels,c)

    max_iter = 100
    iteration = 0
    while True:
        if iteration >= max_iter:
            print("limite atteinte")
            break
        iteration += 1
        cj = calculate_centroids(U, m, pixels, c)
        U_new = update_matrix(pixels, cj, m)
        delta = stop_criteria(U, U_new)
        U = U_new

        if delta < epsilon:
            break
    cj = calculate_centroids(U, m, pixels, c)
    return U, cj
