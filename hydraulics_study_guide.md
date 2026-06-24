# 📘 HYDRAULICS AND HYDRAULIC MACHINERY — COMPLETE STUDY GUIDE
### R22 B.Tech Civil Engineering | II Year II Sem | JNTUHUCESTH

---

# UNIT I — OPEN CHANNEL FLOW (Fundamentals)

## 1.1 Introduction to Open Channel Flow

**Open Channel Flow**: Flow of liquid with a free surface (exposed to atmosphere). The driving force is **gravity**.

### Open Channel Flow vs Pipe Flow

| Feature | Open Channel Flow | Pipe Flow |
|---------|------------------|-----------|
| Free surface | Yes | No (flows full) |
| Driving force | Gravity (slope) | Pressure difference |
| Cross-section | Can vary | Usually constant |
| Hydraulic gradient | Parallel to water surface | Depends on pressure |
| Maximum velocity | At/below free surface | At centre of pipe |
| Pressure | Atmospheric at surface | Above atmospheric |

### Classification of Open Channel Flows

**Based on time:**
- **Steady flow**: Flow properties don't change with time (∂V/∂t = 0)
- **Unsteady flow**: Flow properties change with time (∂V/∂t ≠ 0)

**Based on space:**
- **Uniform flow**: Flow properties don't change with distance (∂V/∂s = 0), depth remains constant
- **Non-uniform (varied) flow**: Flow properties change with distance (∂V/∂s ≠ 0)

**Types of non-uniform flow:**
- **Gradually Varied Flow (GVF)**: Depth changes gradually over a long distance
- **Rapidly Varied Flow (RVF)**: Depth changes abruptly over a short distance (e.g., hydraulic jump)

**Based on Froude Number (Fr):**
- **Sub-critical flow**: Fr < 1 (tranquil flow, depth > critical depth)
- **Critical flow**: Fr = 1
- **Super-critical flow**: Fr > 1 (shooting/rapid flow, depth < critical depth)

$$Fr = \frac{V}{\sqrt{gD}}$$

where D = hydraulic depth = A/T (Area / Top width)

---

## 1.2 Velocity Distribution

- Maximum velocity occurs at about **0.05 to 0.25 × depth** below the free surface
- Average velocity ≈ velocity at **0.6d** from surface
- Or average of velocities at **0.2d and 0.8d** from surface

---

## 1.3 Uniform Flow

In uniform flow:
- Depth (y), velocity (V), area (A) remain constant along the channel
- Water surface is parallel to the channel bed
- Energy gradient = Water surface slope = Bed slope (Sf = Sw = S₀)

### Chezy's Formula

$$V = C\sqrt{RS}$$

$$Q = AC\sqrt{RS}$$

where:
- V = mean velocity (m/s)
- C = Chezy's constant
- R = hydraulic radius = A/P (Area / Wetted Perimeter)
- S = bed slope

### Manning's Formula

$$V = \frac{1}{n} R^{2/3} S^{1/2}$$

$$Q = \frac{1}{n} A R^{2/3} S^{1/2}$$

where:
- n = Manning's roughness coefficient (depends on surface material)
- Typical values: Concrete (0.013), Earth (0.025), Natural streams (0.03-0.05)

### Relationship between Chezy's C and Manning's n:

$$C = \frac{1}{n} R^{1/6}$$

### Bazin's Formula

$$C = \frac{87}{1 + \frac{K}{\sqrt{R}}}$$

where K = Bazin's constant (depends on surface roughness)

### Manning's Roughness Coefficient (n) — Common Values

| Surface | n value |
|---------|---------|
| Glass, plastic | 0.010 |
| Smooth concrete | 0.012 |
| Rough concrete | 0.015 |
| Brick | 0.015 |
| Earth channel (clean) | 0.022 |
| Earth channel (weedy) | 0.030 |
| Natural streams (clean) | 0.030 |
| Natural streams (rough) | 0.045 |

---

## 1.4 Most Economical (Efficient) Sections

A channel section is **most economical** when it carries maximum discharge for a given area, slope, and roughness. This happens when the **wetted perimeter is minimum**.

### Rectangular Section (width = b, depth = y)

- **Condition**: b = 2y (width = twice the depth)
- **Hydraulic radius**: R = y/2
- A = 2y²
- P = 4y

### Trapezoidal Section (bottom width = b, side slope = 1:n, depth = y)

- **Conditions**:
  1. R = y/2
  2. b + 2ny = 2y√(1 + n²) → Half top width = length of sloping side
  3. A hydraulic circle of radius y can be inscribed in the section
- **Most efficient of all trapezoidal** → when it's half a regular hexagon (side slope 60°, n = 1/√3)

### Circular Section

- **Maximum velocity**: when depth = 0.81D (D = diameter)
- **Maximum discharge**: when depth = 0.95D

### Triangular Section

- **Condition**: Vertex angle = 90° (2θ = 90°, θ = 45°)
- R = y/(2√2)

---

## 1.5 Computation of Uniform Flow & Normal Depth

**Normal depth (yₙ)**: The depth at which uniform flow occurs for a given discharge, slope, and roughness.

Using Manning's equation:
$$Q = \frac{1}{n} A R^{2/3} S^{1/2}$$

For a rectangular channel:
$$Q = \frac{1}{n} (by_n) \left(\frac{by_n}{b + 2y_n}\right)^{2/3} S^{1/2}$$

This is solved by **trial and error** for yₙ.

---

## 1.6 Specific Energy & Critical Flow

### Specific Energy

$$E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2gA^2}$$

Specific energy = depth + velocity head (measured from channel bottom)

### Specific Energy Curve
- For a given Q, plotting E vs y gives a curve with **two limbs**
- **Upper limb**: sub-critical flow (Fr < 1)
- **Lower limb**: super-critical flow (Fr > 1)
- **Minimum E** occurs at **critical depth**

### Critical Depth (yc)

At critical flow, specific energy is minimum.

**Condition for critical flow:**

