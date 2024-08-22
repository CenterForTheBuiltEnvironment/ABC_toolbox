---
icon: arrow-left-from-bracket
---

# Output parameters

## Example output JSON file

The file contains some properties that you can change to simulate your simulation. The details will be described below on this page.

<details>

<summary>Click to expand an example JSON file</summary>

{% code title="abc_sample_out.json" %}
````json
```json
{
    "id": 1,
    "name": "Sample",
    "description": "This is a sample file.",
    "reference_time": "2024-02-07T02:31:28",
    "output_freq": 60,
    "comfort_model": {
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
            "Chest": {
                "C1_LTZero": 0.35,
                "C1_GEZero": 1.0,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 39.0,
                "C2_GEZero": 136.0,
                "C3": -2135.0,
                "C31": -0.66,
                "C32": 0.66,
                "C6": 2.1,
                "C8": 0.0,
                "C71": 1.39,
                "C72": 0.9,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Back": {
                "C1_LTZero": 0.3,
                "C1_GEZero": 1.0,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 88.0,
                "C2_GEZero": 192.0,
                "C3": -4054.0,
                "C31": -0.45,
                "C32": 0.45,
                "C6": 2.1,
                "C8": 0.0,
                "C71": 0.96,
                "C72": 0.0,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Pelvis": {
                "C1_LTZero": 0.2,
                "C1_GEZero": 0.4,
                "K1_LTZero": 0.15,
                "K1_GEZero": 0.15,
                "C2_LTZero": 75.0,
                "C2_GEZero": 137.0,
                "C3": -5053.0,
                "C31": -0.59,
                "C32": 0.0,
                "C6": 2.06,
                "C8": -0.51,
                "C71": 0.5,
                "C72": 0.0,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Left Upper Arm": {
                "C1_LTZero": 0.29,
                "C1_GEZero": 0.4,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 156.0,
                "C2_GEZero": 167.0,
                "C3": 0.0,
                "C31": -0.3,
                "C32": 0.35,
                "C6": 2.14,
                "C8": -0.4,
                "C71": 0.0,
                "C72": 0.0,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Right Upper Arm": {
                "C1_LTZero": 0.29,
                "C1_GEZero": 0.4,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 156.0,
                "C2_GEZero": 167.0,
                "C3": 0.0,
                "C31": -0.3,
                "C32": 0.35,
                "C6": 2.14,
                "C8": -0.4,
                "C71": 0.0,
                "C72": 0.0,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Left Lower Arm": {
                "C1_LTZero": 0.3,
                "C1_GEZero": 0.7,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 144.0,
                "C2_GEZero": 125.0,
                "C3": 0.0,
                "C31": -0.23,
                "C32": 0.23,
                "C6": 2.0,
                "C8": -0.68,
                "C71": 0.0,
                "C72": 1.71,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.9,
                "adaptationDeadband_positive": 0.5,
                "local_sensation_dominant_weight": 0.0
            },
            "Right Lower Arm": {
                "C1_LTZero": 0.3,
                "C1_GEZero": 0.7,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 144.0,
                "C2_GEZero": 125.0,
                "C3": 0.0,
                "C31": -0.23,
                "C32": 0.23,
                "C6": 2.0,
                "C8": -0.68,
                "C71": 0.0,
                "C72": 1.71,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.9,
                "adaptationDeadband_positive": 0.5,
                "local_sensation_dominant_weight": 0.0
            },
            "Left Hand": {
                "C1_LTZero": 0.2,
                "C1_GEZero": 0.45,
                "K1_LTZero": 0.15,
                "K1_GEZero": 0.15,
                "C2_LTZero": 19.0,
                "C2_GEZero": 46.0,
                "C3": 0.0,
                "C31": -0.8,
                "C32": 0.8,
                "C6": 1.98,
                "C8": 0.0,
                "C71": 0.48,
                "C72": 0.48,
                "TSL": 0.075,
                "adaptationDeadband_negative": 2.1,
                "adaptationDeadband_positive": 1.4,
                "local_sensation_dominant_weight": 0.0
            },
            "Right Hand": {
                "C1_LTZero": 0.2,
                "C1_GEZero": 0.45,
                "K1_LTZero": 0.15,
                "K1_GEZero": 0.15,
                "C2_LTZero": 19.0,
                "C2_GEZero": 46.0,
                "C3": 0.0,
                "C31": -0.8,
                "C32": 0.8,
                "C6": 1.98,
                "C8": 0.0,
                "C71": 0.48,
                "C72": 0.48,
                "TSL": 0.075,
                "adaptationDeadband_negative": 2.1,
                "adaptationDeadband_positive": 1.4,
                "local_sensation_dominant_weight": 0.0
            },
            "Left Thigh": {
                "C1_LTZero": 0.2,
                "C1_GEZero": 0.29,
                "K1_LTZero": 0.11,
                "K1_GEZero": 0.11,
                "C2_LTZero": 151.0,
                "C2_GEZero": 263.0,
                "C3": 0.0,
                "C31": 0.0,
                "C32": 0.0,
                "C6": 1.98,
                "C8": 0.0,
                "C71": 0.0,
                "C72": 0.0,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Right Thigh": {
                "C1_LTZero": 0.2,
                "C1_GEZero": 0.29,
                "K1_LTZero": 0.11,
                "K1_GEZero": 0.11,
                "C2_LTZero": 151.0,
                "C2_GEZero": 263.0,
                "C3": 0.0,
                "C31": 0.0,
                "C32": 0.0,
                "C6": 1.98,
                "C8": 0.0,
                "C71": 0.0,
                "C72": 0.0,
                "TSL": 0.0,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Left Lower Leg": {
                "C1_LTZero": 0.29,
                "C1_GEZero": 0.4,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 206.0,
                "C2_GEZero": 212.0,
                "C3": 0.0,
                "C31": -0.2,
                "C32": 0.61,
                "C6": 2.0,
                "C8": 0.0,
                "C71": 1.67,
                "C72": 0.0,
                "TSL": 0.075,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Right Lower Leg": {
                "C1_LTZero": 0.29,
                "C1_GEZero": 0.4,
                "K1_LTZero": 0.1,
                "K1_GEZero": 0.1,
                "C2_LTZero": 206.0,
                "C2_GEZero": 212.0,
                "C3": 0.0,
                "C31": -0.2,
                "C32": 0.61,
                "C6": 2.0,
                "C8": 0.0,
                "C71": 1.67,
                "C72": 0.0,
                "TSL": 0.075,
                "adaptationDeadband_negative": 0.0,
                "adaptationDeadband_positive": 0.0,
                "local_sensation_dominant_weight": 0.0
            },
            "Left Foot": {
                "C1_LTZero": 0.25,
                "C1_GEZero": 0.26,
                "K1_LTZero": 0.15,
                "K1_GEZero": 0.15,
                "C2_LTZero": 109.0,
                "C2_GEZero": 162.0,
                "C3": 0.0,
                "C31": -0.91,
                "C32": 0.4,
                "C6": 2.13,
                "C8": 0.0,
                "C71": 0.5,
                "C72": 0.3,
                "TSL": 0.0,
                "adaptationDeadband_negative": 1.9,
                "adaptationDeadband_positive": 0.8,
                "local_sensation_dominant_weight": 0.0
            },
            "Right Foot": {
                "C1_LTZero": 0.25,
                "C1_GEZero": 0.26,
                "K1_LTZero": 0.15,
                "K1_GEZero": 0.15,
                "C2_LTZero": 109.0,
                "C2_GEZero": 162.0,
                "C3": 0.0,
                "C31": -0.91,
                "C32": 0.4,
                "C6": 2.13,
                "C8": 0.0,
                "C71": 0.5,
                "C72": 0.3,
                "TSL": 0.0,
                "adaptationDeadband_negative": 1.9,
                "adaptationDeadband_positive": 0.8,
                "local_sensation_dominant_weight": 0.0
            }
        }
    },
    "simulation_version": 0.1,
    "simulation_version_date": "Feb  7 2024 13:52:37",
    "results": [
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
                    "skin_blood_flow": 4.0321616099971624,
                    "w": 0.13760518798268184,
                    "comfort": 2.5524276645572064,
                    "comfort_weighted": 2.460516885486306,
                    "sensation": -0.04336185613605359,
                    "sensation_weighted": -0.04336185613605359,
                    "tskin_set": 33.67296918164302,
                    "tskin_set_reg": 33.61353035251029
                },
                "Chest": {
                    "tskin": 33.97120820757533,
                    "tcore": 35.97796572458241,
                    "eht": 25.18304449418572,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 15.372038280061009,
                    "q_conv": -3.792000814667927,
                    "q_rad": -5.793743435584766,
                    "q_solar": 0.0,
                    "q_resp": -4.8105705125022435,
                    "q_sweat": -6.290799864680971,
                    "q_blood": -0.8447053910250064,
                    "q_blood_skin": 7.242021450594495,
                    "skin_blood_flow": 3.838021800219568,
                    "w": 0.2101287377175097,
                    "comfort": 2.1794427542341674,
                    "comfort_weighted": 2.205999899477748,
                    "sensation": -0.14494310990117398,
                    "sensation_weighted": -0.09415248301861379,
                    "tskin_set": 34.070354328781995,
                    "tskin_set_reg": 34.04419751033899
                },
                "Back": {
                    "tskin": 33.958322211162866,
                    "tcore": 35.96299018237949,
                    "eht": 25.035503810079273,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 12.785965163903814,
                    "q_conv": -3.1280807016118928,
                    "q_rad": -5.514633987755774,
                    "q_solar": 0.0,
                    "q_resp": -4.8105705125022435,
                    "q_sweat": -5.448821613503826,
                    "q_blood": -1.6916868555703442,
                    "q_blood_skin": 5.1242773827543715,
                    "skin_blood_flow": 2.697685522250606,
                    "w": 0.2187638263646697,
                    "comfort": 1.9514926557440082,
                    "comfort_weighted": 2.097154742471065,
                    "sensation": -0.25809776251831096,
                    "sensation_weighted": -0.15072980932718227,
                    "tskin_set": 34.08238631017117,
                    "tskin_set_reg": 34.08919338675601
                },
                "Pelvis": {
                    "tskin": 34.19023681164585,
                    "tcore": 37.32283532594012,
                    "eht": 24.8026358193084,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 36.99376445314537,
                    "q_conv": -3.6716522228411472,
                    "q_rad": -6.0105691663820595,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -7.966432581872122,
                    "q_blood": -20.44170396856041,
                    "q_blood_skin": 8.87812101689288,
                    "skin_blood_flow": 5.322034249236846,
                    "w": 0.28030699136626147,
                    "comfort": 1.4512767866986587,
                    "comfort_weighted": 1.795518681327723,
                    "sensation": -0.13592090483555808,
                    "sensation_weighted": -0.08964138048580583,
                    "tskin_set": 34.25940579869662,
                    "tskin_set_reg": 34.24858738903664
                },
                "Left Upper Arm": {
                    "tskin": 33.278045377491694,
                    "tcore": 35.22728678656089,
                    "eht": 25.82429165597531,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 1.8472843896439923,
                    "q_conv": -2.497258760161222,
                    "q_rad": -3.366640320237859,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.7949911705389305,
                    "q_blood": 4.683929716786083,
                    "q_blood_skin": 3.010471549158691,
                    "skin_blood_flow": 1.1673574926944927,
                    "w": 0.13746363658010313,
                    "comfort": 0.7116378354096606,
                    "comfort_weighted": 1.3865855620915144,
                    "sensation": -0.5916267635028123,
                    "sensation_weighted": -0.31749430981943294,
                    "tskin_set": 33.488057870547685,
                    "tskin_set_reg": 33.4422561646912
                },
                "Right Upper Arm": {
                    "tskin": 33.278045377491694,
                    "tcore": 35.22728678656089,
                    "eht": 25.82429165597531,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 1.8472843896439923,
                    "q_conv": -2.497258760161222,
                    "q_rad": -3.366640320237859,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.7949911705389305,
                    "q_blood": 4.683929716786083,
                    "q_blood_skin": 3.010471549158691,
                    "skin_blood_flow": 1.1673574926944927,
                    "w": 0.13746363658010313,
                    "comfort": 0.7116378354096606,
                    "comfort_weighted": 1.3865855620915144,
                    "sensation": -0.5916267635028123,
                    "sensation_weighted": -0.31749430981943294,
                    "tskin_set": 33.488057870547685,
                    "tskin_set_reg": 33.4422561646912
                },
                "Left Lower Arm": {
                    "tskin": 32.409218250218736,
                    "tcore": 34.292253571265384,
                    "eht": 25.50494008945592,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.6870163868813414,
                    "q_conv": -1.6991993992995862,
                    "q_rad": -2.0496175987706335,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.7573560038044258,
                    "q_blood": 3.1124549239239125,
                    "q_blood_skin": 1.9785591512307668,
                    "skin_blood_flow": 0.5738985679271573,
                    "w": 0.1099982371385906,
                    "comfort": 0.3990869633420937,
                    "comfort_weighted": 1.118849395235133,
                    "sensation": -0.5971089270873069,
                    "sensation_weighted": -0.32023539161168024,
                    "tskin_set": 32.63957095748933,
                    "tskin_set_reg": 32.710203114898405
                },
                "Right Lower Arm": {
                    "tskin": 32.409218250218736,
                    "tcore": 34.292253571265384,
                    "eht": 25.50494008945592,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.6870163868813414,
                    "q_conv": -1.6991993992995862,
                    "q_rad": -2.0496175987706335,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.7573560038044258,
                    "q_blood": 3.1124549239239125,
                    "q_blood_skin": 1.9785591512307668,
                    "skin_blood_flow": 0.5738985679271573,
                    "w": 0.1099982371385906,
                    "comfort": 0.3990869633420937,
                    "comfort_weighted": 1.118849395235133,
                    "sensation": -0.5971089270873069,
                    "sensation_weighted": -0.32023539161168024,
                    "tskin_set": 32.63957095748933,
                    "tskin_set_reg": 32.710203114898405
                },
                "Left Hand": {
                    "tskin": 33.89894636687396,
                    "tcore": 34.21644924942548,
                    "eht": 24.868525727930198,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.25422203000775967,
                    "q_conv": -1.4853906873812792,
                    "q_rad": -1.5130046932840073,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.2354087660466628,
                    "q_blood": 3.886688076711883,
                    "q_blood_skin": 3.4903929110464573,
                    "skin_blood_flow": 1.7803761672262255,
                    "w": 0.09740652006496892,
                    "comfort": 1.8853713977881836,
                    "comfort_weighted": 1.9790516627953911,
                    "sensation": 0.018199167923189208,
                    "sensation_weighted": -0.01258134410643219,
                    "tskin_set": 33.88677012786055,
                    "tskin_set_reg": 33.78863699128896
                },
                "Right Hand": {
                    "tskin": 33.89894636687396,
                    "tcore": 34.21644924942548,
                    "eht": 24.868525727930198,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.25422203000775967,
                    "q_conv": -1.4853906873812792,
                    "q_rad": -1.5130046932840073,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.2354087660466628,
                    "q_blood": 3.886688076711883,
                    "q_blood_skin": 3.4903929110464573,
                    "skin_blood_flow": 1.7803761672262255,
                    "w": 0.09740652006496892,
                    "comfort": 1.8853713977881836,
                    "comfort_weighted": 1.9790516627953911,
                    "sensation": 0.018199167923189208,
                    "sensation_weighted": -0.01258134410643219,
                    "tskin_set": 33.88677012786055,
                    "tskin_set_reg": 33.78863699128896
                },
                "Left Thigh": {
                    "tskin": 33.790448651110744,
                    "tcore": 35.839647803830836,
                    "eht": 25.010724812540175,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 6.116783297457482,
                    "q_conv": -4.525427183602666,
                    "q_rad": -5.606217585812483,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -4.492991782270599,
                    "q_blood": 6.80279752313418,
                    "q_blood_skin": 5.735607997268014,
                    "skin_blood_flow": 2.7733077057415985,
                    "w": 0.1244505620976397,
                    "comfort": 1.8283212250924585,
                    "comfort_weighted": 1.9217819751566487,
                    "sensation": -0.2103749011609093,
                    "sensation_weighted": -0.12686837864848144,
                    "tskin_set": 33.870469634271466,
                    "tskin_set_reg": 33.78388976891882
                },
                "Right Thigh": {
                    "tskin": 33.790448651110744,
                    "tcore": 35.839647803830836,
                    "eht": 25.010724812540175,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 6.116783297457482,
                    "q_conv": -4.525427183602666,
                    "q_rad": -5.606217585812483,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -4.492991782270599,
                    "q_blood": 6.80279752313418,
                    "q_blood_skin": 5.735607997268014,
                    "skin_blood_flow": 2.7733077057415985,
                    "w": 0.1244505620976397,
                    "comfort": 1.8283212250924585,
                    "comfort_weighted": 1.9217819751566487,
                    "sensation": -0.2103749011609093,
                    "sensation_weighted": -0.12686837864848144,
                    "tskin_set": 33.870469634271466,
                    "tskin_set_reg": 33.78388976891882
                },
                "Left Lower Leg": {
                    "tskin": 32.35162857741898,
                    "tcore": 34.95315773445969,
                    "eht": 25.783748467388495,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 2.69200199393029,
                    "q_conv": -3.4514849527906937,
                    "q_rad": -3.9551056155301465,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.9557062421415954,
                    "q_blood": 4.910535473335382,
                    "q_blood_skin": 2.7374138581058305,
                    "skin_blood_flow": 0.7809209114504964,
                    "w": 0.09863411224968305,
                    "comfort": 1.4406336881958766,
                    "comfort_weighted": 1.817468629666164,
                    "sensation": -0.7225099710599299,
                    "sensation_weighted": -0.38293591359799173,
                    "tskin_set": 32.57031887716825,
                    "tskin_set_reg": 32.52354676682197
                },
                "Right Lower Leg": {
                    "tskin": 32.35162857741898,
                    "tcore": 34.95315773445969,
                    "eht": 25.783748467388495,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 2.69200199393029,
                    "q_conv": -3.4514849527906937,
                    "q_rad": -3.9551056155301465,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.9557062421415954,
                    "q_blood": 4.910535473335382,
                    "q_blood_skin": 2.7374138581058305,
                    "skin_blood_flow": 0.7809209114504964,
                    "w": 0.09863411224968305,
                    "comfort": 1.4406336881958766,
                    "comfort_weighted": 1.817468629666164,
                    "sensation": -0.7225099710599299,
                    "sensation_weighted": -0.38293591359799173,
                    "tskin_set": 32.57031887716825,
                    "tskin_set_reg": 32.52354676682197
                },
                "Left Foot": {
                    "tskin": 33.41960766817477,
                    "tcore": 33.997154778409936,
                    "eht": 24.649084632071695,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.4218184811312029,
                    "q_conv": -1.6426567285441365,
                    "q_rad": -1.7927082567199837,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.2791508755722172,
                    "q_blood": 3.8521964101805084,
                    "q_blood_skin": 3.379104821858091,
                    "skin_blood_flow": 1.3852640557291385,
                    "w": 0.1033097503922443,
                    "comfort": 1.7355018151945987,
                    "comfort_weighted": 2.016269180412434,
                    "sensation": -0.11086442684613207,
                    "sensation_weighted": -0.07711314149109283,
                    "tskin_set": 33.46381216806454,
                    "tskin_set_reg": 33.35525859652944
                },
                "Right Foot": {
                    "tskin": 33.41960766817477,
                    "tcore": 33.997154778409936,
                    "eht": 24.649084632071695,
                    "ta": 25.0,
                    "mrt": 25.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.4218184811312029,
                    "q_conv": -1.6426567285441365,
                    "q_rad": -1.7927082567199837,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.2791508755722172,
                    "q_blood": 3.8521964101805084,
                    "q_blood_skin": 3.379104821858091,
                    "skin_blood_flow": 1.3852640557291385,
                    "w": 0.1033097503922443,
                    "comfort": 1.7355018151945987,
                    "comfort_weighted": 2.016269180412434,
                    "sensation": -0.11086442684613207,
                    "sensation_weighted": -0.07711314149109283,
                    "tskin_set": 33.46381216806454,
                    "tskin_set_reg": 33.35525859652944
                }
            }
        },
        {
            "time": 119,
            "met": 1.0,
            "clo_ensemble_name": "sample_clothing_ensemble",
            "clo": 0.20000000000000007,
            "overall": {
                "comfort": 0.9436814939593878,
                "comfort_weighted": 0.7874923225997557,
                "sensation": 0.3272308490426097,
                "sensation_linear": 0.523244021426976,
                "sensation_weighted": 0.4888722402357986,
                "tskin": 33.654359356053554,
                "tneutral": 27.701172571943268,
                "tblood": 35.78548321148585,
                "pmv": 1.087637916327473,
                "ppd": 0.2995139675949632,
                "eht": 30.081076306077094,
                "ta": 30.0,
                "rh": 0.5,
                "mrt": 30.0,
                "v": 0.10000000000000003,
                "solar": 0.0,
                "q_met": 106.07876073126181,
                "q_conv": -18.931980611791516,
                "q_rad": -24.82233588579838,
                "q_solar": 0.0,
                "q_resp": -7.891604573246447,
                "q_sweat": -48.15946721912119,
                "w": 0.15745048953733903
            },
            "segments": {
                "Head": {
                    "tskin": 33.87984668226708,
                    "tcore": 36.18446654578763,
                    "eht": 29.90974458804576,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 16.888739676047514,
                    "q_conv": -1.647204685616383,
                    "q_rad": -2.040600257450986,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -4.107423015158515,
                    "q_blood": -9.035141114830683,
                    "q_blood_skin": 7.356183926128129,
                    "skin_blood_flow": 3.854797384302465,
                    "w": 0.1448770555158534,
                    "comfort": 0.7186721957342139,
                    "comfort_weighted": 0.6900957143036783,
                    "sensation": 0.6173087222261229,
                    "sensation_weighted": 0.6173087222261229,
                    "tskin_set": 33.67296918164302,
                    "tskin_set_reg": 33.61353035251029
                },
                "Chest": {
                    "tskin": 34.0656631457637,
                    "tcore": 35.94544598324827,
                    "eht": 30.082915723766273,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 15.372038280061009,
                    "q_conv": -1.7177052687063363,
                    "q_rad": -2.624457143137036,
                    "q_solar": 0.0,
                    "q_resp": -3.9458022866232234,
                    "q_sweat": -5.7490526755751,
                    "q_blood": -6.022893055049124,
                    "q_blood_skin": 6.316843894928917,
                    "skin_blood_flow": 3.669731318851343,
                    "w": 0.22317836953162878,
                    "comfort": 2.032312309646869,
                    "comfort_weighted": 1.5526266431678075,
                    "sensation": 0.13259430627597268,
                    "sensation_weighted": 0.3749515142510478,
                    "tskin_set": 34.070354328781995,
                    "tskin_set_reg": 34.04419751033899
                },
                "Back": {
                    "tskin": 34.03630146918013,
                    "tcore": 35.92189252622111,
                    "eht": 30.01598948930463,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 12.785965163903814,
                    "q_conv": -1.40876184304626,
                    "q_rad": -2.4835695371647932,
                    "q_solar": 0.0,
                    "q_resp": -3.9458022866232234,
                    "q_sweat": -4.9779068576620356,
                    "q_blood": -5.072117002565793,
                    "q_blood_skin": 4.5257030118639,
                    "skin_blood_flow": 2.5853327914939555,
                    "w": 0.23261440887455112,
                    "comfort": 1.8577261261575682,
                    "comfort_weighted": 1.3285223669499753,
                    "sensation": 0.13248674068610233,
                    "sensation_weighted": 0.3748977314561126,
                    "tskin_set": 34.08238631017117,
                    "tskin_set_reg": 34.08919338675601
                },
                "Pelvis": {
                    "tskin": 34.24572257392883,
                    "tcore": 37.322921398565406,
                    "eht": 29.908849397599223,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 36.99376445314537,
                    "q_conv": -1.6957145452906313,
                    "q_rad": -2.7759191073447167,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -7.31755918068852,
                    "q_blood": -24.409398575743715,
                    "q_blood_skin": 7.749670367119203,
                    "skin_blood_flow": 5.029533867747836,
                    "w": 0.2992858592122777,
                    "comfort": 2.247831720088556,
                    "comfort_weighted": 2.2768514811984555,
                    "sensation": 0.057106228559010486,
                    "sensation_weighted": 0.3372074753925667,
                    "tskin_set": 34.25940579869662,
                    "tskin_set_reg": 34.24858738903664
                },
                "Left Upper Arm": {
                    "tskin": 33.446168336740485,
                    "tcore": 35.227975794682344,
                    "eht": 30.342844363008414,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 1.8472843896439923,
                    "q_conv": -1.0386749431324023,
                    "q_rad": -1.4002733713283906,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.519658316936065,
                    "q_blood": 4.239311793368326,
                    "q_blood_skin": 2.6982481360057045,
                    "skin_blood_flow": 1.1522946002744725,
                    "w": 0.1443074309149132,
                    "comfort": 2.1552086803383044,
                    "comfort_weighted": 1.816758238522688,
                    "sensation": 0.2734486144902002,
                    "sensation_weighted": 0.44537866835816153,
                    "tskin_set": 33.488057870547685,
                    "tskin_set_reg": 33.4422561646912
                },
                "Right Upper Arm": {
                    "tskin": 33.446168336740485,
                    "tcore": 35.227975794682344,
                    "eht": 30.342844363008414,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 1.8472843896439923,
                    "q_conv": -1.0386749431324023,
                    "q_rad": -1.4002733713283906,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.519658316936065,
                    "q_blood": 4.239311793368326,
                    "q_blood_skin": 2.6982481360057045,
                    "skin_blood_flow": 1.1522946002744725,
                    "w": 0.1443074309149132,
                    "comfort": 2.1552086803383044,
                    "comfort_weighted": 1.816758238522688,
                    "sensation": 0.2734486144902002,
                    "sensation_weighted": 0.44537866835816153,
                    "tskin_set": 33.488057870547685,
                    "tskin_set_reg": 33.4422561646912
                },
                "Left Lower Arm": {
                    "tskin": 32.600141005093164,
                    "tcore": 34.29036819289609,
                    "eht": 30.176979454718172,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.6870163868813414,
                    "q_conv": -0.5955625022158995,
                    "q_rad": -0.7183826608064641,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.5617770939240057,
                    "q_blood": 2.9204310232422266,
                    "q_blood_skin": 1.8271185124643132,
                    "skin_blood_flow": 0.573137909224948,
                    "w": 0.11498486277838893,
                    "comfort": 3.060825075368305,
                    "comfort_weighted": 3.09416130833205,
                    "sensation": 0.22530860969010602,
                    "sensation_weighted": 0.42130866595811445,
                    "tskin_set": 32.63957095748933,
                    "tskin_set_reg": 32.710203114898405
                },
                "Right Lower Arm": {
                    "tskin": 32.600141005093164,
                    "tcore": 34.29036819289609,
                    "eht": 30.176979454718172,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.6870163868813414,
                    "q_conv": -0.5955625022158995,
                    "q_rad": -0.7183826608064641,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.5617770939240057,
                    "q_blood": 2.9204310232422266,
                    "q_blood_skin": 1.8271185124643132,
                    "skin_blood_flow": 0.573137909224948,
                    "w": 0.11498486277838893,
                    "comfort": 3.060825075368305,
                    "comfort_weighted": 3.09416130833205,
                    "sensation": 0.22530860969010602,
                    "sensation_weighted": 0.42130866595811445,
                    "tskin_set": 32.63957095748933,
                    "tskin_set_reg": 32.710203114898405
                },
                "Left Hand": {
                    "tskin": 34.08481910912616,
                    "tcore": 34.22005092368712,
                    "eht": 29.9396813538978,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.25422203000775967,
                    "q_conv": -0.6814774768107027,
                    "q_rad": -0.694146415176274,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.110661272725258,
                    "q_blood": 3.3254091532157437,
                    "q_blood_skin": 2.9534694964259494,
                    "skin_blood_flow": 1.7342778204565328,
                    "w": 0.10081191583408045,
                    "comfort": 1.4313381159858323,
                    "comfort_weighted": 1.0517323359813928,
                    "sensation": 0.2972024465604015,
                    "sensation_weighted": 0.4572555843932622,
                    "tskin_set": 33.88677012786055,
                    "tskin_set_reg": 33.78863699128896
                },
                "Right Hand": {
                    "tskin": 34.08481910912616,
                    "tcore": 34.22005092368712,
                    "eht": 29.9396813538978,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.25422203000775967,
                    "q_conv": -0.6814774768107027,
                    "q_rad": -0.694146415176274,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.110661272725258,
                    "q_blood": 3.3254091532157437,
                    "q_blood_skin": 2.9534694964259494,
                    "skin_blood_flow": 1.7342778204565328,
                    "w": 0.10081191583408045,
                    "comfort": 1.4313381159858323,
                    "comfort_weighted": 1.0517323359813928,
                    "sensation": 0.2972024465604015,
                    "sensation_weighted": 0.4572555843932622,
                    "tskin_set": 33.88677012786055,
                    "tskin_set_reg": 33.78863699128896
                },
                "Left Thigh": {
                    "tskin": 33.91993362156959,
                    "tcore": 35.840697308647215,
                    "eht": 30.00477997294563,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 6.116783297457482,
                    "q_conv": -2.0169508253877293,
                    "q_rad": -2.4986514484155027,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -4.054205585966946,
                    "q_blood": 5.517268709648833,
                    "q_blood_skin": 4.972432286957837,
                    "skin_blood_flow": 2.6626038756288994,
                    "w": 0.13050971473110712,
                    "comfort": 1.4580891049785867,
                    "comfort_weighted": 1.2969545395059208,
                    "sensation": 0.43739378916468663,
                    "sensation_weighted": 0.5273512556954048,
                    "tskin_set": 33.870469634271466,
                    "tskin_set_reg": 33.78388976891882
                },
                "Right Thigh": {
                    "tskin": 33.91993362156959,
                    "tcore": 35.840697308647215,
                    "eht": 30.00477997294563,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 6.116783297457482,
                    "q_conv": -2.0169508253877293,
                    "q_rad": -2.4986514484155027,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -4.054205585966946,
                    "q_blood": 5.517268709648833,
                    "q_blood_skin": 4.972432286957837,
                    "skin_blood_flow": 2.6626038756288994,
                    "w": 0.13050971473110712,
                    "comfort": 1.4580891049785867,
                    "comfort_weighted": 1.2969545395059208,
                    "sensation": 0.43739378916468663,
                    "sensation_weighted": 0.5273512556954048,
                    "tskin_set": 33.870469634271466,
                    "tskin_set_reg": 33.78388976891882
                },
                "Left Lower Leg": {
                    "tskin": 32.5553512343933,
                    "tcore": 34.953487553305266,
                    "eht": 30.27205317267767,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 2.69200199393029,
                    "q_conv": -1.1980724313053237,
                    "q_rad": -1.3728882106341593,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.609615160680025,
                    "q_blood": 4.5275661091306825,
                    "q_blood_skin": 2.511417054649063,
                    "skin_blood_flow": 0.7768023959100421,
                    "w": 0.10255813287319274,
                    "comfort": 1.0561861430719748,
                    "comfort_weighted": 0.8361906267477943,
                    "sensation": 0.5037022413532073,
                    "sensation_weighted": 0.5605054817896651,
                    "tskin_set": 32.57031887716825,
                    "tskin_set_reg": 32.52354676682197
                },
                "Right Lower Leg": {
                    "tskin": 32.5553512343933,
                    "tcore": 34.953487553305266,
                    "eht": 30.27205317267767,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 2.69200199393029,
                    "q_conv": -1.1980724313053237,
                    "q_rad": -1.3728882106341593,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -2.609615160680025,
                    "q_blood": 4.5275661091306825,
                    "q_blood_skin": 2.511417054649063,
                    "skin_blood_flow": 0.7768023959100421,
                    "w": 0.10255813287319274,
                    "comfort": 1.0561861430719748,
                    "comfort_weighted": 0.8361906267477943,
                    "sensation": 0.5037022413532073,
                    "sensation_weighted": 0.5605054817896651,
                    "tskin_set": 32.57031887716825,
                    "tskin_set_reg": 32.52354676682197
                },
                "Left Foot": {
                    "tskin": 33.59319203830091,
                    "tcore": 33.99761331932207,
                    "eht": 29.85034188858332,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.4218184811312029,
                    "q_conv": -0.7005589557138947,
                    "q_rad": -0.7645528139896356,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.1478453147862078,
                    "q_blood": 3.426957152761964,
                    "q_blood_skin": 2.973032120168036,
                    "skin_blood_flow": 1.3546268929103769,
                    "w": 0.107566293767204,
                    "comfort": 1.5165193798310896,
                    "comfort_weighted": 1.2773187944368807,
                    "sensation": 0.4110430922086712,
                    "sensation_weighted": 0.514175907217397,
                    "tskin_set": 33.46381216806454,
                    "tskin_set_reg": 33.35525859652944
                },
                "Right Foot": {
                    "tskin": 33.59319203830091,
                    "tcore": 33.99761331932207,
                    "eht": 29.85034188858332,
                    "ta": 30.0,
                    "mrt": 30.0,
                    "v": 0.1,
                    "rh": 0.5,
                    "solar": 0.0,
                    "q_met": 0.4218184811312029,
                    "q_conv": -0.7005589557138947,
                    "q_rad": -0.7645528139896356,
                    "q_solar": 0.0,
                    "q_resp": -0.0,
                    "q_sweat": -1.1478453147862078,
                    "q_blood": 3.426957152761964,
                    "q_blood_skin": 2.973032120168036,
                    "skin_blood_flow": 1.3546268929103769,
                    "w": 0.107566293767204,
                    "comfort": 1.5165193798310896,
                    "comfort_weighted": 1.2773187944368807,
                    "sensation": 0.4110430922086712,
                    "sensation_weighted": 0.514175907217397,
                    "tskin_set": 33.46381216806454,
                    "tskin_set_reg": 33.35525859652944
                }
            }
        }
    ],
    "state": {
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
}
```
````
{% endcode %}

