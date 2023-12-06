import { Grid } from "@mui/material";
import React from "react";
import SelectDropdown from "./components/SelectDropdown/SelectDropdown";

const App = () => {
  return (
    <Grid
      container
      padding={2}
      spacing={2}
      boxShadow={3}
      margin={1}
      width={"99%"}
    >
      <Grid item xs={12}>
        <SelectDropdown />
      </Grid>

      <Grid item xs={12}>
        <Parameters />
      </Grid>
    </Grid>
  );
};

export default App;
