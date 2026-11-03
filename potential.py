import numpy as np
import matplotlib.pyplot as plt

x_list = np.arange(0.01, 1, 0.01)

A = 1090
p = 0.033
k = 1.44

def V(x):
    return A * np.exp(-x/p) - k/x

def F(x):
    return (A/p) * np.exp(-x/p) - k/(x**2)

def V_2_prime(x):
    return (A/p**2) * np.exp(-x/p) - (2*k)/x**3

def F_prime(x):
    return -V_2_prime(x)


print(V(x_list))




def newton_method(tol, r_est_1,  graphing=True, print_info=False):
    est_list1 = []
    count1 = 0

    est_list1.append(r_est_1) 
    while np.abs(F(r_est_1)) > tol:
        r_est_1 = r_est_1 - F(r_est_1)/F_prime(r_est_1)
        est_list1.append(r_est_1) 

        count1 += 1

    if print_info:
        print(est_list1)
        print("#steps1: ", count1)
    
    if graphing:
        plt.plot(x_list, F(x_list))
        plt.plot(x_list, 0.0 * x_list)
        plt.plot(r_est_1, F(r_est_1), 'ro', label=f"Estimated root = {r_est_1} \n at tolerance"+ rf"at tolerance $\varepsilon = 0.1^{{{int(round(np.log10(tol)))}}}$")
        plt.xlabel("x")
        plt.ylabel("F") 
        plt.title("Force versus distance")
        plt.legend()
        plt.show()

    return r_est_1, count1


# Run Newton's method
res = newton_method(1e-6, 0.2)
root_val = res[0]

# Create a figure with 2 subplots side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Left Subplot: Full Overview ---
ax1.plot(x_list, 0.0 * x_list, "k--", alpha=0.5)  # Reference line at y=0
ax1.plot(x_list, V(x_list), label=r"$V(x)$", color="blue")
ax1.plot(root_val, V(root_val), "ro", label="Minimum")
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$V(x)$")
ax1.set_title("Full View of Ionic Interaction Potential")
ax1.legend()
ax1.grid(True, linestyle=":", alpha=0.6)

# --- Right Subplot: Zoomed-in Window near the Dot ---
ax2.plot(x_list, 0.0 * x_list, "k--", alpha=0.5)
ax2.plot(x_list, V(x_list), color="blue")
ax2.plot(root_val, V(root_val), "ro", label=f"Root at x = {root_val:.6f} \n f(x)={V(root_val):.6f}")
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$V(x)$")
ax2.set_title("Zoomed View Around Minimum")

# Dynamically set zoom limits around the root (e.g., +/- 0.05 around the root)
zoom_margin = 0.05
ax2.set_xlim(root_val - zoom_margin, root_val + zoom_margin)

# Automatically adjust y-limits based on the zoomed x-range
zoom_mask = (x_list >= root_val - zoom_margin) & (
    x_list <= root_val + zoom_margin
)
if any(zoom_mask):
    ax2.set_ylim(
        min(V(x_list[zoom_mask])) - 0.5, max(V(x_list[zoom_mask])) + 0.5
    )

ax2.legend()
ax2.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.show()


# plt.plot(x_list, F(x_list))
# plt.ylabel("F")
plt.plot(x_list, V_2_prime(x_list))
plt.plot(root_val, V(root_val), "ro", label=f"Root at x = {root_val:.6f} \n V''(x)={V_2_prime(root_val):.6f}")
plt.ylabel("V''(x)")
plt.xlabel("x")
plt.title("Second derivative of V versus x")
plt.legend()
plt.show()