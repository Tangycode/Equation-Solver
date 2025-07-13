import streamlit as st
import numpy as np
import scipy as sp
from scipy.linalg import solve
st.set_page_config(page_title="Algebraic Equation Solver",layout="wide")
st.title("Algebraic Equation Solver")
st.markdown("This app was solely built for the purpose of solving equations.")
st.divider()
lin = "linear (ax+b=0)"
quad = "quadratic(ax² + bx + c = 0))"
cub = "cubic(ax³ + bx² + cx + d = 0)"
sys_two = "system of two equations"
sys_three = "system of three equations"
options = st.sidebar.radio("Choose an equation type to solve: ",(lin,quad,cub,sys_two,sys_three))
if options == lin:
    st.subheader("Linear Equation")
    a=st.number_input("Enter a coefficient",value=1)
    b=st.number_input("Enter a constant",value=0)
    st.latex(fr"{a}x + {b}")
    if st.button("Solve Linear Equation"):
        if a!=0:
            result = -b/a
            st.success(f"Root of the equation is: {result}")
        else:
            st.error("Not a valid linear equation")
elif options == quad:
    st.subheader("Quadratic Equation")
    a=st.number_input("Enter a coefficient_1",value=0)
    b=st.number_input("Enter a coefficient_2",value=0)
    c=st.number_input("Enter a constant",value=0)
    st.latex(fr"{a}x^2 + {b}x + {c}")
    if st.button("Solve quadratic equation"):
        coeff=[a,b,c]
        result = np.roots(coeff)
        st.success(f"Roots of the equation are: {result[0]} and {result[1]}")
elif options == cub:
    st.subheader("Cubic Equation")
    a=st.number_input("Enter a coefficient_1", value=0)
    b = st.number_input("Enter a coefficient_2", value=0)
    c = st.number_input("Enter a coefficient_3", value=0)
    d = st.number_input("Enter a constant", value=0)
    st.latex(fr"{a}x^3 + {b}x^2 + {c}x + {d}")
    if st.button("Solve cubic equation"):
        coeff=[a,b,c,d]
        result = np.roots(coeff)
        st.success(f"Roots of the equation are: {result[0]} and {result[1]} and {result[2]}")
elif options == sys_two:
    st.subheader("System of two Equation")
    x_1 = st.number_input("Enter the coeff of x(eqn1): ", value=0)
    y_1 = st.number_input("Enter the coeff of y(eqn1): ", value=0)
    x_2 = st.number_input("Enter the coeff of x(eqn2): ", value=0)
    y_2 = st.number_input("Enter the coeff of y(eqn2): ", value=0)
    con_1 = st.number_input("Enter the constant of eqn1: ", value=0)
    con_2 = st.number_input("Enter the constant of eqn2: ", value=0)
    st.latex(fr"({x_1})x + ({y_1})y = {con_1}")
    st.latex(fr"({x_2})x + ({y_2})y = {con_2}")
    if st.button("Solve Linear Equation"):
        coeff_1 = np.array([[x_1,y_1],
                          [x_2,y_2]])
        con = np.array([con_1,con_2])
        result = solve(coeff_1,con)
        st.success(f"Roots of the equation are x = {result[0]} and y = {result[1]}")
elif options == sys_three:
    st.subheader("System of two Equation")
    x_1 = st.number_input("Enter the coeff of x(eqn1): ", value=0)
    y_1 = st.number_input("Enter the coeff of y(eqn1): ", value=0)
    z_1 = st.number_input("Enter the coeff of z(eqn1): ", value=0)
    x_2 = st.number_input("Enter the coeff of x(eqn2): ", value=0)
    y_2 = st.number_input("Enter the coeff of y(eqn2): ", value=0)
    z_2 = st.number_input("Enter the coeff of z(eqn2): ", value=0)
    x_3 = st.number_input("Enter the coeff of x(eqn3): ", value=0)
    y_3 = st.number_input("Enter the coeff of y(eqn3): ", value=0)
    z_3 = st.number_input("Enter the coeff of z(eqn3): ", value=0)
    con_1 = st.number_input("Enter the constant of eqn1: ", value=0)
    con_2 = st.number_input("Enter the constant of eqn2: ", value=0)
    con_3 = st.number_input("Enter the constant of eqn3: ", value=0)
    st.latex(fr"({x_1})x + ({y_1})y + ({z_1})z = {con_1}")
    st.latex(fr"({x_2})x + ({y_2})y + ({z_2})z = {con_2}")
    st.latex(fr"({x_3})x + ({y_3})y + ({z_3})z = {con_3}")
    if st.button("Solve Linear Equation"):
        coeff = np.array([[x_1,y_1,z_1],
                          [x_2,y_2,z_2],
                            [x_3,y_3,z_3]])
        con = np.array([con_1,con_2,con_3])
        result = solve(coeff,con)
        st.success(f"Roots of the equation are x = {result[0]} and y = {result[1]} and z = {result[2]}")
