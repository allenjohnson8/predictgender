from sklearn import tree
X=[[173,52,7],[174,75,9],[164,50,6],[158,70,8],[135,58,6],[158,70,7],[162,61,7],[173,70,8],[170,68,9],[168,49,9],[170,58,10],[172,58,10]]
Y=['male','male','female','male','male','female','female','male','male','male','male','male']  
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediction=clf.predict([[156,23,11]])
print(prediction)