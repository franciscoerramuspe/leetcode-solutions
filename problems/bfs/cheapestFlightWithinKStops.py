'''
There are n cities connected by some number of flights.
                                                    mvd   bsas   300
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

en criollo: salimos de src, queremos llegar a dst, haciendo como mucho k escalas. devolver el precio (si es que existe) mas barato de src a dst

k=2                 0

                    MVD
                100 / \200
                   /   \
                BSAS    SPO
            500 /         \1000
               /           \
            SGO              PDE
        100/
           /
          PDE


mvd-> bsas-> sgo -> pde: 700, k=1
mvd-> spo -> pde: 1200

we start at point src
we have to get to k with at most k stops
that means, we have to find the cheapest path from src to dst with at most k stops
if we cannot find a path from src to dst with at most k stops, return -1
else return total price


do bfs from src
add its neighbors to a min heap, sorting by the cost to getting to the neighbor
visit the cheapest one, reduce k by one, and add the neighbors of that node to the queue
if you are able to get to src 
'''
# primer intento
# from collections import defaultdict, deque
# import heapq
# def cheapestFlightWithinKStop(flights, src, dst, k):
#     queue=deque((0, src))
#     maxLayovers=k+1
#     totalPrice=0
#     graph = defaultdict(list)
#     minRoutes=[]
#     heapq.heapify(minRoutes)
    
#     for source, destination, p in flights:
#         priceToDestination=set((destination, p))
#         graph[source].append(priceToDestination)

#     while queue:
#         price, city= queue.pop(0) # (100, BSAS), (200, SPO)
#         if city == destination and maxLayovers >= 0:
#             # encontramos una ruta posible
#             minRoutes.append(totalPrice)

#         totalPrice+=price
#         for neighbor in graph[city]:
#             nextDestination, destinationPrice= neighbor
#             queue.append((destinationPrice, nextDestination))
#         maxLayovers-=1

#segundo intento (luego de ver la teoria de bellman ford algorithm)
def cheapestFlightWithinKStop( n, flights, src, dst, k):
    prices=[float('inf')]* n
    prices[src]=0  

    for i in range(k+1):
        tempPrices=prices.copy()
        
        for s, d, p in flights:
            if prices[s] == float('inf'):
                continue
            if prices[s] + p < tempPrices[d]:
                tempPrices[d] =prices[s] + p
        prices=tempPrices
    return prices[dst] if prices[dst]!= float('inf') else -1



print(cheapestFlightWithinKStop([[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1, 3))