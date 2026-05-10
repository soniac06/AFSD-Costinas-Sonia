import random
import matplotlib.pyplot as plt

def runda():
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    if zar1+zar2==7 or zar1+zar2==11:
        return True
    return False
def monte_carlo(N):
    castiguri=0
    for _ in range(N):
        if runda():
            castiguri+=1
    probabilitate=castiguri/N
    return probabilitate
valori_N=[100, 1000, 10000, 100000]
rezultate=[]
print("Estimări Monte Carlo:")
for N in valori_N:
    p=monte_carlo(N)
    rezultate.append(p)
    print(f"N = {N:<7} -> Probabilitate estimată = {p:.5f}")
print("\nExperimente repetate pentru N = 1000")
for i in range(5):
    p=monte_carlo(1000)
    print(f"Rulare {i+1}: {p:.5f}")
plt.figure(figsize=(8, 5))
plt.plot(valori_N, rezultate, marker='o', label='Estimare Monte Carlo')
plt.xscale('log')
plt.xlabel('Număr simulări (N)')
plt.ylabel('Probabilitate estimată')
plt.title('Estimarea probabilității de câștig')
plt.legend()
plt.grid(True)
plt.savefig('monte_carlo_zaruri.png')
plt.show()