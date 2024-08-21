---
icon: stomach
---

# Thermal phygiology model

## Overview

The thermal physiology model within the ABC is based on [Stowijk's model](https://chrome-extension/efaidnbmnnnibpcajpcglclefindmkaj/https://ntrs.nasa.gov/api/citations/19710023925/downloads/19710023925.pdf) of human thermal regulation but includes several significant improvements. Our model allows unlimited body segments (compared to six in the Stolwijk model) and has 16 body segments as default. They are the head, chest, back, pelvis, right and left upper arms, right and left lower arms, right and left hands, right and left thighs, right and left lower legs, and right and left feet. Each segment is modeled as four body layers (core, muscle, fat, and skin tissues) and a clothing layer. The model calculates heat transfer within and between these segments and the environment.&#x20;

Physiological mechanisms such as vasodilation, vasoconstriction, sweating, and metabolic heat production are explicitly considered. Convection, conduction (such as to a car seat or other surface in contact with any part of the body), and radiation between the body and the environment are treated independently. The model can predict human physiological responses to transient, non-uniform thermal environments.

Read more about [our physiological model written by Huizenga et al](https://doi.org/10.1016/S0360-1323\(00\)00061-5).

<figure><img src="../../.gitbook/assets/image (55).png" alt=""><figcaption><p>Model diagram: The body is divided into 16 segments, and each segment transfers the heat through convection, radiation, conduction, and so on with the human thermoregulation system.</p></figcaption></figure>

## Passive system

### Basics of lumped heat capacity model

The ABC model is a lumped heat capacity model that assumes uniform temperature throughout an object's interior. This method is commonly used for building heat transfer, ventilation, and electricity calculations, and so on.

**Calculating a person's body temperature is similar to solving the room temperature at a given time. Let's look at the very simple example below.**&#x20;

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption><p>Simple example of heat exchange between house and outside</p></figcaption></figure>

Given the conditions above, the indoor temperature _T_in can be calculated by solving the following differential equation related to energy as equation (1). The heat flux between inside and outside can be calculated as equation (2). Here, heat transfer coefficient _h_ is the reciprocal of the sum of the resistance values of the indoor and outdoor areas. The resistance values are generally determined by the insulation level of the building and the outdoor air.

$$
C \frac{d T_{\text{in}}}{dt} = Q - q...(1)
$$

$$
q = hA (T_{\text{in}} - T_{\text{out}})...(2)
$$

Where:

* $$𝐶$$: Heat capacity (J/K)
* $$ℎ$$: Heat transfer coefficient (W/(m2・K))
* $$𝐴$$: Area (m²)
* $$𝑇_{in}$$: Indoor temperature (oC)
* $$𝑇_{out}$$: Outdoor temperature (oC)

Below is an example of a simple indoor temperature calculation. Given the physical properties of the building and indoor heat load, we calculate the change in indoor temperature starting from 20 C, with the outside temperature fixed at 0 degrees. The result shows that the indoor temperature decreases from 20 C and reaches approximately 6 C after about 60 minutes.

<figure><img src="../../.gitbook/assets/example_transient_heat_transfer (5).svg" alt=""><figcaption><p>Example of transient heat transfer calculation</p></figcaption></figure>

The code is here. In this program, the differential equation is solved using [the forward difference method (Explicit Euler method)](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter22.03-The-Euler-Method.html). Implementing the forward difference method is easier than the backward difference method but is limited regarding time steps. Note that the solution diverges if you set up a higher value of time step than a certain threshold. This may be a bit geeky, but if you are more interested, you can search how to determine the time increments.

<details>

<summary>Click to expand an example Python code</summary>

```python
import os
import numpy as np
import matplotlib.pyplot as plt

# Parameter settings
C = 500000  # Heat capacity of room air (J/K), calculated for an average house
h = 2  # Heat transfer coefficient (W/(m^2ã»K))
A = 400  # Surface area through which heat escapes (m^2)
T_out = 0  # Outdoor temperature (Â°C)
Q = 5000  # Heat supplied from a heat source (W), assuming a moderate heating system
T_initial = 20  # Initial indoor temperature (Â°C)

# Time settings
t_end = 3600  # Total time for calculation (seconds)
dt = 60  # Time step (seconds)

# Number of time steps
n_steps = int(t_end / dt)

# Initial conditions
temperatures = np.zeros(n_steps)
temperatures[0] = T_initial

# Solving the equation using the Explicit Euler Method
for i in range(1, n_steps):
    dTdt = (Q - h * A * (temperatures[i - 1] - T_out)) / C
    temperatures[i] = temperatures[i - 1] + dTdt * dt

# Generating the time axis
time = np.linspace(0, t_end / 60, n_steps)  # Convert seconds to minutes

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(time, temperatures, label="Room Temperature", marker="o")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (Â°C)")
plt.title("Room Temperature Over Time")
plt.legend()
plt.grid(True)

save_path = "/abc_model_official_documenation/figure"
plt.savefig(os.path.join(save_path, "example_transient_heat_transfer.svg"))
plt.show()

```

</details>

### Thermal network between nodes

In the ABC model, the thermal network is more complex than the example above. The heat exchange within the body can be divided into four conditions based on the presence or absence of clothing and contact, as shown in the diagram below. The model calculates heat exchange with heat capacity for the core, muscles, fat, skin, and clothing. A heat balance equation is constructed for each node, and the temperatures of each node are calculated by solving simultaneous equations for the number of components. The values for thermal resistance and heat capacity of each node are based on [Stowijk's model](https://chrome-extension/efaidnbmnnnibpcajpcglclefindmkaj/https://ntrs.nasa.gov/api/citations/19710023925/downloads/19710023925.pdf).

{% hint style="success" %}
As of 2024, the parameter values, formulas, and programs of the ABC model have not been publicly available, but you can refer to a similar model, [JOS-3](https://doi.org/10.1016/j.enbuild.2020.110575), which is also based on the Stolwijk model.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (50).png" alt=""><figcaption><p>Segment node structure showing four parallel heat paths: top, exposed skin with convective and radiant heat loss, second from top, clothed skin with convection and radiant heat loss; third, clothed skin with conductive loss to contact surface; bottom, bare skin.</p></figcaption></figure>

## Active system

In addition to heat transfer between each node, the ABC model can simulate human thermoregulation. This section explains the basics of thermoregulation and its mathematical formulation.

### Basics of human body thermoregulation

The human body employs sophisticated mechanisms to maintain thermal equilibrium, ensuring our core temperature is kept within a safe range. Two critical responses are triggered depending on whether we're exposed to high or low temperatures, thereby mitigating the risk of temperature-related illnesses. Through these four primary thermoregulation mechanisms - **vasoconstriction** and **shivering** when cold, and **vasodilation** and **sweating** when warm - the body skillfully maintains its thermal equilibrium, protecting against both hyperthermia and hypothermia.



* **Responses to high temperatures**
  * **Vasodilation**: The body responds by dilating blood vessels near the skin's surface. This vasodilation increases blood flow to the skin, allowing for more efficient heat release into the surrounding environment, thus aiding in the cooling process in the body core.
  * **Sweating**: When it is difficult to maintain the core temperature only by vasodilation, our bodies begin to sweat. This process facilitates the loss of latent heat from the skin's surface, effectively cooling the skin and, subsequently, the body's core temperature.
* #### Responses to low temperatures
  * **Vasoconstriction**: Vasoconstriction occurs when body temperature is low, reducing blood flow to the skin by contracting surface blood vessels. This minimizes heat loss from the skin's surface, aiding in heat preservation.
  * **Shivering**: As temperatures drop, the body initiates shivering. This muscle activity generates heat, preserving the body's core temperature.

<figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption><p>Human body change under different ambient temperature</p></figcaption></figure>

### Modeling of human body thermoregulation

In the model, to mathematically describe the thermoregulatory mechanisms, the difference between the set-point temperature _T_set (similar to the set temperature of an air conditioner) and the actual body temperature _T_ is treated as the error signal _Error_ to determine the degree of thermoregulation. Set point temperature is defined as the body temperature in a thermally neutral state. Skin blood flow and sweating increase as the difference between the current temperature and the set-point temperature increases. As the difference decreases, skin blood flow decreases, and shivering thermogenesis increases.&#x20;

$$
Error = T -  T_{set}
$$

{% hint style="info" %}
This model calculates the temperature and set-point temperature for 16 different body regions, so it integrates these signals by computing a weighted average based on each region's sensitivity.
{% endhint %}

## Other features

### Bodybuilder

Most thermal comfort or thermoregulatory models specify a standard man for simulation (body surface area = 1.8m2). These anthropometric parameters have a significant influence over the determination of heat exchange both within the body segments and between its surrounding environment. The ABC model allows users to customize the geometry and physiology of the human being modelled based on simple input parameters (such as weight, height, age, gender) to better account for individual differences. The table below lists physiological data modified by bodybuilder function.&#x20;

Physiological data modified by body builder function (cited by [the Huizenga's paper](https://doi.org/10.1016/S0360-1323\(00\)00061-5))

| Parameter                                                    | Basis for Relationship      | Source                                 |
| ------------------------------------------------------------ | --------------------------- | -------------------------------------- |
| Surface area                                                 | Height, weight              | Dubois (1927)                          |
| \[probably not implemented?] Basal metabolic heat production | Height, weight, gender, age | Harris and Benedict (1958)             |
| Basal cardiac output                                         | Height, weight, body fat    | Gregersen (1950), Allen et al. (1956)  |
| Thermal resistance                                           | Body fat amount             | Stolwijk (1970)                        |
| Thermal capacitance                                          | Height, weight              | Stolwijk (1970)                        |
| Countercurrent heat exchange                                 | Height (extremity length)   | Mitchell and Myers (1968)              |
| Skin solar absorption                                        | Skin color                  | Houdas and Ring (1982) $$1818$$        |
| Clothing solar absorption                                    | Fabric type and color       | Blum (1945)                            |

### \[Not implemented now] Clothing heat and moisture transfer model

The original 65-node model simplified clothing into an insulation layer and assumed moisture equilibrium between the clothing layer and the air.  The new clothing model was developed during Fu Ming’s time at CBE, and allows for more dynamic calculations of clothing absorption/desorption as well as the effects of air speed on heat and moisture transfer. The mathematical description of the clothing model can be found in [Fu et al (2014)](https://doi.org/10.1016/j.buildenv.2014.05.028).

### \[Not implemented now] Other components

The ABC model included extra functionalities that are either redundant or unnecessary when used with detailed CFD models:

1. View factor model
2. Solar radiation
3. Contact model (e.g. seat)
4. Custom number of body segments (clothed/nude; contact/non-contact)
