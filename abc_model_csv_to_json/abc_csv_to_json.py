import pandas as pd
import json


class CSVtoJSONConverter:
    # Define constants for row numbers and column letters based on the new structure
    ID_ROW, NAME_ROW, DESCRIPTION_ROW, OUTPUT_FREQ_ROW = 3, 4, 5, 6
    BODYBUILDER_START_ROW = 8
    CLOTHING_ENSEMBLE_ROW = 20
    OPTIONS_START_ROW = 43

    # Column letters for the sheet
    USER_INPUT_DATA_COL = "C"
    DEFAULT_INPUT_DATA_COL = "D"
    CLOTHING_DATA_COLS = ["C", "D"]  # For fclo and iclo columns

    def __init__(self, file_path):
        self.file_path = file_path
        self.body_segments = [
            "Head",
            "Neck",
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

    def _col_letter_to_index(self, letter):
        """Convert Excel column letters (e.g., 'A', 'B', 'C') to Pandas zero-based indices."""
        letter = letter.upper()
        col = 0
        for char in letter:
            col = col * 26 + (ord(char) - ord("A")) + 1
        return col - 1  # Convert to zero-based index

    def get_value(self, row_index, user_col, default_col, sim_info_df):
        """Get the value from user input column, fallback to default column if user input is NaN."""
        user_value = sim_info_df.iloc[row_index, user_col]
        if pd.isna(user_value):
            return sim_info_df.iloc[row_index, default_col]
        return user_value

    def parse_sim_info(self):
        # Load the "SimInfo" sheet
        sim_info_df = pd.read_excel(self.file_path, sheet_name="SimInfo", header=None)

        print("Index C", self._col_letter_to_index("C"))
        print("ID row", self.ID_ROW)
        print("Body builder start row", self.BODYBUILDER_START_ROW)

        user_col = self._col_letter_to_index(self.USER_INPUT_DATA_COL)
        default_col = self._col_letter_to_index(self.DEFAULT_INPUT_DATA_COL)

        # Extract the SimInfo details
        sim_info = {
            "id": self.get_value(self.ID_ROW - 1, user_col, default_col, sim_info_df),
            "name": self.get_value(
                self.NAME_ROW - 1, user_col, default_col, sim_info_df
            ),
            "description": self.get_value(
                self.DESCRIPTION_ROW - 1, user_col, default_col, sim_info_df
            ),
            "output_freq": self.get_value(
                self.OUTPUT_FREQ_ROW - 1, user_col, default_col, sim_info_df
            ),
            "bodybuilder": {
                "age": int(
                    self.get_value(
                        self.BODYBUILDER_START_ROW, user_col, default_col, sim_info_df
                    )
                ),
                "body_fat": float(
                    self.get_value(
                        self.BODYBUILDER_START_ROW + 1,
                        user_col,
                        default_col,
                        sim_info_df,
                    )
                ),
                "gender": self.get_value(
                    self.BODYBUILDER_START_ROW + 2, user_col, default_col, sim_info_df
                ),
                "height": float(
                    self.get_value(
                        self.BODYBUILDER_START_ROW + 3,
                        user_col,
                        default_col,
                        sim_info_df,
                    )
                ),
                "weight": float(
                    self.get_value(
                        self.BODYBUILDER_START_ROW + 4,
                        user_col,
                        default_col,
                        sim_info_df,
                    )
                ),
                "skin_color": self.get_value(
                    self.BODYBUILDER_START_ROW + 5, user_col, default_col, sim_info_df
                ),
            },
            "options": {
                "sensation_adaptation": self.get_value(
                    self.OPTIONS_START_ROW, user_col, default_col, sim_info_df
                ),
                "sensation_coredTdt": self.get_value(
                    self.OPTIONS_START_ROW + 1, user_col, default_col, sim_info_df
                ),
                "comfort_model": self.get_value(
                    self.OPTIONS_START_ROW + 2, user_col, default_col, sim_info_df
                ),
                "comfort_setpoint_input": self.get_value(
                    self.OPTIONS_START_ROW + 3, user_col, default_col, sim_info_df
                ),
                "passive_comfort_setpoints": self.get_value(
                    self.OPTIONS_START_ROW + 4, user_col, default_col, sim_info_df
                ),
                "transient_comfort_model": self.get_value(
                    self.OPTIONS_START_ROW + 5, user_col, default_col, sim_info_df
                ),
                "user_control_comfort_model": self.get_value(
                    self.OPTIONS_START_ROW + 6, user_col, default_col, sim_info_df
                ),
            },
            "clothing": [
                {
                    "ensemble_name": self.get_value(
                        self.CLOTHING_ENSEMBLE_ROW, user_col, default_col, sim_info_df
                    ),
                    "description": self.get_value(
                        self.CLOTHING_ENSEMBLE_ROW + 1,
                        user_col,
                        default_col,
                        sim_info_df,
                    ),
                    "whole_body": {"fclo": 1, "iclo": 1},  # for now
                    "segment_data": self._extract_clothing_segment_data(sim_info_df),
                }
            ],
        }
        return sim_info

    def _extract_clothing_segment_data(self, sim_info_df):
        """Extracts clothing segment data dynamically for all body segments."""
        # This is a placeholder method until actual clothing segment data structure is clarified
        segment_data = {}
        # Adjust row indices based on actual data layout if needed
        for idx, segment in enumerate(self.body_segments):
            increment_row = 4
            row = self.CLOTHING_ENSEMBLE_ROW + increment_row + idx
            fclo = sim_info_df.iloc[
                row, self._col_letter_to_index(self.CLOTHING_DATA_COLS[0])
            ]
            iclo = sim_info_df.iloc[
                row, self._col_letter_to_index(self.CLOTHING_DATA_COLS[1])
            ]
            segment_data[segment] = {"fclo": fclo, "iclo": iclo}
        return segment_data

    def extract_environment_info(self):
        # Load the "Thermal Environment" sheet
        thermal_env_df = pd.read_excel(self.file_path, sheet_name="Thermal Environment")

        # Fill missing 'ramp' values with 0, then convert them to boolean (False for 0, True otherwise)
        thermal_env_df["ramp"] = thermal_env_df["ramp"].fillna(0).astype(int)
        thermal_env_df["ramp"] = thermal_env_df["ramp"].apply(
            lambda x: False if x == 0 else True
        )

        air_temp_start_idx = 8
        segment_count = len(self.body_segments)
        mrt_start_idx = air_temp_start_idx + segment_count
        rh_start_idx = mrt_start_idx + segment_count
        v_start_idx = rh_start_idx + segment_count
        solar_start_idx = v_start_idx + segment_count

        phases = []

        # Loop through the DataFrame rows
        for _, row in thermal_env_df.iterrows():
            if pd.isnull(row["start_time"]) or pd.isnull(row["end_time"]):
                continue

            phase_info = {
                "condition_name": row["condition_name"],
                "start_time": row["start_time"],
                "end_time": row["end_time"],
                "time_units": row["time_units"],
                "met": row["met"],
                "met_activity_name": row["met_activity_name"],
                "clo_ensemble_name": row["clo_ensemble_name"],
                "ramp": bool(row["ramp"]),
                "personal_comfort_system": [],
                "default_data": {
                    "ta": 24,
                    "mrt": 24,
                    "rh": 0.5,
                    "v": 0.1,
                    "solar": 0,
                },
                "segment_data": self._extract_segments(
                    row,
                    air_temp_start_idx,
                    mrt_start_idx,
                    rh_start_idx,
                    v_start_idx,
                    solar_start_idx,
                ),
            }

            phases.append(phase_info)

        return phases

    def _extract_segments(
        self,
        row,
        air_temp_start_idx,
        mrt_start_idx,
        rh_start_idx,
        v_start_idx,
        solar_start_idx,
    ):
        segments = {}
        for idx, segment in enumerate(self.body_segments):
            segments[segment] = {
                "ta": row.iloc[air_temp_start_idx + idx],
                "mrt": row.iloc[mrt_start_idx + idx],
                "rh": row.iloc[rh_start_idx + idx],
                "v": row.iloc[v_start_idx + idx],
                "solar": row.iloc[solar_start_idx + idx],
            }
        return segments

    def to_json(self, output_file_path):
        # Extract SimInfo and Thermal Environment data
        sim_info = self.parse_sim_info()
        phases = self.extract_environment_info()

        # Merge data into final structure
        sim_info["id"] = 1
        sim_info["phases"] = phases

        # Convert to JSON and save
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(sim_info, json_file, indent=4)

        print(f"Conversion complete. JSON saved to {output_file_path}.")


if __name__ == "__main__":
    # Example usage
    file_path = "C:\\Users\\monyo\\PycharmProjects\\ABC_JSON_schema\\abc_model_csv_to_json\\abc_csv_input_sample.xlsx"
    converter = CSVtoJSONConverter(file_path)
    output_file = "output.json"
    converter.to_json(output_file)
