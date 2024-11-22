import streamlit as sl
R=0.0
Y=0.0
B=0.0
def STAR_DELTA(R1,R2,R3):
    R12=(R1*R2 + R2 * R3 + R3 * R1)/R3
    R23=(R1*R2 + R2 * R3 + R3 * R1)/R1
    R31=(R1*R2 + R2 * R3 + R3 * R1)/R2
    return R12,R23,R31
    
    
sl.title("2305A21L09-PS4")
sl.write("Calculate the resistance values (R12, R23, R31) of the Delta connection network for the given STAR <br> connection network having resistances R1, R2, and R3")

col=sl.columns(2)
with col[0]:
    R1=sl.number_input("R1:Ohms",value=1)
    R2=sl.number_input("R2:Ohms",value=1)
    R3=sl.number_input("R3:Ohms",value=1)
    if sl.button("compute"):
        R,Y,B,= STAR_DELTA(R1,R2,R3)
    
with col[1]:
       sl.write("R12:",R,"Ohms")
       sl.write("R23",Y,"Ohms")
       sl.write("R31",B,"Ohms")    
           
    