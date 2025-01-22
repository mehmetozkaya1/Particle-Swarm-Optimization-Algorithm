# Particle Swarm Optimization (PSO) for Minimizing x² + y²

This repository demonstrates the use of the **Particle Swarm Optimization (PSO)** algorithm to minimize the function `f(x, y) = x² + y²`. The PSO algorithm is a population-based optimization technique inspired by the social behavior of birds and fish. This project serves as an introduction to PSO and showcases its effectiveness in solving simple mathematical optimization problems.

---

## What is PSO?

Particle Swarm Optimization (PSO) is a metaheuristic optimization algorithm inspired by the collective movement and behavior of swarms, such as birds flocking or fish schooling. The key idea is that a group of particles (potential solutions) move through the search space and adjust their positions based on:

1. Their personal best experience (the best solution they have found so far).
2. The global best experience (the best solution found by the entire swarm).

Each particle has:
- **Position:** Represents a potential solution in the search space.
- **Velocity:** Dictates the direction and speed of movement.
- **Fitness:** Evaluates the quality of a solution based on the objective function.

Through iterative updates, particles converge toward an optimal or near-optimal solution.

---

## Function to Minimize

The target function for this project is:

\[
f(x, y) = x^2 + y^2
\]

- **Objective:** Minimize \( f(x, y) \), which achieves its global minimum at \( (x, y) = (0, 0) \), where \( f(0, 0) = 0 \).
- This is a simple convex function, ideal for demonstrating the mechanics of the PSO algorithm.

---

## How It Works

1. **Initialization:**
   - A swarm of particles is randomly initialized in the search space.
   - Each particle is assigned a random position and velocity.

2. **Fitness Evaluation:**
   - Each particle evaluates the fitness of its current position based on \( f(x, y) \).

3. **Update Rules:**
   - The particle updates its velocity based on:
     - **Cognitive Component:** Attraction toward its personal best position.
     - **Social Component:** Attraction toward the global best position.
   - The particle's position is updated based on its new velocity.

4. **Iteration:**
   - The swarm iterates through a predefined number of steps or until a convergence criterion is met.

5. **Result:**
   - The best solution found by the swarm is reported as the global minimum.

---

## Features

- Implements the PSO algorithm from scratch.
- Demonstrates convergence behavior on a simple function.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/PSO-Minimization.git

2. Install necessary dependencies (if any).

3. Run the script:
   ```bash
   python pso_algorithm.py

4. View the output including the visualization of particle movement and the final solution.

# x² + y² Fonksiyonunu Minimize Etmek için Parçacık Sürü Optimizasyonu (PSO)

Bu depo, **Parçacık Sürü Optimizasyonu (PSO)** algoritmasını kullanarak `f(x, y) = x² + y²` fonksiyonunu minimize etmeyi göstermektedir. PSO, kuş sürüleri ve balık topluluklarının sosyal davranışlarından esinlenilmiş, popülasyon tabanlı bir optimizasyon tekniğidir. Bu proje, PSO'ya bir giriş niteliğindedir ve basit matematiksel optimizasyon problemlerinde etkinliğini göstermektedir.

---

## PSO Nedir?

Parçacık Sürü Optimizasyonu (PSO), sürülerin toplu hareket ve davranışlarından ilham alan bir meta-sezgisel optimizasyon algoritmasıdır. Temel fikir, bir grup parçacığın (potansiyel çözümler) arama alanında hareket ederek:

1. Kendi en iyi deneyimlerine (şimdiye kadar buldukları en iyi çözüm).
2. Sürünün en iyi deneyimine (tüm sürünün bulduğu en iyi çözüm) dayalı olarak pozisyonlarını ayarlamalarıdır.

Her bir parçacık:
- **Pozisyon:** Arama alanında potansiyel bir çözümü temsil eder.
- **Hız:** Hareket yönü ve hızını belirler.
- **Uygunluk (Fitness):** Çözümün, hedef fonksiyonuna göre kalitesini değerlendirir.

Parçacıklar, yinelemeli güncellemelerle optimal veya optimal bir çözüme yakın bir sonuca doğru yakınsar.

---

## Minimize Edilecek Fonksiyon

Bu projedeki hedef fonksiyon:

\[
f(x, y) = x^2 + y^2
\]

- **Amaç:** \( f(x, y) \) fonksiyonunu minimize etmektir. Fonksiyon, global minimumunu \( (x, y) = (0, 0) \) noktasında, \( f(0, 0) = 0 \) olarak alır.
- Bu, PSO algoritmasının işleyişini göstermek için ideal olan basit bir konveks fonksiyondur.

---

## Nasıl Çalışır?

1. **Başlatma:**
   - Parçacıklardan oluşan bir sürü, arama alanında rastgele başlatılır.
   - Her parçacığa rastgele bir pozisyon ve hız atanır.

2. **Uygunluk Değerlendirmesi:**
   - Her bir parçacık, \( f(x, y) \) fonksiyonuna göre mevcut pozisyonunun uygunluğunu değerlendirir.

3. **Güncelleme Kuralları:**
   - Parçacık, hızını şu bileşenlere göre günceller:
     - **Bilişsel Bileşen:** Kendi en iyi pozisyonuna doğru çekim.
     - **Sosyal Bileşen:** Sürünün en iyi pozisyonuna doğru çekim.
   - Parçacığın pozisyonu, yeni hızına göre güncellenir.

4. **Yineleme:**
   - Sürü, belirli bir adım sayısı boyunca veya yakınsama kriterine ulaşılana kadar devam eder.

5. **Sonuç:**
   - Sürünün bulduğu en iyi çözüm, global minimum olarak rapor edilir.

---

## Özellikler

- Sıfırdan PSO algoritması uygulanmıştır.
- Basit bir fonksiyon üzerinde yakınsama davranışını gösterir.

---

## Çalıştırma

1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/yourusername/PSO-Minimization.git

2. Gerekli bağımlılıkları kurun (varsa).

3. Script'i çalıştırın:
   ```bash
   python pso_algorithm.py

4. Çıkış sonuçlarını görün.


Eğer eklemek istediğiniz başka bir detay varsa, lütfen söyleyin! 😊
