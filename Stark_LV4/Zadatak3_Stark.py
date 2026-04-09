#ne funkcionira, popravit kod kuće

'''
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import sys

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy

x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

np.random.seed(12)
indeksi = np.random.permutation(len(x))
split = int(np.floor(0.7*len(x)))

xtrain_raw = x[indeksi[:split]]
ytrain = y_measured[indeksi[:split]]
xtest_raw = x[indeksi[split:]]
ytest = y_measured[indeksi[split:]]

degrees = [2, 6, 15]
MSETrain = []
MSETest = []

plt.figure(figsize=(10, 6))
plt.plot(x, y_true, 'k--', label='Pozadinska funkcija', alpha=0.3)

for d in degrees:
    poly = PolynomialFeatures(degree=d)
    xtrain = poly.fit_transform(xtrain_raw)
    xtest = poly.transform(xtest_raw)

    model = lm.LinearRegression()
    model.fit(xtrain, ytrain)

    ytrain_p = model.predict(xtrain)
    ytest_p = model.predict(xtest)

    MSETrain.append(mean_squared_error(ytrain, ytrain_p))
    MSETest.append(mean_squared_error(ytest, ytest_p))

    x_plot = np.linspace(1, 10, 100).reshape(-1, 1)
    y_plot = model.predict(poly.transform(x_plot))
    plt.plot(x_plot, y_plot, label=f'Model stupnja {d}')

plt.scatter(xtrain_raw, ytrain, color = 'black', label = 'Podatci za učenje')
plt.legend()
plt.title("Usporedba polinoma različite veličine")

plt.draw()
print("Graf je generiran, zatvorite prozor grafa za nastavak.")
plt.show()

print("MSETrain: ", MSETrain)
print("MSETest: ", MSETest)
sys.stdout.flush()
'''
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# 1. DEFINICIJA FUNKCIJA
def non_func(x):
    # Prava funkcija koju pokušavamo otkriti
    return 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)

def add_noise(y):
    # Dodavanje nasumičnog šuma (greške mjerenja)
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    return y + 0.1 * varNoise * np.random.normal(0, 1, len(y))

# 2. PRIPREMA PODATAKA
x = np.linspace(1, 10, 50) # 50 uzoraka (promijeni ovo za simulaciju manjeg/većeg broja)
y_true = non_func(x)
y_measured = add_noise(y_true)

# Scikit-learn zahtijeva 2D niz (kolonu)
x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# 3. PODJELA PODATAKA (70% Trening, 30% Test)
np.random.seed(12)
indeksi = np.random.permutation(len(x))
split = int(np.floor(0.7 * len(x)))

xtrain_raw = x[indeksi[:split]]
ytrain = y_measured[indeksi[:split]]
xtest_raw = x[indeksi[split:]]
ytest = y_measured[indeksi[split:]]

# 4. PETLJA ZA RAZLIČITE STUPNJEVE POLINOMA
degrees = [2, 6, 15]
MSETrain = []
MSETest = []

plt.figure(figsize=(10, 6))
x_fine = np.linspace(1, 10, 100).reshape(-1, 1)
plt.plot(x_fine, non_func(x_fine), 'k--', label='Prava funkcija', alpha=0.3)

for d in degrees:
    # Transformacija x u [1, x, x^2, ..., x^d]
    poly = PolynomialFeatures(degree=d)
    xtrain = poly.fit_transform(xtrain_raw)
    xtest = poly.transform(xtest_raw)

    # Treniranje modela na trening podacima
    model = lm.LinearRegression()
    model.fit(xtrain, ytrain)

    # Predviđanje za izračun pogreške
    ytrain_p = model.predict(xtrain)
    ytest_p = model.predict(xtest)

    # Spremanje MSE (Mean Squared Error) u vektore
    MSETrain.append(mean_squared_error(ytrain, ytrain_p))
    MSETest.append(mean_squared_error(ytest, ytest_p))

    # Crtanje linije modela
    y_plot = model.predict(poly.transform(x_fine))
    plt.plot(x_fine, y_plot, label=f'Stupanj {d}')

# 5. PRIKAZ REZULTATA
plt.scatter(xtrain_raw, ytrain, color='black', label='Trening podaci')
plt.legend()
plt.title("Usporedba modela: Underfitting vs Overfitting")

# ISPIS U KONZOLU (Ovo ćeš sigurno vidjeti)
print("\n--- REZULTATI IZVOĐENJA ---")
print(f"MSETrain: {MSETrain}")
print(f"MSETest:  {MSETest}")

# ZAUSTAVLJANJE PROGRAMA DOK SE GRAF NE ZATVORI
print("\nGraf se otvara... Zatvorite prozor grafa za kraj programa.")
plt.show()