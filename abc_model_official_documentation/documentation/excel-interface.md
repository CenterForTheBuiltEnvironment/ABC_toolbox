---
icon: windows
description: Description about Web user interface
---

# Excel interface

## Overview

This Excel workbook has been designed to integrate the ABC model directly into Excel. One of its key advantages is that it allows users to easily input thermal environmental conditions (e.g., air temperature, relative humidity) for different body segments across multiple time steps. While the same functionality is available through the web interface, the Excel workbook offers a more user-friendly alternative for this feature.

We understand that some researchers want to evaluate thermal comfort and physiological responses using their own environmental measurement data, and we hope this workbook proves to be a valuable tool for that purpose.

{% hint style="info" %}
Notes

This sheet is integrated with the ABC\_toolbox. Please download the toolbox from our GitHub repository (https://github.com/CenterForTheBuiltEnvironment/ABC\_toolbox) and specify the correct file path for the downloaded folder. **The model will not run if the file path for the toolbox is incorrect.**
{% endhint %}

## Sheet descriptions

### Simulation Information

You can define all information except thermal environmental data here.&#x20;

{% hint style="warning" %}
To run the model, **specify the file path for the downloaded ABC toolbox folder** on your computer (refer to the image below). Additionally, provide the required input fields highlighted in yellow.
{% endhint %}

{% hint style="info" %}
The **"Simulate" button** on this sheet allows you to execute the model. In its current format, you can enter your data into the cells in column C. If left empty, the default values in column D will be used.
{% endhint %}

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>Simulation Informatuion Sheet: All the simulation inputs except thermal environmental parameters shoud be input here.</p></figcaption></figure>

### Thermal Environment

This sheet is for defining thermal environment information.

{% hint style="info" %}
You need to specify the required input fields highlighted in yellow.
{% endhint %}

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption><p>Thermal Environment Sheet: You can define thermal conditions for each local body part over time.</p></figcaption></figure>

### Results

The output results of the ABC model will be written here.&#x20;

{% hint style="info" %}
If you are unsure about the meaning of the columns, please refer to the output file ([input-and-output](input-and-output/ "mention")).
{% endhint %}

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption><p>Results Sheet: The output results of the ABC model will be written here.</p></figcaption></figure>

### Clothing Reference

This sheet contains past clothing insulation data by J Lee et al. ([link](https://escholarship.org/uc/item/18f0r375)). Use it as a reference for entering clothing insulation values in the Simulation Infomation sheet.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption><p>Clothing Reference Sheet: You can refer this dataset for your clothing input</p></figcaption></figure>

## Change Log

For version control.
