import { Button, Grid } from "@mui/material";
import React, { useState } from "react";
import SelectDropdown from "./components/SelectDropdown/SelectDropdown";
import Parameters from "./components/Parameters/Parameters";
import axios from "axios";

const App = () => {
  const defaultData = {
    type: "minimal_cover",
    f: "A.BC,BC.D",
    R: "ABCD",
    RSet: "ABC,BCD",
    fdSeparator: ",",
    sideSeparator: ".",
    char: "a",
  };

  const [data, setData] = useState(defaultData);
  const [result, setResult] = useState([]);

  const runCode = async () => {
    const resp = await axios.post(
      import.meta.env.VITE_DBMS_CODES_BACKEND_URL + "/run_algo",
      data
    );

    setResult(resp.data.split("\n"));
  };

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
        <SelectDropdown data={data} setData={setData} />
      </Grid>

      <Grid item xs={12}>
        <Parameters data={data} setData={setData} />
      </Grid>
      <Grid item xs={12}>
        <Button variant="contained" onClick={runCode} fullWidth>
          Run Algorithm
        </Button>
      </Grid>
      <Grid item xs={12}>
        <div style={{ height: "50vh", overflow: "scroll" }}>
          {result.map((row) => {
            return <h4>{row}</h4>;
          })}
        </div>
      </Grid>
    </Grid>
  );
};

export default App;
