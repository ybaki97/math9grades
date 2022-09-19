import streamlit as st
import numpy as np

st.markdown('# Math 9 Grade Calculator')

st.markdown('## Essential Outcomes')

essout = st.multiselect("Select all EO's that you have completed:",["Select All","EO1","EO2","EO3","EO4","EO5","EO6"])
if "Select All" in essout:
    essout = ["EO1","EO2","EO3","EO4","EO5","EO6"]                                                                   
essouttot = len(essout)


st.markdown('## General Outcomes')

geoutMa = st.multiselect("Select all MATLAB EO's that you have completed:",["GOMa1","GOMa2","GOMa3","GOMa4","GOMa5","GOMa6"])
geoutMAtot = len(geoutMa)

geoutPy = st.multiselect("Select all MATLAB EO's that you have completed:",["GOPy1","GOPy2","GOPy3","GOPy4","GOPy5","GOPy6"])
geoutPytot = len(geoutPy)

totalgo = geoutPytot + geoutMAtot

st.markdown('## Homework Assignments')

matlabhomework = st.multiselect("Select all MATLAB homeworks you have passed:",["MLHW1","MLHW2","MLHW3","MLHW4"])

pyhomework = st.multiselect("Select all python homeworks you have passed:",["PyHW 1","PyHW 2","PyHW 3","PyHW 4"])

pyhomeworktotal = len(pyhomework)
matlabhomeworktotal = len(matlabhomework)

totalhw = matlabhomeworktotal + pyhomeworktotal

st.markdown('## Video Quizzes')

videoquiztot = st.number_input("How many video quizzes do you have credit for?",min_value=0, max_value=104,step=1)

st.markdown('## Grade Computation')

#gradelist = [totalgo, matlabgos, pygos, totalhw, matlabhw, pyhw, videoquiz ]
studentgradelist = [totalgo,geoutMAtot,geoutPytot,totalhw, matlabhomeworktotal, pyhomeworktotal, videoquiztot]

def gradecheck(student):
    for grade in grades:
        for b in range(len(grades[grade])):
            print([student[a] in grades[grade][b][a] for a in range(7)])            
            total = sum([student[a] in grades[grade][b][a] for a in range(7)])
            if total == 7:
                return grade
    return None


Aplus = ([12],[6],[6],[8],[4],[4],[100])
A = (range(10,13),range(5,7),range(5,7),range(7,9),range(3,5),range(3,5),range(90,105))
Aminusv1 = ([9],range(5,7),range(5,7),range(7,9),range(3,5),range(3,5),range(90,105))
Aminusv2 = (range(10,13),range(5,7),range(5,7),[6],range(3,5),range(3,5),range(90,105))
Aminusv3 = (range(10,13),range(5,7),range(5,7),range(7,9),range(3,5),range(3,5),range(81,90))
Bplus = ([9],range(4,7),range(4,7),range(6,9),range(2,5),range(2,5),range(85,105))
B = (range(8,13),range(4,7),range(4,7),range(5,9),range(2,5),range(2,5),range(80,105))
Bminusv1 = (range(8,13),range(4,7),range(4,7),range(4,9),range(2,5),range(2,5),range(80,105))
Bminusv2 = (range(7,13),range(4,7),range(4,7),range(5,9),range(2,5),range(2,5),range(80,105))
Bminusv3 = (range(8,13),range(4,7),range(4,7),range(5,9),range(2,5),range(2,5),range(71,90))
Cplus = (range(7,13),range(3,7),range(3,7),range(5,9),range(2,5),range(2,5),range(75,105))
C = (range(6,13),range(3,7),range(3,7),range(4,9),range(2,5),range(2,5),range(70,105))
Cminusv1 = (range(6,13),range(3,7),range(3,7),range(3,9),range(5),range(5),range(70,105))
Cminusv2 = (range(5,13),range(7),range(7),range(4,9),range(2,5),range(2,5),range(70,105))
Cminusv3 = (range(6,13),range(3,7),range(3,7),range(4,9),range(2,5),range(2,5),range(70))

grades = {"A+":[Aplus,],"A":[A,],"A-":[Aminusv1,Aminusv2,Aminusv3],"B+":[Bplus,],"B":[B,],"B-":[Bminusv1,Bminusv2,Bminusv3],"C+":[Cplus,],"C":[C,],"C-":[Cminusv1,Cminusv2,Cminusv3]}

if essouttot != 6:
    st.write("All 6 EO's must be passed to pass the class. See syllabus for what happens in this case.")
else:
    if gradecheck(studentgradelist) is None:
        st.write("No grade returned. Perhaps you do not meet minimum requirements for any grade category. If you believe this is in error please contact your instructor.")
    else:
        grade = gradecheck(studentgradelist)
        st.write(f"Your grade: {grade}")
    

