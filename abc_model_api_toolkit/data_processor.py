import json
import csv
import logging


def output_json_to_csv(output_json_file_path, csv_file_path):
    with open(output_json_file_path) as json_file:
        data = json.load(json_file)

    rows = []

    for result in data["results"]:
        base_data = {
            "elapsed_time": result["time"],
            "Met": result["met"],
            "Clo": result["clo"],
        }

        overall_data = {
            "Ta": result["overall"]["ta"],
            "MRT": result["overall"]["mrt"],
            "RH": result["overall"]["rh"],
            "Velocity": result["overall"]["v"],
            "Solar": result["overall"]["solar"],
            "Overall_Comfort": result["overall"]["comfort"],
            "Overall_Comfort_weighted": result["overall"]["comfort_weighted"],
            "Overall_Sensation": result["overall"]["sensation"],
            "Overall_Sensation_Linear": result["overall"]["sensation_linear"],
            "Overall_Sensation_Weighted": result["overall"]["sensation_weighted"],
            "MeanSkinTemp": result["overall"]["tskin"],
            "Tblood": result["overall"]["tblood"],
            "Tneutral": result["overall"]["tneutral"],
            "PMV": result["overall"]["pmv"],
            "PPD": result["overall"]["ppd"],
            "EHT": result["overall"]["eht"],
            "Qmet": result["overall"]["q_met"],
            "Qconv": result["overall"]["q_conv"],
            "Qrad": result["overall"]["q_rad"],
            "Qsolar": result["overall"]["q_solar"],
            "Qresp": result["overall"]["q_resp"],
            "Qsweat": result["overall"]["q_sweat"],
        }
        base_data.update(overall_data)

        for segment, segment_data in result["segments"].items():
            segment_data_prefixed = {
                f"Tskin-{segment}": segment_data["tskin"],
                f"Tcore-{segment}": segment_data["tcore"],
                f"Sens-{segment}": segment_data["sensation"],
                f"Sens_weighted-{segment}": segment_data["sensation_weighted"],
                f"Comfort-{segment}": segment_data["comfort"],
                f"Comfort_weighted-{segment}": segment_data["comfort_weighted"],
                f"EHT-{segment}": segment_data["eht"],
                f"Tskin_set-{segment}": segment_data["tskin_set"],
                f"Tskin_set_reg-{segment}": segment_data["tskin_set_reg"],
            }
            base_data.update(segment_data_prefixed)

        rows.append(base_data)

    # Define the desired column order
    column_order = [
        "elapsed_time",
        "Ta",
        "MRT",
        "RH",
        "Velocity",
        "Solar",
        "Clo",
        "Met",
        "Overall_Comfort",
        "Overall_Comfort_weighted",
        "Overall_Sensation",
        "Overall_Sensation_Linear",
        "Overall_Sensation_Weighted",
        "MeanSkinTemp",
        "Tblood",
        "Tneutral",
        "PMV",
        "PPD",
        "EHT",
        "Qmet",
        "Qconv",
        "Qrad",
        "Qsolar",
        "Qresp",
        "Qsweat",
    ]

    # Add segment columns to the order
    segments = [
        "Head",
        "Chest",
        "Back",
        "Pelvis",
        "Left Upper Arm",
        "Right Upper Arm",
        "Left Lower Arm",
        "Right Lower Arm",
        "Left Hand",
        "Right Hand",
        "Left Thigh",
        "Right Thigh",
        "Left Lower Leg",
        "Right Lower Leg",
        "Left Foot",
        "Right Foot",
    ]

    for segment in segments:
        column_order.extend(
            [
                f"Tskin-{segment}",
                f"Tcore-{segment}",
                f"Sens-{segment}",
                f"Sens_weighted-{segment}",
                f"Comfort-{segment}",
                f"Comfort_weighted-{segment}",
                f"EHT-{segment}",
                f"Tskin_set-{segment}",
                f"Tskin_set_reg-{segment}",
            ]
        )

    # Ensure all columns are present in each row
    for row in rows:
        for col in column_order:
            if col not in row:
                row[col] = None

    # Write the data to CSV
    with open(csv_file_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_order)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Data successfully written to {csv_file_path}")


