class Tree:
    '''this is the class of Tree'''
    def __init__(self,cargo,left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)

class DecisionTree(Tree):
    """we define the decision tree based on the Tree"""
    def __init__(self,cargo,dataset,left = None,right = None):
        super().__init__(cargo,left,right)
        self.dataset = dataset
        """input of dataset is created"""
    def gini(self):
        """ method of calculating gini for each split of the data
        then return the splitting point with minimum gini
        also return the split data set """
        self.dataset = sorted(self.dataset)
        print(self.dataset)
        """sort the data set by the feature"""
        split = [0]*(len(self.dataset)-1)
        #print("The split is :",split)
        """creating a list saving splitting point"""
        for i in range(len(split)):
            """creating and saving splitting point"""
            split[i] = (self.dataset[i][0] + self.dataset[i+1][0])/2
            #print(split[i])
        response = [0]*len(self.dataset)
        """create a list to store response variables which are 0s and 1s"""
        for i in range(len(self.dataset)):
            response[i] = self.dataset[i][1]
        Gini = [0]*(len(split))
        """calculating gini for each split data set"""
        for i in range(len(Gini)):
            D = len(self.dataset)
            """total items in D"""
            D0 = i + 1
            D1 = D - D0
            """items in D0 and D1"""
            p1_D0 = sum(response[:i+1])/(i+1)
            p0_D0 = 1 - p1_D0
            p1_D1 = sum(response[i+1:])/(D - (i+1))
            p0_D1 = 1 - p1_D1
            print("p1_D0 = p0_D0= p1_D1= p0_D1=",p1_D0,p0_D0,p1_D1,p0_D1)
            """purity of D0 and D1"""
            Gini[i] = (D0/D) * (1 - p0_D0**2 - p1_D0**2) + (D1/D) * (1 - p0_D1**2 - p1_D1**2)
            print("Gini is",Gini)
            """calculation of gini"""

        for i in range(len(Gini)):
            """find out the split point and corresponding data set, which minimize the gini"""
            if Gini[i] == min(Gini):
                return [split[i],self.dataset[:i+1],self.dataset[i+1:]]








data = [[5,0],[7,0],[3,0],[6,1],[8,1]]
dt = DecisionTree(dataset=data,cargo = 0)
tree = Tree(None)

print(dt.gini())
