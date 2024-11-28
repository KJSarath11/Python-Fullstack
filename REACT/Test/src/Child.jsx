import React from "react";

const child = (e) => {
  return (
    <>
      <h3>
        My name is {e.data[0].name}.<br/> I am {e.data[0].age} old.<br/> Currently i am
        recideing in {e.data[0].city} <br/> i am {e.data[0].job}
      </h3>
      <h3>
        My name is {e.data[1].name}. I am {e.data[1].age} old. Currently i am
        recideing in {e.data[1].city} and i am in {e.data[1].job}
      </h3>
    </>
  );
};

export default child;
