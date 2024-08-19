# Input parameters

## Example input JSON file

The file contains some properties that you can change to simulate your simulation. The details will be described below on this page.

<details>

<summary>Click to expand an example JSON file</summary>

{% code title="abc_sample.json" %}
```json
{
  "name": "Sample",
  "description": "This is a sample file.",
  "reference_time": "2024-02-07T02:31:28",
  "output_freq": 60,
  "options": {
    "csvOutput": false,
    "sensation_adaptation": false,
    "sensation_coredTdt": false
  },
  "comfort_model": {
    "overall_sensation_model": "original",
    "local_sensation_model": "original",
    "overall_comfort_model": "original",
    "local_comfort_model": "original"
  },
  "clothing": [
    {
      "ensemble_name": "sample_clothing_ensemble",
      "description": "customary defined clothing data",
      "segment_data": {
        "Head": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Chest": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Back": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Pelvis": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Left Upper Arm": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Right Upper Arm": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Left Lower Arm": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Right Lower Arm": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Left Hand": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Right Hand": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Left Thigh": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Right Thigh": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Left Lower Leg": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Right Lower Leg": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Left Foot": {
          "fclo": 1.1,
          "iclo": 0.2
        },
        "Right Foot": {
          "fclo": 1.1,
          "iclo": 0.2
        }
      }
    }
  ],
  "bodybuilder": {
    "height": 1.8,
    "weight": 70.4,
    "age": 25,
    "gender": "male",
    "body_fat": 0.15,
    "skin_color": "white"
  },
  "id": 1,
  "phases": [
    {
      "start_time": 0,
      "ramp": false,
      "end_time": 1,
      "time_units": "minutes",
      "met_activity_name": "Seated",
      "met": 1.0,
      "default_data": {
        "rh": 0.5,
        "v": 0.10,
        "solar": 0.000,
        "ta": 25.0,
        "mrt": 25.0
      },
      "clo_ensemble_name": "sample_clothing_ensemble"
    },
    {
      "start_time": 1,
      "ramp": false,
      "end_time": 2,
      "time_units": "minutes",
      "met_activity_name": "Seated",
      "met": 1.0,
      "default_data": {
        "rh": 0.5,
        "v": 0.10,
        "solar": 0.000,
        "ta": 30.0,
        "mrt": 30.0
      },
      "clo_ensemble_name": "sample_clothing_ensemble"
    }
  ]
}

```
{% endcode %}

</details>

## Note

