---
description: Description about input and output parameters of ABC model
icon: file-lines
---

# Input and output

## Overview

The current ABC model uses a [JSON format file](https://en.wikipedia.org/wiki/JSON) for inputs and outputs. The input file should include data on the thermal environment and human body shapes to be simulated. The output file generated by the model provides detailed information on thermal sensation and comfort, as well as physiological parameters such as skin temperature and sweating.

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption><p>Simulation flow</p></figcaption></figure>

## Main Input parameters

* Thermal environmental parameters
  * Air temperature
  * Mean radiant temperature
  * Air velocity
  * Relative humidity
* Personal parameters
  * Clothing insulation
  * Metabolic rate

For more details, please visit the page below:

{% content-ref url="input-parameters.md" %}
[input-parameters.md](input-parameters.md)
{% endcontent-ref %}

## Main output parameters

* Subjective responses
  * Thermal sensation (ex. Cold, Neutral, Warm)
  * Thermal comfort (ex. Uncomfortable, Slightly comfortable)
* Physiological responses
  * Skin temperature
  * Core temperature

For more details, please visit the page below:

{% content-ref url="output-parameters.md" %}
[output-parameters.md](output-parameters.md)
{% endcontent-ref %}
