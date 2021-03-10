
# python program 
# marklist analysis
# create function
def marks(X):
    Name=input("Enter the name - : "  )
    PRN=input("Enter the PRN - : ")
    print("pleas enter the marks :")
    P=int(input("Probability theory :- "))
    P1=int(input("internal mark(Probability theory)  :- "))
    T=int(input("Theory of testing hypothesis :- "  ))
    T1=int(input("internal mark(Theory of testing hypothesis) :- "))
    M=int(input("Multivariate analysis  :- "  ))
    M1=int(input("internal mark(Multivariate analysis):- "))
    L=int(input("Linear Models and Design of experiments :- "))
    L1=int(input("internal mark(Linear Models and Design of experiments) :- "))
    S=int(input("Sampling theory  :- "))
    S1=int(input("internal mark(Sampling theory)  :- "))
    p=int(input("Practical Exam  :- "))
    p_code=['69802',"-",'69803',"-",'69804',"-",'69805',"-",'69806',"-",'69807']   
    a=[32,8,32,8,32,8,32,8,32,8,80]
    print("Name :-",str(Name))
    print("University PRN  :-",PRN )
    print("College: S.G.M.Karad")
    print("Branch : Statistics (CBCS)")
    print("Seat NO : ",X)
    print("Exam center: S.G.M.karad")
    print("M.SC.Part I ")
    Mark=[P,P1,T,T1,M,M1,L,L1,S,S1,p]
    import numpy as np
    mark=np.array(Mark)
    h= mark.cumsum()
    aa=np.array([80,20,80,20,80,20,80,20,80,20,100])
    g=[P+P1,'-',T+T1,'-',M+M1,'-',L+L1,'-',S+S1,'-',p]
    j=[100,'-',100,'-',100,'-',100,'-',100,'-',100]
    per=(mark/aa)*100
    pas=[]
    for i in range(0,11):
        if i%2==0 and i!=10:
            if Mark[i]>=32:
                pas.append("pass")
            else:
                pas.append("false")
        if i==10:
            if Mark[i]>=40:
                pas.append("pass")
            else:
                pas.append("false")       
        if i%2!=0:
            if Mark[i]>=8:
                pas.append("pass")
            else:
                pas.append("false")   
    import pandas as pd
    D=pd.DataFrame({'Paper_Code':p_code,'Subject_Name':['Probability Theory','internal_1','testing Hypothesis',
                                                     'internal_2','Multivariate analysis','internal_3',
                                                    'Linear Model','internal_4','Sampling Theory',
                                                    'internal_5','Practical I'],
                    'Type':['TH','TW','TH','TW','TH','TW','TH','TW','TH','TW','TH'],
                    'paper_mark':aa,'Passing':a,'Marks':Mark,'__%__':per,'subject_total_mark':j,'Subject_marks':g,'cumsum':h,'result':pas})
    
    a=len(D[D['result']=='false'])
    v=[]
    if a<=4 and a!=0:
        v.append('pass-ATKT')
    if a==0:
        v.append('pass-(all clear)')
    if a>4:
        v.append('False')
    print("final Result =",v)
    print("back_subject : ",a)
    avg=sum(Mark)/6
    print("Total = ",sum(Mark))
    print("Percentage = ",avg,"%")
    print(D['Marks'].describe())
    import matplotlib.pyplot as plt
    plt.bar(p_code,Mark)
    plt.title("BAR CHART OF YOUR MARKS")
    plt.ylabel("MARKS")
    plt.xlabel("SUBJECTE CODE")
    plt.show()
    print(D)
    a1=[P+P1,T+T1,M+M1,L+L1,S+S1,p]
    a2=['69802','69803','69804','69805','69806','69807'] 
    A=['c','m','r','k','b','y']
    plt.pie(a1,labels=a2,colors=A,startangle=90,shadow=True,explode=(0,0,0,0,0,0.1),autopct='%1.1f%%')
    plt.title('Intresting Graph')
    plt.show()