$$\frac{Q^2 T}{g A^3} = 1 \quad \text{or} \quad Fr = 1$$

**For rectangular channel:**

$$y_c = \left(\frac{q^2}{g}\right)^{1/3}$$

where q = Q/b = discharge per unit width

$$E_c = \frac{3}{2} y_c$$

$$V_c = \sqrt{g y_c}$$

$$q = \sqrt{g y_c^3}$$

### Critical Slope

The bed slope at which normal depth equals critical depth:

$$S_c = \frac{gn^2}{y_c^{1/3}}$$ (for wide rectangular channel)

### Alternate Depths
For a given specific energy (E > Emin), there are **two possible depths**:
- y₁ (super-critical, y₁ < yc)
- y₂ (sub-critical, y₂ > yc)

These are called **alternate depths**.

---

## 1.7 Channel Transitions

### Raised Bottom (Hump)

When a hump of height Δz is placed on the channel bed:

$$E_1 = E_2 + \Delta z$$

$$y_1 + \frac{V_1^2}{2g} = y_2 + \frac{V_2^2}{2g} + \Delta z$$

- If Δz < Δzmax: flow remains sub-critical, water surface dips over the hump
- If Δz = Δzmax: critical flow occurs at the hump
- If Δz > Δzmax: choking occurs, upstream depth increases

$$\Delta z_{max} = E_1 - E_c$$

### Width Contraction

When the channel width is reduced from b₁ to b₂:
- Continuity: q₂ = Q/b₂ > q₁ = Q/b₁
- If contraction is not too severe: flow adjusts, water surface changes
- If b₂ < b₂min: choking occurs

---

---

# UNIT II — OPEN CHANNEL FLOW (Non-Uniform Flow)

## 2.1 Gradually Varied Flow (GVF)

Flow where depth changes **gradually** over a long distance. Assumptions:
1. Pressure distribution is hydrostatic
2. Friction losses same as uniform flow (Manning's/Chezy's applicable)
3. Bed slope is small
4. Channel is prismatic

### Dynamic Equation of GVF

$$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$$

where:
- dy/dx = rate of change of depth along channel
- S₀ = bed slope
- Sf = friction slope (energy gradient)
- Fr = Froude number

**Key observations:**
| Condition | dy/dx | Water surface |
|-----------|-------|---------------|
| S₀ > Sf and Fr < 1 | Positive | Depth increases (backwater) |
| S₀ > Sf and Fr > 1 | Negative | Depth decreases |
| S₀ < Sf and Fr < 1 | Negative | Depth decreases (drawdown) |
| S₀ < Sf and Fr > 1 | Positive | Depth increases |

### Classification of Channel Slopes

| Type | Symbol | Condition |
|------|--------|-----------|
| Mild | M | S₀ < Sc (yn > yc) |
| Steep | S | S₀ > Sc (yn < yc) |
| Critical | C | S₀ = Sc (yn = yc) |
| Horizontal | H | S₀ = 0 |
| Adverse | A | S₀ < 0 (negative slope) |

### Surface Profile Classifications

**Zone 1**: y > yn and y > yc (above both normal and critical depth lines)
**Zone 2**: y is between yn and yc
**Zone 3**: y < yn and y < yc (below both lines)

#### Mild Slope Profiles (M):
- **M1 (Backwater curve)**: y > yn > yc → dy/dx > 0 → depth increases → caused by dam/weir
- **M2 (Drawdown curve)**: yn > y > yc → dy/dx < 0 → depth decreases → caused by sudden drop/free overfall
- **M3**: yn > yc > y → dy/dx > 0 → depth increases → after sluice gate on mild slope

#### Steep Slope Profiles (S):
- **S1**: y > yc > yn → dy/dx > 0 → depth increases → caused by obstruction on steep slope
- **S2**: yc > y > yn → dy/dx < 0 → depth decreases → at entrance to steep channel
- **S3**: yc > yn > y → dy/dx > 0 → depth increases → after sluice gate on steep slope

#### Critical Slope Profiles (C):
- **C1**: y > yn = yc → dy/dx > 0
- **C3**: y < yn = yc → dy/dx > 0

#### Horizontal Slope Profiles (H): (no normal depth exists)
- **H2**: y > yc → dy/dx < 0
- **H3**: y < yc → dy/dx > 0

#### Adverse Slope Profiles (A): (no normal depth exists)
- **A2**: y > yc → dy/dx < 0
- **A3**: y < yc → dy/dx > 0

**Total: 12 types** of GVF profiles (M1, M2, M3, S1, S2, S3, C1, C3, H2, H3, A2, A3)

---

## 2.2 Computation of GVF Profiles

### Direct Step Method

Used for **prismatic channels**. Steps:

