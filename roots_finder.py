import numpy as np
import matplotlib.pyplot as plt

x_list = np.arange(-6.5, 3.5, 0.1)

a = 1
b = 3 
c = -1

def f(x):
    return a * x**2 + b * x + c

def mid(x_1, x_2):
    return (x_1+x_2)/2

X_1 = -4
X_3 = 3
X_2 = mid(X_1,X_3)

X_1_in = X_1
X_3_in = X_3

tol = 0.0001

def check(x1,x3):
    if f(x1) < 0:
        if f(x3) > 0:
            print("All good")
            return True
        else:
            print("f(X_3) must be larger than 0")
            return False
    else:
        print("f(X_1) must be smaller than 0")
        return False

print("-"*100,"\n1 root check")
checked = check(X_1, X_3)
print(checked)

def check_2roots(A_1,A_2):
    midP = mid(A_1, A_2)
    print(midP)
    print(f(midP))
    if a > 0:
        if f(A_1) > 0 and f(A_2) > 1:
            if f(midP) < 0:
                print("Parabola U-shaped, everything is good")
                return True 
            else:
                print("Midpoint must have negative f")
                return False
        else:
            print("both f(A_1) and f(A_2) must be bigger then zero")
            return False
    if a < 0:
        if f(A_1) < 0 and f(A_2) < 1:
            if f(midP) > 0:
                print("Parabola ∩-shaped, everything is good")
                return True 
            else:
                print("Midpoint must have positive f")
                return False
        else:
            print("both f(A_1) and f(A_2) must be lower then zero")   
            return False
    else:
        print("Your function is linear")    
        return False

print("-"*100,"\n2 roots check")
checked2 = check_2roots(X_1,X_3)
print(checked2)

def rootFinding(tol, a_1, a_3, need_res_print = True):
    m_root = mid(a_1,a_3)

    m_roots_list = []
    root = 0
    count = 0
    
    while np.abs(f(m_root)) > tol:
        m_root = mid(a_1,a_3)
        
        if f(m_root) > 0:
            if f(a_3) > f(a_1):
                a_3 = m_root
            else:
                a_1 = m_root

        elif f(m_root) < 0:
            if f(a_3) > f(a_1):
                a_1 = m_root
            else:
                a_3 = m_root

        else:
            print(f"root found, it's {m_root}")
            break
        m_roots_list.append(m_root)

        count += 1

    # print(m_roots_list)
    root = m_root

    if need_res_print:
        print(f"Final value of root: {root}")

    return m_roots_list, root, count 



graph_needed = False
graph_6 = False

# one root version
if checked and graph_needed:
    x_2_list, root, count = rootFinding(tol, X_1, X_3)

    plt.plot(x_list, f(x_list), label = (
                    rf"a={a}, b={b}, c={c}"  # Standard text
                    + "\n"  # Newline outside of math mode
                    + rf"$X_1={X_1_in},\ X_2={X_3_in}$"  # Math mode for subscripts
                ))
    plt.plot(x_list, 0.0 * x_list)
    if graph_6:
        plt.plot(x_2_list[0], f(x_2_list[0]), 'ro', label=f"({x_2_list[0]},f({x_2_list[0]}))=({x_2_list[0]},{f(x_2_list[0])})")
    else:
        plt.plot(root, f(root), 'ro', label=f"({root},{f(root)})")

    plt.legend(loc="upper left")

    plt.show()

# two roots version
if checked2 and graph_needed:
    x_21_list, root1, count1 = rootFinding(tol, X_1, X_2)
    x_22_list, root2, count2 = rootFinding(tol, X_2, X_3)

    plt.plot(x_list, f(x_list), label = (
                    rf"a={a}, b={b}, c={c}"  # Standard text
                    + "\n"  # Newline outside of math mode
                    + rf"$X_1={X_1_in},\ X_2={X_3_in}$"  # Math mode for subscripts
                ))
    plt.plot(x_list, 0.0 * x_list)
    plt.plot(root1, f(root1), 'ro', label=f"({root1},{f(root1)})")
    plt.plot(root2, f(root2), 'ro', label=f"({root2},{f(root2)})")
    plt.legend(loc="upper left")
    plt.show()



print("-"*100,"\nTolerance change")
# few tolerances
tol_list = [0.1**i for i in range(10) ]
tol_log_list = np.log10(tol_list)

res1_count_list = []
res2_count_list = []

if checked2 and not graph_needed:
    for toler in tol_list:
        res1 = rootFinding(toler, X_1, X_2, False)
        res2 = rootFinding(toler, X_2, X_3, False)

        res1_count_list.append(res1[2])
        res2_count_list.append(res2[2])

    plt.plot(res1_count_list, tol_log_list, label="First root")
    plt.plot(res2_count_list, tol_log_list, label="Second root")
    plt.plot([], [], ' ', 
            label = (
                rf"a={a}, b={b}, c={c}"  # Standard text
                + "\n"  # Newline outside of math mode
                + rf"$X_1={X_1_in},\ X_2={X_3_in}$"  # Math mode for subscripts
            ))
    plt.xlabel("Steps count (n)")
    plt.ylabel(r"$\log_{10}(\varepsilon)$")
    plt.legend(loc="upper right")
    plt.show()

    print(tol_list)
    print(res1_count_list)
    print(res2_count_list)
