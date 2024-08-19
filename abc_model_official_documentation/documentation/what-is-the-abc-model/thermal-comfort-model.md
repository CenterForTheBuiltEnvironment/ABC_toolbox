# Thermal comfort model

## Overview

The thermal sensation and thermal comfort module is the most significant original contribution by CBE to the thermoregulatory model. It is based on work by Hui Zhang during her PhD and uses physiological parameters (local skin temperatures and core temperature) to predict both local and whole-body thermal sensation and thermal comfort. The conceptual basis is detailed in three papers – see the three papers by Zhang et al:

* [Part 1: Predicting local sensation](https://doi.org/10.1016/j.buildenv.2009.06.018)
* [Part 2: Predicting local comfort](https://doi.org/10.1016/j.buildenv.2009.06.015)
* [Part 3: Predicting whole-body sensation and comfort](https://doi.org/10.1016/j.buildenv.2009.06.020)

In the experiment, they provided heating and cooling to local body parts, measured skin and core temperature, and collected subjects' thermal sensation and comfort votes. They then formulated the relationship between physiological metrics and thermal sensation/comfort.

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption><p>Experimental configurations: (a) a photo during the experiment, (b) skin temperature sensor, (c) core temperature sensor, (d) thermal sensation scale, (e) thermal comfort scale</p></figcaption></figure>

In summary, this model consists of four components, as illustrated in the figure. The main input parameters are 1) skin temperature, 2) its time derivative, 3) core temperature, and 4) its derivative. Using physiological data, the model predicts local thermal sensations. From these local thermal sensations, the overall thermal sensation and local comfort are calculated. Finally, it calculates overall comfort from local comfort.

$$
Sensation, Comfort = f(T_{sk}, \frac{d T_{\text{skin}}}{dt}, \frac{d T_{\text{core}}}{dt})
$$

<figure><img src="../../.gitbook/assets/image (58).png" alt=""><figcaption><p>Prediction flow of four models</p></figcaption></figure>

