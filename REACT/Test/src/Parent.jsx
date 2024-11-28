import React from "react";
import Child from "./Child";
const parent = () => {
  // passing multiple objects here
  let obj = [
    { name: "sarath", age: 22, city: "kochi", job: "Jobless" },
    { name: "vaishnav", age: 21, city: "Pkd", job: "Wipro" },
  ];
  return (
    <div>
      <Child data={obj} />
    </div>
  );
};

export default parent;
