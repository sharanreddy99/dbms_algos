import React from "react";

import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";

const SelectDropdown = ({ data, setData } = props) => {
  const selectOptions = [
    {
      key: "All Candidate Keys",
      value: "all_candidate_keys",
    },
    {
      key: "BCNF Decomposition",
      value: "bcnf_decomposition",
    },
    {
      key: "Chase Test",
      value: "chase_test",
    },
    {
      key: "Check 3NF",
      value: "check_3nf",
    },
    {
      key: "Check BCNF",
      value: "check_bcnf",
    },
    {
      key: "Dependency Preserving",
      value: "dependency_preserving",
    },
    {
      key: "Exponential Product",
      value: "exponential_product",
    },
    {
      key: "FD Restriction",
      value: "fd_restriction",
    },
    {
      key: "Minimal Cover",
      value: "minimal_cover",
    },
    {
      key: "Non Additive Test Bin Decomposition",
      value: "non_additive_test_bin_decomposition",
    },
    {
      key: "3NF Synthesis",
      value: "3nf_synthesis",
    },
  ];

  return (
    <FormControl fullWidth>
      <InputLabel id="algo_types">Algo Types</InputLabel>
      <Select
        labelId="algo_types"
        id="algo_types_select"
        value={data.type}
        label="Algo Types"
        onChange={(e) => {
          setData({ ...data, type: e.target.value });
        }}
      >
        {selectOptions.map((option) => {
          return (
            <MenuItem key={option.key} value={option.value}>
              {option.key}
            </MenuItem>
          );
        })}
      </Select>
    </FormControl>
  );
};

export default SelectDropdown;