**\[Not implemented now]** Additional work on the implementation of the thermal sensation and comfort module was done by [Zhao et al (2014)](https://doi.org/10.1016/j.buildenv.2013.11.004). The focus of that work was two-fold: first, determining the neutral setpoint for each body segment, an important requirement for the sensation model; and second, to smooth the jumps in the predicted thermal sensation arising from the piecewise model. The first issue (setpoint determination) was resolved using PMV and the physiological model – details are given in section 2. The second issue (model jumps) was resolved by implementing a smoothing function for the sensation predictions – details are given in section 3.

## [Part 1: Predicting local sensation](https://doi.org/10.1016/j.buildenv.2009.06.018)

This model predicts local thermal sensation ($$𝑆_{local}$$) based on physiological quantities. Local thermal sensation ($$𝑆_{local}$$) is expressed as the sum of static thermal sensation ($$𝑆_{local, static}$$) and dynamic thermal sensation ($$𝑆_{local, dynamic}$$). These two predictive equations are formulated based on experimental data.

$$
S_{local} = S_{local, static} +S_{local, dynamic}
$$

Observing the experimental data, it was found that the relationship between local thermal sensation ($$𝑆_{local, static}$$) and local skin temperature ($$T_{skin, local}$$) in a steady state can be well represented by a logistic function. It is generally assumed that when the difference between skin temperature and neutral skin temperature ($$T_{skin, local}-T_{skin, local,set}$$) is zero, the thermal sensation becomes zero, indicating neutrality. However, it was found that local thermal sensations differ even with the same skin temperature, depending on the overall thermal state of the body. For example, if the whole body is colder than a local area, that area may feel warmer, even if its skin temperature is the same as the neutral state. The coefficients representing the slope of the logistic function ($$C_{1}$$)  and the ones representing the effects of whole-body sensation on local thermal sensation ($$K$$) are different by body part and were optimized based on experimental data. For details on the coefficients, please refer to [the original paper](https://doi.org/10.1016/j.buildenv.2009.06.018).

$$
\text{S}_{local,static} = 4 \left\{ \frac{2}{1 + e^{-C1_{local} (T_{skin, local} - T_{skin, local, set}) - K1_{local} \left\{ (T_{skin, local} - T_{skin,local,set}) - (T_{skin,mean} - T_{skin,mean,set}) \right\}}} - 1 \right\}
$$

Dynamic elements are represented by the time derivatives of skin temperature ($$\frac{dT_{skin, local}}{dt}$$) and core temperature using the following equation. The coefficients $$C_{1}$$and $$C_{2}$$vary by body parts and have been optimized based on experimental data. For details on the coefficients, refer to [the original paper](https://doi.org/10.1016/j.buildenv.2009.06.018).

$$
S_{local, dynamic} = C_{2, local} \frac{dT_{skin, local}}{dt} + C_{3,local} \frac{dT_{cr, local}}{dt}
$$

where:&#x20;

* $$S_{local}$$: local thermal sensation \[-]
* $$T_{skin,local}$$: local skin temperature \[°C]
* $$T_{skin, set, local}$$: local skin temperature set point \[°C]
* $$T_{skin, mean}$$: mean skin temperature \[°C]
* $$T_{skin, mean, set}$$: mean skin temperature set point \[°C]
* $$T_{core}$$: core temperature \[°C]
* $$t$$: time \[s]
* $$C_{1}$$: regression coefficient for the slope of a logistic curve of steady-state prediction \[-]
* $$C_{2}, C_{3}$$: regression coefficient for the dynamic factors \[-]
* $$K$$:  regression coefficient for the effect of whole body thermal sensation on local thermal sensation \[-]

<figure><img src="../../.gitbook/assets/image (62).png" alt=""><figcaption><p>Schematic diagram for predicting local thermal sensation in a steady state</p></figcaption></figure>

## [Part 2: Predicting local comfort](https://doi.org/10.1016/j.buildenv.2009.06.015)

This model predicts local thermal comfort ($$Comfort_{local}$$) based on local thermal sensation ($$𝑆_{local}$$) calculated above and the figure below shows the schematic diagram.&#x20;

Basically, the thermal sensation of a body part is most comfortable when it is neutral, and discomfort increases as it deviates from neutrality. The figure illustrates how local thermal comfort is influenced by overall thermal sensation. Even if the local thermal sensation is the same, the comfort level can vary depending on the overall thermal sensation. For example, if the whole body feels cold/warm, the same warm/cold local area may feel comfortable. The model mathematically represents this concept. The equations are a bit complicated so we do not show them here. If you are more interested, [see the original paper](https://doi.org/10.1016/j.buildenv.2009.06.015). \[Aki could not understand the nature of equations, need some help]

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

## [Part 3: Predicting whole-body sensation and comfort](https://doi.org/10.1016/j.buildenv.2009.06.020)

### Overall sensation model

The whole-body (overall) sensation model has two forms, depending on whether all of the body's segments have sensations effectively in the same direction (e.g warm or cool), or whether some segments have sensations opposite to those of the rest of the body. For each, individual body parts have different weights for warm versus cool sensations, and strong local sensations dominate the overall sensation. If all sensations are near neutral, the overall sensation is close to the average of all body sensations.

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption><p>Diagram of different types of overall sensation models</p></figcaption></figure>

#### No opposite sensation model

This model is applied when sensations are mostly uniform or slightly vary within the context of the body feeling overall warm or cool. &#x20;

* **Complainant model (when the third-most-extreme thermal sensation (**$$|S_{local, third, extream​}|$$**) is more than 2 ("warm" or "cool")**: We found that a weighted average of the most extreme sensation plus the third most extreme sensation effectively determines overall sensation ($$S_{overall​}$$) for both the warm and the cold sides. When the third-most-extreme thermal sensation ($$S_{local, third, extream​}$$) is above "+2: warm" or below "-2: cool" ($$∣𝑆_{𝑙𝑜𝑐𝑎𝑙}∣≥2$$), for example your feet are cold, the influence of local sensations on the overall sensation is dominant. Only the most extreme sensations are used in the calculation, employing a weighted average to determine the overall sensation ($$S_{overall​}$$), where $$a$$ and $$b$$ are regression coefficients.

$$
S_{overall} = a・S_{local,max,extream} + b・S_{local,third,extream}
$$

*   **Gradual model (when the third-most-extreme thermal sensation (**$$|S_{local, third, extream​}|$$**) is less than 2 ("warm" or "cool")):** As local sensations move towards neutral, extreme sensations begin to lose their strong influence on overall sensation. The complaint-driven process becomes less obvious, and the overall sensation approaches the mean of all local sensations. In order to avoid a discontinuity between the two methods (complaint-based or mean-based), we gradually add increasingly less extreme local body sensations to the extreme ones to obtain an average that becomes the overall sensation. Actually, there are a few more detailed considerations, but basically, as long as certain conditions are met, adding parts of the extreme in order and averaging them. If a certain threshold is exceeded, stop the process there.

    $$
    𝑆_{𝑜𝑣𝑒𝑟𝑎𝑙𝑙}=average(S_{local,max,extream}, S_{local,second,extream},…,S_{local,min,extream})
    $$

#### **Opposite sensation model (asymmetrical conditions)**

* This model addresses scenarios where some body parts feel significantly cooler or warmer compared to the overall body temperature.
* The threshold for an 'opposite sensation' is set at ±1. In other words, if$$|S_{overall} - S_{local}|>1$$, those body parts significantly influence the overall body sensation.
* The model first calculates the overall thermal sensation using the gradual model mentioned above, and then considers the influence of the opposite sensation. See [the original paper](https://doi.org/10.1016/j.buildenv.2009.06.020) for details on this calculation method.

### Overall comfort model

The overall comfort model also has two forms. Under stable conditions, people evaluate their overall comfort by a complaint-driven process, meaning that when two body parts are strongly uncomfortable, no matter how comfortable the other body parts might be, the overall comfort will be near the discomfort level of the two most uncomfortable parts. When the environmental conditions are transient, or people have control over their environments, overall comfort is better than that of the two most uncomfortable body parts. This can be accounted for by adding the most comfortable vote to the two most uncomfortable ones.

Our final proposed rule-based overall thermal comfort model is pretty simple and presented in the table below. The comfort model is calculated either by the two minimum local comfort votes (Rule 1), or from the average of the two minimum votes and the maximum comfort vote (Rule 2).

<table><thead><tr><th width="103">Rule</th><th>Description</th></tr></thead><tbody><tr><td>Rule 1</td><td>Overall comfort is the average of the two minimum local comfort votes unless Rule 2 applies.</td></tr><tr><td>Rule 2</td><td><p>Overall comfort is the average of the two minimum votes and the maximum comfort vote if either of the following criteria are met: </p><p>(a) the subject has some control over his/her thermal environment, </p><p>(b) the thermal conditions are transient. </p></td></tr></tbody></table>

**Note:** If both hands or both feet comprise the two most uncomfortable body parts, ignore the second lowest hand or foot comfort value, and use the third lowest local comfort vote as the second lowest vote in Rule 1 and Rule 2.