</details>

## Note

{% hint style="info" %}
**For editors of this document**: The following markdown text is generated from the JSON schema using a Python package called [jsonschema2md](https://pypi.org/project/jsonschema2md/).  Please use [this CBE Github repository](https://github.com/CenterForTheBuiltEnvironment/ABC\_JSON\_schema) with your updated JSON schema file for updates or modifications.
{% endhint %}

## Output JSON Schema

### Properties

*   **`id`** _(integer)_: Unique identifier for the simulation.

    Examples:

    ```json
    1
    ```
*   **`name`** _(string)_: Name of the simulation.

    Examples:

    ```json
    "Sample"
    ```
*   **`description`** _(string)_: Description of the simulation's purpose and setup.

    Examples:

    ```json
    "Sample simulation for thermal comfort assessment."
    ```
*   **`reference_time`** _(string)_: Timestamp for when the simulation results were generated.

    Examples:

    ```json
    "2023-03-01T12:00:00Z"
    ```
*   **`output_freq`** _(integer)_: Frequency at which data is output during the simulation. Unit: seconds.

    Examples:

    ```json
    60
    ```
*   **`comfort_model`** _(object)_: Configuration of the models used to assess comfort and sensation.

    * **`overall_sensation_model`** _(string)_: Model used for assessing overall sensation. Must be one of: `["original", "weighted"]`. Default: `"original"`.
    * **`local_sensation_model`** _(string)_: Model for assessing local sensation. Must be one of: `["original", "weighted"]`. Default: `"original"`.
    * **`overall_comfort_model`** _(string)_: Model for evaluating overall comfort. Must be one of: `["original", "weighted"]`. Default: `"original"`.
    * **`local_comfort_model`** _(string)_: Model for evaluating local comfort. Must be one of: `["original", "weighted"]`. Default: `"original"`.
    * **`segment_data`** _(object)_: Detailed parameters for each body segment influencing the comfort and sensation models.
      * **`Head`** _(object)_: Comfort model properties for the Head segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Chest`** _(object)_: Comfort model properties for the Chest segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Back`** _(object)_: Comfort model properties for the Back segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Pelvis`** _(object)_: Comfort model properties for the Pelvis segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Left Upper Arm`** _(object)_: Comfort model properties for the Left Upper Arm segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Right Upper Arm`** _(object)_: Comfort model properties for the Right Upper Arm segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Left Lower Arm`** _(object)_: Comfort model properties for the Left Lower Arm segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Right Lower Arm`** _(object)_: Comfort model properties for the Right Lower Arm segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Left Hand`** _(object)_: Comfort model properties for the Left Hand segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Right Hand`** _(object)_: Comfort model properties for the Right Hand segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Left Thigh`** _(object)_: Comfort model properties for the Left Thigh segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Right Thigh`** _(object)_: Comfort model properties for the Right Thigh segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Left Lower Leg`** _(object)_: Comfort model properties for the Left Lower Leg segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Right Lower Leg`** _(object)_: Comfort model properties for the Right Lower Leg segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Left Foot`** _(object)_: Comfort model properties for the Left Foot segment. Refer to _#/definitions/comfortModelProperties_.
      * **`Right Foot`** _(object)_: Comfort model properties for the Right Foot segment. Refer to _#/definitions/comfortModelProperties_.

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
*   **`results`** _(array)_: Array of simulation results.

    * **`time`** _(integer)_: Simulation time at which the results were recorded. Unit: seconds.
    * **`met`** _(number)_: Metabolic rate at the recorded time. Unit: met.
    * **`clo_ensemble_name`** _(string)_: Name of the clothing ensemble.
    * **`clo`** _(number)_: Clothing insulation value. Unit: clo.
    * **`overall`** _(object)_: Simulation results for the overall body. Refer to _#/definitions/resultProperties_.
    * **`segments`** _(object)_: Detailed segment-specific results for each body part.
      * **`Head`** _(object)_: Result properties for the Head segment. Refer to _#/definitions/resultProperties_.
      * **`Chest`** _(object)_: Result properties for the Chest segment. Refer to _#/definitions/resultProperties_.
      * **`Back`** _(object)_: Result properties for the Back segment. Refer to _#/definitions/resultProperties_.
      * **`Left Arm`** _(object)_: Result properties for the Left Arm segment. Refer to _#/definitions/resultProperties_.
      * **`Right Arm`** _(object)_: Result properties for the Right Arm segment. Refer to _#/definitions/resultProperties_.
      * **`Left Hand`** _(object)_: Result properties for the Left Hand segment. Refer to _#/definitions/resultProperties_.
      * **`Right Hand`** _(object)_: Result properties for the Right Hand segment. Refer to _#/definitions/resultProperties_.
      * **`Left Upper Leg`** _(object)_: Result properties for the Left Upper Leg segment. Refer to _#/definitions/resultProperties_.
      * **`Right Upper Leg`** _(object)_: Result properties for the Right Upper Leg segment. Refer to _#/definitions/resultProperties_.
      * **`Left Lower Leg`** _(object)_: Result properties for the Left Lower Leg segment. Refer to _#/definitions/resultProperties_.
      * **`Right Lower Leg`** _(object)_: Result properties for the Right Lower Leg segment. Refer to _#/definitions/resultProperties_.
      * **`Left Foot`** _(object)_: Result properties for the Left Foot segment. Refer to _#/definitions/resultProperties_.
      * **`Right Foot`** _(object)_: Result properties for the Right Foot segment. Refer to _#/definitions/resultProperties_.

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
*   **`simulation_version`** _(number)_: Version number of the simulation software.

    Examples:

    ```json
    0.1
    ```
*   **`simulation_version_date`** _(string)_: Release date of the simulation software version.

    Examples:

    ```json
    "Feb  7 2024 13:52:37"
    ```
*   **`state`** _(object)_: Final state of the simulation, including temperatures and other state variables for each body segment.

    * **`version`** _(integer)_: Version number of the data format.
    * **`nSegments`** _(integer)_: Number of body segments included in the model.
    * **`time`** _(number)_: Final state of simulation time. Unit: seconds.
    * **`nodeT`** _(object)_
      * **`Head`**: Temperature at each node in the Head segment. Refer to _#/definitions/bodySegment_.
      * **`Chest`**: Temperature at each node in the Chest segment. Refer to _#/definitions/bodySegment_.
      * **`Back`**: Temperature at each node in the Back segment. Refer to _#/definitions/bodySegment_.
      * **`Pelvis`**: Temperature at each node in the Pelvis segment. Refer to _#/definitions/bodySegment_.
      * **`Left Upper Arm`**: Temperature at each node in the Left Upper Arm segment. Refer to _#/definitions/bodySegment_.
      * **`Right Upper Arm`**: Temperature at each node in the Right Upper Arm segment. Refer to _#/definitions/bodySegment_.
      * **`Left Lower Arm`**: Temperature at each node in the Left Lower Arm segment. Refer to _#/definitions/bodySegment_.
      * **`Right Lower Arm`**: Temperature at each node in the Right Lower Arm segment. Refer to _#/definitions/bodySegment_.
      * **`Left Hand`**: Temperature at each node in the Left Hand segment. Refer to _#/definitions/bodySegment_.
      * **`Right Hand`**: Temperature at each node in the Right Hand segment. Refer to _#/definitions/bodySegment_.
      * **`Left Thigh`**: Temperature at each node in the Left Thigh segment. Refer to _#/definitions/bodySegment_.
      * **`Right Thigh`**: Temperature at each node in the Right Thigh segment. Refer to _#/definitions/bodySegment_.
      * **`Left Lower Leg`**: Temperature at each node in the Left Lower Leg segment. Refer to _#/definitions/bodySegment_.
      * **`Right Lower Leg`**: Temperature at each node in the Right Lower Leg segment. Refer to _#/definitions/bodySegment_.
      * **`Left Foot`**: Temperature at each node in the Left Foot segment. Refer to _#/definitions/bodySegment_.
      * **`Right Foot`**: Temperature at each node in the Right Foot segment. Refer to _#/definitions/bodySegment_.
      * **`blood`** _(number)_: Central blood temperature. Unit: °C.
    * **`neutralSetpoint_clo_ensemble`** _(string)_: Name of the clothing ensemble used to calculate the setpoint for the comfort model.
    * **`neutralSetpoint_met`** _(number)_: Metabolic rate used to calculate the setpoint for the comfort model. Unit: met.
    * **`neutralSetpoints`** _(object)_: Neutral temperature setpoints for each body segment.
      * **`Head`** _(number)_: Neutral temperature setpoint for the Head segment. Unit: °C.
      * **`Chest`** _(number)_: Neutral temperature setpoint for the Chest segment. Unit: °C.
      * **`Back`** _(number)_: Neutral temperature setpoint for the Back segment. Unit: °C.
      * **`Pelvis`** _(number)_: Neutral temperature setpoint for the Pelvis segment. Unit: °C.
      * **`Left Upper Arm`** _(number)_: Neutral temperature setpoint for the Left Upper Arm segment. Unit: °C.
      * **`Right Upper Arm`** _(number)_: Neutral temperature setpoint for the Right Upper Arm segment. Unit: °C.
      * **`Left Lower Arm`** _(number)_: Neutral temperature setpoint for the Left Lower Arm segment. Unit: °C.
      * **`Right Lower Arm`** _(number)_: Neutral temperature setpoint for the Right Lower Arm segment. Unit: °C.
      * **`Left Hand`** _(number)_: Neutral temperature setpoint for the Left Hand segment. Unit: °C.
      * **`Right Hand`** _(number)_: Neutral temperature setpoint for the Right Hand segment. Unit: °C.
      * **`Left Thigh`** _(number)_: Neutral temperature setpoint for the Left Thigh segment. Unit: °C.
      * **`Right Thigh`** _(number)_: Neutral temperature setpoint for the Right Thigh segment. Unit: °C.
      * **`Left Lower Leg`** _(number)_: Neutral temperature setpoint for the Left Lower Leg segment. Unit: °C.
      * **`Right Lower Leg`** _(number)_: Neutral temperature setpoint for the Right Lower Leg segment. Unit: °C.
      * **`Left Foot`** _(number)_: Neutral temperature setpoint for the Left Foot segment. Unit: °C.
      * **`Right Foot`** _(number)_: Neutral temperature setpoint for the Right Foot segment. Unit: °C.

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

### Definitions

* **`comfortModelProperties`** _(object)_
  * **`C1_LTZero`** _(number)_: Static regression coefficient for local thermal sensation prediction model when skin temperature is lower than set-point (slope of logistic curve). Unit: dimensionless.
  * **`C1_GEZero`** _(number)_: Static regression coefficient for local thermal sensation prediction model when skin temperature is higher than set-point (slope of logistic curve). Unit: dimensionless.
  * **`K1_LTZero`** _(number)_: Factor for effect of whole-body temperature on local thermal sensation when skin temperature is lower than set-point. Unit: dimensionless.
  * **`K1_GEZero`** _(number)_: Factor for effect of whole-body temperature on local thermal sensation when skin temperature is higher than set-point. Unit: dimensionless.
  * **`C2_LTZero`** _(number)_: Dynamic regression coefficient of the local thermal sensation prediction model when skin temperature is lower than the set temperature. Unit: dimensionless.
  * **`C2_GEZero`** _(number)_: Dynamic regression coefficient of the local thermal sensation prediction model when skin temperature is higher than set-point. Unit: dimensionless.
  * **`C3`** _(number)_: Dynamic regression coefficient of the local thermal sensation prediction model when core temperature changes. Unit: dimensionless.
  * **`C31`** _(number)_: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  * **`C32`** _(number)_: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  * **`C6`** _(number)_: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  * **`C8`** _(number)_: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  * **`C71`** _(number)_: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  * **`C72`** _(number)_: Regression coefficient of the local thermal comfort prediction. Unit: dimensionless.
  * **`TSL`** _(number)_: \[???] Unit: ???
  * **`adaptationDeadband_negative`** _(number)_: \[???] Negative range for adaptation deadband. Unit: ???
  * **`adaptationDeadband_positive`** _(number)_: \[???] Positive range for adaptation deadband. Unit: ???
  * **`local_sensation_dominant_weight`** _(number)_: \[???] Weight for local sensation in the overall comfort model. Unit: dimensionless.
* **`resultProperties`** _(object)_
  * **`comfort`** _(number)_: Thermal comfort (-4: Very uncomfortable, -2: Uncomfortable, -0: Just uncomfortable, +2: Comfortable, +4: Very comfortable). Unit: dimensionless.
  * **`comfort_weighted`** _(number)_: Thermal comfort predicted by weighted comfort model. Unit: dimensionless.
  * **`sensation`** _(number)_: Thermal sensation (-4: Very cold, -3: Cold, -2: Cool, -2: Slightly cool, 0: Neutral, +1: Slightly warm, +2: Warm, +3: Hot, +4: Very hot). Unit: dimensionless.
  * **`sensation_weighted`** _(number)_: Thermal sensation predicted by weighted comfort model. Unit: dimensionless.
  * **`tskin`** _(number)_: Skin temperature. Unit: °C.
  * **`tneutral`** _(number)_: Operative temperature at which the PMV = 0 under given conditions. Unit: °C.
  * **`tblood`** _(number)_: Central blood temperature. Unit: °C.
  * **`tcore`** _(number)_: Core temperature. Unit: °C.
  * **`tskin_set`** _(number)_: Skin temperature setpoint for the comfort model. Unit: °C.
  * **`tskin_set_reg`** _(number)_: Skin temperature setpoint for the physiology model. Unit: °C.
  * **`pmv`** _(number)_: Predicted mean vote calculated by the original PMV model. Unit: dimensionless.
  * **`ppd`** _(number)_: Predicted percentage of dissatisfied. Unit: dimensionless.
  * **`eht`** _(number)_: Equivalent homogenous temperature. Unit: °C.
  * **`ta`** _(number)_: Air temperature. Unit: °C.
  * **`rh`** _(number)_: Relative humidity. Unit: fraction.
  * **`mrt`** _(number)_: Mean radiant temperature. Unit: °C.
  * **`v`** _(number)_: Air velocity. Unit: m/s.
  * **`solar`** _(number)_: Solar radiation. Unit: W/m2.
  * **`q_met`** _(number)_: Metabolic heat production in the body. Unit: W/m2.
  * **`q_conv`** _(number)_: Convective heat transfer between the body and ambient environment. Unit: W/m2.
  * **`q_rad`** _(number)_: Radiative heat transfer between the body and ambient environment. Unit: W/m2.
  * **`q_solar`** _(number)_: Solar radiation received by the body. Unit: W/m2.
  * **`q_resp`** _(number)_: Respiratory heat transfer between the body and ambient environment. Unit: W/m2.
  * **`q_sweat`** _(number)_: Sweat evaporation heat transfer between the body and ambient environment. Unit: W/m2.
  * **`q_blood`** _(number)_: Heat transfer due to blood flow between arteries and veins. Unit: W/m2.
  * **`q_blood_skin`** _(number)_: Heat transfer due to blood flow in the skin. Unit: W/m2.
  * **`skin_blood_flow`** _(number)_: Blood flow rate in the skin. Unit: L/h.
  * **`w`** _(number)_: Total skin wettedness. Unit: fraction.
* **`bodySegment`** _(object)_
  * **`Core`** _(number)_: Core temperature of the segment. Unit: °C.
  * **`Muscle`** _(number)_: Muscle temperature of the segment. Unit: °C.
  * **`Fat`** _(number)_: Fat temperature of the segment. Unit: °C.
  * **`Skin`** _(number)_: Skin temperature of the segment. Unit: °C.

