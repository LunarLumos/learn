Got it ✅ — I’ll explain this in **extra detail** so it’s as beginner-friendly as possible,
with **small steps, examples, and a visual way to check your understanding**.

---

## **1. What This Code Does**

This is an implementation of **Dijkstra’s shortest path algorithm**.
It finds the *shortest distance from a starting point to all other points* in a network (graph).

Think of the **graph** as a **map**:

* Locations = **nodes** (like Admission Office, Food Court, GYM…)
* Roads = **edges** (like “AB-4 to Food Court costs 13”)

---

## **2. Imports and Comments**

```python
#Bismillahir_Rahmanir_Rahim   # Opening line in Arabic, "In the name of Allah..."
# dijkstra                    # Name of the algorithm
#O((V + E) log V)              # The time complexity

import heapq
```

* **heapq**: lets us use a **priority queue** → a structure that always gives us the smallest item first.
* This is important because Dijkstra needs to always explore the **closest location** next.

---

## **3. The Function Header**

```python
def dijkstra(graph, start):
```

* **graph** → dictionary of `{node: [(neighbor, weight), ...]}`
* **start** → where we begin the search.

---

## **4. Step 1 — Set All Distances to Infinity**

```python
distances = {node: float('inf') for node in graph}
distances[start] = 0
```

* We don’t know distances yet → so we set all to **∞** (infinity).
* But the **start node’s distance = 0** (because it’s zero steps from itself).

Example after this step (starting at `"Admission_Office"`):

```python
{
  'Admission_Office': 0,
  'AB-4': inf,
  'Green_Garden': inf,
  'Food_Court': inf,
  ...
}
```

---

## **5. Step 2 — Priority Queue Initialization**

```python
priority_queue = [(0, start)]
```

* A **list** that heapq will treat like a min-heap.
* Stores `(distance, node)` pairs.
* Starts with `(0, 'Admission_Office')`.

---

## **6. Step 3 — Main Loop**

```python
while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)
```

* **while priority\_queue** → keep going until we have no more nodes to check.
* **heapq.heappop** removes the smallest distance node from the queue.

Example first loop:

```
current_distance = 0
current_node = 'Admission_Office'
```

---

## **7. Step 4 — Skip Outdated Distances**

```python
if current_distance > distances[current_node]:
    continue
```

* If we already found a **shorter path** to this node earlier, skip it.
* This avoids wasted work.

---

## **8. Step 5 — Visit Neighbors**

```python
for neighbor, weight in graph[current_node]:
    distance = current_distance + weight
```

* Go through each connected location (`neighbor`) from the current node.
* **weight** = distance to that neighbor.
* `distance` = distance so far + this road’s cost.

Example from `"Admission_Office"`:

```
Neighbor: 'AB-4', weight: 3 → distance = 0 + 3 = 3
Neighbor: 'Green_Garden', weight: 9 → distance = 0 + 9 = 9
```

---

## **9. Step 6 — Update Shortest Path if Better**

```python
if distance < distances[neighbor]:
    distances[neighbor] = distance
    heapq.heappush(priority_queue, (distance, neighbor))
```

* If the new path is shorter than the recorded one:

  1. Update it in `distances`.
  2. Push `(distance, neighbor)` into the queue to explore later.

Example after first loop:

```
distances = {
  'Admission_Office': 0,
  'AB-4': 3,
  'Green_Garden': 9,
  ...others = inf
}
priority_queue = [(3, 'AB-4'), (9, 'Green_Garden')]
```

---

## **10. Step 7 — Finish**

```python
return distances
```

* After all reachable nodes are visited, return the dictionary with shortest paths.

---

## **11. Graph Example**

Here’s a simpler way to picture the **graph**:

```
Admission_Office --3--> AB-4 --13--> Food_Court --5--> GYM
    \                                  ↑         |
     \                                 8         8
      9                               Medical_Center
       \                             /
        v                          /
     Green_Garden --6--> Central_Mosque --2--> AB-1 --1--> Innovation_LAB --12--> R/A_Hall --15--> YKG_2 --7--> Engineering_Building
```

---

## **12. Code Output Example**

If you run:

```python
start_node = 'Admission_Office'
shortest_distances = dijkstra(graph, start_node)

for node, dist in shortest_distances.items():
    print("Distance from node", start_node, "to node", node, "is", dist)
```

You might get something like:

```
Distance from node Admission_Office to node Admission_Office is 0
Distance from node Admission_Office to node AB-4 is 3
Distance from node Admission_Office to node Green_Garden is 9
Distance from node Admission_Office to node Food_Court is 16
Distance from node Admission_Office to node GYM is 21
...
```

---

If you want, I can **make a step-by-step table** showing exactly how the priority queue changes in each round of Dijkstra’s run for this graph.
That will make it *super* easy to check your understanding.

Do you want me to prepare that table?
