import { Button, Grid, TextField } from "@mui/material";
import React, { useEffect, useState } from "react";
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
    password: "",
  };

  useEffect(() => {
    const password = localStorage.getItem("password");
    if (password) {
      setData({ ...data, password: password });
    }
  }, []);

  const [data, setData] = useState(defaultData);
  const [result, setResult] = useState([]);

  const runCode = async () => {
    const resp = await axios.post(
      import.meta.env.VITE_DBMS_ALGOS_BACKEND_URL + "/run_algo",
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
        <TextField
          fullWidth
          required
          id="password"
          name="password"
          label="password"
          value={data.password}
          onChange={(e) => {
            setData({ ...data, password: e.target.value });
            localStorage.setItem("password", e.target.value);
          }}
        />
      </Grid>
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
