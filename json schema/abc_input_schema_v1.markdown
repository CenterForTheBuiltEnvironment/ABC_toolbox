# JSON Schema

*Schema for ABC model input JSON, Version 1 (Generated on 2024-05-20 09:54:55)*

## Properties

- **`id`** *(integer)*: Unique identifier for the simulation.

  Examples:
  ```json
  1
  ```

- **`name`** *(string)*: Name of the simulation. Default: `""`.

  Examples:
  ```json
  "Sample"
  ```

- **`description`** *(string)*: Detailed description of the simulation. Default: `""`.

  Examples:
  ```json
  "This is an input file for a sample project."
  ```

- **`bodybuilder`** *(object)*: Body to be simulated. This function customizes  the geometry and physiology of the human being modeled based on simple input parameters (such as height, weight, age, gender and so on) to better account for individual differences. See [the paper](https://doi.org/10.1016/S0306-4565(01)00051-1) for more details.
  - **`age`** *(integer)*: Age of the individual. Unit: years. Minimum: `5`. Maximum: `100`. Default: `25`.
  - **`body_fat`** *(number)*: Body fat percentage. Unit: fraction. Minimum: `0.01`. Maximum: `0.7`. Default: `0.13`.
  - **`gender`** *(string)*: Gender of the individual. Must be one of: `["male", "female"]`. Default: `"male"`.
  - **`height`** *(number)*: Height of the individual. Unit: m. Minimum: `1`. Maximum: `3`. Default: `1.72`.
  - **`weight`** *(number)*: Weight of the individual. Unit: kg. Minimum: `25`. Maximum: `200`. Default: `74.4`.
  - **`skin_color`** *(string)*: Skin color of the individual. The solar radiation absorption rate varies depending on this skin color setting. White skin absorbs 62%, brown skin absorbs 70%, and black skin absorbs 77%. Must be one of: `["white", "brown", "black"]`. Default: `"brown"`.
  - **`bloodFlow_factor`** *(number)*: [For researchers] A special additional multiplier for cardiac output. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.
  - **`skinBloodFlow_factor`** *(number)*: [For researchers] A special additional multiplier for skin blood flow. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.
  - **`conductance_factor`** *(number)*: [For researchers] A special additional multiplier for thermal conductance of the body. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.
  - **`capacitance_factor`** *(number)*: [For researchers] A special additional multiplier for thermal capacity of the body. Unit: dimensionless. Minimum: `0`. Maximum: `10`. Default: `1`.

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

- **`clothing`** *(array)*: Array of clothing ensembles with specific insulation and area factor values for each body segment. Default: `[]`.
  - **Items** *(object)*
    - **`ensemble_name`** *(string, required)*: Name of the clothing ensemble.
    - **`description`** *(string)*: Description of the clothing ensemble's use or conditions. Default: `""`.
    - **`segment_data`** *(object, required)*: Local clothing insulation and area factor data for body segments.
      - **`Head`** *(object, required)*: Parameters for head clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Chest`** *(object, required)*: Parameters for chest clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Back`** *(object, required)*: Parameters for back clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Pelvis`** *(object, required)*: Parameters for pelvis clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Left Upper Arm`** *(object, required)*: Parameters for left upper arm clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Right Upper Arm`** *(object, required)*: Parameters for right upper arm clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Left Lower Arm`** *(object, required)*: Parameters for left lower arm clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Right Lower Arm`** *(object, required)*: Parameters for right lower arm clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Left Hand`** *(object, required)*: Parameters for left hand clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Right Hand`** *(object, required)*: Parameters for right hand clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Left Thigh`** *(object, required)*: Parameters for left thigh clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Right Thigh`** *(object, required)*: Parameters for right thigh clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Left Lower Leg`** *(object, required)*: Parameters for left lower leg clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Right Lower Leg`** *(object, required)*: Parameters for right lower leg clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Left Foot`** *(object, required)*: Parameters for left foot clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.
      - **`Right Foot`** *(object, required)*: Parameters for right foot clothing insulation and area factor. Refer to *[#/definitions/clothingParameters](#definitions/clothingParameters)*.

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

- **`options`** *(object)*: Simulation options.
  - **`csvOutput`** *(boolean)*: If true, generate CSV output file. Default: `false`.
  - **`sensation_adaptation`** *(boolean)*: If true, use sensation adaptation model. Default: `false`.
  - **`sensation_coredTdt`** *(boolean)*: If true, use core temperature time derivative in sensation model. See [the paper](https://doi.org/10.1016/j.buildenv.2009.06.018) for more details. Default: `false`.
  - **`comfort_model`** *(boolean)*: [Mainly for developer] If true, run comfort model using skin temperature input. This option can be used when you have skin temperature data obtained from human subject experiments or thermal manikins and want to use them. Default: `false`.
  - **`comfort_setpoint_input`** *(boolean)*: [Mainly for developer] If true, read comfort setpoints from input. Default: `false`.
  - **`passive_comfort_setpoints`** *(boolean)*: [Mainly for developer] If true, disable regulatory model when calculating comfort setpoints. Default: `false`.
  - **`transient_comfort_model`** *(boolean)*: If true, use comfort model for transient conditions. See [the paper](https://doi.org/10.1016/j.buildenv.2009.06.015) for more details. Default: `false`.
  - **`user_control_comfort_model`** *(boolean)*: If true, use comfort model for user controlled conditions. See [the paper](https://doi.org/10.1016/j.buildenv.2009.06.015) for more details. Default: `false`.

  Examples:
  ```json
  {
      "csvOutput": true,
      "sensation_coredTdt": true
  }
  ```

- **`output_freq`** *(integer)*: Output frequency. Minimum: `1`. Default: `60`.

  Examples:
  ```json
  60
  ```

- **`phases`** *(array)*: Array of conditions to be simulated.
  - **Items** *(object)*
    - **`clo_ensemble_name`** *(string, required)*: Clothing ensemble name for this condition. Default: `""`.
    - **`default_data`** *(object, required)*: Default environmental conditions. Refer to *[#/definitions/environmentalConditions](#definitions/environmentalConditions)*.
    - **`end_time`** *(integer, required)*: End time. Unit: time_units. Minimum: `0`.
    - **`met`** *(number, required)*: Metabolic rate. Unit: met. Minimum: `0.7`. Maximum: `10`. Default: `1.0`.
    - **`met_activity_name`** *(string)*: Metabolic activity name [currently not implemented]. Default: `""`.
    - **`ramp`** *(boolean)*: Linear ramp from previous condition. Default: `false`.
    - **`start_time`** *(integer, required)*: Start time. Unit: time_units. Minimum: `0`.
    - **`time_units`** *(string)*: Time units for start and end times. Unit: seconds. Must be one of: `["seconds", "minutes", "hours"]`. Default: `"seconds"`.
    - **`segment_data`** *(object)*: Specific environmental conditions for body segments. Can contain additional properties. Default: `{}`.
      - **Additional properties**: Refer to *[#/definitions/environmentalConditions](#definitions/environmentalConditions)*.

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

## Definitions

- <a id="definitions/environmentalConditions"></a>**`environmentalConditions`** *(object)*
  - **`mrt`** *(number, required)*: Mean radiant temperature. Unit: °C. Minimum: `0`. Maximum: `50`. Default: `25`.
  - **`rh`** *(number, required)*: Relative humidity. Unit: fraction. Minimum: `0.0`. Maximum: `1.0`. Default: `0.5`.
  - **`solar`** *(number)*: Solar flux. Unit: W/m2. Minimum: `0`. Maximum: `10000`. Default: `0`.
  - **`ta`** *(number, required)*: Dry bulb air temperature. Unit: °C. Minimum: `0`. Maximum: `50`. Default: `25`.
  - **`v`** *(number, required)*: Air velocity. Unit: m/s. Minimum: `0.0`. Maximum: `20`. Default: `0.1`.
- <a id="definitions/clothingParameters"></a>**`clothingParameters`** *(object)*
  - **`fclo`** *(number, required)*: Clothing area factor. Unit: fraction. Minimum: `0`.
  - **`iclo`** *(number, required)*: Clothing thermal insulation. Unit: clo (1 clo = 1/0.155 W/m2K). Minimum: `0`.
