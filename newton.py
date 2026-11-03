import numpy as np
import matplotlib.pyplot as plt

x_list = np.arange(-9.1, 6.2, 0.1)
a = 1
b = 3
c = -1

# r_est_1 = 5.234
r_est_1 = 1
# r_est_2 = -5.26123123
r_est_2 = -6

X_1_in=r_est_1
X_3_in=r_est_2


def f(x):
    return a * x**2 + b * x + c

def f_prime(x):
    return 2*a*x + b


def newton_method(tol, r_est_1, r_est_2,  graphing=True, print_info=False, extra=False):
    est_list1 = []
    est_list2 = []
    count1 = 0
    count2 = 0

    est_list1.append(r_est_1) 
    while np.abs(f(r_est_1)) > tol:
        r_est_1 = r_est_1 - f(r_est_1)/f_prime(r_est_1)
        est_list1.append(r_est_1) 

        count1 += 1

    est_list2.append(r_est_2) 
    while np.abs(f(r_est_2)) > tol:
        r_est_2 = r_est_2 - f(r_est_2)/f_prime(r_est_2)
        est_list2.append(r_est_2) 

        count2 += 1

        # print(r_est_1)


    # while f_prime(r_est_2) > 0:
    #     r_est2 = r_est_2 + prime_step if a > 0 else r_est_2 - prime_step

    # might not work in some situations
    # if est_list[-2] > est_list[-1]:
    #     while f_prime(r_est_2) <

    if print_info:
        print(est_list1)
        print(est_list2)
        print("#steps1: ", count1)
        print("#steps2: ", count2)
    
    if graphing:
        plt.plot(x_list, f(x_list), label = (
                    rf"a={a}, b={b}, c={c}"  # Standard text
                    + "\n"  # Newline outside of math mode
                    + rf"$X_1={X_1_in},\ X_3={X_3_in}$"  # Math mode for subscripts
                ))
        plt.plot(x_list, 0.0 * x_list)
        if extra:
            plt.plot(est_list1[0], f(est_list1[0]), 'ro', label=f"({est_list1[0]},{f(est_list1[0])})")
            plt.plot(est_list2[0], f(est_list2[0]), 'ro', label=f"({est_list2[0]},{f(est_list2[0])})")
        else:
            plt.plot(r_est_1, f(r_est_1), 'ro', label=f"({r_est_1} , {f(r_est_1)})")
            plt.plot(r_est_2, f(r_est_2), 'ro', label=f"({r_est_2} , {f(r_est_2)})")
        plt.legend(loc="upper center")
        plt.show()

    return r_est_1, r_est_2, count1, count2


# res_1it = newton_method(0.001, r_est_1, r_est_2, graphing=True)
# print(res_1it)


# few tolerances
tol_list = [(1e-1)**i for i in range(10) ]
tol_log_list = np.log10(tol_list)

steps_list_1 = []
steps_list_2 = []

res_list_1 = []
res_list_2 = []

for tol in tol_list:
    res = newton_method(tol, r_est_1, r_est_2, graphing=False)
    
    res_list_1.append(res[0])
    res_list_2.append(res[1])
    steps_list_1.append(res[2])
    steps_list_2.append(res[3])


print("-"*30)
plot_choice = input("Show tol plot - 1\nShow results plot - 2\nEnter your choice: ")
print("-"*30)

if plot_choice == "1":
    plt.plot(tol_log_list, steps_list_1)
    plt.plot(tol_log_list, steps_list_2)
    plt.xlabel(r"$\log_{10}(\varepsilon)$")
    plt.ylabel("steps")
    plt.show()

    print(tol_list)
    print(steps_list_1)
    print(steps_list_2)

elif plot_choice == "2":
    abs_f_list_1 = np.abs(f(np.array(res_list_1)))
    abs_f_list_2 = np.abs(f(np.array(res_list_2)))


    min_f_abs_1 = np.min(abs_f_list_1)
    tol_of_min_1 = tol_log_list[np.argmin(abs_f_list_1, axis=0)]
    root1 = res_list_1[np.argmin(abs_f_list_1, axis=0)] 

    min_f_abs_2 = np.min(abs_f_list_2)
    tol_of_min_2 = tol_log_list[np.argmin(abs_f_list_2, axis=0)]
    root2 = res_list_1[np.argmin(abs_f_list_2, axis=0)] 


    fig, ax = plt.subplots(1, 2)



    ax[0].plot(tol_log_list, abs_f_list_1)
    ax[0].plot(tol_of_min_1, min_f_abs_1, 'ro', label = (
            r"Most accurate approximation is"
            + "\n"
            + rf"$x = {root1}$"
            + "\n"
            + rf"at tolerance $\varepsilon = 0.1^{{{int(tol_of_min_1)}}}$"
        ))
    ax[0].set_ylabel(r"$|f(\mathrm{result})|$")
    ax[0].set_xlabel(r"$\log_{10}(\varepsilon)$")
    ax[0].legend(loc="upper left")
    ax[0].set_title("First root")

    ax[1].plot(tol_log_list, abs_f_list_2)
    ax[1].plot(tol_of_min_2, min_f_abs_2, 'ro', label = (
            r"Most accurate approximation is"
            + "\n"
            + rf"$x = {root2}$"
            + "\n"
            + rf"at tolerance $\varepsilon = 0.1^{{{int(tol_of_min_2)}}}$"
        ))
    ax[1].set_ylabel(r"$|f(\mathrm{result})|$")
    ax[1].set_xlabel(r"$\log_{10}(\varepsilon)$")
    ax[1].legend(loc="upper left")
    ax[1].set_title("Second root")

    print(tol_list)
    print(res_list_1)
    print(steps_list_1)
    print(abs_f_list_1)
    print(res_list_2)
    print(steps_list_2)
    print(abs_f_list_2)
    
    plt.show()
else:
    print("No such a choice exists")
