# JSON Schema

*Generated on 2024-05-20 09:54:55*

## Properties

- **`id`** *(integer)*: Unique identifier for the simulation.

  Examples:
  ```json
  1
  ```

- **`name`** *(string)*: Name of the simulation.

  Examples:
  ```json
  "Sample"
  ```

- **`description`** *(string)*: Description of the simulation's purpose and setup.

  Examples:
  ```json
  "Sample simulation for thermal comfort assessment."
  ```

- **`reference_time`** *(string)*: Timestamp for when the simulation results were generated.

  Examples:
  ```json
  "2023-03-01T12:00:00Z"
  ```

- **`output_freq`** *(integer)*: Frequency at which data is output during the simulation. Unit: seconds.

  Examples:
  ```json
  60
  ```

- **`comfort_model`** *(object)*: Configuration of the models used to assess comfort and sensation.
  - **`overall_sensation_model`** *(string)*: Model used for assessing overall sensation. Must be one of: `["original", "weighted"]`. Default: `"original"`.
  - **`local_sensation_model`** *(string)*: Model for assessing local sensation. Must be one of: `["original", "weighted"]`. Default: `"original"`.
  - **`overall_comfort_model`** *(string)*: Model for evaluating overall comfort. Must be one of: `["original", "weighted"]`. Default: `"original"`.
  - **`local_comfort_model`** *(string)*: Model for evaluating local comfort. Must be one of: `["original", "weighted"]`. Default: `"original"`.
  - **`segment_data`** *(object)*: Detailed parameters for each body segment influencing the comfort and sensation models.
    - **`Head`** *(object)*: Comfort model properties for the Head segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Chest`** *(object)*: Comfort model properties for the Chest segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Back`** *(object)*: Comfort model properties for the Back segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Pelvis`** *(object)*: Comfort model properties for the Pelvis segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Left Upper Arm`** *(object)*: Comfort model properties for the Left Upper Arm segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Right Upper Arm`** *(object)*: Comfort model properties for the Right Upper Arm segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Left Lower Arm`** *(object)*: Comfort model properties for the Left Lower Arm segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Right Lower Arm`** *(object)*: Comfort model properties for the Right Lower Arm segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Left Hand`** *(object)*: Comfort model properties for the Left Hand segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Right Hand`** *(object)*: Comfort model properties for the Right Hand segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Left Thigh`** *(object)*: Comfort model properties for the Left Thigh segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Right Thigh`** *(object)*: Comfort model properties for the Right Thigh segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Left Lower Leg`** *(object)*: Comfort model properties for the Left Lower Leg segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Right Lower Leg`** *(object)*: Comfort model properties for the Right Lower Leg segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Left Foot`** *(object)*: Comfort model properties for the Left Foot segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.
    - **`Right Foot`** *(object)*: Comfort model properties for the Right Foot segment. Refer to *[#/definitions/comfortModelProperties](#definitions/comfortModelProperties)*.

  Examples:
  ```json
  {
      "overall_sensation_model": "original",
      "local_sensation_model": "original",
      "overall_comfort_model": "original",
      "local_comfort_model": "original",
      "segment_data": {
          "Head": {
              "C1_LTZero": 0.38,
              "C1_GEZero": 0.9,
              "K1_LTZero": 0.18,
              "K1_GEZero": 0.18,
              "C2_LTZero": 543.0,
              "C2_GEZero": 90.0,
              "C3": 0.0,
              "C31": -0.35,
              "C32": 0.35,
              "C6": 2.17,
              "C8": 0.5,
              "C71": 0.28,
              "C72": 0.4,
              "TSL": 0.6,
              "adaptationDeadband_negative": 0.0,
              "adaptationDeadband_positive": 0.0,
              "local_sensation_dominant_weight": 0.5
          },
          "COMMENT": "Data for other body segments are listed below."
      }
  }
  ```

- **`results`** *(array)*: Array of simulation results.
  - **`time`** *(integer)*: Simulation time at which the results were recorded. Unit: seconds.
  - **`met`** *(number)*: Metabolic rate at the recorded time. Unit: met.
  - **`clo_ensemble_name`** *(string)*: Name of the clothing ensemble.
  - **`clo`** *(number)*: Clothing insulation value. Unit: clo.
  - **`overall`** *(object)*: Simulation results for the overall body. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
  - **`segments`** *(object)*: Detailed segment-specific results for each body part.
    - **`Head`** *(object)*: Result properties for the Head segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Chest`** *(object)*: Result properties for the Chest segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Back`** *(object)*: Result properties for the Back segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Left Arm`** *(object)*: Result properties for the Left Arm segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Right Arm`** *(object)*: Result properties for the Right Arm segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Left Hand`** *(object)*: Result properties for the Left Hand segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Right Hand`** *(object)*: Result properties for the Right Hand segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Left Upper Leg`** *(object)*: Result properties for the Left Upper Leg segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Right Upper Leg`** *(object)*: Result properties for the Right Upper Leg segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Left Lower Leg`** *(object)*: Result properties for the Left Lower Leg segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Right Lower Leg`** *(object)*: Result properties for the Right Lower Leg segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Left Foot`** *(object)*: Result properties for the Left Foot segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.
    - **`Right Foot`** *(object)*: Result properties for the Right Foot segment. Refer to *[#/definitions/resultProperties](#definitions/resultProperties)*.

  Examples:
  ```json
  [
      {
          "time": 59,
          "met": 1.0,
          "clo_ensemble_name": "sample_clothing_ensemble",
          "clo": 0.20000000000000007,
          "overall": {
              "comfort": 0.503270587364616,
              "comfort_weighted": 1.2080947841872602,
              "sensation": -0.43474571844335996,
              "sensation_linear": -0.17513830599647934,
              "sensation_weighted": -0.20194141423607243,
              "tskin": 33.521280298936865,
              "tneutral": 27.701172571943268,
              "tblood": 35.85687923557489,
              "pmv": -1.278521576607289,
              "ppd": 0.39168821410776106,
              "eht": 25.224561570220335,
              "ta": 25.000000000000004,
              "rh": 0.5,
              "mrt": 25.000000000000004,
              "v": 0.10000000000000003,
              "solar": 0.0,
              "q_met": 106.07876073126181,
              "q_conv": -44.87946370284568,
              "q_rad": -58.45047848818311,
              "q_solar": 0.0,
              "q_resp": -9.621141025004487,
              "q_sweat": -53.242858815254614,
              "w": 0.14937603520781131
          },
          "segments": {
              "Head": {
                  "tskin": 33.674143513410776,
                  "tcore": 36.20124895095861,
                  "eht": 24.798093292451924,
                  "ta": 25.0,
                  "mrt": 25.0,
                  "v": 0.1,
                  "rh": 0.5,
                  "solar": 0.0,
                  "q_met": 16.888739676047514,
                  "q_conv": -3.6848945401655415,
                  "q_rad": -4.56494375775029,
                  "q_solar": 0.0,
                  "q_resp": -0.0,
                  "q_sweat": -4.505595074448825,
                  "q_blood": -4.934093623310259,
                  "q_blood_skin": 8.812110381995405,
                  "skin_blood_flow": 4.032161609997162,
                  "w": 0.13760518798268184,
                  "comfort": 2.5524276645572064,
                  "comfort_weighted": 2.460516885486306,
                  "sensation": -0.04336185613605359,
                  "sensation_weighted": -0.04336185613605359,
                  "tskin_set": 33.67296918164302,
                  "tskin_set_reg": 33.61353035251029
              },
              "COMMENT": "Data for other body segments are listed below."
          }
      }
  ]
  ```

- **`simulation_version`** *(number)*: Version number of the simulation software.

  Examples:
  ```json
  0.1
  ```

- **`simulation_version_date`** *(string)*: Release date of the simulation software version.

  Examples:
  ```json
  "Feb  7 2024 13:52:37"
  ```

- **`state`** *(object)*: Final state of the simulation, including temperatures and other state variables for each body segment.
  - **`version`** *(integer)*: Version number of the data format.
  - **`nSegments`** *(integer)*: Number of body segments included in the model.
  - **`time`** *(number)*: Final state of simulation time. Unit: seconds.
  - **`nodeT`** *(object)*
    - **`Head`**: Temperature at each node in the Head segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Chest`**: Temperature at each node in the Chest segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Back`**: Temperature at each node in the Back segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Pelvis`**: Temperature at each node in the Pelvis segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Left Upper Arm`**: Temperature at each node in the Left Upper Arm segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Right Upper Arm`**: Temperature at each node in the Right Upper Arm segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Left Lower Arm`**: Temperature at each node in the Left Lower Arm segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Right Lower Arm`**: Temperature at each node in the Right Lower Arm segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Left Hand`**: Temperature at each node in the Left Hand segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Right Hand`**: Temperature at each node in the Right Hand segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Left Thigh`**: Temperature at each node in the Left Thigh segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Right Thigh`**: Temperature at each node in the Right Thigh segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Left Lower Leg`**: Temperature at each node in the Left Lower Leg segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Right Lower Leg`**: Temperature at each node in the Right Lower Leg segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Left Foot`**: Temperature at each node in the Left Foot segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`Right Foot`**: Temperature at each node in the Right Foot segment. Refer to *[#/definitions/bodySegment](#definitions/bodySegment)*.
    - **`blood`** *(number)*: Central blood temperature. Unit: °C.
  - **`neutralSetpoint_clo_ensemble`** *(string)*: Name of the clothing ensemble used to calculate the setpoint for the comfort model.
  - **`neutralSetpoint_met`** *(number)*: Metabolic rate used to calculate the setpoint for the comfort model. Unit: met.
  - **`neutralSetpoints`** *(object)*: Neutral temperature setpoints for each body segment.
    - **`Head`** *(number)*: Neutral temperature setpoint for the Head segment. Unit: °C.
    - **`Chest`** *(number)*: Neutral temperature setpoint for the Chest segment. Unit: °C.
    - **`Back`** *(number)*: Neutral temperature setpoint for the Back segment. Unit: °C.
    - **`Pelvis`** *(number)*: Neutral temperature setpoint for the Pelvis segment. Unit: °C.
    - **`Left Upper Arm`** *(number)*: Neutral temperature setpoint for the Left Upper Arm segment. Unit: °C.
    - **`Right Upper Arm`** *(number)*: Neutral temperature setpoint for the Right Upper Arm segment. Unit: °C.
    - **`Left Lower Arm`** *(number)*: Neutral temperature setpoint for the Left Lower Arm segment. Unit: °C.
    - **`Right Lower Arm`** *(number)*: Neutral temperature setpoint for the Right Lower Arm segment. Unit: °C.
    - **`Left Hand`** *(number)*: Neutral temperature setpoint for the Left Hand segment. Unit: °C.
    - **`Right Hand`** *(number)*: Neutral temperature setpoint for the Right Hand segment. Unit: °C.
    - **`Left Thigh`** *(number)*: Neutral temperature setpoint for the Left Thigh segment. Unit: °C.
    - **`Right Thigh`** *(number)*: Neutral temperature setpoint for the Right Thigh segment. Unit: °C.
    - **`Left Lower Leg`** *(number)*: Neutral temperature setpoint for the Left Lower Leg segment. Unit: °C.
    - **`Right Lower Leg`** *(number)*: Neutral temperature setpoint for the Right Lower Leg segment. Unit: °C.
    - **`Left Foot`** *(number)*: Neutral temperature setpoint for the Left Foot segment. Unit: °C.
    - **`Right Foot`** *(number)*: Neutral temperature setpoint for the Right Foot segment. Unit: °C.

  Examples:
  ```json
  {
      "version": 2,
      "nSegments": 16,
      "time": 120.0,
      "nodeT": {
          "Head": {
              "Core": 36.184117321912964,
              "Muscle": 34.66026633001447,
              "Fat": 34.31495371807684,
              "Skin": 33.88214331311155
          },
          "Chest": {
              "Core": 35.94485624876934,
              "Muscle": 35.893012177724536,
              "Fat": 34.75281969516458,
              "Skin": 34.06681181331917
          },
          "Back": {
              "Core": 35.92118804803738,
              "Muscle": 35.95175231389065,
              "Fat": 34.75248927885405,
              "Skin": 34.03728479574949
          },
          "Pelvis": {
              "Core": 37.3229027956757,
              "Muscle": 36.12070523016749,
              "Fat": 35.046140564777104,
              "Skin": 34.24643184166579
          },
          "Left Upper Arm": {
              "Core": 35.22798211049536,
              "Muscle": 34.97708096558404,
              "Fat": 34.17262406134781,
              "Skin": 33.44810724763884
          },
          "Right Upper Arm": {
              "Core": 35.22798211049536,
              "Muscle": 34.97708096558404,
              "Fat": 34.17262406134781,
              "Skin": 33.44810724763884
          },
          "Left Lower Arm": {
              "Core": 34.29033245946408,
              "Muscle": 33.958051421616624,
              "Fat": 33.16661252348846,
              "Skin": 32.60234108240707
          },
          "Right Lower Arm": {
              "Core": 34.29033245946408,
              "Muscle": 33.958051421616624,
              "Fat": 33.16661252348846,
              "Skin": 32.60234108240707
          },
          "Left Hand": {
              "Core": 34.2201856668809,
              "Muscle": 34.19586498321876,
              "Fat": 34.14554448757694,
              "Skin": 34.086768027122964
          },
          "Right Hand": {
              "Core": 34.2201856668809,
              "Muscle": 34.19586498321876,
              "Fat": 34.14554448757694,
              "Skin": 34.086768027122964
          },
          "Left Thigh": {
              "Core": 35.840713140510196,
              "Muscle": 35.727458025494535,
              "Fat": 34.54653120223985,
              "Skin": 33.92151906697877
          },
          "Right Thigh": {
              "Core": 35.840713140510196,
              "Muscle": 35.727458025494535,
              "Fat": 34.54653120223985,
              "Skin": 33.92151906697877
          },
          "Left Lower Leg": {
              "Core": 34.95349203440435,
              "Muscle": 34.8591773694206,
              "Fat": 33.404839393690224,
              "Skin": 32.557859260602235
          },
          "Right Lower Leg": {
              "Core": 34.95349203440435,
              "Muscle": 34.8591773694206,
              "Fat": 33.404839393690224,
              "Skin": 32.557859260602235
          },
          "Left Foot": {
              "Core": 33.99763962670445,
              "Muscle": 33.876192051898876,
              "Fat": 33.76160118217878,
              "Skin": 33.59524621750699
          },
          "Right Foot": {
              "Core": 33.99763962670445,
              "Muscle": 33.876192051898876,
              "Fat": 33.76160118217878,
              "Skin": 33.59524621750699
          },
          "blood": 35.785137637887665
      },
      "neutralSetpoint_clo_ensemble": "sample_clothing_ensemble",
      "neutralSetpoint_met": 1.0,
      "neutral_temperature": 27.701172571943268,
      "neutralSetpoints": {
          "Head": 33.67296918164302,
          "Chest": 34.070354328781995,
          "Back": 34.08238631017117,
          "Pelvis": 34.25940579869662,
          "Left Upper Arm": 33.488057870547685,
          "Right Upper Arm": 33.488057870547685,
          "Left Lower Arm": 32.63957095748933,
          "Right Lower Arm": 32.63957095748933,
          "Left Hand": 33.88677012786055,
          "Right Hand": 33.88677012786055,
          "Left Thigh": 33.870469634271466,
          "Right Thigh": 33.870469634271466,
          "Left Lower Leg": 32.57031887716825,
          "Right Lower Leg": 32.57031887716825,
          "Left Foot": 33.46381216806454,
          "Right Foot": 33.46381216806454
      }
  }
  ```

## Definitions

- <a id="definitions/comfortModelProperties"></a>**`comfortModelProperties`** *(object)*
  - **`C1_LTZero`** *(number)*: Static regression coefficient for local thermal sensation prediction model when skin temperature is lower than set-point (slope of logistic curve). Unit: dimensionless.
  - **`C1_GEZero`** *(number)*: Static regression coefficient for local thermal sensation prediction model when skin temperature is higher than set-point (slope of logistic curve). Unit: dimensionless.
  - **`K1_LTZero`** *(number)*: Factor for effect of whole-body temperature on local thermal sensation when skin temperature is lower than set-point. Unit: dimensionless.
  - **`K1_GEZero`** *(number)*: Factor for effect of whole-body temperature on local thermal sensation when skin temperature is higher than set-point. Unit: dimensionless.
  - **`C2_LTZero`** *(number)*: Dynamic regression coefficient of the local thermal sensation prediction model when skin temperature is lower than the set temperature. Unit: dimensionless.
  - **`C2_GEZero`** *(number)*: Dynamic regression coefficient of the local thermal sensation prediction model when skin temperature is higher than set-point. Unit: dimensionless.
  - **`C3`** *(number)*: Dynamic regression coefficient of the local thermal sensation prediction model when core temperature changes. Unit: dimensionless.
  - **`C31`** *(number)*: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  - **`C32`** *(number)*: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  - **`C6`** *(number)*: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  - **`C8`** *(number)*: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  - **`C71`** *(number)*: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  - **`C72`** *(number)*: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  - **`TSL`** *(number)*: [???] Unit: ???
  - **`adaptationDeadband_negative`** *(number)*: [???] Negative range for adaptation deadband. Unit: ???
  - **`adaptationDeadband_positive`** *(number)*: [???] Positive range for adaptation deadband. Unit: ???
  - **`local_sensation_dominant_weight`** *(number)*: [???] Weight for local sensation in the overall comfort model. Unit: dimensionless.
- <a id="definitions/resultProperties"></a>**`resultProperties`** *(object)*
  - **`comfort`** *(number)*: Thermal comfort (-4: Very uncomfortable, -2: Uncomfortable, -0: Just uncomfortable, +2: Comfortable, +4: Very comfortable). Unit: dimensionless.
  - **`comfort_weighted`** *(number)*: Thermal comfort predicted by weighted comfort model. Unit: dimensionless.
  - **`sensation`** *(number)*: Thermal sensation (-4: Very cold, -3: Cold, -2: Cool, -2: Slightly cool, 0: Neutral, +1: Slightly warm, +2: Warm, +3: Hot, +4: Very hot). Unit: dimensionless.
  - **`sensation_weighted`** *(number)*: Thermal sensation predicted by weighted comfort model. Unit: dimensionless.
  - **`tskin`** *(number)*: Skin temperature. Unit: °C.
  - **`tneutral`** *(number)*: Operative temperature at which the PMV = 0 under given conditions. Unit: °C.
  - **`tblood`** *(number)*: Central blood temperature. Unit: °C.
  - **`tcore`** *(number)*: Core temperature. Unit: °C.
  - **`tskin_set`** *(number)*: Skin temperature setpoint for the comfort model. Unit: °C.
  - **`tskin_set_reg`** *(number)*: Skin temperature setpoint for the physiology model. Unit: °C.
  - **`pmv`** *(number)*: Predicted mean vote calculated by the original PMV model. Unit: dimensionless.
  - **`ppd`** *(number)*: Predicted percentage of dissatisfied. Unit: dimensionless.
  - **`eht`** *(number)*: Equivalent homogenous temperature. Unit: °C.
  - **`ta`** *(number)*: Air temperature. Unit: °C.
  - **`rh`** *(number)*: Relative humidity. Unit: fraction.
  - **`mrt`** *(number)*: Mean radiant temperature. Unit: °C.
  - **`v`** *(number)*: Air velocity. Unit: m/s.
  - **`solar`** *(number)*: Solar radiation. Unit: W/m2.
  - **`q_met`** *(number)*: Metabolic heat production in the body. Unit: W/m2.
  - **`q_conv`** *(number)*: Convective heat transfer between the body and ambient environment. Unit: W/m2.
  - **`q_rad`** *(number)*: Radiative heat transfer between the body and ambient environment. Unit: W/m2.
  - **`q_solar`** *(number)*: Solar radiation received by the body. Unit: W/m2.
  - **`q_resp`** *(number)*: Respiratory heat transfer between the body and ambient environment. Unit: W/m2.
  - **`q_sweat`** *(number)*: Sweat evaporation heat transfer between the body and ambient environment. Unit: W/m2.
  - **`q_blood`** *(number)*: Heat transfer due to blood flow between arteries and veins. Unit: W/m2.
  - **`q_blood_skin`** *(number)*: Heat transfer due to blood flow in the skin. Unit: W/m2.
  - **`skin_blood_flow`** *(number)*: Blood flow rate in the skin. Unit: L/h.
  - **`w`** *(number)*: Total skin wettedness. Unit: fraction.
- <a id="definitions/bodySegment"></a>**`bodySegment`** *(object)*
  - **`Core`** *(number)*: Core temperature of the segment. Unit: °C.
  - **`Muscle`** *(number)*: Muscle temperature of the segment. Unit: °C.
  - **`Fat`** *(number)*: Fat temperature of the segment. Unit: °C.
  - **`Skin`** *(number)*: Skin temperature of the segment. Unit: °C.
