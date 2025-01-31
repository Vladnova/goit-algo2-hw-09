import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = [random.uniform(*bound) for bound in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        new_solution = [
            max(bounds[i][0], min(bounds[i][1], current_solution[i] + random.uniform(-0.1, 0.1)))
            for i in range(len(bounds))
        ]
        new_value = func(new_solution)

        if abs(new_value - current_value) < epsilon:
            break

        if new_value < current_value:
            current_solution, current_value = new_solution, new_value

    return current_solution, current_value

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(*bound) for bound in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        new_solution = [random.uniform(*bound) for bound in bounds]
        new_value = func(new_solution)

        if new_value < best_value:
            best_solution, best_value = new_solution, new_value

        if best_value < epsilon:
            break

    return best_solution, best_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_solution = [random.uniform(*bound) for bound in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break

        new_solution = [
            max(bounds[i][0], min(bounds[i][1], current_solution[i] + random.uniform(-1, 1)))
            for i in range(len(bounds))
        ]
        new_value = func(new_solution)

        delta = new_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_solution, current_value = new_solution, new_value

    return current_solution, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