1. Divide depth range into N steps (y₁ to y₂)
2. For each depth increment, calculate:
   - Area (A), wetted perimeter (P), hydraulic radius (R)
   - Velocity (V = Q/A)
   - Specific energy: E = y + V²/2g
   - Friction slope: $S_f = \frac{n^2 V^2}{R^{4/3}}$ (from Manning's)
   - Average friction slope between sections: $\bar{S_f} = \frac{S_{f1} + S_{f2}}{2}$
3. Calculate distance: $\Delta x = \frac{\Delta E}{S_0 - \bar{S_f}}$
4. Sum all Δx to get total length of GVF profile

### Standard Step Method (Numerical)
- Used for **non-prismatic channels**
- Trial-and-error approach
- Fix Δx, find y₂ by iteration

---

## 2.3 Rapidly Varied Flow — Hydraulic Jump

A **hydraulic jump** is an abrupt rise in water level when flow changes from **super-critical to sub-critical**.

### Hydraulic Jump in Rectangular Channel

**Sequent (conjugate) depth relationship:**

$$\frac{y_2}{y_1} = \frac{1}{2}\left(-1 + \sqrt{1 + 8Fr_1^2}\right)$$

$$\frac{y_1}{y_2} = \frac{1}{2}\left(-1 + \sqrt{1 + 8Fr_2^2}\right)$$

where y₁ = depth before jump (super-critical), y₂ = depth after jump (sub-critical)

**Note**: y₁ and y₂ are NOT alternate depths. They are called **sequent depths** or **conjugate depths**.

### Energy Loss in Hydraulic Jump

$$\Delta E = E_1 - E_2 = \frac{(y_2 - y_1)^3}{4y_1 y_2}$$

### Height of Jump

$$h_j = y_2 - y_1$$

### Length of Jump

$$L_j \approx 5 \text{ to } 7 \times h_j$$

(Empirically, L ≈ 6.9(y₂ - y₁) for Fr₁ = 4.5 to 9)

### Efficiency of Hydraulic Jump

$$\eta = \frac{E_2}{E_1} = \frac{(8Fr_1^2 + 1)^{3/2} - 4Fr_1^2 + 1}{8Fr_1^2(2 + Fr_1^2)}$$

### Classification of Hydraulic Jumps

| Fr₁ | Type | Energy Loss |
|-----|------|-------------|
| 1.0 - 1.7 | Undular jump | < 5% |
| 1.7 - 2.5 | Weak jump | 5-15% |
| 2.5 - 4.5 | Oscillating jump | 15-45% |
| 4.5 - 9.0 | Steady (stable) jump | 45-70% |
| > 9.0 | Strong (choppy) jump | 70-85% |

### Applications of Hydraulic Jump
1. Energy dissipation below spillways and sluice gates
2. Raising water level for irrigation
3. Mixing of chemicals in water treatment
4. Aeration of water
5. Removal of air pockets in water supply lines

### Location of Hydraulic Jump
- The jump forms where the sequent depth relationship is satisfied
- Controlled by downstream conditions (tailwater depth)

---

## 2.4 Surges (Theory Only)

### Positive Surge
- A moving wave front that increases the depth of flow
- Travels upstream when downstream gate is suddenly closed
- Travels downstream when upstream gate is suddenly opened

**Celerity of surge wave:**
$$V_w = \frac{V_1 y_1 - V_2 y_2}{y_1 - y_2}$$

### Negative Surge
- A moving wave front that decreases the depth of flow
- Travels upstream when downstream gate is suddenly opened
- Less stable, tends to flatten out

---

---

# UNIT III — DIMENSIONAL ANALYSIS & TURBO MACHINERY BASICS

## 3.1 Dimensional Analysis

The process of grouping variables into dimensionless groups to reduce the number of variables in a problem.

### Fundamental Dimensions (MLT System)

| Quantity | Dimension |
|----------|-----------|
| Mass | M |
| Length | L |
| Time | T |
| Velocity | LT⁻¹ |
| Acceleration | LT⁻² |
| Force | MLT⁻² |
| Pressure | ML⁻¹T⁻² |
| Density | ML⁻³ |
| Dynamic viscosity | ML⁻¹T⁻¹ |
| Kinematic viscosity | L²T⁻¹ |
| Discharge | L³T⁻¹ |
| Work/Energy | ML²T⁻² |
| Power | ML²T⁻³ |
| Surface tension | MT⁻² |

### Dimensional Homogeneity
An equation is dimensionally homogeneous if the dimensions on both sides are the same.

---

### Rayleigh's Method

Steps:
1. Identify the dependent variable and all independent variables
2. Write the functional relationship with unknown exponents
3. Write dimensions of each variable
4. Equate powers of M, L, T on both sides
5. Solve for exponents
6. Substitute back

**Example**: Drag force F on a sphere:
$$F = f(D, V, \rho, \mu)$$
$$F = C \cdot D^a V^b \rho^c \mu^d$$

Solving gives:
$$F = \rho V^2 D^2 \phi\left(\frac{\mu}{\rho V D}\right)$$

---

### Buckingham's π Theorem

**Statement**: If there are n variables in a physical phenomenon and these contain m fundamental dimensions (M, L, T), then the variables can be grouped into **(n - m)** dimensionless π terms.

$$f(X_1, X_2, ..., X_n) = 0$$
$$\phi(\pi_1, \pi_2, ..., \pi_{n-m}) = 0$$

**Steps:**
1. List all n variables involved
2. Determine m (number of fundamental dimensions)
3. Select m **repeating variables** (must contain all m dimensions among them, should not form a dimensionless group themselves)
   - Usually choose: one geometric (L or D), one kinematic (V), one dynamic (ρ)
4. Form each π term by combining repeating variables with one of the remaining variables
5. Solve for exponents in each π term using dimensional homogeneity
6. Write the final functional relationship

**Rules for selecting repeating variables:**
- Should collectively contain all fundamental dimensions
- Should NOT form a dimensionless group
- Dependent variable should NOT be a repeating variable
- Preference: geometric > kinematic > dynamic variables

---

## 3.2 Dimensionless Numbers

| Number | Formula | Significance | Ratio |
|--------|---------|-------------|-------|
| **Reynolds (Re)** | ρVL/μ | Viscous flow | Inertia / Viscous |
| **Froude (Fr)** | V/√(gL) | Free surface flow | Inertia / Gravity |
| **Euler (Eu)** | V/√(p/ρ) | Pressure flow | Inertia / Pressure |
| **Weber (We)** | V/√(σ/ρL) | Surface tension flow | Inertia / Surface tension |
| **Mach (Ma)** | V/C | Compressible flow | Inertia / Elastic |

---

## 3.3 Similitude & Model Studies

### Types of Similarity

1. **Geometric Similarity**: Model and prototype have the same shape (linear scale ratio Lr = Lp/Lm)
2. **Kinematic Similarity**: Velocity and acceleration ratios are the same at corresponding points
3. **Dynamic Similarity**: Force ratios are the same at corresponding points (all relevant dimensionless numbers are equal)

### Types of Models

1. **Undistorted Models**: Geometric similarity is maintained in all directions (Lr horizontal = Lr vertical)
2. **Distorted Models**: Different scale ratios for horizontal and vertical dimensions

### Model Laws (Similarity Laws)

| Law | Criterion | Application |
|-----|-----------|-------------|
| **Reynolds Model Law** | (Re)m = (Re)p | Pipe flow, submarine, aircraft |
| **Froude Model Law** | (Fr)m = (Fr)p | Open channel, spillways, weirs |
| **Euler Model Law** | (Eu)m = (Eu)p | Pressure-dominated flow |
| **Weber Model Law** | (We)m = (We)p | Capillary flows |
| **Mach Model Law** | (Ma)m = (Ma)p | Compressible flow, aerodynamics |

### Froude Model Law Scale Ratios (Most Important for Hydraulics)

If length scale ratio = Lr:

| Quantity | Scale Ratio |
|----------|-------------|
| Length | Lr |
| Velocity | Lr^(1/2) |
| Time | Lr^(1/2) |
| Discharge | Lr^(5/2) |
| Force | Lr³ |
| Pressure | Lr |
| Power | Lr^(7/2) |
| Roughness | Lr^(1/6) (Manning's n) |

### Distorted Models

**Reasons for distortion:**
- To maintain turbulent flow in the model
- To reduce model size
- To maintain accurate bed material movement
- To obtain measurable velocities and depths

**Advantages:**
- Vertical exaggeration makes measurements easier
- Reduces cost and space

**Disadvantages:**
- Velocity distribution is not truly similar
- Wave patterns are distorted
- Extrapolation of results is uncertain

---

## 3.4 Force on Jets (Turbo Machinery Basics)

### Force on a Stationary Flat Plate (Normal to Jet)

$$F = \rho a V^2$$

where a = area of jet, V = velocity of jet

### Force on a Stationary Flat Plate (Inclined at angle θ)

$$F_n = \rho a V^2 \sin\theta$$

- Component along jet: $F_x = \rho a V^2 \sin^2\theta$
- Component perpendicular: $F_y = \rho a V^2 \sin\theta \cos\theta$

### Force on a Moving Flat Plate

$$F = \rho a (V - u)^2$$

where u = velocity of plate

- Work done/sec = F × u = ρa(V-u)²u
- Efficiency: $\eta = \frac{2u(V-u)^2}{V^3}$ (for normal plate)
- Maximum efficiency occurs when **u = V/3**, giving **η_max = 8/27 = 29.6%**

### Force on a Stationary Curved Vane

For a curved vane deflecting jet through angle θ:

$$F_x = \rho a V^2 (1 + \cos\theta)$$
$$F_y = \rho a V^2 \sin\theta$$

If the vane is semicircular (θ = 180°):
$$F_x = 2\rho a V^2$$ (double the force of flat plate!)

### Force on a Moving Curved Vane (Single)

Replace V with relative velocity (V - u):

$$F_x = \rho a (V - u)^2 (1 + \cos\theta)$$

- Work done/sec = Fx × u
- Maximum efficiency when **u = V/2** (for semicircular vane: η_max = 100% theoretically)

### Force on a Series of Vanes (Turbine Runner)

$$F_x = \rho a V (V - u)(1 + \cos\theta)$$

(All water is utilized, unlike single vane)

- Work done/sec = ρaV(V-u)(1 + cosθ) × u
- Maximum efficiency when **u = V/2**
- For semicircular vane: **η_max = 100%**

---

## 3.5 Velocity Triangles

### At Inlet of Runner
- **V₁** = absolute velocity of water at inlet
- **u₁** = tangential velocity of vane at inlet = πD₁N/60
- **Vr₁** = relative velocity at inlet
- **Vw₁** = whirl velocity (tangential component of V₁) = V₁cosα₁
- **Vf₁** = flow velocity (radial component of V₁) = V₁sinα₁
- **α₁** = guide vane angle (angle of V₁ with u₁)
- **β₁** = vane angle at inlet (angle of Vr₁ with u₁)

### At Outlet of Runner
- Similar notation with subscript 2
- For maximum efficiency: **Vw₂ = 0** (whirl at outlet = 0)

### Vector Relationship
$$\vec{V} = \vec{u} + \vec{V_r}$$

$$V_{w1} = V_1 \cos\alpha_1$$
$$V_{f1} = V_1 \sin\alpha_1$$

### Euler's Equation (Work done per second)

$$W = \rho Q (V_{w1}u_1 \pm V_{w2}u_2)$$

(+ if Vw₂ and u₂ are in opposite directions)
(- if Vw₂ and u₂ are in same direction)

For maximum efficiency, Vw₂ = 0:
$$W = \rho Q V_{w1} u_1$$

### Work done per unit weight (Head)

$$H_e = \frac{1}{g}(V_{w1}u_1 \pm V_{w2}u_2)$$

This is also called **Euler's head**.

### Degree of Reaction

$$R = 1 - \frac{V_{w1}u_1}{2gH}$$

- R = 0: Impulse turbine (Pelton wheel)
- R = 0.5: 50% reaction (Francis turbine typical)

### Angular Momentum

$$\text{Torque} = \rho Q (V_{w1}r_1 - V_{w2}r_2)$$

---

---

# UNIT IV — HYDRAULIC TURBINES

## 4.1 Hydroelectric Power Plant — Elements

### Main Components:
1. **Dam/Reservoir**: Stores water at height
2. **Penstock**: Pipe carrying water from reservoir to turbine
3. **Turbine**: Converts hydraulic energy to mechanical energy
4. **Draft tube**: Connects turbine exit to tailrace (recovers kinetic energy)
5. **Tailrace**: Channel carrying water away after passing through turbine
6. **Generator**: Converts mechanical energy to electrical energy
7. **Surge tank**: Controls water hammer in penstock

---

## 4.2 Heads and Efficiencies

### Types of Heads

| Head | Definition |
|------|-----------|
| **Gross Head (Hg)** | Difference between headwater and tailwater levels |
| **Net/Effective Head (H)** | Hg - losses in penstock = H available at turbine inlet |
| **Velocity Head** | V²/2g |
| **Pressure Head** | p/ρg |

$$H = H_g - h_f$$

where hf = friction and other losses in penstock

### Types of Efficiencies

**1. Hydraulic Efficiency (ηh):**
$$\eta_h = \frac{\text{Power developed by runner}}{\text{Power supplied by water}} = \frac{V_{w1}u_1}{gH}$$

(assuming Vw₂ = 0)

**2. Mechanical Efficiency (ηm):**
$$\eta_m = \frac{\text{Power at shaft}}{\text{Power developed by runner}} = \frac{P_{shaft}}{P_{runner}}$$

**3. Volumetric Efficiency (ηv):**
$$\eta_v = \frac{Q - \Delta Q}{Q}$$

where ΔQ = leakage

**4. Overall Efficiency (ηo):**
$$\eta_o = \eta_h \times \eta_m \times \eta_v = \frac{P_{shaft}}{\rho g Q H}$$

---

## 4.3 Classification of Turbines

| Basis | Type 1 | Type 2 |
|-------|--------|--------|
| **Energy at inlet** | Impulse (Pelton) | Reaction (Francis, Kaplan) |
| **Direction of flow** | Tangential | Radial / Axial / Mixed |
| **Head** | High head | Medium / Low head |
| **Specific speed** | Low Ns | Medium / High Ns |

---

## 4.4 Pelton Wheel (Impulse Turbine)

### Working Principle
- Water from nozzle strikes **buckets/cups** on the runner
- All pressure energy converted to kinetic energy in the nozzle (no pressure change in runner)
- **Impulse turbine**: Pressure at inlet and outlet of runner is atmospheric

### Key Components
1. **Nozzle with spear (needle) valve**: Controls jet discharge
2. **Runner with buckets**: Double-hemispherical (splitter) cups
3. **Casing**: Prevents splashing
4. **Braking jet**: To stop the wheel quickly
5. **Deflector**: Diverts jet away during sudden load rejection

### Key Relationships

**Jet velocity:**
$$V_1 = C_v \sqrt{2gH}$$

where Cv = coefficient of velocity (0.97-0.99)

**Velocity of bucket:**
$$u = \frac{\pi D N}{60}$$

where D = pitch circle diameter

**Speed ratio (φ):**
$$\phi = \frac{u}{V_1} = \frac{u}{\sqrt{2gH}}$$

Optimum: **φ = 0.46** (theoretical = 0.5)

**Hydraulic efficiency:**
$$\eta_h = \frac{2(V_1 - u)(1 + \cos\phi)u}{V_1^2}$$

Maximum when u = V₁/2:
$$\eta_{h,max} = \frac{1 + \cos\phi}{2}$$

For φ = 165° to 170°: η_h,max ≈ 98%

**Number of buckets:**
$$z = 15 + \frac{D}{2d}$$

where d = jet diameter

**Number of jets**: Usually 1-6 (to increase power without increasing runner size)

**Jet ratio**: m = D/d (usually 12 for maximum efficiency)

---

## 4.5 Francis Turbine (Reaction Turbine — Inward Radial Flow)

### Working Principle
- Water enters **radially inward** and exits **axially**
- Both pressure and velocity change in the runner (reaction turbine)
- Runner is always submerged (runs full of water)

### Key Components
1. **Spiral/Scroll casing**: Distributes water uniformly around runner, area decreases gradually
2. **Stay vanes**: Structural support
3. **Guide vanes (wicket gates)**: Control discharge and direction of flow, adjustable
4. **Runner**: Has curved vanes (12-16 blades)
5. **Draft tube**: Recovers kinetic energy at runner exit

### Key Relationships

**Discharge:**
$$Q = \pi D_1 B_1 V_{f1} = \pi D_2 B_2 V_{f2}$$

where B = width of runner

**Work done per second:**
$$P = \rho Q (V_{w1}u_1 - V_{w2}u_2)$$

For best efficiency: Vw₂ = 0 (discharge is purely axial)

**Speed ratio:** φ = u₁/√(2gH) = 0.6 to 0.9

**Flow ratio:** ψ = Vf₁/√(2gH) = 0.15 to 0.3

**Degree of reaction:** R = 1 - Vw₁u₁/(2gH)

Typical: R = 0.5 to 0.7

**Applicable head range:** 30m to 300m (medium head)

**Specific speed range:** 60 to 300

---

## 4.6 Kaplan Turbine (Reaction Turbine — Axial Flow)

### Working Principle
- Water flows **axially** through the runner (parallel to the axis)
- Runner has **adjustable blades** (like a propeller)
- Used for **low heads and high discharges**

### Key Features
- Runner has 3-8 blades (fewer than Francis)
- **Both guide vanes and runner blades are adjustable** → double regulation
- Hub (boss) diameter ratio: d/D = 0.35 to 0.6
- More efficient than Francis at part loads due to blade adjustment

### Key Relationships

**Same as Francis**, but:

$$Q = \frac{\pi}{4}(D^2 - d^2) V_f$$

where D = outer diameter, d = hub diameter

**Speed ratio:** φ = u/√(2gH) = 1.4 to 2.0

**Flow ratio:** ψ = Vf/√(2gH) = 0.35 to 0.75

**Applicable head range:** 2m to 70m (low head)

**Specific speed range:** 300 to 900

---

## 4.7 Comparison of Turbines

| Parameter | Pelton | Francis | Kaplan |
|-----------|--------|---------|--------|
| Type | Impulse | Reaction | Reaction |
| Flow | Tangential | Radial inward→axial | Axial |
| Head | High (>250m) | Medium (30-300m) | Low (2-70m) |
| Speed | Low | Medium | High |
| Specific speed (Ns) | 10-35 | 60-300 | 300-900 |
| Efficiency | 85-90% | 90-94% | 90-93% |
| Number of blades | 15-25 buckets | 12-16 | 3-8 |
| Regulation | Nozzle/spear | Guide vanes | Guide vanes + runner blades |
| Draft tube | Not needed | Needed | Needed |

---

## 4.8 Draft Tube

A **gradually expanding tube** connecting turbine exit to tailrace.

### Purpose:
1. Allows turbine to be placed above tailrace level (for maintenance)
2. Recovers kinetic energy at runner exit → increases net head and efficiency
3. Creates suction (negative pressure) at runner exit

### Draft Tube Theory

Applying Bernoulli's between runner exit (2) and tailwater (3):

$$\frac{p_2}{\rho g} = H_s - \frac{V_2^2 - V_3^2}{2g} + h_f$$

where Hs = height of runner exit above tailrace

**Efficiency of draft tube:**

$$\eta_d = \frac{V_2^2 - V_3^2 - h_f \cdot 2g}{V_2^2}$$

### Types of Draft Tubes

1. **Conical (straight divergent)**: Simple, η ≈ 90%, used for low Ns
2. **Moody spreading (bell-shaped)**: Reduces whirl, η ≈ 85%
3. **Simple elbow**: Saves excavation, η ≈ 60%
4. **Elbow with circular to rectangular transition**: Most common, η ≈ 60%

---

## 4.9 Governing of Turbines

Maintains **constant speed** despite load variations.

### Components:
1. **Centrifugal governor / Pendulum**: Senses speed change
2. **Servo motor (hydraulic)**: Amplifies governor signal
3. **Relay valve / Control valve**: Directs oil to servo motor
4. **Spear valve (Pelton) / Guide vanes (Francis/Kaplan)**: Controls water flow

### Working:
- Load decreases → speed increases → governor balls fly out → sleeve rises → relay valve opens → servo motor closes guide vanes/spear → reduced flow → speed returns to normal
- Load increases → opposite process

---

## 4.10 Surge Tanks

A **vertical tank** connected to the penstock to control **water hammer** pressure.

### Purpose:
1. Protect penstock from water hammer
2. Act as a supply reservoir during sudden load increase
3. Provide regulated flow to the turbine

### Types:
1. **Simple surge tank**: Open cylindrical tank
2. **Restricted orifice**: Has a restricted opening at the bottom → better damping
3. **Differential surge tank**: Has a small inner riser and large outer tank

---

## 4.11 Unit Quantities

Used to compare performance of same turbine under different heads.

### Unit Speed:
$$N_u = \frac{N}{\sqrt{H}}$$

### Unit Discharge:
$$Q_u = \frac{Q}{\sqrt{H}}$$

### Unit Power:
$$P_u = \frac{P}{H^{3/2}}$$

### Relationships:
If a turbine operates at (N₁, Q₁, P₁) under H₁, and we want values at H₂:

$$N_2 = N_1 \sqrt{\frac{H_2}{H_1}}$$

$$Q_2 = Q_1 \sqrt{\frac{H_2}{H_1}}$$

$$P_2 = P_1 \left(\frac{H_2}{H_1}\right)^{3/2}$$

---

## 4.12 Specific Speed

**Definition**: Speed of a geometrically similar turbine that produces **unit power (1 kW) under unit head (1 m)**.

$$N_s = \frac{N \sqrt{P}}{H^{5/4}}$$

where:
- N = speed in rpm
- P = power in kW
- H = net head in m

### Importance:
- Determines the **type of turbine** to use
- Higher Ns → lower head, higher discharge

| Ns Range | Turbine Type |
|----------|-------------|
| 10 - 35 | Pelton (single jet) |
| 35 - 60 | Pelton (multi-jet) |
| 60 - 300 | Francis |
| 300 - 900 | Kaplan / Propeller |

---

## 4.13 Performance Characteristics

### Main Characteristic Curves (at constant speed N)
- Plot η, Q, P against varying head H
- Or: Plot η, P against varying Q at constant N

### Operating Characteristic Curves (at constant speed)
- Plot η, P, Q against varying gate opening (load)

### Muschel Curves (Iso-efficiency / Hill Charts)
- Contours of equal efficiency plotted on a graph of N (or N₁₁) vs Q (or Q₁₁)
- Used to find the **best operating point**

---

## 4.14 Geometric Similarity & Model Testing

For geometrically similar turbines (model m, prototype p):

$$\frac{N_m}{N_p} = \frac{D_p}{D_m} \sqrt{\frac{H_m}{H_p}}$$

$$\frac{Q_m}{Q_p} = \left(\frac{D_m}{D_p}\right)^3 \frac{N_m}{N_p}$$

$$\frac{P_m}{P_p} = \left(\frac{D_m}{D_p}\right)^5 \left(\frac{N_m}{N_p}\right)^3$$

$$N_{s,m} = N_{s,p}$$

---

## 4.15 Cavitation in Turbines

**Cavitation** occurs when local pressure falls below the **vapor pressure** of water, forming vapor bubbles that collapse violently, causing damage.

### Thoma's Cavitation Number (σ):

$$\sigma = \frac{H_a - H_v - H_s}{H}$$

where:
- Ha = atmospheric pressure head
- Hv = vapor pressure head
- Hs = suction head (height of runner above tailwater)
- H = net head on turbine

**Critical cavitation number (σc)**: Below this, cavitation occurs.

$$\sigma > \sigma_c$$ → No cavitation (safe)

### Prevention of Cavitation:
1. Install turbine below tailwater level (reduce Hs)
2. Use cavitation-resistant materials (stainless steel)
3. Proper design of runner blades
4. Operate turbine at design conditions

### Selection of Turbines

| Criterion | Decision |
|-----------|----------|
| Head > 250m | Pelton wheel |
| Head 30-250m | Francis turbine |
| Head < 30m | Kaplan turbine |
| Also consider: | Specific speed, efficiency, cost, size |

---

---

# UNIT V — CENTRIFUGAL PUMPS & RECIPROCATING PUMPS

## 5.1 Centrifugal Pump — Introduction

A centrifugal pump converts **mechanical energy to hydraulic energy** by means of centrifugal force acting on the fluid.

### Main Components:
1. **Impeller**: Rotating element with curved vanes, adds energy to fluid
2. **Casing**: 
   - Volute casing (spiral shaped, converts velocity to pressure)
   - Vortex casing (circular space between impeller and volute)
   - Diffuser casing (guide vanes around impeller)
3. **Suction pipe with foot valve and strainer**
4. **Delivery pipe with delivery valve**

### Classification of Centrifugal Pumps

| Basis | Types |
|-------|-------|
| Casing | Volute, Vortex, Diffuser |
| Impeller | Closed, Semi-open, Open |
| Number of stages | Single-stage, Multi-stage |
| Suction | Single suction, Double suction |
| Flow direction | Radial, Mixed, Axial |

---

## 5.2 Work Done by Centrifugal Pump

$$W = \rho Q (V_{w2}u_2 - V_{w1}u_1)$$

For **radial entry** (Vw₁ = 0, α₁ = 90°):

$$W = \rho Q V_{w2} u_2$$

### Euler's Head (ideal head):

$$H_e = \frac{V_{w2}u_2}{g}$$

---

## 5.3 Heads in Centrifugal Pumps

### Suction Head (hs)
Vertical height of pump centre above water surface in sump

### Delivery Head (hd)
Vertical height of outlet above pump centre

### Static Head (Hs)
$$H_s = h_s + h_d$$

### Manometric Head (Hm)
Total head against which the pump has to work:

$$H_m = h_s + h_d + h_{fs} + h_{fd} + \frac{V_d^2}{2g}$$

where hfs, hfd = friction losses in suction and delivery pipes

**OR equivalently:**

$$H_m = \frac{V_{w2}u_2}{g} - \text{losses in pump}$$

$$H_m = \eta_h \times \frac{V_{w2}u_2}{g}$$

---

## 5.4 Efficiencies

### Manometric Efficiency (ηman):
$$\eta_{man} = \frac{gH_m}{V_{w2}u_2}$$

### Mechanical Efficiency (ηmech):
$$\eta_{mech} = \frac{\rho Q V_{w2}u_2}{\text{Power input to shaft}}$$

### Overall Efficiency (ηo):
$$\eta_o = \frac{\rho g Q H_m}{P_{shaft}} = \eta_{man} \times \eta_{mech} \times \eta_{vol}$$

### Volumetric Efficiency (ηvol):
$$\eta_{vol} = \frac{Q}{Q + Q_L}$$

where QL = leakage

---

## 5.5 Minimum Starting Speed

For the pump to start delivering, the centrifugal head must overcome the manometric head:

$$\frac{u_2^2 - u_1^2}{2g} \geq H_m$$

$$N_{min} = \frac{60}{\pi} \sqrt{\frac{2g H_m}{D_2^2 - D_1^2}}$$

Or, using manometric efficiency:

$$N_{min} = \frac{60}{2\pi} \sqrt{\frac{2g \eta_{man} V_{w2} u_2}{D_2^2 - D_1^2}}$$

---

## 5.6 Losses and Efficiencies Summary

| Loss | Location |
|------|----------|
| Hydraulic losses | Friction in impeller passages, shock losses |
| Mechanical losses | Bearing friction, disc friction |
| Leakage losses | Through clearance between impeller and casing |

---

## 5.7 Specific Speed of Pump

$$N_s = \frac{N\sqrt{Q}}{H_m^{3/4}}$$

where:
- N = speed (rpm)
- Q = discharge (m³/s)
- Hm = manometric head (m)

**Note**: For pump Ns, we use Q (not P as in turbines)

| Ns Range | Pump Type |
|----------|-----------|
| 10-30 | Slow speed radial |
| 30-50 | Medium speed radial |
| 50-80 | High speed radial |
| 80-160 | Mixed flow |
| 160-500 | Axial flow (propeller) |

---

## 5.8 Multistage Pumps

### For High Head (Series arrangement):
- Impellers mounted on **same shaft** in series
- Total head = n × Hm (n = number of stages)
- Discharge remains same

### For High Discharge (Parallel arrangement):
- Pumps working in parallel, each connected to common delivery pipe
- Total discharge = n × Q
- Head remains same

---

## 5.9 Pumps in Parallel

- Each pump has the **same head** but contributes a share of total discharge
- Used when a single pump cannot provide the required discharge
- Total Q = Q₁ + Q₂ + ...
- System head curve determines operating point

---

## 5.10 Characteristic Curves of Centrifugal Pump

### Main Characteristics (at constant speed):
- Plot Hm, P, η vs Q

### Operating Characteristics (at constant speed):
- Same as main characteristics but most commonly used

### Key features of the H-Q curve:
- Head decreases as discharge increases
- Maximum η at design point (Best Efficiency Point — BEP)
- Power generally increases with discharge

### Iso-efficiency Curves
- Contours of constant efficiency on N vs Q plot
- Used to find best operating range

---

## 5.11 NPSH (Net Positive Suction Head)

**NPSH** = Total suction head available at pump inlet above vapor pressure

$$NPSH = \frac{p_a}{\rho g} - \frac{p_v}{\rho g} - h_s - h_{fs}$$

where:
- pa = atmospheric pressure
- pv = vapor pressure
- hs = suction lift
- hfs = friction loss in suction pipe

### NPSH Available (NPSHA):
The actual NPSH at the installation

### NPSH Required (NPSHR):
Minimum NPSH required by the pump (from manufacturer)

**Condition for no cavitation:**
$$NPSH_A > NPSH_R$$

---

## 5.12 Cavitation in Pumps

Same phenomenon as in turbines — vapor bubble formation and collapse.

### Thoma's Cavitation Parameter:

$$\sigma = \frac{NPSH}{H_m}$$

$$\sigma > \sigma_c$$ → Safe operation

### Prevention:
1. Reduce suction lift
2. Use larger suction pipe (reduce friction)
3. Avoid sharp bends in suction pipe
4. Keep pump close to water level
5. Use priming to remove air

---

## 5.13 Priming

**Priming** = Filling the suction pipe, pump casing, and delivery pipe (up to delivery valve) with water to remove air before starting the pump.

**Why needed**: Centrifugal pump cannot pump air (centrifugal force on air is negligible due to low density)

**Methods**: Manual filling, vacuum pump, self-priming design

---

## 5.14 Reciprocating Pumps

### Working Principle
A piston/plunger moves back and forth in a cylinder:
- **Suction stroke**: Piston moves backward → creates vacuum → suction valve opens → water drawn in
- **Delivery stroke**: Piston moves forward → pressure increases → delivery valve opens → water pushed out

### Types:
1. **Single-acting**: Water on one side of piston only
2. **Double-acting**: Water on both sides of piston

### Discharge

**Single-acting:**
$$Q = \frac{ALN}{60}$$

where A = area of piston, L = stroke length, N = speed (rpm)

**Double-acting:**
$$Q = \frac{2ALN}{60}$$ (approximately, ignoring piston rod area)

More precisely:
$$Q = \frac{(2A - a)LN}{60}$$

where a = area of piston rod

---

## 5.15 Slip

$$\text{Slip} = Q_{theoretical} - Q_{actual}$$

$$\% \text{Slip} = \frac{Q_{th} - Q_{act}}{Q_{th}} \times 100$$

$$C_d = \frac{Q_{act}}{Q_{th}} = 1 - \text{Slip}$$

**Negative slip**: When Qactual > Qtheoretical (happens at high speeds with long suction pipe)

---

## 5.16 Indicator Diagrams

A graph of pressure in the cylinder vs. stroke (or volume displaced).

### Ideal Indicator Diagram
- Rectangle with area = work done per stroke
- **Work done = ρgAL(hs + hd)**

### Effect of Acceleration

Acceleration head:
$$h_a = \frac{l}{g} \times \frac{A}{a} \times \omega^2 r \cos\theta$$

where:
- l = length of pipe
- A/a = ratio of piston area to pipe area
- ω = angular velocity = 2πN/60
- r = crank radius = L/2

**Maximum acceleration head** (at θ = 0° and θ = 180°):
$$h_{a,max} = \frac{l}{g} \times \frac{A}{a} \times \omega^2 r$$

### Effect of Friction

Friction head:
$$h_f = \frac{f l}{g \times d} \times \left(\frac{A}{a}\right)^2 \times \omega^2 r^2 \sin^2\theta$$

**Maximum friction head** (at θ = 90°, mid-stroke):
$$h_{f,max} = \frac{f l}{g d} \times \left(\frac{A}{a}\right)^2 \times \omega^2 r^2$$

### Modified Indicator Diagram
- Acceleration modifies the straight lines to sinusoidal curves
- Friction adds a parabolic curve on top
- **Work done remains the same** (acceleration head averages to zero)
- But **friction increases work done**:
$$W = \rho g A L \left(h_s + h_d + \frac{2}{3}h_{fs} + \frac{2}{3}h_{fd}\right)$$

### Separation
If acceleration pressure drops below 2.5 m (abs), dissolved gases come out and **separation** occurs. This limits the maximum speed of the pump.

---

## 5.17 Air Vessels

A **closed chamber** connected to suction/delivery pipe to:
1. **Reduce acceleration head** → smoother flow → allows higher speed
2. **Reduce friction losses** → saves power
3. **Obtain uniform discharge** (even though piston motion is reciprocating)

### Work saved by fitting air vessels

**For single-acting pump:**
- Friction work without air vessel: (2/3) × hf × ALρg
- Friction work with air vessel: Uses mean velocity instead of varying velocity
- **Work saved ≈ 84.8%** in friction for suction/delivery side

**For double-acting pump:**
- **Work saved ≈ 39.2%**

---

---

# 📝 IMPORTANT FORMULAS — QUICK REFERENCE

## Open Channel Flow
| Formula | Expression |
|---------|-----------|
| Chezy's | V = C√(RS) |
| Manning's | V = (1/n)R^(2/3)S^(1/2) |
| Froude No. | Fr = V/√(gD) |
| Critical depth (rect.) | yc = (q²/g)^(1/3) |
| Specific energy | E = y + V²/2g |
| Ec (rectangular) | Ec = 1.5yc |
| GVF equation | dy/dx = (S₀ - Sf)/(1 - Fr²) |
| Hydraulic jump | y₂/y₁ = ½(-1 + √(1+8Fr₁²)) |
| Energy loss (jump) | ΔE = (y₂-y₁)³/(4y₁y₂) |

## Dimensional Analysis
| Formula | Expression |
|---------|-----------|
| π terms | n - m dimensionless groups |
| Reynolds No. | Re = ρVL/μ |
| Froude No. | Fr = V/√(gL) |

## Turbines
| Formula | Expression |
|---------|-----------|
| Euler's equation | W = ρQ(Vw₁u₁ ± Vw₂u₂) |
| Hydraulic η | ηh = Vw₁u₁/(gH) |
| Specific speed | Ns = N√P / H^(5/4) |
| Unit speed | Nu = N/√H |
| Unit discharge | Qu = Q/√H |
| Unit power | Pu = P/H^(3/2) |
| Thoma's σ | σ = (Ha - Hv - Hs)/H |

## Pumps
| Formula | Expression |
|---------|-----------|
| Manometric head | Hm = hs + hd + hfs + hfd + Vd²/2g |
| Manometric η | ηman = gHm/(Vw₂u₂) |
| Specific speed | Ns = N√Q / Hm^(3/4) |
| NPSH | = pa/ρg - pv/ρg - hs - hfs |
| Q (single-acting) | Q = ALN/60 |
| Q (double-acting) | Q = 2ALN/60 |
| Acceleration head | ha = (l/g)(A/a)ω²r cosθ |

---

**ALL THE BEST FOR YOUR EXAM!** 🎓✨
