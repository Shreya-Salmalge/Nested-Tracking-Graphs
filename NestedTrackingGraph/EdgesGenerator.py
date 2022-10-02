import pickle

inputpath = "./nodes/"

def connectedComponents(comp1, comp2):
    edges = set()
    for i in range(len(comp1)):
        if(comp1[i]>0 and comp2[i]>0):
            edges.add((comp1[i],comp2[i]))
    return edges


#NESTING TREE
def createNestedTrees():
    EdgesN = set()
    for timestep in range(41,45):
        inputFile = inputpath+"nodes_t"+str(timestep)+".pickle"
        pickle_in = open(inputFile,"rb")
        nodes_in_timestep = pickle.load(pickle_in)
        pickle_in.close()

        comp1 = nodes_in_timestep["componentMatrix1"]
        comp2 = nodes_in_timestep["componentMatrix2"]
        comp3 = nodes_in_timestep["componentMatrix3"]

        #level 1 and level 2 - connected components
        edges_l1_l2 = connectedComponents(comp1, comp2)

        #level 2 and level 3
        edges_l2_l3 = connectedComponents(comp2, comp3)
        
        for (p1,p2) in list(edges_l1_l2):
            id1 = "t"+str(timestep)+"_l1_"+str(p1)
            id2 = "t"+str(timestep)+"_l2_"+str(p2)
            EdgesN.add((id1,id2))
        
        for (p1,p2) in list(edges_l2_l3):
            id1 = "t"+str(timestep)+"_l2_"+str(p1)
            id2 = "t"+str(timestep)+"_l3_"+str(p2)
            EdgesN.add((id1,id2))
    return EdgesN

#TRACKING GRAPH
def createTrackingTree():
    EdgesT = set()
    inputFile1 = inputpath+"nodes_t41.pickle"
    pickle_in = open(inputFile1,"rb")
    nodes_in_timestep1 = pickle.load(pickle_in)
    pickle_in.close()

    for timestep in range(42,45):
        inputFile = inputpath+"nodes_t"+str(timestep)+".pickle"
        pickle_in = open(inputFile,"rb")
        nodes_in_timestep2 = pickle.load(pickle_in)
        pickle_in.close()

        #level 1
        t1_comp = nodes_in_timestep1["componentMatrix1"]
        t2_comp = nodes_in_timestep2["componentMatrix1"]
        edgesL1_t1_t2 = connectedComponents(t1_comp, t2_comp)

        #level 2
        t1_comp = nodes_in_timestep1["componentMatrix2"]
        t2_comp = nodes_in_timestep2["componentMatrix2"]
        edgesL2_t1_t2 = connectedComponents(t1_comp, t2_comp)

        #level 3
        t1_comp = nodes_in_timestep1["componentMatrix3"]
        t2_comp = nodes_in_timestep2["componentMatrix3"]
        edgesL3_t1_t2 = connectedComponents(t1_comp, t2_comp)

        
        for (p1,p2) in list(edgesL1_t1_t2):
            id1 = "t"+str(timestep-1)+"_l1_"+str(p1)
            id2 = "t"+str(timestep)+"_l1_"+str(p2)
            EdgesT.add((id1,id2))
        
        for (p1,p2) in list(edgesL2_t1_t2):
            id1 = "t"+str(timestep-1)+"_l2_"+str(p1)
            id2 = "t"+str(timestep)+"_l2_"+str(p2)
            EdgesT.add((id1,id2))

        for (p1,p2) in list(edgesL3_t1_t2):
            id1 = "t"+str(timestep-1)+"_l3_"+str(p1)
            id2 = "t"+str(timestep)+"_l3_"+str(p2)
            EdgesT.add((id1,id2))

        nodes_in_timestep1  = nodes_in_timestep2
    return EdgesT