{% hint style="info" %}
**For editors of this document**: The following markdown text is generated from the JSON schema using a Python package called [jsonschema2md](https://pypi.org/project/jsonschema2md/).  Please use [this CBE Github repository](https://github.com/CenterForTheBuiltEnvironment/ABC\_JSON\_schema) with your updated JSON schema file for updates or modifications.
{% endhint %}

## JSON Schema

_Schema for ABC model input JSON, Version 1 (Generated on 2024-05-20 09:54:55)_

### Properties

*   **`id`** _(integer)_: Unique identifier for the simulation.

    Examples:

    ```json
    1
    ```
*   **`name`** _(string)_: Name of the simulation. Default: `""`.

    Examples:

    ```json
    "Sample"
    ```
*   **`description`** _(string)_: Detailed description of the simulation. Default: `""`.

    Examples:

    ```json
    "This is an input file for a sample project."
    ```
*   **`bodybuilder`** _(object)_: Body to be simulated. This function customizes the geometry and physiology of the human being modeled based on simple input parameters (such as height, weight, age, gender and so on) to better account for individual differences. See [the paper](https://doi.org/10.1016/S0306-4565\(01\)00051-1) for more details.

    * **`age`** _(integer)_: Age of the individual. Unit: years. Minimum: `5`. Maximum: `100`. Default: `25`.
    * **`body_fat`** _(number)_: Body fat percentage. Unit: fraction. Minimum: `0.01`. Maximum: `0.7`. Default: `0.13`.
    * **`gender`** _(string)_: Gender of the individual. Must be one of: `["male", "female"]`. Default: `"male"`.
    * **`height`** _(number)_: Height of the individual. Unit: m. Minimum: `1`. Maximum: `3`. Default: `1.72`.
    * **`weight`** _(number)_: Weight of the individual. Unit: kg. Minimum: `25`. Maximum: `200`. Default: `74.4`.
    * **`skin_color`** _(string)_: Skin color of the individual. The solar radiation absorption rate varies depending on this skin color setting. White skin absorbs 62%, brown skin absorbs 70%, and black skin absorbs 77%. Must be one of: `["white", "brown", "black"]`. Default: `"brown"`.
    * **`bloodFlow_factor`** _(number)_: \[For researchers] A special additional multiplier for cardiac output. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.
    * **`skinBloodFlow_factor`** _(number)_: \[For researchers] A special additional multiplier for skin blood flow. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.
    * **`conductance_factor`** _(number)_: \[For researchers] A special additional multiplier for thermal conductance of the body. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.
    * **`capacitance_factor`** _(number)_: \[For researchers] A special additional multiplier for thermal capacity of the body. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.

    Examples:

    ```json
    {
        "age": 25,
        "body_fat": 0.15,
        "gender": "male",
        "height": 1.8,
        "weight": 70.4,
        "skin_color": "white"
    }
    ```
*   **`clothing`** _(array)_: Array of clothing ensembles with specific insulation and area factor values for each body segment. Default: `[]`.

    * **Items** _(object)_
      * **`ensemble_name`** _(string, required)_: Name of the clothing ensemble.
      * **`description`** _(string)_: Description of the clothing ensemble's use or conditions. Default: `""`.
      * **`segment_data`** _(object, required)_: Local clothing insulation and area factor data for body segments.
        * **`Head`** _(object, required)_: Parameters for head clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Chest`** _(object, required)_: Parameters for chest clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Back`** _(object, required)_: Parameters for back clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Pelvis`** _(object, required)_: Parameters for pelvis clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Left Upper Arm`** _(object, required)_: Parameters for left upper arm clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Right Upper Arm`** _(object, required)_: Parameters for right upper arm clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Left Lower Arm`** _(object, required)_: Parameters for left lower arm clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Right Lower Arm`** _(object, required)_: Parameters for right lower arm clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Left Hand`** _(object, required)_: Parameters for left hand clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Right Hand`** _(object, required)_: Parameters for right hand clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Left Thigh`** _(object, required)_: Parameters for left thigh clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Right Thigh`** _(object, required)_: Parameters for right thigh clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Left Lower Leg`** _(object, required)_: Parameters for left lower leg clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Right Lower Leg`** _(object, required)_: Parameters for right lower leg clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Left Foot`** _(object, required)_: Parameters for left foot clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.
        * **`Right Foot`** _(object, required)_: Parameters for right foot clothing insulation and area factor. Refer to _#/definitions/clothingParameters_.

    Examples:

    ```json
    [
        {
            "ensemble_name": "sample clothing ensemble",
            "description": "This is sample clothing ensemble data.",
            "segment_data": {
                "Head": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Chest": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Back": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Pelvis": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Left Upper Arm": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Right Upper Arm": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Left Lower Arm": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Right Lower Arm": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Left Hand": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Right Hand": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Left Thigh": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Right Thigh": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Left Lower Leg": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Right Lower Leg": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Left Foot": {
                    "fclo": 1.1,
                    "iclo": 0.2
                },
                "Right Foot": {
                    "fclo": 1.1,
                    "iclo": 0.2
                }
            }
        }
    ]
    ```
*   **`options`** _(object)_: Simulation options.

    * **`csvOutput`** _(boolean)_: If true, generate CSV output file. Default: `false`.
    * **`sensation_adaptation`** _(boolean)_: If true, use sensation adaptation model. Default: `false`.
    * **`sensation_coredTdt`** _(boolean)_: If true, use core temperature time derivative in sensation model. See [the paper](https://doi.org/10.1016/j.buildenv.2009.06.018) for more details. Default: `false`.
    * **`comfort_model`** _(boolean)_: \[Mainly for developer] If true, run comfort model using skin temperature input. This option can be used when you have skin temperature data obtained from human subject experiments or thermal manikins and want to use them. Default: `false`.
    * **`comfort_setpoint_input`** _(boolean)_: \[Mainly for developer] If true, read comfort setpoints from input. Default: `false`.
    * **`passive_comfort_setpoints`** _(boolean)_: \[Mainly for developer] If true, disable regulatory model when calculating comfort setpoints. Default: `false`.
    * **`transient_comfort_model`** _(boolean)_: If true, use comfort model for transient conditions. See [the paper](https://doi.org/10.1016/j.buildenv.2009.06.015) for more details. Default: `false`.
    * **`user_control_comfort_model`** _(boolean)_: If true, use comfort model for user controlled conditions. See [the paper](https://doi.org/10.1016/j.buildenv.2009.06.015) for more details. Default: `false`.

    Examples:

    ```json
    {
        "csvOutput": true,
        "sensation_coredTdt": true
    }
    ```
*   **`output_freq`** _(integer)_: Output frequency. Minimum: `1`. Default: `60`.

    Examples:

    ```json
    60
    ```
*   **`phases`** _(array)_: Array of conditions to be simulated.

    * **Items** _(object)_
      * **`clo_ensemble_name`** _(string, required)_: Clothing ensemble name for this condition. Default: `""`.
      * **`default_data`** _(object, required)_: Default environmental conditions. Refer to _#/definitions/environmentalConditions_.
      * **`end_time`** _(integer, required)_: End time. Unit: time\_units. Minimum: `0`.
      * **`met`** _(number, required)_: Metabolic rate. Unit: met. Minimum: `0.7`. Maximum: `10`. Default: `1.0`.
      * **`met_activity_name`** _(string)_: Metabolic activity name \[currently not implemented]. Default: `""`.
      * **`ramp`** _(boolean)_: Linear ramp from previous condition. Default: `false`.
      * **`start_time`** _(integer, required)_: Start time. Unit: time\_units. Minimum: `0`.
      * **`time_units`** _(string)_: Time units for start and end times. Unit: seconds. Must be one of: `["seconds", "minutes", "hours"]`. Default: `"seconds"`.
      * **`segment_data`** _(object)_: Specific environmental conditions for body segments. Can contain additional properties. Default: `{}`.
        * **Additional properties**: Refer to _#/definitions/environmentalConditions_.

    Examples:

    ```json
    [
        {
            "start_time": 0,
            "ramp": false,
            "end_time": 3,
            "time_units": "hours",
            "met_activity_name": "Seated",
            "met": 1.0,
            "default_data": {
                "rh": 0.5,
                "v": 0.1,
                "solar": 0.0,
                "ta": 24.0,
                "mrt": 24.0
            },
            "clo_ensemble_name": "sample clothing ensemble"
        }
    ]
    ```

### Definitions

* **`environmentalConditions`** _(object)_
  * **`mrt`** _(number, required)_: Mean radiant temperature. Unit: °C. Minimum: `0`. Maximum: `50`. Default: `25`.
  * **`rh`** _(number, required)_: Relative humidity. Unit: fraction. Minimum: `0.0`. Maximum: `1.0`. Default: `0.5`.
  * **`solar`** _(number)_: Solar flux. Unit: W/m2. Minimum: `0`. Maximum: `10000`. Default: `0`.
  * **`ta`** _(number, required)_: Dry bulb air temperature. Unit: °C. Minimum: `0`. Maximum: `50`. Default: `25`.
  * **`v`** _(number, required)_: Air velocity. Unit: m/s. Minimum: `0.0`. Maximum: `20`. Default: `0.1`.
* **`clothingParameters`** _(object)_
  * **`fclo`** _(number, required)_: Clothing area factor. Unit: fraction. Minimum: `0`.
  * **`iclo`** _(number, required)_: Clothing thermal insulation. Unit: clo (1 clo = 1/0.155 W/m2K). Minimum: `0`.
