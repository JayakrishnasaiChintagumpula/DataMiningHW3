# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because agglomerative hierarchical clustering processes do not rely on the concept of centroids, outliers can be incorporated into the appropriate clusters during the hierarchical merging phase, making them more resilient against outliers."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Both k-means and agglomerative hierarchical clustering can produce different clusterings for the same dataset in different runs due to randomness in initialization and tie-breaking rules."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means is generally faster and requires less memory than agglomerative hierarchical clustering, but it's not always the most efficient clustering algorithm overall. Other algorithms, like DBSCAN, may be more suitable for certain datasets and tasks"

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "The change in SSE of a clustering cannot be determined solely by splitting a cluster in K-means. It depends on whether the new centroid improves the representation of the data points or not."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Decreasing SSE in K-means implies tighter clustering, which means increased cohesion within clusters"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "SSB (Sum of Squares Between) measures the variability between clusters in K-means clustering. When SSB increases, it means that the distance between cluster centroids increases, indicating greater separation between clusters. Therefore, when SSB increases, separation between clusters also increases"

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Improving cohesion (smaller SSE) in K-Means doesn't necessarily improve separation (larger SSB), as they measure different aspects of clustering: cohesion refers to intra-cluster similarity, while separation refers to inter-cluster dissimilarity"

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "(SST) remains constant throughout the clustering process. This is because it represents the total variance in the data, which doesn't change due to the algorithm's operations."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = " Increasing cohesion (lower SSE) doesn't guarantee increased separation (higher SSB). They are independent measures, and optimizing one doesn't necessitate improvement in the other."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Clusters are too far from the centroid, as seen in the picture, to draw points from other."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The clusters will contain points from both of the shaded zones because, as the picture illustrates, the shaded regions are close to one another."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since the 12.5 centroid is far from every point, every other cluster will eventually empty out."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a)+(b*b)+(c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2)+((R/2)^2))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since A and B have the same amount of distance and points, one centroid will be drawn in the direction of A. The two centroids are now on the right side of B. Despite the centroid's initial absence, Circle C, which has 100,000 points more than Circle B and is positioned similarly, is guaranteed to keep a centroid because of its higher attraction. Due to their comparable pulls, each centroid in A and B should be attracted by an even distribution of points."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Because of the current points in A and the lack of a greater pull, the centroid will remain at A. One centroid from B will be drawn in by a stronger pull from C. As a result, the centroids of all three circles will be 1, 1, 1."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid in circle A will get the points from circles B and A because they are near to each other but far from circle C. Two centroids will split up the points in C. Since the number of points in A and B are equal, the centroid in A will shift between the two. The centroids in C will remain in C with half of the points even though they will slightly diverge."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A", "Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since the leftmost point of B and the rightmost point of A have the smallest single link distance, group A and group B can be combined."

    # type: set
    answers["(b)"] = {"Group A", "Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since the rightmost point in Group A and the farthest point in Group C have the smallest complete link distance, the two groups can be combined."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {"B", "C", "E", "F", "I", "J", "L", "M"}

    # type: set
    answers["(a) boundary"] = {"D", "G"}

    # type: set
    answers["(a) noise"] = {"A", "H"}

    # type: set
    answers["(b) cluster 1"] = {"B", "C", "D", "E", "F", "G"}

    # type: set
    answers["(b) cluster 2"] = {"I", "J", "L", "M"}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {"B", "C", "D", "E", "F", "G", "I", "J", "L", "M"}

    # type: set
    answers["(c)-a boundary"] = {"A", "H"}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {"B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M"}

    # type: set
    answers["(c)-b cluster 2"] = {"A"}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the highest entropy among all(approx 2.5). This is because the categories are more evenly distributed"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has the least entropy among all(approx0.07). This is because there is unequal distribution in categories"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "There is a difference in blueness in terms of the contrast between the two diagonal entries, suggesting that clusters B and C have better cohesiveness than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "As the colors of non diagonal elements of row 1 and 3 are different we can consider cluster A and cluster C belong there respectively. Row 2 and 4 are corresponded to clusters B and D respectively. In both rows 2 and 4, the distance to A and C is the same and have the same colors in their respective rows."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "There is a difference in blueness in terms of the contrast between the two diagonal entries, suggesting that clusters B and C have better cohesiveness than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "The colors of the rows with less distinct diagonal entries vary, suggesting that the distances between these clusters and all other clusters are variable. Rows that have more distinct diagonal entries have two colors that are the same, meaning that they are far from one cluster and have the same distance from two clusters. "

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "There is a difference in blueness in terms of the contrast between the two diagonal entries, suggesting that clusters B and C have better cohesiveness than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "We can notice that every row in this matrix have 1 different color and other 2 matches. We can say that each cluster has two other clusters closer and one other cluster relatively farther  "

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "We can observe that the diagonal entry has less contrast blue color which indicates that the cluster is less cohesive. We can also observe that all non-diagonal elements have different colors which indicates all other clusters have different distances."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "We can observe that the diagonal entry has more contrast blue color when compared which indicates that the cluster is more cohesive. We can also observe that 2 non-diagonal elements have the same color(even though sharpness varies in A and C) which indicates 2 clusters are closer and D is the farthest."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "We can observe that the diagonal entry has more contrast blue color when compared which indicates that the cluster is more cohesive. We can also observe that 2 non-diagonal elements have the same color(even though sharpness varies in B and D) which indicates 2 clusters are closer and A is the farthest."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "We can observe that the diagonal entry has less contrast blue color which indicates that the cluster is less cohesive. We can also observe that all non-diagonal entries have different colors which indicates that all clusters have different distances(A is farther and C is closer)."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["Hierarchical", "Overlapping", "Partial"]

    # type: list
    answers["(b)"] = ["Partitional", "Exclusive", "Complete"]

    # type: list
    answers["(c)"] = ["Partitional", "Exclusive", "Complete"]

    # type: list
    answers["(d)"] = ["Hierarchical", "Overlapping", "Partial"]

    # type: list
    answers["(e)"] = ["Partitional", "Exclusive", "Complete"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Letter grades are discrete categories which makes them partitional. Each student can only receive one grade which is exclusive. Every student in the class will earn a grade which is complete."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "We can use DBSCAN to find clusters corresponding to the patterns represented by the nose, eyes, and mouth. DBSCAN can be used to find clustering for low and high-density areas and areas with arbitrary shapes."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means is generally more suitable for identifying clusters in datasets where clusters have a relatively uniform density, rather than datasets with varying density regions but, we can use K-means in higher density areas if clusters are compact and well separated."

    # type: string
    answers["(c)"] = "I would prefer DBSCAN clustering because it can be used in higher and lower density areas and can be used even if there are irregular shapes"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
