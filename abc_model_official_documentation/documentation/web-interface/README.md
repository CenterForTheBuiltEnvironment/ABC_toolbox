---
icon: globe-pointer
---

# Web interface

## Overview

This graphical user interface allows you to interact with the ABC model. The interface performs the following steps to run the model:

1. **Create JSON file** - Generate a JSON file with the input conditions set by the user on the interface.
2. **Send to API** - Send the JSON file to the ABC model API.
3. **Receive results** - Receive the simulation results from the ABC model API.
4. **Visualize results** - Visualize the results on the interface.

## Entry page

This is the entry page of the Advanced Berkeley Comfort Tool. On this page, you can set the conditions for the thermal environment you want to simulate.&#x20;

We will explain in more detail below but let's first try a quick simulation using the following features:

1. **Set the number of conditions** - Add conditions to simulate, such as Condition #1, Condition #2, etc.
2. **Change/Delete condition names** - Rename conditions or delete unnecessary ones.
3. **Set input conditions -** In each condition, configure exposure time and thermal environment settings (e.g., a person is sitting at 25C of air temperature for 60 minutes ).&#x20;
4. **Run simulation** - Click the **"Simulation"** button.

<figure><img src="../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>

## Main page

This page appears after running a simulation. The left side displays the input conditions, and the right side shows the output results. You can edit the input conditions and run the simulation again on this page.

**Input section (left side):**

* Edit your input conditions here.

**Output section (right side):**

* **Time-series results:** Displays your selected result over time.
* **3D manikin:** Visualizes results for different body parts. Clicking on any time point in the time-series data updates the manikin with data from that moment.
* **Upper tabs**
  * **Compare tab:** Compare one simulation and the other to see the difference in the graph.
  * **Body segment tab:** Select different body segments (Overall, Head, Chest, Arm, etc.) and&#x20;
  * **Result item tab:** Select result items (Comfort, Sensation, Skin temperature, Core temperature, etc.) to view specific results that you want to see.
  * **CSV export tab:** Save all the simulation results to your local environment.

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>
