# What is the ABC model?

## Overview

The Advanced Berkeley Comfort (ABC) model, initially developed by the Building Sciences Group at the University of California, Berkeley, for evaluating human comfort in automobiles, is one of the most sophisticated thermal comfort models. The comfort models for local body parts and overall are based on intensive human subject tests carried out at the CBE environmental chamber. So far, these are the only models available which predict comfort for local body parts, therefore a good model to predict comfort under non-uniform environments. The model has been under development at UC Berkeley since the early 90s.&#x20;

This model integrates a physiological model that calculates the skin's surface and core temperatures by taking into account human body's thermoregulatory functions such as perspiration and blood flow adjustments in response to the surrounding thermal environment and the body's thermal balance. Additionally, it incorporates a comfort model that predicts thermal comfort levels—ranging from feeling hot or cold to experiencing comfort or discomfort—based on the skin temperature.

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption><p>(a) Previous Windows-based interface: The model predicts local and overall thermal sensation and comfort; (b) Prediction flow: the ABC model comprises the thermal physiology model and thermal comfort model.</p></figcaption></figure>

## Features (differences from other comfort models)

Several numerical models for comfort assessment have been proposed over time, such as the [PMV (Predicted Mean Vote) by Fanger](https://en.wikipedia.org/wiki/Thermal\_comfort#PMV/PPD\_method) and the [2-node model by Gagge et al](https://chrome-extension/efaidnbmnnnibpcajpcglclefindmkaj/https://www.aivc.org/sites/default/files/airbase\_2522.pdf). Thermal comfort evaluations using these models are advocated by standards such as ISO (International Organization for Standardization) and ASHRAE (American Society of Heating, Refrigerating and Air-Conditioning Engineers) Standard 55. However, these models simplify the human body with one or two nodes, and they are not suitable for the following conditions:

* **Non-uniform condition:** In situations where the temperature around us isn't the same everywhere—for example, when using heated or cooled seats, foot warmers, desk fans, or being close to the outer walls of a building where one side of the body feels different from the other.
* **Transient condition:** In situations where the temperature changes quickly, like going from a hot place outside to a cooler place inside.

To address non-uniform and transient conditions, it is essential to set nodes for multiple body parts to more accurately represent the heat transfer of thermal distribution across the body and to solve transient heat balance equations. [Stowijk's model](https://chrome-extension/efaidnbmnnnibpcajpcglclefindmkaj/https://ntrs.nasa.gov/api/citations/19710023925/downloads/19710023925.pdf), which divides the body into ten parts, is a classical model that deals with the issues above. Many researchers have proposed multi-node models based on Stolowijk's model. The ABC model is also developed based on the Stolowijk model, and the main improvements are as follows:

* Increase the number of body segments to 16
* Improved blood flow model, including counter flow heat exchange in the limbs, and modified blood perfusion from vessels to tissues
* Added body builder model that considers the effect of the body (body height, weight, age, and sex) on thermal physiology
* Integrated the Berkeley comfort model (comfort equations proposed by CBE)

<figure><img src="../../.gitbook/assets/image (47).png" alt=""><figcaption><p>aaaaaaaaaaaaaaa</p></figcaption></figure>

## Benefits of comfort simulation

* **Reducing experimental costs and effort:** Actual assessments of comfort require human subject experiments. However, these experiments require precisely temperature-controlled rooms and a large number of participants, as well as ethical reviews before the experiments, which can be costly and time-consuming. While thermal manikins exist for evaluating comfort, they are expensive, and only large laboratories are likely able to afford them.
* **Enabling evaluation of extreme** **environments:** From an ethical and health-risk standpoint, it is not desirable to have subjects stay in environments that are too hot or cold. However, simulations allow for the evaluation of such extreme conditions.

<figure><img src="../../.gitbook/assets/image (46).png" alt=""><figcaption><p>Real thermal comfort evaluation methods: (a) human subject experiments, (b) thermal manikin measurements</p></figcaption></figure>
