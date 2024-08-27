---
icon: pen-to-square
description: Description about how to edit input data
---

# Edit input data

## Overview

As explained in the input conditions section, the Input section of the ABC model includes six main input conditions: air temperature, mean radiant temperature, air velocity, relative humidity, metabolic rate, and clothing insulation.&#x20;

Please refer to the detailed explanation here ([input-and-output](../input-and-output/ "mention")) of each parameter.&#x20;

## Environmental parameters

For air temperature, mean radiant temperature, air velocity, and relative humidity, you need to input the values you want to simulate. You can edit these parameters from the "Edit variable data" tab.

Here, let's take air temperature as an example to illustrate how to edit it. When you click on Edit ambient temp, a tab will open as shown below.

### Applying the same values to all body segment

Enter a temperature in the top left corner to set a uniform temperature for the entire body. For example, input 20 degrees and click "Apply to all" to set all body parts to 20 degrees.

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption><p>Applying the same values to all body segment</p></figcaption></figure>

### Stratified data

Typically, warm air tends to rise and cool air tends to sink. Therefore, the temperature a person is exposed to can vary, such as when the feet are colder than the head. To easily represent this temperature distribution, enter a value in the delta part of the "Optional" section and click on either "Stratify standing" or "Stratify sitting". For example, if the feet are 2 degrees cooler than the head when sitting, the temperature distribution will be formed as shown below.

<figure><img src="../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

### Manual input to local body segments

If you want to input data for each body part individually, please edit the input data for each part accordingly.

## Metabolic rate and clothing level

The input for metabolic rate and clothing insulation is done via dropdown menus.

### Metabolic rate

You can choose from five activity levels: 1) Sleeping, 2) Sitting quietly, 3) Standing quietly, 4) Walking at 3.2 km/h, and 5) Walking at 4.3 km/h.

<figure><img src="../../.gitbook/assets/image (73).png" alt=""><figcaption><p>Dropdown menu for matabolic rate</p></figcaption></figure>

### Clothing level

You can choose from seven clothing levels: 1) Node, 2) Summer light, 3) Summer casual, 4) Summer business casual, 5) Winter casual, 6) Winter business formal, and 7) Winter outerwear. When you choose one of them, you will see the clothing insulation (unit: clo) and description of the clothing ensemble that you choose.&#x20;

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption><p>Dropdown menu for clothing level</p></figcaption></figure>

## Personal comfort system

We call devices like desk fans and foot warmers Personal Comfort Systems (PCS), and you can analyze the impact of these devices on comfort and sensation. We defined the change in thermal environment by each PCS and you can choose all that apply.

For example, in this screen capture below, the desk fan is selected.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

Fans provide air movement. If you click on the Edit air speed\<Edit variable data, you will see the contributions by the desk fan in red.&#x20;

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

The table below summarizes the impact of typical PCS on thermal environmental parameters.

{% hint style="info" %}
Strictly speaking, the air velocity created by a fan is different depending on the measurement point. Therefore, the default values are set to represent the heat loss equivalent to an air velocity of X m/s when a person is in a wind tunnel. These calculations are estimated based on previous data obtained using a thermal manikin. However, these values can vary significantly depending on the type of PCS, and further study is needed.
{% endhint %}

{% embed url="https://docs.google.com/spreadsheets/d/1scnjIKb0Uv4f06IYkGwM3cYgfPXqjM1lr7FocDw5coQ/edit?usp=sharing" %}
Default data of typical PCS
{% endembed %}
