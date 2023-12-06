import {
  FormControl,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import React from "react";

const Parameters = ({ data, setData } = props) => {
  const minCoverOptions = [
    { key: "Standard or Canonical Cover or Decomposition Rule", value: "a" },
    { key: "Non Standard or Union Rule", value: "b" },
  ];

  const changeHandler = (e) => {
    const name = e.target.name;
    const value = e.target.value;

    setData({ ...data, [name]: value });
  };

  return (
    <Grid container margin={2} spacing={3}>
      <Grid item xs={11}>
        <TextField
          fullWidth
          required
          id="f"
          name="f"
          label="f"
          value={data.f}
          onChange={changeHandler}
        />
      </Grid>
      <Grid item xs={4}>
        <TextField
          fullWidth
          required
          id="R"
          name="R"
          label="R"
          value={data.R}
          onChange={changeHandler}
        />
      </Grid>
      <Grid item xs={7}>
        <TextField
          fullWidth
          required
          id="RSet"
          name="RSet"
          label="RSet"
          value={data.RSet}
          onChange={changeHandler}
        />
      </Grid>
      <Grid item xs={2}>
        <TextField
          fullWidth
          required
          id="fdSeparator"
          name="fdSeparator"
          label="fdSeparator"
          value={data.fdSeparator}
          onChange={changeHandler}
        />
      </Grid>
      <Grid item xs={2}>
        <TextField
          fullWidth
          required
          id="sideSeparator"
          name="sideSeparator"
          label="sideSeparator"
          value={data.sideSeparator}
          onChange={changeHandler}
        />
      </Grid>
      <Grid item xs={6}>
        <FormControl fullWidth>
          <InputLabel id="algo_types">Min Cover Types</InputLabel>
          <Select
            labelId="min_cover_types"
            id="min_cover_types_select"
            value={data.char}
            label="Min Cover Types"
            onChange={(e) => {
              setData({ ...data, char: e.target.value });
            }}
          >
            {minCoverOptions.map((option) => {
              return (
                <MenuItem key={option.value} value={option.value}>
                  {option.key}
                </MenuItem>
              );
            })}
          </Select>
        </FormControl>
      </Grid>
    </Grid>
  );
};

export default Parameters;
