import React from "react";
import Child from "./Child";
import json from "./index.json"
const parent = () => {
  // passing multiple objects here
  // let obj = [
  //   { name: "sarath", age: 22, city: "kochi", job: "Jobless" },
  //   { name: "vaishnav", age: 21, city: "Pkd", job: "Wipro" },
  // ];

  return (
    // <div>
    //   <Child data={obj} />
    // </div>
    // --------------
    // <>
    //   <Child users={json}/>      
    // </>
    //---------------
    <>
      <Child users={json}/>
    </>

  )
};

export default parent;
