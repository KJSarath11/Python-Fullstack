import React from "react";
import Son from "./Son";

const Father = (e) => {
  return (
    <div>
      <Son props2={e.props1}/>
    </div>
  );
};

export default Father;