def process_json(output_json_file_path, csv_output=False, csv_file_path=None):
    with open(output_json_file_path) as json_file:
        data = json.load(json_file)

    rows = []

    for result in data["results"]:
        base_data = {
            "elapsed_time": result["time"],
            "Met": result["met"],
            "Clo": result["clo"],
        }

        overall_data = {
            "Ta": result["overall"]["ta"],
            "MRT": result["overall"]["mrt"],
            "RH": result["overall"]["rh"],
            "Velocity": result["overall"]["v"],
            "Solar": result["overall"]["solar"],
            "Overall_Comfort": result["overall"]["comfort"],
            "Overall_Comfort_weighted": result["overall"]["comfort_weighted"],
            "Overall_Sensation": result["overall"]["sensation"],
            "Overall_Sensation_Linear": result["overall"]["sensation_linear"],
            "Overall_Sensation_Weighted": result["overall"]["sensation_weighted"],
            "MeanSkinTemp": result["overall"]["tskin"],
            "Tblood": result["overall"]["tblood"],
            "Tneutral": result["overall"]["tneutral"],
            "PMV": result["overall"]["pmv"],
            "PPD": result["overall"]["ppd"],
            "EHT": result["overall"]["eht"],
            "Qmet": result["overall"]["q_met"],
            "Qconv": result["overall"]["q_conv"],
            "Qrad": result["overall"]["q_rad"],
            "Qsolar": result["overall"]["q_solar"],
            "Qresp": result["overall"]["q_resp"],
            "Qsweat": result["overall"]["q_sweat"],
        }
        base_data.update(overall_data)

        for segment, segment_data in result["segments"].items():
            segment_data_prefixed = {
                f"Tskin-{segment}": segment_data["tskin"],
                f"Tcore-{segment}": segment_data["tcore"],
                f"Sens-{segment}": segment_data["sensation"],
                f"Sens_weighted-{segment}": segment_data["sensation_weighted"],
                f"Comfort-{segment}": segment_data["comfort"],
                f"Comfort_weighted-{segment}": segment_data["comfort_weighted"],
                f"EHT-{segment}": segment_data["eht"],
                f"Tskin_set-{segment}": segment_data["tskin_set"],
                f"Tskin_set_reg-{segment}": segment_data["tskin_set_reg"],
            }
            base_data.update(segment_data_prefixed)

        rows.append(base_data)

    if csv_output and csv_file_path:
        # Define the desired column order
        column_order = [
            "elapsed_time",
            "Ta",
            "MRT",
            "RH",
            "Velocity",
            "Solar",
            "Clo",
            "Met",
            "Overall_Comfort",
            "Overall_Comfort_weighted",
            "Overall_Sensation",
            "Overall_Sensation_Linear",
            "Overall_Sensation_Weighted",
            "MeanSkinTemp",
            "Tblood",
            "Tneutral",
            "PMV",
            "PPD",
            "EHT",
            "Qmet",
            "Qconv",
            "Qrad",
            "Qsolar",
            "Qresp",
            "Qsweat",
        ]

        # Add segment columns to the order
        segments = [
            "Head",
            "Chest",
            "Back",
            "Pelvis",
            "Left Upper Arm",
            "Right Upper Arm",
            "Left Lower Arm",
            "Right Lower Arm",
            "Left Hand",
            "Right Hand",
            "Left Thigh",
            "Right Thigh",
            "Left Lower Leg",
            "Right Lower Leg",
            "Left Foot",
            "Right Foot",
        ]

        for segment in segments:
            column_order.extend(
                [
                    f"Tskin-{segment}",
                    f"Tcore-{segment}",
                    f"Sens-{segment}",
                    f"Sens_weighted-{segment}",
                    f"Comfort-{segment}",
                    f"Comfort_weighted-{segment}",
                    f"EHT-{segment}",
                    f"Tskin_set-{segment}",
                    f"Tskin_set_reg-{segment}",
                ]
            )

        # Ensure all columns are present in each row
        for row in rows:
            for col in column_order:
                if col not in row:
                    row[col] = None

        # Write the data to CSV
        with open(csv_file_path, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=column_order)
            writer.writeheader()
            writer.writerows(rows)

        logging.info(f"Data successfully written to {csv_file_path}")

    return rows
